# streamlit-custom-style

A reference Streamlit app showing the modern styling stack: reusable theme config, light/dark and sidebar theming, stable shared page bootstrap, minimal keyed CSS, and CI-backed regression protection.

Tested with **Streamlit 1.55.x**.

## Styling layers

This repo demonstrates four styling layers, ordered from most stable to least:

| Level | Technique | Stability | Where |
|-------|-----------|-----------|-------|
| 1 | Native theme config | Highest | `.streamlit/brand-theme.toml` |
| 2 | Shared bootstrap (`st.set_page_config`, `st.logo`) | High | `helpers.py` |
| 3 | Keyed CSS (`.st-key-*`) | Medium | `assets/styles.css` |
| 4 | DOM-targeted CSS / framework injection | Lowest | avoid unless necessary |

**Use layer 1 for everything you can. Drop to layer 3 only for custom component variants that config cannot express. Avoid layer 4.**

## 1. Theme config (layer 1)

All colors, fonts, borders, chart palettes, light/dark modes, and sidebar theming are defined in a reusable theme file:

`.streamlit/config.toml` references the theme:

```toml
[server]
enableStaticServing = true

[theme]
base = ".streamlit/brand-theme.toml"
```

`.streamlit/brand-theme.toml` contains the full visual system:

```toml
[theme]
base = "light"
font = "Manrope, sans-serif"
primaryColor = "#5FB79B"
backgroundColor = "#FFFFFF"
textColor = "#12283F"
# ... full token set including sidebar, dark mode, chart colors
```

This file can be shared across multiple apps for consistent branding.

### Custom fonts

Fonts are self-hosted in `static/fonts/` and loaded natively:

```toml
[[theme.fontFaces]]
family = "Manrope"
url = "app/static/fonts/Manrope-VariableFont_wght.ttf"
style = "normal"
```

This avoids Google Fonts CDN dependencies and the privacy/compliance risks they carry.

### Light/dark themes

Both are defined in `brand-theme.toml`:

```toml
[theme]
primaryColor = "#5FB79B"
backgroundColor = "#FFFFFF"

[theme.dark]
primaryColor = "#7CCDB1"
backgroundColor = "#0E1117"
```

Users can switch between them in the Streamlit settings menu.

### Sidebar theming

```toml
[theme.sidebar]
backgroundColor = "#12283F"
textColor = "#F8FAFC"
```

## 2. Shared bootstrap (layer 2)

Every page calls `init_page()` from `helpers.py`, which centralizes:

- `st.set_page_config()` with per-page title
- CSS loading via `st.html()` (not `st.markdown(..., unsafe_allow_html=True)`)
- `st.logo()` for sidebar branding

```python
from helpers import init_page
init_page(page_title="Input Elements")
```

## 3. Keyed CSS (layer 3)

Custom component variants use Streamlit's `key` parameter, which generates a stable `.st-key-*` CSS class:

```python
st.button("Warning", key="warning")
st.button("Success", key="success")
st.button("Outline", key="outline")

with st.container(key="card"):
    st.write("Card content")
```

```css
.st-key-warning button {
  background-color: #C14545;
  color: #FFFFFF;
}
```

This is the most stable CSS approach because the `key` attribute is user-controlled and won't change with Streamlit upgrades.

## Logo

```python
st.logo("images/logo.svg", icon_image="images/logo_closed.svg")
```

## Buttons

Streamlit supports `primary`, `secondary`, and `tertiary` button types natively. Use keyed CSS only for additional brand variants (warning, success, outline).

## Claude Code skill

This repo includes a Claude Code skill (`.claude/skills/streamlit-custom-style/`) that teaches Claude how to style Streamlit apps using this layered approach. The skill activates automatically when you ask Claude to style, theme, brand, or customize a Streamlit app's appearance.

It covers:

- Choosing the right styling layer for the job
- Theme TOML configuration (colors, fonts, dark mode, sidebar, chart palettes)
- Self-hosting fonts
- Shared page bootstrap with `init_page()`
- Scoped CSS patterns using `.st-key-*` selectors
- Common pitfalls to avoid (hashed classes, global selectors, `unsafe_allow_html`)

## Run the app

```bash
pip install -r requirements.txt
streamlit run Home.py
```

## Run tests

```bash
pytest tests/
```

## Project structure

```
.streamlit/
  config.toml              # Project config, references brand-theme.toml
  brand-theme.toml         # Reusable theme: colors, fonts, dark mode, sidebar
assets/
  styles.css               # Tiny scoped CSS, only .st-key-* rules
static/
  fonts/
    Manrope-VariableFont_wght.ttf
images/
  logo.svg
  logo_closed.svg
helpers.py                 # Shared init_page() bootstrap
Home.py                    # Main page
pages/
  01_Text.py               # Typography showcase
  02_Input.py              # Input widgets + keyed button variants
  03_Data.py               # DataFrames, tables, metrics
  04_Chart.py              # Charts (inherit theme colors)
  05_Chat.py               # Native chat components
  06_Status.py             # Alerts, progress, spinner
tests/
  test_smoke.py            # AppTest smoke tests
.github/workflows/
  streamlit-app.yml        # CI with Streamlit App Action
```

## Considerations

- **CSS injection is an escape hatch, not a foundation.** Even `st.html()` is not guaranteed stable across DOM changes. Keep injected CSS minimal and scoped.
- **Streamlit branding is not fully removable.** This repo does not claim white-label behavior.
- **Version upgrades may break CSS.** Pin your Streamlit version and run tests before upgrading.
- **Self-host fonts for privacy.** External font CDNs transmit user IP addresses.
- **Third-party styling libraries** like `st_yled` can complement this approach but are not required.

## Future direction

- [brand.yml support](https://github.com/streamlit/streamlit/issues/13025) may eventually replace TOML theme files
- [st.set_theme()](https://github.com/streamlit/streamlit/pull/14179) enables runtime theme switching
- [Components v2](https://docs.streamlit.io/develop/concepts/custom-components) is the recommended path for truly custom UI elements
