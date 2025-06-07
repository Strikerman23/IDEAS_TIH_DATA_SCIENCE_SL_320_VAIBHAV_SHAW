# IDEAS_TIH_ISI_Kolkata_DATA_SCIENCE_B_SL_320_VAIBHAV_SHAW
ASSIGNMENT: Create an Ingestion page which handles file uploading and uploads a csv file to a database and generate a summary report using ReportLab.

                                                    ASSIGNMENT
Overview of the Streamlit App: Interactive Data Explorer
This Streamlit app is a simple and interactive data exploration tool that allows users to filter and visualize data related to different fruits. Here's a breakdown of its functionality:

🔹 Dataset
A sample dataset is loaded using the load_data() function.

This dataset contains 3 columns:

Fruit: Names of fruits.

Quantity: Number of each fruit available.

Price: Price per unit of each fruit.

The dataset is displayed using st.dataframe() to allow interactive exploration.

🔹 Sidebar Filter
A sidebar widget allows the user to select one or more fruits from a list.

The selection is done via a multiselect dropdown.

By default, all fruits are selected.

🔹 Filtered Data Display
Based on the selected fruits from the sidebar, the app filters the dataset.

The filtered dataset is shown in another interactive table.

🔹 Data Visualization
A bar chart is generated using Matplotlib.

The chart visualizes the quantity of selected fruits.

The chart includes:

X-axis: Fruit names.

Y-axis: Quantities.

Title: "Quantity of Selected Fruits".

Color: Light blue bars (skyblue).


