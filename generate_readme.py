readme_content = """
# Equity Research News Tool

## Project Overview

This project is an AI-powered Equity Research News Tool built using LangChain, Streamlit, NewsAPI, Groq, and Gemini.

The application allows users to:

- Search for company or market-related news
- Fetch news articles using NewsAPI
- Generate AI-powered summaries and analysis
- Choose between Groq LLaMA 3.3 and Gemini 1.5 Flash
- Control the number of articles analyzed

---

## Features

- NewsAPI Integration
- AI-Powered News Summarization
- Equity Research Analysis
- Groq LLaMA 3.3 Support
- Gemini 1.5 Flash Support
- Streamlit User Interface
- Dynamic Model Selection
- Error Handling
- Environment Variable Support

---

## Project Structure

NEWS_RESEARCH/

├── app.py

├── langchain_config.py

├── .env

├── requirements.txt

├── README.md

├── notebook_1_setup.ipynb

└── notebook_2_enhance.ipynb

---

## Technologies Used

- Python
- Streamlit
- LangChain
- NewsAPI
- Groq API
- Google Gemini API
- python-dotenv

---

## Installation

1. Clone the repository

2. Install dependencies

pip install -r requirements.txt

---

## Environment Variables

Create a .env file and add:

GROQ_API_KEY=your_groq_api_key

NEWSAPI_KEY=your_newsapi_key

GEMINI_API_KEY=your_gemini_api_key

---

## Running the Application

Run the Streamlit app:

streamlit run app.py

---

## How It Works

1. User enters a news query.
2. NewsAPI fetches relevant articles.
3. Articles are summarized.
4. LangChain sends the summaries to the selected LLM.
5. The model generates an equity research analysis.
6. Results are displayed in Streamlit.

---

## Supported Models

### Groq

- LLaMA 3.3 70B Versatile
- Fast response time
- Free API access

### Gemini

- Gemini 1.5 Flash
- Google's Generative AI model
- Good reasoning capabilities

---

## Future Enhancements

- Sentiment Analysis
- PDF Report Export
- Interactive Dashboard
- Historical News Tracking
- Stock Price Integration
- Data Visualization

---

## Author

Created as part of an AI/GenAI Internship Project.

"""

with open("README.md", "w", encoding="utf-8") as file:
    file.write(readme_content)

print("README.md generated successfully!")