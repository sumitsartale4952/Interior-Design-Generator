from flask import Blueprint, render_template, request, jsonify, send_from_directory
from werkzeug.utils import secure_filename
import os

# Import image processing and diffusion model
from utils.image_processing import preprocess_image
from utils.diffusion_inference import load_diffusion_model, generate_design_with_diffusion

# Initialize Flask Blueprint
routes_bp = Blueprint('routes', __name__)

# Upload folder path
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Load the diffusion model (fine-tuned)
diffusion_model, device = load_diffusion_model(model_path="D:/Interior-Design-Generator/models/finetuned_models/epoch_5")

def allowed_file(filename):
    """
    Validate allowed file extensions for uploaded images.
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route: Home Page
@routes_bp.route('/')
def index():
    return render_template('index.html')

# Route: Upload Page
@routes_bp.route('/upload', methods=['GET', 'POST'])
def upload_page():
    if request.method == 'POST':
        return generate_design()  # Call the image generation function
    return render_template('upload.html')

# Route: Handle image upload and generate design
@routes_bp.route('/generate', methods=['POST'])
def generate_design():
    try:
        if 'roomImage' not in request.files:
            return jsonify({"error": "No file part in the request."}), 400

        room_image = request.files['roomImage']
        design_prompt = request.form.get('designPrompt')

        if room_image and allowed_file(room_image.filename):
            # Save the uploaded image securely
            filename = secure_filename(room_image.filename)
            image_path = os.path.join(UPLOAD_FOLDER, filename)
            room_image.save(image_path)

            # Preprocess image (resize, normalization)
            preprocessed_image = preprocess_image(image_path)

            # Generate the design with the fine-tuned diffusion model
            generated_image_path = os.path.join('data/generated', f'generated_{filename}')
            generated_image = generate_design_with_diffusion(design_prompt, diffusion_model, device, generated_image_path)

            if generated_image:
                return jsonify({
                    "message": "Design generated successfully!",
                    "generated_image_url": f"/uploads/{generated_image_path.split('/')[-1]}"
                })
            else:
                return jsonify({"error": "Failed to generate the design."}), 500
        else:
            return jsonify({"error": "Invalid file type. Please upload a PNG, JPG, or JPEG image."}), 400

    except Exception as e:
        print(f"❌ Error during image generation: {e}")
        return jsonify({"error": "An error occurred while generating the design."}), 500

# Route: Serve generated image
@routes_bp.route('/uploads/<filename>')
def serve_generated_image(filename):
    """
    Serve the generated image to the user.
    """
    return send_from_directory('data/generated', filename)

# Health Check Route
@routes_bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "Server is running!"}), 200