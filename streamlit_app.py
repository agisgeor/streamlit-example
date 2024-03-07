import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

# Initialize session state variables for login status, username, and password if not already done
if 'login_status' not in st.session_state:
    st.session_state['login_status'] = False

# Welcome message
st.title("Welcome to Streamlit!")

# Check if user is already logged in
if st.session_state['login_status']:
    st.success("You are successfully logged in!")
else:
    # Placeholder for login message
    login_message = st.empty()

    # Create a simple login form
    with st.sidebar:
        st.sidebar.header("Login")
        entered_username = st.sidebar.text_input("Username")
        entered_password = st.sidebar.text_input("Password", type="password")
        login_button = st.sidebar.button("Login")

    if login_button:
        if entered_username == st.secrets["app_secrets"]["username"] and entered_password == st.secrets["app_secrets"]["password"]:
            st.session_state['login_status'] = True
            st.success("You are successfully logged in!")
        else:
            login_message.error("Invalid username or password. Please try again.")

# Show the spiral and other components only if logged in
if st.session_state['login_status']:
    num_points = st.slider("Number of points in spiral", 1, 10000, 1100)
    num_turns = st.slider("Number of turns in spiral", 1, 300, 31)
    
    indices = np.linspace(0, 1, num_points)
    theta = 2 * np.pi * num_turns * indices
    radius = indices
    
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    
    df = pd.DataFrame({
        "x": x,
        "y": y,
        "idx": indices,
        "rand": np.random.randn(num_points),
    })
    
    st.altair_chart(alt.Chart(df, height=700, width=700)
        .mark_point(filled=True)
        .encode(
            x=alt.X("x", axis=None),
            y=alt.Y("y", axis=None),
            color=alt.Color("idx", legend=None, scale=alt.Scale()),
            size=alt.Size("rand", legend=None, scale=alt.Scale(range=[1, 150])),
        ))
