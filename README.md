# HumanOrMachine: Detecting AI-Generated Text

A deep learning and machine learning approach to distinguish between human-written and AI-generated text.

## Project Overview

This project focuses on developing a binary classifier to distinguish between human-written and AI-generated text. As large language models become increasingly sophisticated, the ability to differentiate between human and machine-generated content is becoming an important technological challenge.

The model achieves approximately 68% accuracy in identifying whether a text was written by a human or generated by an AI system, with strong performance metrics:
- F1-Score: 0.64
- Precision: 0.72
- Recall: 0.58

## Dataset

The dataset consists of:

1. **Human-generated texts**: A collection of jokes from Reddit's r/jokes subreddit, focusing specifically on music-related humor. These posts were created by human users and represent natural human writing patterns, humor structures, and linguistic choices.

2. **AI-generated texts**: A parallel dataset of AI-generated jokes using similar prompts and themes. These were created using large language models to mimic human-written jokes but contain subtle patterns and characteristics unique to AI generation.

Both datasets contain structured joke content with titles and punchlines, providing a balanced comparison between human and machine text generation capabilities.

## Features

- Balanced dataset with equal representation of human and AI-generated content
- Data preprocessing and cleaning pipeline
- Multiple model architectures explored (TF-IDF, Bag of Words, BERT, RoBERTa)
- Hyperparameter tuning for optimal performance
- Detailed error analysis and model interpretability
- Comprehensive evaluation metrics

## Model Architecture

After experimenting with several approaches, the best performance was achieved with a fine-tuned BERT-base model with the following configuration:
- Batch size: 32
- Learning rate: 2e-5
- 3 training epochs with early stopping

## Results

The model demonstrates strong performance in distinguishing between human and AI texts:

```
Classification Performance:
- Accuracy: 0.6783
- F1-Score: 0.6446
- Precision: 0.7202
- Recall: 0.5833

Per-class Performance:
- Human texts (class 0) - Precision: 0.6499, Recall: 0.7733, F1: 0.7062
- AI texts (class 1) - Precision: 0.7202, Recall: 0.5833, F1: 0.6446
```

### Error Analysis

The error analysis reveals that the model tends to misclassify AI-generated texts as human more often than the reverse:
- False Positives (Human texts classified as AI): 11.33%
- False Negatives (AI texts classified as Human): 20.83%

## Strengths & Limitations

### Strengths
- High overall accuracy and F1-score
- Effective at distinguishing most human and AI-generated texts
- Pre-trained language model provides strong language understanding
- Handles variable text lengths well

### Limitations
- Still misclassifies some examples where style is ambiguous
- Fine-tuning is computationally expensive
- May struggle with very short texts where there are fewer distinguishing features
- May be sensitive to the specific AI model used to generate the training data

## Getting Started

### Prerequisites
- Python 3.7+
- PyTorch
- Transformers (Hugging Face)
- scikit-learn
- pandas
- numpy
- matplotlib
- seaborn

### Installation

```bash
git clone https://github.com/MuhammadYeasin/HumanOrMachine.git
cd HumanOrMachine
pip install -r requirements.txt
```

### Usage

```python
# Load the pre-trained model
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("models/bert-base-uncased_bs_32")
model = AutoModelForSequenceClassification.from_pretrained("models/bert-base-uncased_bs_32")

# Predict on new text
def predict(text):
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=128)
    outputs = model(**inputs)
    probs = torch.softmax(outputs.logits, dim=1)
    prediction = torch.argmax(probs, dim=1).item()
    return "AI-generated" if prediction == 1 else "Human-written", probs[0][prediction].item()

# Example usage
text = "What do you call a musician who's lost his sheet music? Adrift in treble."
label, confidence = predict(text)
print(f"This text is {label} with {confidence:.2f} confidence.")
```

## Project Structure

```
HumanOrMachine/
├── data/
│   ├── train.csv
│   ├── val.csv
│   ├── test.csv
│   └── combined_enriched.csv
├── models/
│   └── bert-base-uncased_bs_32/
├── notebooks/
│   ├── 1_data_exploration.ipynb
│   ├── 2_statistical_models.ipynb
│   └── 3_transformer_models.ipynb
├── src/
│   ├── data_preprocessing.py
│   ├── feature_extraction.py
│   ├── model_training.py
│   └── evaluation.py
├── requirements.txt
└── README.md
```

## Future Work

- Experiment with more diverse text types beyond jokes
- Implement ensemble methods combining multiple models
- Explore adversarial training to make the model more robust
- Develop a web interface for real-time classification
- Extend the model to multi-class classification for different AI models

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Dataset collected from Reddit's r/jokes subreddit
- Implementation based on Hugging Face Transformers library
- Special thanks to the open-source NLP community
