# Interior Design Generator

An AI-powered interior design generation system that creates unique interior designs based on text prompts using fine-tuned Stable Diffusion models.

## 🌟 Features

- Text-to-image generation for interior designs
- Web interface for easy interaction
- Image preprocessing and validation
- Fine-tuned Stable Diffusion model
- BLIP model integration for image captioning
- Safety filters and content moderation

## 🏗️ Project Structure

```
Interior-Design-Generator/
├── app/
│   ├── main.py              # Flask application entry point
│   ├── routes.py            # API routes
│   ├── templates/           # HTML templates
│   ├── static/              # Static assets
│   └── utils/               # Utility functions
├── data/
│   ├── images/              # Training images
│   └── captions_metadata/   # Image metadata
├── models/
│   └── finetuned_models/    # Fine-tuned model weights
├── notebooks/
│   ├── data_analysis.ipynb
│   └── model_finetuning.ipynb
├── tests/                   # Unit tests
└── vae/                     # VAE model components
```

## 🛠️ Technologies Used

- Python 3.8+
- PyTorch
- Flask
- Stable Diffusion
- BLIP
- Transformers
- PIL (Python Imaging Library)

## 🤖 Models Used

1. **Stable Diffusion**: Fine-tuned model based on [CompVis/stable-diffusion-v1-5](https://huggingface.co/CompVis/stable-diffusion-v1-5)
2. **BLIP**: [Salesforce/BLIP](https://huggingface.co/Salesforce/BLIP) for image captioning

## 🚀 Getting Started

### Prerequisites

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Running the Application

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Interior-Design-Generator.git
cd Interior-Design-Generator
```

2. Set up the environment:
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Start the Flask server:
```bash
python app/main.py
```

4. Open http://localhost:5000 in your browser

## 📝 Usage

1. Visit the web interface
2. Upload an interior image or enter a text prompt
3. Click "Generate Design"
4. View and download the generated interior design

## 🧪 Testing

Run the test suite:
```bash
python -m pytest tests/
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔒 Safety and Limitations

- The model has content filters to prevent inappropriate content
- Image generation is limited to interior design contexts
- See [vae/README.md](vae/README.md) for detailed model limitations

## 🙏 Acknowledgments

- [Stable Diffusion](https://github.com/CompVis/stable-diffusion) by CompVis
- [BLIP](https://github.com/salesforce/BLIP) by Salesforce