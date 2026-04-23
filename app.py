import streamlit as st
import sympy as sp
from sympy.parsing.sympy_parser import (
    parse_expr,
    standard_transformations,
    implicit_multiplication_application
)

st.title("🧮 Algebra Solver with Steps")

st.write("Enter an equation like: x^2 + 5x + 6 = 0")

transformations = standard_transformations + (implicit_multiplication_application,)

x = sp.symbols('x')

equation_input = st.text_input("Enter equation:")

if st.button("Solve"):
    try:
        equation_input = equation_input.replace("^", "**")
        left, right = equation_input.split("=")

        left_expr = parse_expr(left, transformations=transformations)
        right_expr = parse_expr(right, transformations=transformations)

        expr = left_expr - right_expr

        st.subheader("📘 Steps")

        # Step 1: Original equation
        st.write("1. Original equation:")
        st.latex(f"{sp.latex(left_expr)} = {sp.latex(right_expr)}")

        # Step 2: Move everything to one side
        st.write("2. Move everything to one side:")
        st.latex(f"{sp.latex(expr)} = 0")

        # Step 3: Show expanded form (important!)
        expanded = sp.expand(expr)
        st.write("3. Expanded form:")
        st.latex(sp.latex(expanded))

        # Step 4: Factor
        factored = sp.factor(expr)
        st.write("4. Factor (ontbinding):")
        st.latex(f"{sp.latex(expanded)} = {sp.latex(factored)}")

        # Step 5: Solve
        solutions = sp.solve(expr, x)

        st.write("5. Solve each factor:")
        for sol in solutions:
            st.latex(f"x = {sp.latex(sol)}")

        result_text = " or ".join([f"x = {sol}" for sol in solutions])
        st.success(f"Final Answer: {result_text}")

    except Exception:
        st.error("❌ Invalid equation. Try: x^2 + 5x + 6 = 0")

