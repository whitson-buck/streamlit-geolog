import streamlit as st 
import leafmap.foliumap as leafmap

st.set_page_config(layout = "wide")

col1, col2 = st.columns([4,1])

options = list(leafmap.basemaps.keys())

index= options.index("OpenTopoMap")


with col2:
    dropdown = st.selectbox("Basemap", options, index)

    url = st.text_input("Enter URL")

with col1:
    m = leafmap.Map(locate_control=True, latlon_control=True, draw_export=True, minimap_control=True)
    if url:
        m.add_tile_layer(url, name="Your Basemap", attribution="")
    else:
        m.add_basemap(dropdown)
    # m.to_streamlit(height=700)
    m.to_streamlit()
