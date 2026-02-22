import sys
from pathlib import Path
import streamlit as st

# Ensure project root is on sys.path so the top-level
# `restaurant_generator.py` can be imported when Streamlit
# runs the script from inside the `resturant_ai` package.
project_root = Path(__file__).parent.parent.resolve()
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from restaurant_generator import generate_restaurant_details

st.set_page_config(page_title="Restaurant Generator")

st.title("🍽️ Restaurant Name & Menu Generator")

st.write("Generate restaurant name and menu using FREE local AI via Ollama")


cuisine = st.selectbox(
    "Select Cuisine",
    ["Indian", "Italian", "Chinese", "Mexican"],
    key="cuisine_select"
)


if st.button("Generate", key="generate_button"):

    name, menu = generate_restaurant_details(cuisine)

    st.subheader("🏪 Restaurant Name")
    st.write(name)

    st.subheader("📜 Menu Items")
    st.write(menu)