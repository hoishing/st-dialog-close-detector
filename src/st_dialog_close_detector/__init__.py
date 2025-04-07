import streamlit.components.v1 as components


def dialog_close_detector(key: str = "dialog_close_detector", dev=False):
    opt = {"name": key}
    opt |= {"path": "frontend/dist"} if dev else {"url": "http://localhost:5173"}
    component_func = components.declare_component("dialog_close_detector", **opt)
    return component_func(key=key, default=False)
