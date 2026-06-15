import streamlit as st
import pandas as pd

df = pd.read_csv("dataset\\ONINE_FOOD_DELIVERY_ANALYSIS.CSV")

st.set_page_config(page_title="Food Delivery Dashboard", layout="wide")

st.title("🍔 Online Food Delivery Analysis Dashboard")

st.subheader("Dataset Preview")
st.dataframe(df.head())

st.subheader("📊 Key Metrics")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Orders", len(df))

with col2:
    st.metric("Total Revenue", f"₹{df['Final_Amount'].sum():,.0f}")

with col3:
    st.metric("Average Order Value", f"₹{df['Order_Value'].mean():.2f}")

st.subheader("🍽 Top Restaurants")
st.bar_chart(df["Restaurant_Name"].value_counts().head(10))

st.subheader("💳 Payment Mode Distribution")
st.bar_chart(df["Payment_Mode"].value_counts())

st.subheader("🏙 Orders by City")
st.bar_chart(df["City"].value_counts().head(10))

st.success("Dashboard Loaded Successfully!")