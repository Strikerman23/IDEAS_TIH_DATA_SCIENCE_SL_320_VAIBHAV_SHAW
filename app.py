import streamlit as st
import pandas as pd
import numpy as np

# Set page title and icon
st.set_page_config(page_title="My Streamlit App", page_icon=":rocket:")

# Title
st.title("Welcome to My Streamlit App!")
st.subheader("A simple demo of Streamlit features")

# Sidebar
st.sidebar.header("Configuration")
user_name = st.sidebar.text_input("Enter your name", "John Doe")
age = st.sidebar.slider("Select your age", 0, 100, 25)
color = st.sidebar.color_picker("Pick a color", "#00f900")

# Display user input
st.write(f"Hello, {user_name}! You're {age} years old.")
st.write("Your chosen color is:", color)

# Dataframe
st.header("Random Data")
data = pd.DataFrame({
    'A': np.random.randn(100),
    'B': np.random.rand(100) * 100,
    'C': np.random.choice(['X', 'Y', 'Z'], 100)
})
st.dataframe(data.head())

# Chart
st.header("Data Visualization")
chart_type = st.selectbox("Choose chart type", ["Line Chart", "Bar Chart", "Area Chart"])

if chart_type == "Line Chart":
    st.line_chart(data['B'])
elif chart_type == "Bar Chart":
    st.bar_chart(data['B'])
else:
    st.area_chart(data['B'])

# Map
st.header("Map Example")
map_data = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])
st.map(map_data)

# Expander
with st.expander("Click to see more information"):
    st.write("""
        This is additional information that you can show or hide.
        Streamlit makes it easy to create interactive web apps with Python!
    """)

# Button
if st.button("Click me for a surprise"):
    st.balloons()
    st.success("🎉 Surprise! You clicked the button!")

# File uploader
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
if uploaded_file is not None:
    uploaded_data = pd.read_csv(uploaded_file)
    st.write("Uploaded data:")
    st.write(uploaded_data)