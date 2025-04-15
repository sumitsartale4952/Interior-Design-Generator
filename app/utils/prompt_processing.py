from transformers import CLIPTokenizer
import os

# Load the CLIP tokenizer
def load_tokenizer(model_name="openai/clip-vit-base-patch16"):
    """
    Load the CLIP tokenizer from the pre-trained model.

    Args:
        model_name (str): The name or path of the pre-trained model.

    Returns:
        tokenizer: The loaded tokenizer.
    """
    try:
        tokenizer = CLIPTokenizer.from_pretrained(model_name)
        print(f"✅ Tokenizer loaded from {model_name}")
        return tokenizer
    except Exception as e:
        print(f"❌ Error loading tokenizer: {e}")
        return None

def preprocess_prompt(prompt, tokenizer, max_length=77):
    """
    Preprocess the user's prompt for model inference.

    Args:
        prompt (str): The user-provided text prompt.
        tokenizer: The tokenizer for text preprocessing.
        max_length (int): The maximum length for the tokenized prompt.

    Returns:
        dict: The tokenized input for the model.
    """
    try:
        # Tokenize the prompt with the CLIP tokenizer
        tokenized_inputs = tokenizer(
            prompt,
            padding="max_length",  # Ensure all prompts are the same length
            truncation=True,  # Truncate longer prompts
            max_length=max_length,
            return_tensors="pt"
        )
        print(f"✅ Prompt tokenized: {prompt}")
        return tokenized_inputs
    except Exception as e:
        print(f"❌ Error during prompt preprocessing: {e}")
        return None

def refine_prompt(original_prompt, additional_info="A beautiful design"):
    """
    Refine the user's prompt with additional information to make it more detailed.

    Args:
        original_prompt (str): The original user-provided prompt.
        additional_info (str): Additional information to improve the prompt.

    Returns:
        str: The refined prompt.
    """
    try:
        # Combine original prompt with additional information
        refined_prompt = f"{original_prompt}, {additional_info}"
        print(f"✅ Prompt refined: {refined_prompt}")
        return refined_prompt
    except Exception as e:
        print(f"❌ Error refining the prompt: {e}")
        return original_prompt  # Return original prompt in case of error