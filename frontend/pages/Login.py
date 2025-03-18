import streamlit as st

st.set_page_config(page_title="Login", page_icon="🔑")

st.title("🔑 Login")

st.markdown("Enter your credentials to access the dashboard.")

#form for login
with st.form("login_form"):
    email = st.text_input("📧 Email")
    password = st.text_input("🔑 Password", type="password")
    
    submit_button = st.form_submit_button("Login")
    
    if submit_button:
        if email and password:
            st.success("✅ Login successful!")
        else:
            st.error("❌ Invalid credentials.")