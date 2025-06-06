import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set the title of the app
st.title("Interactive Data Explorer")

# Load sample data
@st.cache_data
def load_data():
    data = {
        'Fruit': ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry'],
        'Quantity': [10, 15, 20, 25, 30],
        'Price': [0.5, 0.25, 0.75, 1.0, 2.0]
    }
    df = pd.DataFrame(data)
    return df

df = load_data()

# Display the dataframe
st.subheader("Dataset")
st.dataframe(df)

# Sidebar for user input
st.sidebar.header("Filter Options")
selected_fruits = st.sidebar.multiselect(
    "Select fruits to display",
    options=df['Fruit'].unique(),
    default=df['Fruit'].unique()
)

# Filter data based on selection
filtered_df = df[df['Fruit'].isin(selected_fruits)]

# Display filtered data
st.subheader("Filtered Dataset")
st.dataframe(filtered_df)

# Plotting
st.subheader("Quantity by Fruit")
fig, ax = plt.subplots()
ax.bar(filtered_df['Fruit'], filtered_df['Quantity'], color='skyblue')
ax.set_xlabel("Fruit")
ax.set_ylabel("Quantity")
ax.set_title("Quantity of Selected Fruits")
st.pyplot(fig)
