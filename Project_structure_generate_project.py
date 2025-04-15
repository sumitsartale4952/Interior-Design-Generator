import os

# Define the project structure
project_structure = {
    "Interior-Design-Generator": {
        "app": {
            "main.py": "# Entry point for the Flask app\n",
            "routes.py": "# Flask routes for handling API requests\n",
            "templates": {
                "index.html": "<!-- HTML UI for image upload and result display -->\n"
            },
            "static": {
                
                "css": {
                    "styles.css": "/* CSS styling for the web interface */\n"
                },
                "js": {
                    "scripts.js": "// JavaScript for frontend interactions\n"
                },
                "images": {}
            },
            "utils": {
                "image_processing.py": "# Functions for image preprocessing\n",
                "metadata_generator.py": "# Functions to generate metadata\n",
                "model_inference.py": "# Functions for model loading and inference\n",
                "postprocessing.py": "# Functions for image postprocessing\n"
            }
        },
        "data": {
            "images": {},
            "processed": {},
            "captions_metadata.json": "[]  # Placeholder for image captions and metadata\n"
        },
        "models": {
            "pretrained": {},
            "fine_tuned": {},
            "model_utils.py": "# Functions to load/save models\n"
        },
        "scripts": {
            "generate_captions.py": "# Script to generate captions for images\n",
            "generate_metadata.py": "# Script to generate metadata\n",
            "fine_tune_model.py": "# Script to fine-tune models\n"
        },
        "notebooks": {
            "data_analysis.ipynb": "# Jupyter notebook for data analysis\n",
            "model_finetuning.ipynb": "# Jupyter notebook for model fine-tuning\n"
        },
        "tests": {
            "test_image_processing.py": "# Tests for image processing\n",
            "test_model_inference.py": "# Tests for model inference\n",
            "test_routes.py": "# Tests for Flask routes\n"
        },
        "uploads": {},
        "feature_scope": {
            "README.md": "# Future feature roadmap\n",
            "ai_model_experiments": {
                "gpt_integration.py": "# Experiment integrating GPT for suggestions\n"
            },
            "ui_mockups": {},
            "api_integration": {
                "design_api.py": "# Code for integrating external design APIs\n"
            }
        },
        "requirements.txt": "# Required Python packages\n",
        "setup.py": "# Project setup configuration\n",
        "README.md": "# Project overview and setup guide\n",
        "LICENSE": "MIT License\n"
    }
}

# Function to create the project structure
def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w") as file:
                file.write(content)

# Define the base path for the project
base_path = "Interior-Design-Generator"

# Create the project structure
create_structure(base_path, project_structure)

print(f"Project structure created at: {os.path.abspath(base_path)}")
