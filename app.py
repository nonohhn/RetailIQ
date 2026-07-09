import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("RetailIQ")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Sales Analysis",
        "Customer Analysis",
        "Product Analysis",
        "Profit Analysis",
        "Regional Analysis",
        "Data Explorer",
        "About",
    ]
)

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("data/Sample - Superstore.csv", encoding="latin1")

# Convert Order Date to datetime
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Create Month-Year column
df["Month-Year"] = df["Order Date"].dt.to_period("M").astype(str)

# -----------------------------
# Dashboard Page
# -----------------------------
if page == "Dashboard":
    st.title("Dashboard")

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    st.subheader("Dataset Information")
    st.write(f"Rows and Columns: {df.shape}")
    st.write("Column Names:")
    st.write(list(df.columns))
    st.write("Data Types:")
    st.write(df.dtypes)

    st.subheader("Missing Values")
    st.write(df.isnull().sum())

    st.subheader("Duplicate Rows")
    duplicates = df.duplicated().sum()
    st.write(f"Number of duplicate rows: {duplicates}")

    st.subheader("Key Performance Indicators")

    total_sales = df["Sales"].sum()
    total_profit = df["Profit"].sum()
    total_orders = df["Order ID"].nunique()
    average_order_value = total_sales / total_orders

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Sales", f"${total_sales:,.2f}")

    with col2:
        st.metric("Total Profit", f"${total_profit:,.2f}")

    with col3:
        st.metric("Total Orders", total_orders)

    with col4:
        st.metric("Average Order Value", f"${average_order_value:,.2f}")

    st.subheader("Monthly Sales Trend")

    monthly_sales = df.groupby("Month-Year")["Sales"].sum().reset_index()

    fig_monthly_sales = px.line(
        monthly_sales,
        x="Month-Year",
        y="Sales",
        title="Monthly Sales Trend",
        markers=True
    )

    st.plotly_chart(fig_monthly_sales, use_container_width=True)

# -----------------------------
# Other Pages
# -----------------------------
elif page == "Sales Analysis":
    st.title("Sales Analysis")
    st.write("We will build this page next.")

elif page == "Customer Analysis":
    st.title("Customer Analysis")
    st.write("We will build this page later.")

elif page == "Product Analysis":
    st.title("Product Analysis")
    st.write("We will build this page later.")

elif page == "Profit Analysis":
    st.title("Profit Analysis")
    st.write("We will build this page later.")

elif page == "Regional Analysis":
    st.title("Regional Analysis")
    st.write("We will build this page later.")

elif page == "Data Explorer":
    st.title("Data Explorer")
    st.dataframe(df)

elif page == "About":
    st.title("About")
    st.write("RetailIQ is an interactive retail sales analytics dashboard built with Python, Pandas, Plotly, and Streamlit.")