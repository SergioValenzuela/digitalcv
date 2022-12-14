import streamlit as st
from pathlib import Path
from PIL import Image as im


# -- PATH SETTINGS --

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV-Sergio Valenzuela.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"

# -- GENERAL SETTINGS --

PAGE_TITLE = "Curriculum Digital | Sergio Valenzuela"
PAGE_ICON = "📝"
NAME = "Sergio Valenzuela"
DESCRIPTION = """
Ingeniero en Sistemas de Información | Ingeniero de Soporte.
"""
PHONE_NUMBER = '📱 (662) 479 2634'
EMAIL = "contacto@sergiovalenzuela.com.mx"

SOCIAL_MEDIA = {

    "Github": "https://github.com/sergiovalenzuela",
    "Twitter": "https://twitter.com/sergiovalnzla",
    "LinkedIn": "https://www.linkedin.com/in/sergiovalnzla/",
    "Instagram": "https://instagram.com/sergiovalnzla"
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF Y PROFILE PIC ---

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = im.open(profile_pic)


#--- PROFILE SECTION ---

col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)
with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.write(PHONE_NUMBER)
    st.write("📧", EMAIL)
    st.download_button(label="Descargar curriculum",
                      data=PDFbyte,
                      file_name=resume_file.name, 
                      mime="application/octet-stream",
                      )

# --- SOCIAL LINKS ---

st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
     cols[index].write(f"[{platform}]({link})")

# --- SKILS ---

st.write("#")
st.subheader("Experiencia, competencias y habilidades")
st.write("""

* ✅ +5 años de experiencia en soporte para los siguientes sectores:
    - ◾ Medios de comunicación
    - ◾ Tiendas de conveniencia
    - ◾ Grupos gasolineros.
* ✅ Conocimientos de automatización de reportes usando Python y Excel.
    - ◾ Librería Pandas.
    - ◾ Visualización de datos con framework Streamlit.
* ✅ Comunicación efectiva para soporte al cliente.
    - ◾ Habilidad de comunicación para trato con el usuario.
    - ◾ Soporte efectivo vía telefónica, correo y/o chat.
* ✅ Excelente miembro y mentor de equipo.
    - ◾ Ayuda y soporte efectivo a miembros del equipo de TI.
    - ◾ Coaching y mentoría para implementar la mejor solución.
* ✅ Experiencia en el uso de software para asistencia remota: 
    - ◾ Anydesk
    - ◾ TeamViewer
    - ◾ LogMeIn
* ✅ Manejo de herramientas de tickets como Freshdesk.
    - ◾ Prioridad a tickets que afecten venta y/o producción.

""")

# --- JOBS ---

st.write("#")
st.write("---")

st.subheader("Experiencia laboral")
st.write("👨‍💻", """**INGENIERO DE SOPORTE | Grupo Centra Empresarial**""")
st.write(" - 📅", "07/2019 - actual")

st.write("""

- ◾   Resuelvo incidencias del área de TI.
- ◾   Encargado de los reportes diarios que se envían a los diferentes departamentos para que sean analizados.
- ◾   Gestiono las tareas a realizar por medio de tickets para que sean atendidas en tiempo y forma.
- ◾   Apoyo a miembros del equipo de TI en la resolución de incidencias.
- ◾   Escalamiento de tickets con las áreas o proveedores correspondientes para su resolución.

""")

st.write("#")
st.write("👨‍💻", """**AUXILIAR DE SISTEMAS | Medio Informativo de Sonora**""")
st.write(" - 📅", "04/2017 - 06/2019")

st.write("""

- ◾ Implementé servidor con sistema operativo Windows Server.
- ◾ Gestioné uso y espacio de almacenamiento del servidor para las diferentes tareas que se realizaban.
- ◾ Realicé soporte a usuarios internos vía remota y/o presencial.

""")

st.write("---")
st.subheader("Proyectos")
st.write(""" 

* 🥇 Implementación de sistema de reconocimiento de spots publicitarios.

* 🥇 Implementación de nueva interface de comuniaciones para bombas despachadoras de gasolina en 4 estaciones gasolineras.

* 🥇 Implementación de nuevo sistema volumétrico en 9 estaciones gasolineras.

* 🥇 Proceso ETL para migración de datos de SQL 2014 a SQL 2019 y PostreSQL.

""")