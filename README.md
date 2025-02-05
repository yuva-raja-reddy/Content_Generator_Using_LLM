<!-- ---
title: Content Generator Using LLM
emoji: 📝
colorFrom: indigo
colorTo: blue
sdk: streamlit
sdk_version: 1.41.1
app_file: app.py
pinned: false
license: mit
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference -->

# LinkedIn Content Generator Using LLM 📝

An AI-powered LinkedIn content generator that creates engaging posts using LLaMA 3.3 70B model through GROQ API.

## Features

- Generate LinkedIn posts in English and Hinglish
- Customizable post length (Short, Medium, Long)
- Topic-based content generation
- Few-shot learning from real LinkedIn posts
- User-friendly Streamlit interface

## Tech Stack

- Python 3.9+
- Streamlit
- LangChain
- GROQ API (LLaMA 3.3 70B model)
- Pandas
- Python-dotenv

## Installation

1. Clone the repository
```bash
git clone https://github.com/yuva-raja-reddy/Content_Generator_Using_LLM.git
cd Content_Generator_Using_LLM
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Create a .env file and add your GROQ API key
```bash
GROQ_API_KEY=your_api_key_here
```

## Usage
1. Run the Streamlit app:
```bash
streamlit run app.py
```

2. Select your preferences:

- Choose a topic
- Select post length (Short, Medium, Long)
- Choose language (English, Hinglish)

3. Click "Generate" to create your LinkedIn post