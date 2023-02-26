import streamlit as st
from multiapp import MultiApp
from apps import home, data, model # import your app modules here

app = MultiApp()

st.markdown("""# Multi-Page App""")

# Add all your application here
app.add_app("app", app.app)
app.add_app("cluster", cluster.app)
# The main app
app.run()
