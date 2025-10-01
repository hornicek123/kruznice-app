
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from fpdf import FPDF
import io

# Sidebar - Author and technologies
st.sidebar.title("O autorovi")
st.sidebar.markdown("**Jméno:** Lukáš Novák")
st.sidebar.markdown("**Kontakt:** lukas.novak@example.com")
st.sidebar.markdown("**Použité technologie:** Streamlit, Matplotlib, NumPy, FPDF")

# Hlavní nadpis
st.title("Body na kružnici – Webová aplikace")

# Uživatelské vstupy
st.header("Zadejte parametry kružnice")
x_center = st.number_input("Souřadnice středu X (m)", value=0.0)
y_center = st.number_input("Souřadnice středu Y (m)", value=0.0)
radius = st.number_input("Poloměr kružnice (m)", min_value=0.1, value=1.0)
num_points = st.number_input("Počet bodů na kružnici", min_value=1, step=1, value=8)
color = st.color_picker("Barva bodů", "#FF0000")

# Výpočet bodů na kružnici
angles = np.linspace(0, 2 * np.pi, int(num_points), endpoint=False)
x_points = x_center + radius * np.cos(angles)
y_points = y_center + radius * np.sin(angles)

# Vykreslení grafu
st.header("Vykreslení kružnice s body")
fig, ax = plt.subplots()
ax.scatter(x_points, y_points, color=color, label="Body")
ax.set_aspect('equal')
ax.set_xlabel("X (m)")
ax.set_ylabel("Y (m)")
ax.set_title("Body na kružnici")
ax.grid(True)
ax.axhline(0, color='gray', linewidth=0.5)
ax.axvline(0, color='gray', linewidth=0.5)
st.pyplot(fig)

# Generování PDF
st.header("Export do PDF")

def generate_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Body na kružnici – Výstup", ln=True, align='C')
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Střed kružnice: ({x_center}, {y_center}) m", ln=True)
    pdf.cell(200, 10, txt=f"Poloměr: {radius} m", ln=True)
    pdf.cell(200, 10, txt=f"Počet bodů: {num_points}", ln=True)
    pdf.cell(200, 10, txt=f"Barva bodů: {color}", ln=True)
    pdf.ln(10)
    pdf.cell(200, 10, txt="Autor: Lukáš Novák", ln=True)
    pdf.cell(200, 10, txt="Kontakt: lukas.novak@example.com", ln=True)

    return pdf.output(dest='S').encode('latin1')

if st.button("Stáhnout PDF"):
    pdf_bytes = generate_pdf()
    st.download_button(label="📄 Stáhnout PDF", data=pdf_bytes, file_name="kruznice_vystup.pdf", mime="application/pdf")

# Výzva k nahrání na GitHub
st.markdown("---")
st.subheader("Nahrání na GitHub")
st.markdown("1. Založ si účet na [GitHubu](https://github.com)")
st.markdown("2. Vytvoř nový repozitář (např. `kruznice-app`)")
st.markdown("3. Nahraj tento soubor `kruznice_app.py`")
st.markdown("4. Propoj GitHub se [Streamlit Cloud](https://streamlit.io/cloud) a nasazuj aplikaci online")
