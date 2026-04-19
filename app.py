
          import streamlit as st
from sympy import symbols, factor, expand
from sympy.parsing.sympy_parser import (
    parse_expr, standard_transformations,
    implicit_multiplication_application
)

st.title("🔢 Kwadratische vergelijkingen (met stappen)")

x = symbols('x')
transformations = standard_transformations + (implicit_multiplication_application,)

expr_input = st.text_input("Voer een vergelijking in (bijv. x^2 + 5x + 6):")

if expr_input:
    try:
        expr_input = expr_input.replace("^", "**")
        expr = parse_expr(expr_input, transformations=transformations)

        st.subheader("📥 Origineel")
        st.latex(expr)

        # Expand to standard form ax^2 + bx + c
        expr_expanded = expand(expr)

        st.subheader("📌 Stap 1: Standaardvorm")
        st.latex(expr_expanded)

        # Get coefficients
        a = expr_expanded.coeff(x, 2)
        b = expr_expanded.coeff(x, 1)
        c = expr_expanded.coeff(x, 0)

        st.write(f"a = {a}, b = {b}, c = {c}")

        # Discriminant
        D = b**2 - 4*a*c

        st.subheader("📌 Stap 2: Discriminant")
        st.latex(f"D = b^2 - 4ac = {D}")

        # Factor result
        factored = factor(expr_expanded)

        st.subheader("📤 Ontbinding")
        st.latex(factored)

        # Extra explanation
        if D < 0:
            st.info("Geen reële oplossingen (D < 0)")
        elif D == 0:
            st.info("1 oplossing (dubbele wortel)")
        else:
            st.success("2 oplossingen → kan ontbonden worden")

    except Exception:
        st.error("❌ Ongeldige invoer. Probeer iets zoals: x^2 + 5x + 6")
