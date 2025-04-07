import streamlit as st
from pathlib import Path
from pytest import fixture
from streamlit.runtime.state.safe_session_state import SafeSessionState
from streamlit.testing.v1 import AppTest


@fixture(scope="module")
def base_app_str():
    return Path("./sample_app.py").read_text()


@fixture(scope="module")
def app_no_detector(base_app_str):
    return AppTest.from_string(base_app_str)



def test_with_detector(base_app_str):
    app_str = base_app_str + "\nst_dialog_close_detector()"
    app = AppTest.from_string(app_str)
    app.button[0].click().run()



def test_no_detector(base_app_str):
    ...