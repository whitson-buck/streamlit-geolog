import streamlit as st 
import leafmap.foliumap as leafmap

st.set_page_config(layout = "wide")

col1, col2 = st.columns([4,1])

options = list(leafmap.basemaps.keys())


with col2:
    dropdown = st.selectbox("Basemap", options)

    default_url = leafmap.basemaps[dropdown].tiles

    url = st.text_input("Enter URL", default_url)

m = leafmap.Map(locate_control=True, latlon_control=True, draw_export=True, minimap_control=True)
m.add_basemap(options)
# m.to_streamlit(height=700)

if url:
    m.add_tile_layer(url, name= 'Tile Layer', attribution=' ')

with col1:
    m.to_streamlit()
