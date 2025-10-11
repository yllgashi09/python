import streamlit as st
import requests
import pandas as pd
from dotenv import load_dotenv
import os

from projekt.app import response

load_dotenv()

API_BASE_URL = os.getenv("API_BASE_URL")


def get_categories():
    response = request.get(f"{API_BASE_URL}/categories/")
    return response.json()

def get_recipes(cuisine=None, difficulty=None):
    params = {}
    if cuisine:
        params['cuisine'] = cuisine
    if difficulty:
        params['difficulty'] = difficulty
        response = request.get(f"{API_BASE_URL}/recipies/", params=params)
        return response.json()

    def create_category(category_name):
        response = request.get(f"{API_BASE_URL}/categories/", json={"name": category_name})
        return response.json()

    def update_category(category_id, new_name):
        response = request.put(f"{API_BASE_URL}/categories/{category_id}", json={"name": new_name})
        return response.json()

    def delete_category(category_id):
        response = request.delete(f"{API_BASE_URL}/categories/{category_id})
        return response.json()

    def create_recipe(recipe_name, description, ingredients, instruction, cuisine, difficulty, category_id ):
        response = request.post(f"{API_BASE_URL}/recipies/", json={"name": recipe_name,
                                                                   "description": descriptiom,
                                                                   "ingredients": ingredients,
                                                                   "instruction": instructions,
                                                                   "cuisine": cuisine,
                                                                   "difficulty": difficulty,
                                                                   "category_id": category_id})

        return response.json()

    def create_recipe(recipe_name, description, ingredients, instruction, cuisine, difficulty, category_id ):
    response = request.put(f"{API_BASE_URL}/recipies/{recipe_id}", json={"name": recipe_name,
                                                               "description": descriptiom,
                                                               "ingredients": ingredients,
                                                               "instruction": instructions,
                                                               "cuisine": cuisine,
                                                               "difficulty": difficulty,
                                                               "category_id": category_id})
    return response.json()
