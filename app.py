import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Function to load the dataset
@st.cache
def load_data(uploaded_file):
    data = pd.read_csv(uploaded_file, parse_dates=['Date'])
    return data

# Title of the app
st.title("Sales Data Analysis App")

# Upload the dataset through sidebar
uploaded_file = st.sidebar.file_uploader("Upload your CSV file", type=["csv"])

# Check if file is uploaded
if uploaded_file is not None:
    data = load_data(uploaded_file)
    
    # Filter data for a specific date (2011-01-01)
    selected_date = pd.to_datetime("2011-01-01")
    filtered_data = data[data['Date'] == selected_date]
    
    # Create columns for layout
    col1, col2 = st.columns(2)

    # Part 1: Display uploaded data and filtered data for 2011-01-01 in a single row
    with col1:
        st.subheader("Uploaded Data")
        st.write(data.head())  # Display the first few rows of the uploaded data
        
    with col2:
        st.subheader(f"Filtered Data for {selected_date.date()}")
        st.write(filtered_data)  # Display filtered data for the selected date
    
    # Part 2: Display Sales Revenue by Product and Sales Trends in the second row
    col3, col4 = st.columns(2)

    with col3:
        st.subheader("Sales Revenue by Product")
        sales_summary = filtered_data.groupby('Product')['Revenue'].sum().reset_index()
        st.bar_chart(sales_summary.set_index('Product')['Revenue'])

    with col4:
        st.subheader("Sales Trends Over Time")
        sales_trends = data.groupby('Date')['Revenue'].sum().reset_index()
        st.line_chart(sales_trends.set_index('Date')['Revenue'])

else:
    st.sidebar.write("Please upload a CSV file to get started.")
