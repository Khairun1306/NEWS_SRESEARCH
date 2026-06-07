# langchain_config.py

import os
from dotenv import load_dotenv
from newsapi import NewsApiClient
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

# ── LLM selection ─────────────────────────────────────────────────────────────
# Set USE_GROQ = True  → LLaMA 3.3 via Groq  (free, fast)
# Set USE_GROQ = False → Gemini 1.5 Flash     (requires GEMINI_API_KEY)


def get_llm(model_choice):
    if model_choice == "Groq (LLaMA 3.3)":
        return ChatGroq(
            groq_api_key=os.getenv("GROQ_API_KEY"),
            model_name="llama-3.3-70b-versatile"
        )

    return ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        google_api_key=os.getenv("GEMINI_API_KEY")
    )
    
def get_chain(model_choice):
    llm = get_llm(model_choice)
    return prompt | llm | StrOutputParser()

# ── NewsAPI client ─────────────────────────────────────────────────────────────
newsapi = NewsApiClient(api_key=os.getenv("NEWSAPI_KEY"))

# ── News helpers ───────────────────────────────────────────────────────────────
def get_news_articles(query: str, page_size: int = 5) -> list:
    """Fetch up to `page_size` articles for `query` from NewsAPI."""

    try:
        response = newsapi.get_everything(
            q=query,
            language="en",
            sort_by="relevancy",
            page_size=page_size
        )

        if response.get("status") == "ok":
            return response["articles"]

    except Exception as e:
        print(f"NewsAPI Error: {e}")

    return []


def summarize_articles(articles: list) -> str:
    """
    Convert a list of article dicts into bullet-point strings.
    Articles with no description are skipped.
    """
    summaries = [
    f"- {a.get('title', 'No Title')}: {a.get('description', '')}"
    for a in articles
    if a.get("description")
]
    return "\n".join(summaries)

def get_summary(query: str, page_size: int = 5) -> str:
    articles = get_news_articles(query, page_size)
    return summarize_articles(articles)


# ── LangChain prompt & chain ───────────────────────────────────────────────────
prompt = ChatPromptTemplate.from_template("""
You are an AI assistant helping an research analyst.

Query:
{query}

News Summaries:
{summaries}

Your analysis:
""")

# ── Convenience wrapper ────────────────────────────────────────────────────────
def analyze_news(query: str, model_choice="Groq (LLaMA 3.3)") -> str:
    summaries = get_summary(query)

    chain = get_chain(model_choice)

    return chain.invoke({
        "query": query,
        "summaries": summaries
    })
