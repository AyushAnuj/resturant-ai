import streamlit as st
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