import streamlit as st
import requests
import pandas as pd
from dotenv import load_dotenv
import os

from unicodedata import category

from lesson19.lesson19 import selected_Year

load_dotenv()

API_BASE_URL = os.getenv("API_BASE_URL")



def get_categories():
    response = requests.get(f"{API_BASE_URL}/categories/")
    return response.json()

def get_recipes(cuisine=None, difficulty=None):
    params = {}
    if cuisine:
        params['cuisine'] = cuisine
    if difficulty:
        params['difficulty'] = difficulty
        response = requests.get(f"{API_BASE_URL}/recipes/", params=params)
        return response.json()

def create_category(category_name):
    response = requests.post(f"{API_BASE_URL}/categories/", json={"name": category_name})
    return response.json()

def update_category(category_id, new_name):
    response = requests.put(f"{API_BASE_URL}/categories/{category_id}", json={"name": new_name})
    return response.json()

def delete_category(category_id):
    response = requests.delete(f"{API_BASE_URL}/categories/{category_id}")
    return response.json()

def create_recipe(recipe_name, description, ingredients, instructions, cuisine, difficulty, category_id):
    response = requests.post(f"{API_BASE_URL}/recipes/", json={"name": recipe_name,
                                                                  "description": description,
                                                                  "ingredients": ingredients,
                                                                  "instructions": instructions,
                                                                  "cuisine": cuisine,
                                                                  "difficulty": difficulty,
                                                                  "category_id": category_id})
    return response.json()

def update_recipe(recipe_id, recipe_name, description, ingredients, instructions, cuisine, difficulty, category_id):
    response = requests.put(f"{API_BASE_URL}/recipes/{recipe_id}", json={"name": recipe_name,
                                                                  "description": description,
                                                                  "ingredients": ingredients,
                                                                  "instructions": instructions,
                                                                  "cuisine": cuisine,
                                                                  "difficulty": difficulty,
                                                                  "category_id": category_id})

    return response.json()

def delete_recipe(recipe_id):
    response = requests.delete(f"{API_BASE_URL}/recipes/{recipe_id}")
    return response.json()

st.title("Online Recipe Book")

menu = ["Dashboard", "Manage Recipe", "Manage Categories"]
selected_menu = st.sidebar.selectbox("Menu", menu)

if selected_menu == "Dashboard":
    st.header("Dashboard")

    st.subheader("Recipes")
    recipe_list = get_recipes()
    if recipe_list:
        df_recipes= pd.DataFrame(recipe_list)

        if 'id' in df_recipes.columns:
            df_recipes = df_recipes.drop(columns=['id'])
        df_recipes.reset_index(drop=True, inplace=True)
        df_recipes.index += 1
        st.dataframe(df_recipes, use_container_width=True)
    else:
        st.info("No Recipes found")


    st.subheader("Categories")
    category_list = get_categories()
    if category_list:
        df_categories = pd.DataFrame(category_list)
        if 'id' in df_categories.columns:
            df_categories = df_categories.drop(columns=['id'])
        df_categories.reset_index(drop=True, inplace=True)
        df_categories.index += 1
        st.dataframe(df_categories, use_container_width=True)
    else:
        st.info("No Categories found")

elif selected_menu == "Manage Recipes":
    st.header("Manage Recipes")

    st.subheader("Add a New Recipe")
    recipe_name = st.text_input("Recipe Name", key="new_recipe_name")
    recipe_description = st.text_area("Description", key="new_recipe_description")
    recipe_ingredients = st.text_area("Ingredients", key="new_recipe_ingredients")
    recipe_instructions = st.text_area("Instructions", key="new_recipe_instructions")
    recipe_cuisine = st.text_input("Cuisine", key="new_recipe_cuisine")
    recipe_difficulty = st.selectbox("Difficulty", key="new_recipe_difficulty")

    category_list = get_categories()
    if category_list:
        category_name = [cat['name'] for cat in category_list]
        selected_category_name = st.selectbox("Category", category_name, key="new_recipe_category")
        selected_category_id = next(cat['id'] for cat in category_list if cat['name'] == selected_category_name)
    else:
        st.error("Failed to retrieve categories.")
        selected_category_id = None

    if st.button("Add Recipe", key="add_recipe_button"):
        if all([recipe_name,recipe_description,recipe_ingredients, recipe_instructions,recipe_cuisine,recipe_difficulty, selected_category_id is not None]):
            create_recipe(recipe_name, recipe_description, recipe_ingredients, recipe_instructions, recipe_cuisine, recipe_difficulty, selected_category_id)
            st.success(f"Recipe '{recipe_name} added successfully!")
        else:
            st.error("All fields must be filled any category selected to add a recipe.")

    st.subheader("Edit or delete recipe")
    recipe_list = get_recipes()

    if recipe_list:
        recipe_name = [recipe['name'] for recipe in recipe_list]
        manage_action = st.radio("choose action", ["Edit","delete"], key="manage_recipe_action")

        if manage_action == "Edit":
            recipe_to_edit = st.selectbox("Select a recipe to edit", recipe_name, key="edit_recipe_select")
            if recipe_to_edit:
                selected_recipe = next(recipe for recipe in recipe_list if recipe['name'] ==recipe_to_edit )
                st.subheader(f"Edit Recipe: {selected_recipe['name']}")
                edit_name = st.text_input("Recipe Name", value=selected_recipe['name'], key="edit_recipe_name")
                edit_description = st.text_area("description", value=selected_recipe['description'], key="edit_recipe_descriptiom")
                edit_ingredients = st.text_area("ingredients", value=selected_recipe['ingredients'], key="edit_recipe_ingredients")
                edit_ingredients = st.text_area("ingredients", value=selected_recipe['ingredients'],key="edit_recipe_ingredients")
                edit_cuisine = st.text_area("cuisine", value=selected_recipe['cuisine'],key="edit_recipe_cuisine")
                edit_difficulty = st.text_area("difficulty",["Easy","Medium","Hard"],index=["Easy","Medium","Hard"].index(slected_recipe)['difficulty']),
                                                key="edit_recipe_cuisine")
                category_list = get_categories()
                if category_list:
                    category_name = [cat['name']for cat in category_list]
                    edit_category_name = st.selectbox("Category", category_name, index=category_name.index(next(cat['name']for cat in category_list
                                                                                                                            if cat['id'] == selected_recipe['category_id']))),

                edit_category_id = next(cat['name'] for cat in category_list if category_list if cat['name'] == edit_category_name)
            else:
                st.error("Falied to retrive categories.")
                edit_category_id = None

            if st.button("Update Recipe", key="update_recipe_button"):
                if all([edit_name, edit_description, edit_ingredients, edit_instructions, edit_cuisine, edit_difficulty, edit_category_id is mot None])
                    update_recipe(selected_recipe['id'], edit_name, edit_instrucions, edit_cuisine,
                                edit_difficulty, edit_category_id)
            st.success(f"Recipe '{edit_name}' update successfully!")
        else:
            st.error("All fields must be filled and category selected to update a recipe.")

        elif mange_actiom == "delete":
            recipe_to delete = st.selectbox("select a recipe to delete", recipe_name, key="delete_recipe_select")
        if recipe_to_delete:
            selected_recipe = next(recipe for recipe in recipe_list if recipe['name'] == recipe_to_delete)
            if st.button(f"delete '{selected_recipe['name']}'", key="delete_recipe_button"):
                delete_recipe(selected_recipe['id'])
                st.success(f"recoipe ' {selected_recipe['name']}' deleted successfully")
        else:
            st.info("no recipes available to manage.")

