import streamlit as st
import math

# Page Config
st.set_page_config(
    page_title="Advanced Calculator",
    page_icon="🧮",
    layout="centered"
)

# Session State for History
if "history" not in st.session_state:
    st.session_state.history = []

st.title("🧮 Advanced Calculator")
st.markdown("Perform Basic, Advanced and Scientific Calculations")

# Sidebar
st.sidebar.header("Settings")

operation = st.sidebar.selectbox(
    "Choose Operation",
    [
        "Addition",
        "Subtraction",
        "Multiplication",
        "Division",
        "Power",
        "Square Root",
        "Factorial",
        "Sin",
        "Cos",
        "Tan",
        "Log10",
        "Natural Log"
    ]
)

# Inputs
num1 = st.number_input("Enter First Number", value=0.0)

if operation not in [
    "Square Root",
    "Factorial",
    "Sin",
    "Cos",
    "Tan",
    "Log10",
    "Natural Log"
]:
    num2 = st.number_input("Enter Second Number", value=0.0)

# Calculate Button
if st.button("Calculate"):

    try:

        if operation == "Addition":
            result = num1 + num2
            expression = f"{num1} + {num2}"

        elif operation == "Subtraction":
            result = num1 - num2
            expression = f"{num1} - {num2}"

        elif operation == "Multiplication":
            result = num1 * num2
            expression = f"{num1} × {num2}"

        elif operation == "Division":

            if num2 == 0:
                st.error("Cannot divide by zero.")
                st.stop()

            result = num1 / num2
            expression = f"{num1} ÷ {num2}"

        elif operation == "Power":
            result = num1 ** num2
            expression = f"{num1}^{num2}"

        elif operation == "Square Root":

            if num1 < 0:
                st.error("Negative number not allowed.")
                st.stop()

            result = math.sqrt(num1)
            expression = f"√{num1}"

        elif operation == "Factorial":

            if num1 < 0:
                st.error("Factorial only works for positive numbers.")
                st.stop()

            result = math.factorial(int(num1))
            expression = f"{int(num1)}!"

        elif operation == "Sin":
            result = math.sin(math.radians(num1))
            expression = f"sin({num1})"

        elif operation == "Cos":
            result = math.cos(math.radians(num1))
            expression = f"cos({num1})"

        elif operation == "Tan":
            result = math.tan(math.radians(num1))
            expression = f"tan({num1})"

        elif operation == "Log10":

            if num1 <= 0:
                st.error("Number must be greater than zero.")
                st.stop()

            result = math.log10(num1)
            expression = f"log10({num1})"

        elif operation == "Natural Log":

            if num1 <= 0:
                st.error("Number must be greater than zero.")
                st.stop()

            result = math.log(num1)
            expression = f"ln({num1})"

        st.success(f"Result = {result}")

        st.session_state.history.append(
            f"{expression} = {result}"
        )

    except Exception as e:
        st.error(f"Error: {e}")

# Clear History
if st.button("Clear History"):
    st.session_state.history = []

# History Section
st.subheader("Calculation History")

for item in reversed(st.session_state.history):
    st.write(item)
