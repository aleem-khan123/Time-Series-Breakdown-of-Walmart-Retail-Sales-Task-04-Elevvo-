import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load and prepare the dataset
train = pd.read_csv("train.csv")
train['Date'] = pd.to_datetime(train['Date'])
train = train.sort_values('Date').reset_index(drop=True)
train.set_index('Date', inplace=True)

# Dashboard title and intro
st.title("Walmart Sales Dashboard")
st.write("This dashboard allows exploration of sales trends across stores and departments with holiday comparisons.")

# Sidebar filters
stores = train['Store'].unique()
depts = train['Dept'].unique()

selected_store = st.sidebar.selectbox("Select Store", options=["All"] + list(stores))
selected_dept = st.sidebar.selectbox("Select Department", options=["All"] + list(depts))
holiday_filter = st.sidebar.radio("Filter by Holiday", options=["All", "Holiday Only", "Non-Holiday"])

# Apply filters to the dataset
data = train.copy()
if selected_store != "All":
    data = data[data['Store'] == selected_store]
if selected_dept != "All":
    data = data[data['Dept'] == selected_dept]
if holiday_filter == "Holiday Only":
    data = data[data['IsHoliday'] == True]
elif holiday_filter == "Non-Holiday":
    data = data[data['IsHoliday'] == False]

# Monthly sales trend (line plot)
st.subheader("Sales Trend Over Time")
monthly_sales = data['Weekly_Sales'].resample('M').sum()

fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(monthly_sales.index, monthly_sales.values, marker='o')
ax.set_title("Monthly Sales Trend")
ax.set_xlabel("Date")
ax.set_ylabel("Total Sales")
st.pyplot(fig)

# Store comparison (bar chart)
if selected_store == "All":
    st.subheader("Total Sales by Store")
    store_sales = train.groupby('Store')['Weekly_Sales'].sum().sort_values(ascending=False)
    st.bar_chart(store_sales)

# Holiday vs Non-Holiday impact
st.subheader("Holiday Impact on Sales")
holiday_sales = data.groupby('IsHoliday')['Weekly_Sales'].mean()
st.bar_chart(holiday_sales)
