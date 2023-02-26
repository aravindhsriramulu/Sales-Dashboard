# Contents of ~/streamlit_app.py
import streamlit as st

def app():
    st.markdown("# app 🎈")
    st.sidebar.markdown("# app 🎈")

def cluster():
    st.markdown("# cluster ❄️")
    st.sidebar.markdown("# cluster ❄️")

page_names_to_funcs = {
    "app": app,
    "cluster": cluster,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
