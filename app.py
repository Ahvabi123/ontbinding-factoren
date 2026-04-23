
import streamlit as st
import sympy as sp

st.title("🧮 Algebra Solver")

st.write("Enter an equation like: x^2 + 5*x + 6 = 0")

# Define variable
x = sp.symbols('x')

# Input field
equation_input = st.text_input("Enter equation:")

if st.button("Solve"):
    try:
        # Replace ^ with ** for Python
        equation_input = equation_input.replace("^", "**")

        # Split left and right side
        left, right = equation_input.split("=")

        # Convert to sympy expressions
        left_expr = sp.sympify(left)
        right_expr = sp.sympify(right)

        # Move everything to one side
        equation = sp.Eq(left_expr, right_expr)

        # Solve
        solutions = sp.solve(equation, x)

        if solutions:
            result_text = " or ".join([f"x = {sol}" for sol in solutions])
            st.success(result_text)
        else:
            st.warning("No solution found")

    except Exception as e:
        st.error("❌ Invalid equation. Try something like: x^2 + 5*x + 6 = 0")
