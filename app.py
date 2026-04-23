import streamlit as st
import sympy as sp

st.title("🧮 Algebra Solver")

st.write("Type: x^2 + 5x + 6 = 0")

x = sp.symbols('x')

equation_input = st.text_input("Enter equation:")

if st.button("Solve"):
    try:
        if not equation_input:
            st.warning("Enter something first")
            st.stop()

        # Fix input
        eq = equation_input.replace("^", "**")
        eq = eq.replace(" ", "")

        # 👉 IMPORTANT FIX: manually add * between number and x
        import re
        eq = re.sub(r'(\d)(x)', r'\1*\2', eq)

        # Handle =
        if "=" in eq:
            left, right = eq.split("=")
        else:
            left = eq
            right = "0"

        left_expr = sp.sympify(left)
        right_expr = sp.sympify(right)

        expr = left_expr - right_expr

        st.subheader("📘 Steps")

        # 1 Original
        st.write("1. Original:")
        st.latex(f"{sp.latex(left_expr)} = {sp.latex(right_expr)}")

        # 2 Move
        st.write("2. Move to one side:")
        st.latex(f"{sp.latex(expr)} = 0")

        # 3 Expanded (this keeps your x²+5x+6!)
        expanded = sp.expand(expr)
        st.write("3. Expression:")
        st.latex(sp.latex(expanded))

        # 4 Factor
        factored = sp.factor(expr)
        st.write("4. Factor:")
        st.latex(f"{sp.latex(expanded)} = {sp.latex(factored)}")

        # 5 Solve
        solutions = sp.solve(expr, x)

        st.write("5. Solution:")
        for sol in solutions:
            st.latex(f"x = {sp.latex(sol)}")

        st.success(" or ".join([f"x = {s}" for s in solutions]))

    except Exception as e:
        st.error("Error:")
        st.code(str(e))
