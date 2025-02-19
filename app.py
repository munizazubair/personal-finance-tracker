import streamlit as st
import requests
import matplotlib.pyplot as plt
from io import BytesIO

API_URL = "https://c6aa-2400-9fc0-5-3ab-a823-98c2-e874-1ddf.ngrok-free.app"

st.title("📊 Personal Finance Tracker")

# Create input fields for monthly income and expense
income = st.number_input("Enter your Monthly Income:", min_value=0.0)
expense = st.number_input("Enter your Monthly Expense:", min_value=0.0)

if st.button("Calculate Savings"):
# Send a GET request to the FastAPI backend with income and expense as parameters
    response = requests.get(f"{API_URL}/calculate", params={"income": income, "expense": expense})
    if response.status_code == 200:
        data = response.json()
# Display the calculated savings to the user
        st.write(f"💰 Your Monthly Savings: **{data['savings']}**")

# Create a bar chart to visualize income, expense, and savings
        fig, ax = plt.subplots()
        ax.bar(["Income", "Expense", "Savings"], [data["income"], data["expense"], data["savings"]], color=["green", "red", "blue"])
        ax.set_title("Income vs Expense vs Savings")
        st.pyplot(fig)

# Save the chart as a PNG image in memory
        img_bytes = BytesIO()
        fig.savefig(img_bytes, format="png")
        img_bytes.seek(0)

# Add a download button for the chart
        st.download_button(
            label="📥 Download Graph",
            data=img_bytes,
            file_name="finance_chart.png",
            mime="image/png"
        )
    else:
# Display an error message if the request fails
        st.error("Error calculating savings!")
