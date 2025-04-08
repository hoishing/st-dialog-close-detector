# Streamlit Dialog Close Detector

> rerun streamlit app when dialog is closed

## The Problem

As of Streamlit v1.44, the official `st.dialog` won't be able to trigger app rerun if the user close the dialog by clicking outside the dialog or pressing escape key.

We can add a button inside the dialog to trigger rerun though, it will be nice if all widget states inside the dialog are automatically reflected on the main app when the dialog is closed, ie. app auto rerun when the dialog is close.

## The Solution

Use custom component to inject javacript for detecting the close of the dialog, and update the value of the custom component. The value update will automatically trigger an app rerun.

## Usage

- installation

`uv add st-dialog-close-detector`

- put it **anywhere** in your main stremlit app

```python
from st_dialog_close_detector import dialog_close_detector

dialog_close_detector()
```
