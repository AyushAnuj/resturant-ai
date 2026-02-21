from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate


llm = ChatOllama(
    model="llama3",
    temperature=0.7
)


def generate_restaurant_details(cuisine):

    name_prompt = PromptTemplate.from_template(
        "Suggest a fancy restaurant name for {cuisine} food. Only return the name."
    )

    name_chain = name_prompt | llm

    name_result = name_chain.invoke({
        "cuisine": cuisine
    })

    restaurant_name = name_result.content


    menu_prompt = PromptTemplate.from_template(
        "Suggest 8 menu items for restaurant named {restaurant_name}."
    )

    menu_chain = menu_prompt | llm

    menu_result = menu_chain.invoke({
        "restaurant_name": restaurant_name
    })


    return restaurant_name, menu_result.content