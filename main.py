import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore

# Inicializa Firebase (solo una vez)
if not firebase_admin._apps:
    cred = credentials.Certificate('ruta/a/tu/clave.json')
    firebase_admin.initialize_app(cred)
db = firestore.client()

st.title("Editor de Código HTML")

html_code = st.text_area("Pega aquí tu código HTML")

if st.button("Guardar en la nube"):
    doc_ref = db.collection('html_content').document('pagina')
    doc_ref.set({'html': html_code})
    st.success("Código guardado correctamente")

