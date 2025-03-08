import streamlit as st

# Title of the Streamlit app
st.title("Hello, World with Streamlit!")

# Welcome message
st.write("Welcome to the Streamlit app")

# Button and checkbox interaction
if st.button('Click Me'):
    st.write('Button clicked!')
    st.checkbox("Check me")

# Checkbox to display some text
if st.checkbox("Check me to show some text"):
    st.write("Hello Digitalschool")

# Text input for entering name
name = st.text_input("Enter your name", "John Doe")
st.write(f"Your Name: {name}")

# Number input for age
age = st.number_input("Enter your age", min_value=1, max_value=120)
st.write(f"You are {age} years old.")

# Number input for height (in cm or meters)
height = st.number_input("Enter your height (in cm)", min_value=50, max_value=300)
st.write(f"Your height is {height} cm.")

# Radio button for a selection
choice = st.radio("Pick one", ['Choice 1', 'Choice 2', 'Choice 3'])
st.write(f"You chose: {choice}")

# Button to display a success message
if st.button("Success"):
    st.success("It was sent successfully")

# Handle exception for division by zero (just as an example)
try:
    1 / 0
except Exception as e:
    st.exception(e)

# You can define any other logic here if needed
