from fastapi import FastAPI

# Create a FastAPI instance
app = FastAPI()

# Define a GET endpoint for calculating savings
@app.get("/calculate")
def calculate_savings(income: float, expense: float):
    savings = income - expense
    return {"income": income, "expense": expense, "savings": savings}