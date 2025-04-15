import json
import random
import os

# Load the original JSON data
with open('D:/Interior-Design-Generator/data/captions_metadata_no_caption_size.json', 'r') as f:
    data = json.load(f)

# Define possible metadata values
styles = ["Modern", "Minimalist", "Rustic", "Industrial", "Classic", "Bohemian"]
room_types = ["Living Room", "Bedroom", "Kitchen", "Bathroom", "Dining Room", "Office"]
color_palette_options = ["White", "Gray", "Brown", "Black", "Blue", "Green", "Beige", "Gold"]

# Function to extract key features from caption
def extract_key_features(caption):
    keywords = ["table", "chair", "sofa", "plant", "lamp", "window", "shelf", "mirror", "bed", "desk", "rug"]
    return [word.capitalize() for word in caption.split() if word.lower() in keywords]

# Enhance each entry with metadata
for item in data:
    item["image_path"] = item["image_path"].replace("\\", "/")  # Normalize path format
    item["metadata"] = {
        "style": random.choice(styles),
        "room_type": random.choice(room_types),
        "key_features": extract_key_features(item["caption"]),
        "color_palette": random.sample(color_palette_options, k=3)
    }

# Save the enhanced JSON data
output_path = 'D:/Interior-Design-Generator/data/captions_metadata_with_metadata.json'

with open(output_path, 'w') as f:
    json.dump(data, f, indent=4)

print(f"✅ Enhanced JSON saved to {output_path}")
