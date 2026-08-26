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
df = pd.read_csv(
    "data/Sample - Superstore.csv",
    encoding="latin1"
)

# Convert Order Date to datetime
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Create Month-Year column
df["Month-Year"] = df["Order Date"].dt.to_period("M").astype(str)

# Create Year column
df["Year"] = df["Order Date"].dt.year

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

    # -----------------------------
    # KPI Section
    # -----------------------------
    st.subheader("Key Performance Indicators")

    total_sales = df["Sales"].sum()
    total_profit = df["Profit"].sum()
    total_orders = df["Order ID"].nunique()
    average_order_value = total_sales / total_orders

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Total Sales",
            f"${total_sales:,.2f}"
        )

    with col2:
        st.metric(
            "Total Profit",
            f"${total_profit:,.2f}"
        )

    with col3:
        st.metric(
            "Total Orders",
            total_orders
        )

    with col4:
        st.metric(
            "Average Order Value",
            f"${average_order_value:,.2f}"
        )

    # -----------------------------
    # Monthly Sales Trend
    # -----------------------------
    st.subheader("Monthly Sales Trend")

    monthly_sales = (
        df.groupby("Month-Year")["Sales"]
        .sum()
        .reset_index()
    )

    fig_monthly_sales = px.line(
        monthly_sales,
        x="Month-Year",
        y="Sales",
        title="Monthly Sales Trend",
        markers=True
    )

    st.plotly_chart(
        fig_monthly_sales,
        use_container_width=True
    )

# -----------------------------
# Sales Analysis Page
# -----------------------------
elif page == "Sales Analysis":
    st.title("Sales Analysis")

    # -----------------------------
    # Year Filter
    # -----------------------------
    selected_year = st.selectbox(
        "Select Year",
        sorted(df["Year"].unique())
    )
    # Category Filter
    selected_categories = st.multiselect(
    "Select Category",
    options=sorted(df["Category"].unique()),
    default=sorted(df["Category"].unique())
)


    
    selected_regions = st.multiselect(
    "Select Region",
    options=sorted(df["Region"].unique()),
    default=sorted(df["Region"].unique())
)
    

    # -----------------------------
    # Sales by Region
    # -----------------------------
    st.subheader("Sales by Region")

    sales_by_region = (
        filtered_df.groupby("Region")["Sales"]
        .sum()
        .reset_index()
        .sort_values(
            by="Sales",
            ascending=False
        )
    )

    st.dataframe(sales_by_region)

    fig_region = px.bar(
        sales_by_region,
        x="Region",
        y="Sales",
        title=f"Total Sales by Region - {selected_year}"
    )

    st.plotly_chart(
        fig_region,
        use_container_width=True
    )

    # -----------------------------
    # Sales by Category
    # -----------------------------
    st.subheader("Sales by Category")

    sales_by_category = (
        filtered_df.groupby("Category")["Sales"]
        .sum()
        .reset_index()
        .sort_values(
            by="Sales",
            ascending=False
        )
    )

    st.dataframe(sales_by_category)

    fig_category = px.bar(
        sales_by_category,
        x="Category",
        y="Sales",
        title=f"Total Sales by Category - {selected_year}"
    )

    st.plotly_chart(
        fig_category,
        use_container_width=True
    )

    # -----------------------------
    # Sales by Segment
    # -----------------------------
    st.subheader("Sales by Segment")

    sales_by_segment = (
        filtered_df.groupby("Segment")["Sales"]
        .sum()
        .reset_index()
        .sort_values(
            by="Sales",
            ascending=False
        )
    )

    st.dataframe(sales_by_segment)

    fig_segment = px.bar(
        sales_by_segment,
        x="Segment",
        y="Sales",
        title=f"Total Sales by Segment - {selected_year}"
    )

    st.plotly_chart(
        fig_segment,
        use_container_width=True
    )

    # -----------------------------
    # Sales by State
    # -----------------------------
    st.subheader("Top 10 States by Sales")

    sales_by_state = (
        filtered_df.groupby("State")["Sales"]
        .sum()
        .reset_index()
        .sort_values(
            by="Sales",
            ascending=False
        )
    )

    top_10_states = sales_by_state.head(10)

    st.dataframe(top_10_states)

    fig_state = px.bar(
        top_10_states,
        x="Sales",
        y="State",
        orientation="h",
        title=f"Top 10 States by Sales - {selected_year}"
    )

    fig_state.update_layout(
        yaxis={
            "categoryorder": "total ascending"
        }
    )

    st.plotly_chart(
        fig_state,
        use_container_width=True
    )

# -----------------------------
# Customer Analysis Page
# -----------------------------
elif page == "Customer Analysis":
    st.title("Customer Analysis")
    st.write("Coming Soon.")

# -----------------------------
# Product Analysis Page
# -----------------------------
elif page == "Product Analysis":
    st.title("Product Analysis")
    st.write("Coming Soon.")

# -----------------------------
# Profit Analysis Page
# -----------------------------
elif page == "Profit Analysis":
    st.title("Profit Analysis")
    st.write("Coming Soon.")

# -----------------------------
# Regional Analysis Page
# -----------------------------
elif page == "Regional Analysis":
    st.title("Regional Analysis")
    st.write("Coming Soon.")

# -----------------------------
# Data Explorer Page
# -----------------------------
elif page == "Data Explorer":
    st.title("Data Explorer")
    st.dataframe(df)

# -----------------------------
# About Page
# -----------------------------
elif page == "About":
    st.title("About")

    st.write(
        "RetailIQ is an interactive retail sales analytics dashboard "
        "built with Python, Pandas, Plotly, and Streamlit."
    )