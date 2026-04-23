import streamlit as st
import sympy as sp
from sympy.parsing.sympy_parser import (
    parse_expr,
    standard_transformations,
    implicit_multiplication_application
)

st.title("🧮 Algebra Solver with Steps")

st.write("Enter an equation like: x^2 + 5x + 6 = 0")

# Setup parsing (allows 5x instead of 5*x)
transformations = standard_transformations + (implicit_multiplication_application,)

x = sp.symbols('x')

equation_input = st.text_input("Enter equation:")

if st.button("Solve"):
    try:
        # Replace ^ with **
        equation_input = equation_input.replace("^", "**")

        # Split equation
        left, right = equation_input.split("=")

        # Parse expressions
        left_expr = parse_expr(left, transformations=transformations)
        right_expr = parse_expr(right, transformations=transformations)

        # Move everything to one side
        expr = left_expr - right_expr

        st.subheader("📘 Steps")

        # Step 1
        st.write(f"1. Move everything to one side:")
        st.latex(f"{sp.latex(left_expr)} = {sp.latex(right_expr)}")
        st.latex(f"\\Rightarrow {sp.latex(expr)} = 0")

        # Step 2: Factor
        factored = sp.factor(expr)
        st.write("2. Factor the equation:")
        st.latex(f"{sp.latex(expr)} = {sp.latex(factored)}")

        # Step 3: Solve
        solutions = sp.solve(expr, x)

        st.write("3. Solve each factor:")
        for sol in solutions:
            st.latex(f"x = {sp.latex(sol)}")

        # Final answer
        result_text = " or ".join([f"x = {sol}" for sol in solutions])
        st.success(f"Final Answer: {result_text}")

    except Exception:
        st.error("❌ Invalid equation. Try: x^2 + 5x + 6 = 0")
