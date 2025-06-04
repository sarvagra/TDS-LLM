# 🧠 LLM-Powered Semantic & Vision Toolkit

This repository is a modular suite of tools combining **semantic search**, **image processing**, **text extraction**, **image-encoding**, and **sentiment analysis** using modern machine learning techniques.

---
## ✨ Features
- 🧠 **Sentiment Analysis**: Classify the sentiment of text-based questions and answers.<br><br>
- 🔍 **Semantic Search API**: Search over documents using sentence embeddings and cosine similarity.<br><br>

- 🖼️ **Image to Text Extraction(Vision)**: Extract structured text like invoices or statements from image files.<br><br>

- 🧬 **Base64 Encoding/Decoding**: Encode or decode files/images for transmission or storage.<br><br>

- 📍 **Address Parser.py** : Extracts structured geographical info (state name/code, ZIP code, and country name/code) from real-world addresses using the OpenAI API with both basic and JSON schema-based approaches, and outputs results as a DataFrame.<br><br>
- 🧪 **API Playground**: Test endpoints directly via the built-in Swagger UI.
---

## 📂 Project Structure

```bash
.
├── base64/                  # Utilities for encoding/decoding
├── resources/               # Data files (.env, images, CSVs)
├── semantic_search_api/     # FastAPI semantic search project
├── sentiment analysis/      # Sentiment classification using sample movie reviews
├── text extraction/         # OCR and text parsing tools
├── vision/                  # Image analysis and invoice parsing
├── .gitignore
├── README.md                # Description(you're here!!)

```
---
## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/llm-semantic-vision-toolkit.git
cd llm-semantic-vision-toolkit
```
