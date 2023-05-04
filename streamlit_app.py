import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

# Customize the sidebar
markdown = """
(change this) Web App URL: <https://geotemplate.streamlit.app>
GitHub Repository: <https://github.com/whitson-buck/geolog>
"""

st.sidebar.title("About")
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
1. For the [GitHub repository](https://github.com/giswqs/streamlit-multipage-template) or [use it as a template](https://github.com/giswqs/streamlit-multipage-template/generate) for your own project.
2. Customize the sidebar by changing the sidebar text and logo in each Python files.
3. Find your favorite emoji from https://emojipedia.org.
4. Add a new app to the `pages/` directory with an emoji in the file name, e.g., `1_🚀_Chart.py`.

"""

st.markdown(markdown)

m = leafmap.Map(minimap_control=True)
m.add_basemap("OpenTopoMap")
m.to_streamlit(height=500)
