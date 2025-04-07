import streamlit as st
from st_dialog_close_detector import dialog_close_detector

sess = st.session_state


@st.dialog("my modal", width="large")
def my_modal():
    sess.dialog_toggle = st.toggle("toggle", value=sess.get("dialog_toggle", False))


if st.button("show modal"):
    my_modal()


st.write(f"dialog_toggle: {sess.get('dialog_toggle')}")
