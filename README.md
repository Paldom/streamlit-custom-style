# streamlit-custom-style
Sample streamlit app demonstrating official and unofficial custom styling options for your design system.

## Theming

Streamlit’s basic theming parameters are configured in `.streamlit/config.toml`. Learn more in the [Streamlit Theming Documentation](https://docs.streamlit.io/develop/concepts/configuration/theming).

```toml
[theme]
primaryColor="#5FB79B"
backgroundColor="#FFFFFF"
secondaryBackgroundColor="#F6F8FA"
textColor="#12283F"
font="sans serif"
```

## Logo

Streamlit supports displaying a logo in both the open and closed side menu:

```python
st.logo("images/logo.svg", icon_image="images/logo_closed.svg")
```

## Custom SCSS / CSS

A common approach is to replicate your theme parameters in a `style.scss`, compile it into CSS, and load it in each page using a helper function:

```python
with open("styles.css") as f:
    st.markdown(f"<style>\${f.read()}</style>", unsafe_allow_html=True)
```

> **Note:** This approach is not officially supported by Streamlit and may break with future version updates.

## Custom Fonts, Frameworks, and More

With the previous approach, you can include custom fonts or frameworks (e.g., Bootstrap) and more by injecting any HTML:

```python
st.markdown(
    """
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    """,
    unsafe_allow_html=True

)
```

## Buttons

Streamlit supports multiple button types out of the box: **"primary"**, **"secondary"**, or **"tertiary"**.  
Refer to the [Streamlit Button API](https://docs.streamlit.io/develop/api-reference/widgets/st.button) for details.

## Custom Key

To create additional styling alternatives for a component, add a custom key to the widget like this:

```python
st.button("Warning button", key="warning")
```

Access it froms scss:

```scss
.st-key-warning button 
```

This approach lets you implement a more detailed design system.

## Compile SCSS

```bash
brew install sassc
sassc styles.scss styles.css
```

## Run App

```bash
pip install streamlit
streamlit run Home.py
```

## Considerations

- Future Streamlit updates may alter or deprecate the CSS classes, potentially breaking your custom styles.
- Third-party Components may not match your custom design system’s styling without additional effort.