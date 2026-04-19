import streamlit as st
from sympy import symbols, factor
from sympy.parsing.sympy_parser import (
    parse_expr, standard_transformations,
    implicit_multiplication_application
)

st.title("Kwadratische vergelijkingen (met uitleg)")

x = symbols('x')
transformations = standard_transformations + (implicit_multiplication_application,)

expr_input = st.text_input("Voer een vergelijking in (bijv. x^2 + 5x + 6):")

if expr_input:
    try:
        expr_input = expr_input.replace("^", "**")
        expr = parse_expr(expr_input, transformations=transformations)

        st.subheader("📥 Origineel")
        st.write(expr)

        factored = factor(expr)

        st.subheader("📤 Ontbinding")
        st.write(factored)

        # Simple explanation
        st.subheader("📌 Uitleg (idee)")
        st.write("We zoeken twee getallen die:")
        st.write("- Vermenigvuldigen tot de laatste term")
        st.write("- Optellen tot de middelste term")

    except Exception:
        st.error("❌ Ongeldige invoer")
