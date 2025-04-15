from PIL import Image
import os
from werkzeug.utils import secure_filename  # ✅ Corrected import

# Allowed file extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    """
    Validate allowed file extensions.

    Args:
        filename (str): Uploaded file name.

    Returns:
        bool: True if file is allowed, else False.
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def resize_image(image_path, output_size=(512, 512)):
    """
    Resize the image to the specified size.

    Args:
        image_path (str): Path to the image.
        output_size (tuple): Desired image size (width, height).

    Returns:
        str: Path to the resized image or None if an error occurred.
    """
    try:
        img = Image.open(image_path)
        img = img.convert("RGB")  # Ensure RGB format for consistency
        img = img.resize(output_size, Image.ANTIALIAS)  # Resize image
        img.save(image_path)  # Save the resized image
        print(f"✅ Image resized and saved at: {image_path}")
        return image_path
    except Exception as e:
        print(f"❌ Error resizing image: {e}")
        return None

def preprocess_image(uploaded_image, upload_folder="uploads"):
    """
    Save and preprocess the uploaded image.

    Args:
        uploaded_image (FileStorage): Uploaded image file.
        upload_folder (str): Folder to save the image.

    Returns:
        str: Path to the saved and resized image or None if an error occurred.
    """
    try:
        if uploaded_image and allowed_file(uploaded_image.filename):
            filename = secure_filename(uploaded_image.filename)
            file_path = os.path.join(upload_folder, filename)

            # Ensure upload folder exists, if not create it
            if not os.path.exists(upload_folder):
                os.makedirs(upload_folder)

            # Save the uploaded image to the designated folder
            uploaded_image.save(file_path)
            print(f"📥 Image uploaded to: {file_path}")

            # Resize the image for model input
            resized_path = resize_image(file_path)
            if resized_path:
                print(f"✅ Image preprocessing completed successfully: {resized_path}")
                return resized_path
            else:
                print("❌ Failed to resize the image.")
                return None
        else:
            print("❌ Invalid file format. Only PNG, JPG, and JPEG are allowed.")
            return None

    except Exception as e:
        print(f"❌ Error in image preprocessing: {e}")
        return None