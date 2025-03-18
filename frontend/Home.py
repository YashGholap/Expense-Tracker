import streamlit as st

st.set_page_config(page_title="Expense Tracker", page_icon="💰", layout="wide")

#Sidebar Navigation
st.sidebar.title("Navigation")
st.sidebar.page_link("Home.py", label="🏠 Home")
st.sidebar.page_link("pages/Register.py",label="📝 Register")
st.sidebar.page_link("pages/Login.py", label="🔑 Login")

#main Section
st.title("💰 Expense Tracker")
st.markdown("""
### About This Project
This **Expense Tracker** helps users manage and analyze their expenses efficiently.  
It provides **secure authentication, expense logging, and analytics**.

### Created By:
👨‍💻 **Yash Gholap**  
📌 **Purpose:** This project was built as part of my learning in full-stack development, integrating **Django for the backend** and **Streamlit for the frontend**.
""")

# st.image("https://www.svgrepo.com/show/497848/money-graph.svg", width=300)
