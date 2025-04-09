import random
import streamlit as st
from st_dialog_close_detector import dialog_close_detector

sess = st.session_state


@st.dialog("my modal")
def my_modal():
    if st.button("generate number"):
        sess.num = random.randint(0, 100)
        st.write("random number: ", sess.num)


if st.button("show modal", key="show-toggle-button"):
    my_modal()

st.write("")
st.write("")
st.write("randon number below will be updated when the dialog is closed")
dialog_close_detector()
st.write("number in dialog: ", sess.get("num"))
