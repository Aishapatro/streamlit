import streamlit as st 

st.title("Text Summarizer")

text=st.text_area("Enter Text")

if st.button("Summarizer"):
    summary=" ".join(text.split()[:30])
    st.write("Summary:")
    st.write(summary)
 
 