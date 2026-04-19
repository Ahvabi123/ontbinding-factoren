import streamlit as st
from sympy import symbols, factor
from sympy.parsing.sympy_parser import (
    parse_expr, standard_transformations,
    implicit_multiplication_application
)

st.title("Kwadratische vergelijkingen (ontbinding factoren)")

x = symbols('x')
transformations = standard_transformations + (implicit_multiplication_application,)

expr_input = st.text_input("Voer een vergelijking in (bijv. x^2 + 5x + 6):")

if expr_input:
    try:
        # ^ vervangen door **
        expr_input = expr_input.replace("^", "**")

        expr = parse_expr(expr_input, transformations=transformations)

        st.write("**Origineel:**", expr)

        factored = factor(expr)

        st.write("**Ontbonden:**", factored)

    except Exception as e:
        st.error(f"Fout: {e}")
