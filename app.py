import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("CARS.csv")

# App title
st.title("Car Brand & Horsepower Visualization")

# Show available brands in dropdown
brands = df["Make"].unique()
selected_brand = st.selectbox("Select a Car Brand", brands)

# Filter data for selected brand
s = df[df["Make"] == selected_brand]

# Plot
fig, ax = plt.subplots(figsize=(10, 6))
sb.barplot(x="Model", y="Horsepower", data=s, ax=ax)
plt.xticks(rotation=90)
plt.title(f"Models and Horsepower for {selected_brand}")

# Show plot in Streamlit
st.pyplot(fig)
