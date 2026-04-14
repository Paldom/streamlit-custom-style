from pathlib import Path
import streamlit as st


def _load_css(path: str | Path = "assets/styles.css") -> None:
    css_path = Path(path)
    if css_path.exists():
        st.html(f"<style>{css_path.read_text(encoding='utf-8')}</style>")


def init_page(
    page_title: str = "Streamlit Custom UI Design",
    page_icon: str = "images/logo_closed.svg",
    layout: str = "wide",
    sidebar_state: str = "expanded",
    load_css: bool = True,
) -> None:
    st.set_page_config(
        page_title=page_title,
        page_icon=page_icon,
        layout=layout,
        initial_sidebar_state=sidebar_state,
    )

    if load_css:
        _load_css()

    st.logo("images/logo.svg", icon_image="images/logo_closed.svg")
    st.sidebar.markdown("Hi!")
