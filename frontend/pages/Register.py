import streamlit as st
import time

# Initialize session state if not already set
if "registered" not in st.session_state:
    st.session_state["registered"] = False

# If registration is successful, redirect to login
if st.session_state["registered"]:
    st.session_state["registered"] = False  # Reset the flag
    st.switch_page("pages/login.py")  # Redirect to login page

st.title("📝 Register")

# User Inputs
username = st.text_input("👤 Username")
email = st.text_input("📧 Email")
password = st.text_input("Password", type="password")
confirm_password = st.text_input("Confirm Password", type="password")

# Registration logic
if st.button("Register"):
    if password != confirm_password:
        st.error("❌ Passwords do not match!")
    elif username and password:  # Ensure fields are not empty
        # TODO: Add backend logic to store user details
        st.success("✅ Registration Successful! Redirecting to login...")
        
        # Set session state flag to trigger redirect
        st.session_state["registered"] = True
        
        time.sleep(3)
        st.rerun()  # Refresh page to trigger redirect
    else:
        st.warning("⚠️ Please fill in all fields!")
