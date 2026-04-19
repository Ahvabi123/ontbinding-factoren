import streamlit as st
from sympy import symbols, factor, simplify
from sympy.parsing.sympy_parser import (
    parse_expr,
    standard_transformations,
    implicit_multiplication_application
)

# Title
st.title("🔢 Kwadratische vergelijkingen - ontbinden in factoren")

st.write("Voer een algebraïsche uitdrukking in en zie meteen de ontbinding in factoren.")

# Symbol
x = symbols('x')

# Better parsing settings
transformations = standard_transformations + (implicit_multiplication_application,)

# Examples for classmates
st.markdown("### 📌 Voorbeelden:")
st.code("x^2 + 5x + 6")
st.code("x^2 - 9")
st.code("2x^2 + 7x + 3")

# Input
expr_input = st.text_input("✏️ Voer je vergelijking in:")

if expr_input:
    try:
        # Replace ^ with **
        expr_input = expr_input.replace("^", "**")

        # Parse expression
        expr = parse_expr(expr_input, transformations=transformations)

        st.subheader("📥 Invoer")
        st.latex(expr)

        # Simplify (extra improvement)
        simplified = simplify(expr)
        factored = factor(simplified)

        st.subheader("📤 Resultaat")
        st.latex(factored)

        # Nice explanation
        if str(expr) == str(factored):
            st.info("Deze uitdrukking kan niet verder ontbonden worden.")
        else:
            st.success("Dit is de ontbonden vorm!")

    except Exception:
        st.error("❌ Oeps! Controleer je invoer. Gebruik bijvoorbeeld: x^2 + 5x + 6")
