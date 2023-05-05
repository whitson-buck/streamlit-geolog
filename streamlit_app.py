import streamlit as st
import leafmap.foliumap as leafmap
import geolog

st.set_page_config(layout="wide")

# Customize the sidebar
markdown = """
Web App URL: <https://geolog.streamlit.app>
GitHub Repository: <https://github.com/whitson-buck/geolog>
"""

st.sidebar.title("Globe!")
st.sidebar.info(markdown)
logo = "https://i.pinimg.com/originals/0b/f2/85/0bf2854f6e017a49d461c719402425dc.gif"
st.sidebar.image(logo)

# Customize page title
st.title("geolog for landuse")

st.markdown(
    """
    This is a final project for GEOG 510 and includes a package I wrote for the class, geolog.
    """
)

st.header("Instructions")

markdown = """
1. Step one
2. Step two
3. Step three
4. Step four

"""

st.markdown(markdown)

m = leafmap.Map()
m.add_basemap("OpenTopoMap")
m.to_streamlit(height=500)