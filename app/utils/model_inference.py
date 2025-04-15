import os
from transformers import BlipProcessor, BlipForConditionalGeneration
import torch
from PIL import Image

def load_pretrained_blip():
    """Load the pre-trained BLIP model."""
    try:
        model_path = "models/pretrained/blip"

        if not os.path.exists(model_path):
            print("❌ Pre-trained model folder not found.")
            return None, None, None

        # Load the processor and model from the path
        processor = BlipProcessor.from_pretrained(model_path)
        model = BlipForConditionalGeneration.from_pretrained(model_path)

        # Determine the device (GPU if available, otherwise CPU)
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        model.to(device)

        print("✅ Pre-trained BLIP model loaded successfully!")
        return model, processor, device

    except Exception as e:
        print(f"❌ Error loading the pre-trained BLIP model: {e}")
        return None, None, None

def generate_caption(image_path, model, processor, device, prompt=""):
    """
    Generate a caption for the uploaded image.

    Args:
        image_path (str): Path to the uploaded image.
        model: Pre-trained BLIP model.
        processor: BLIP processor for preprocessing.
        device: CPU/GPU.
        prompt (str): Optional prompt to provide context for caption generation.

    Returns:
        str: Generated caption or error message.
    """
    try:
        # Check if the model and processor are loaded
        if model is None or processor is None:
            return "Model or processor is not loaded properly."

        # Load and preprocess the image
        image = Image.open(image_path).convert("RGB")
        inputs = processor(images=image, text=prompt, return_tensors="pt").to(device)

        # Generate the caption
        outputs = model.generate(**inputs, max_length=50)
        caption = processor.decode(outputs[0], skip_special_tokens=True)

        print(f"📝 Generated Caption: {caption}")
        return caption

    except Exception as e:
        print(f"❌ Error generating caption: {e}")
        return "Error generating caption."

