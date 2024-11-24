# streamlit run .\main.py
# import streamlit as st
#from openai import OpenAI
#import getpass
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
#from langchain.llms import OpenAI

# Intialization
load_dotenv()
api_key = os.environ["OPEN_API_KEY"]
chat = ChatOpenAI(model='gpt-3.5-turbo-0125', api_key=api_key)
#client = OpenAI(open_api_key=api_key)

""" def generate_drink(ingredients):
    prompt_template = f"Give me an in depth recipe a drink. The drink should be made from the following list of ingredients: {ingredients}"
    response = chat(
        [
            SystemMessage(content='You are an AI Bartender. Give an in depth recipe for the required amount of servings of the drink, including the time to make, ingredients, price, steps, and a few slight alterations that can be made to the drink (i.e. more/less boosy and more/less bitter). Leave out the ingredients that we already have out of the price estimation and state why they were left out.'),
            HumanMessage(content=prompt_template)
        ]
    )
    return response.content """

""" def generate_drink_name(ingredients):
    prompt_template = f"Name a drink that uses {ingredients}."
    response = chat(
        [
            SystemMessage(content='You are an AI Bartender. List only the names of the drinks with detail, and nothing else.'),
            HumanMessage(content=prompt_template)
        ]
    )
    return response.content

def generate_drink_ingredients(ingredients):
    prompt_template = f"Come up with a drink that uses {ingredients}, then write the ingredient list and quantities. If one of the ingredients is harmful, do not note that it is harmful; simply only use the other ingredients."
    response = chat(
        [
            SystemMessage(content='You are an AI Bartender. Return a list of ingredients and their quantities, and nothing else.'),
            HumanMessage(content=prompt_template)
        ]
    )
    return response.content """

# This is what I was experimenting with, but I couldn't get it to work.
# TODO: Fix the "drink suggestion" if you don't have ingredients
# TODO: incorporate cocktail book

""" def generate_drink(ingredients):
    prompt_template = f"Name a drink that uses {ingredients}, then write a list of ingredients with quantities after them. Separate the two with an @ symbol. If one of the ingredients is harmful, do not note that it is harmful; simply only use the other ingredients. If the ingredient list given is insufficient for making a tasty beverage, suggest the complete drink that it is closest to. Add additional ingredients that would need to be bought, and denote them with the word (buy) in parentheses;"
    response = chat(
        [
            SystemMessage(content='You are an AI Bartender. Return only the name of a drink and then the list of ingredients, including ingredients which are necessary but which I do not have. Separate the two with a @.'),
            HumanMessage(content=prompt_template)
        ]
    )
    return response.content """

def generate_drink(ingredients):
    prompt_template = f"Name a drink that uses {ingredients}, then write a list of ingredients with quantities after them. Separate the two with an @ symbol. If one of the ingredients is harmful, do not note that it is harmful; simply only use the other ingredients."
    response = chat(
        [
            SystemMessage(content='You are an AI Bartender. Return only the name of a drink and then the list of ingredients. Separate the two with a @.'),
            HumanMessage(content=prompt_template)
        ]
    )
    return response.content

# def main():
#     st.title('AI Bartender')
#     st.header('Hello from your AI Bartender: I will help you make a drink')

#     ingredients = st.text_input('What ingredients do you have?')
#     if ingredients:
#         appliance_options = ["None", "Shaker", "Blender"]
#         appliance = st.multiselect("What appliances do you have to use?", appliance_options)
#         if appliance:
#             servings = st.text_input("How many servings do you want to make?")
#             if servings:
#                 price = st.slider("How many much would you like to spend on this drink?", min_value=0, max_value=100, step=1, value=(10,20), format=" $%d")
#                 submit_button = st.button("Submit")
#                 if submit_button:
#                     drink_name = generate_drink_name(ingredients=ingredients, appliance=appliance)
#                     drink_recipie = generate_drink(ingredients=ingredients, appliance=appliance, servings=servings, price=price)
#                     st.write(f'You can make {drink_name}, here is the recipie')
#                     st.write(drink_recipie)

# #Run the Streamlit app
# if __name__ == '__main__':
#     main()
