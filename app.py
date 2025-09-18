import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("Sales Dashboard 📊")

# Upload CSV file
uploaded_file = st.file_uploader("Upload your sales CSV file", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("📌 Data Preview")
    st.write(df.head())

    st.subheader("📌 Summary Statistics")
    st.write(df.describe())

    # Total Sales
    total_sales = df["Sales"].sum()
    st.metric("💰 Total Sales", f"${total_sales}")

    # Sales by Category
    st.subheader("📌 Sales by Category")
    sales_by_cat = df.groupby("Category")["Sales"].sum()

    fig, ax = plt.subplots()
    sales_by_cat.plot(kind="bar", ax=ax)
    st.pyplot(fig)

    # Sales Trend
    st.subheader("📌 Sales Trend Over Time")
    df["Date"] = pd.to_datetime(df["Date"])
    sales_trend = df.groupby("Date")["Sales"].sum()

    fig2, ax2 = plt.subplots()
    sales_trend.plot(ax=ax2, marker="o")
    st.pyplot(fig2)
