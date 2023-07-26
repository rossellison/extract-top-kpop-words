import streamlit as st
import pandas as pd
import openai_helper

col1, col2 = st.columns([3,2])

kpop_data_df = pd.DataFrame({
        "Word": ["", "", "", "", ""],
        "Count": ["", "", "", "", ""]
    })

with col1:
    st.title("Top Kpop Word Extraction Tool")
    news_article = st.text_area("Paste your Kpop Lyrics here, find out which words from your song are in the top 25 most common words in Kpop", height=300)
    if st.button("Extract"):
        kpop_data_df = openai_helper.extract_kpop_data(news_article)

with col2:
    st.markdown("<br/>" * 5, unsafe_allow_html=True)  # Creates 5 lines of vertical space
    st.dataframe(
        kpop_data_df,
        column_config={
            "Measure": st.column_config.Column(width=150),
            "Value": st.column_config.Column(width=150)
        },
        hide_index=True
    )
