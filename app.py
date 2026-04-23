import streamlit as st
import sympy as sp
from sympy.parsing.sympy_parser import (
    parse_expr,
    standard_transformations,
    implicit_multiplication_application
)

st.title("🧮 Algebra Solver with Steps")

st.write("Type something like: x^2 + 5x + 6 = 0")

# Allow 5x instead of 5*x
transformations = standard_transformations + (implicit_multiplication_application,)

x = sp.symbols('x')

equation_input = st.text_input("Enter equation:")

if st.button("Solve"):
    try:
        if equation_input.strip() == "":
            st.warning("⚠️ Please enter an equation")
            st.stop()

        # Replace ^ with **
        eq = equation_input.replace("^", "**")

        # If no '=' → assume = 0
        if "=" in eq:
            left, right = eq.split("=")
        else:
            left = eq
            right = "0"

        left_expr = parse_expr(left, transformations=transformations)
        right_expr = parse_expr(right, transformations=transformations)

        expr = left_expr - right_expr

        st.subheader("📘 Steps")

        # 1. Original
        st.write("1. Original equation:")
        st.latex(f"{sp.latex(left_expr)} = {sp.latex(right_expr)}")

        # 2. Move to one side
        st.write("2. Move everything to one side:")
        st.latex(f"{sp.latex(expr)} = 0")

        # 3. Expanded (your important part)
        expanded = sp.expand(expr)
        st.write("3. Expression (expanded):")
        st.latex(sp.latex(expanded))

        # 4. Factor
        factored = sp.factor(expr)
        st.write("4. Factor (ontbinding factoren):")
        st.latex(f"{sp.latex(expanded)} = {sp.latex(factored)}")

        # 5. Solve
        solutions = sp.solve(expr, x)

        if solutions:
            st.write("5. Solutions:")
            for sol in solutions:
                st.latex(f"x = {sp.latex(sol)}")

            result_text = " or ".join([f"x = {sol}" for sol in solutions])
            st.success(f"Final Answer: {result_text}")
        else:
            st.warning("No solutions found")

    except Exception as e:
        st.error("❌ Something went wrong")
        st.code(str(e))
