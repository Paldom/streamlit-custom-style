from streamlit.testing.v1 import AppTest


def run_page(path: str):
    at = AppTest.from_file(path)
    at.run()
    assert not at.exception
    return at


def test_home_page_runs():
    at = run_page("Home.py")
    assert at.title[0].value.startswith("Welcome")


def test_text_page_runs():
    run_page("pages/01_Text.py")


def test_input_page_runs():
    at = run_page("pages/02_Input.py")
    labels = [button.label for button in at.button]
    assert "Warning" in labels


def test_data_page_runs():
    run_page("pages/03_Data.py")


def test_chart_page_runs():
    run_page("pages/04_Chart.py")


def test_chat_page_runs():
    run_page("pages/05_Chat.py")


def test_status_page_runs():
    run_page("pages/06_Status.py")
