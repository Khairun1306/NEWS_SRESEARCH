# app.py

import streamlit as st
from langchain_config import get_summary, get_chain

st.set_page_config(page_title="Research News Tool", page_icon="📰")

st.title(" Research News Tool")
st.write("Enter a company, topic, or ticker to get AI-summarised news.")

# ── Sidebar ────────────────────────────────────────────────────────────────────
st.sidebar.header("⚙️ Settings")
model_choice = st.sidebar.selectbox(
    "LLM Backend", ["Groq (LLaMA 3.3)", "Gemini 1.5 Flash"]
)
st.sidebar.info("Edit `USE_GROQ` in `langchain_config.py` to switch models.")

num_articles = st.sidebar.slider("Number of articles to fetch", 3, 10, 5)

# ── Main input ─────────────────────────────────────────────────────────────────
query = st.text_input("🔍 Search query", placeholder="e.g. Apple earnings 2024")

if st.button("Get News Summary"):
    if query.strip():
        with st.spinner("Fetching news and generating analysis..."):
            summaries = get_summary(query, num_articles)

            if not summaries:
                st.warning("No articles found for that query. Try a different search term.")
            else:
                chain = get_chain(model_choice)

                response = chain.invoke({
                    "query": query,
                    "summaries": summaries
                })

                st.subheader("📋 Raw News Bullets")
                st.text(summaries)

                st.subheader("🤖 AI Analysis")
                st.write(response)

                st.download_button(
                    label="📥 Download Report",
                    data=response,
                    file_name="news_analysis.txt",
                    mime="text/plain"
                )

    else:
        st.warning("Please enter a query first.")
    
