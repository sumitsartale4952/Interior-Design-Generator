from diffusers import StableDiffusionPipeline
import torch
import os

def load_diffusion_model(model_path="D:/Interior-Design-Generator/models/finetuned_models/epoch_5"):
    """Loads the fine-tuned Stable Diffusion model from a specified path."""
    try:
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        print(f"🖥️  Using device: {device}")

        # Check if the required model file exists
        if not os.path.exists(os.path.join(model_path, "text_encoder", "pytorch_model.bin")):
            raise FileNotFoundError(f"Error no file named pytorch_model.bin found in directory {model_path}/text_encoder")

        # Load the fine-tuned model
        model = StableDiffusionPipeline.from_pretrained(
            model_path,
            torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
            revision="fp16" if torch.cuda.is_available() else "main",  # Ensure compatibility with model precision
            safety_checker=None,  # Optionally disable the safety checker for faster performance
            use_auth_token=False,  # Set to False if accessing a local model
            weights_only=True  # Set to True for safer loading of model weights
        )
        model.to(device)

        print("✅ Fine-tuned Diffusion model loaded successfully!")
        return model, device

    except Exception as e:
        print(f"❌ Failed to load the fine-tuned diffusion model: {str(e)}")
        return None, None

def generate_design_with_diffusion(prompt, model, device, output_path):
    """Generates an image based on a given text prompt using the loaded model."""
    if not model:
        print("❌ Error: Model is not loaded.")
        return None

    try:
        print(f"🚀 Generating design for prompt: '{prompt}'")

        # Context manager for handling CUDA out of memory issues
        with torch.autocast(device.type):
            result = model(prompt, guidance_scale=7.5)  # Adjust guidance_scale for more creative freedom

        # Save the generated image
        result.images[0].save(output_path)
        print(f"✅ Image generated and saved at: {output_path}")

        return output_path

    except Exception as e:
        print(f"❌ Error during image generation: {str(e)}")
        return None

# Test the model independently
if __name__ == "__main__":
    model, device = load_diffusion_model(model_path="D:/Interior-Design-Generator/models/finetuned_models/epoch_5")

    if model:
        test_output_path = os.path.join("uploads", "test_generated_image.png")
        prompt = "A modern luxury living room with large windows and minimalist decor"
        generated_image = generate_design_with_diffusion(prompt, model, device, test_output_path)

        if generated_image:
            print("🎉 Test image generated successfully!")
        else:
            print("❌ Test image generation failed.")
    else:
        print("❌ Model failed to load for testing.")