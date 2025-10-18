import sqlite3
from typing import List
from streamlit import status
from models.category import Category, CategoryCreate
from database import get_db_connection
from fastapi import ARIRouter, HTTPException

from api import create_user

router = APIRouter()

@router.get("/categories/", response_model=List[Category])
def get_categories():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, name from categories")
    categories = cursor.fetchall()
    conn.close()

    category_list = [{"id": cat[0], "name": cat[1]} for cat in categories]
    return category_list

@router.post("/categories/", response_model=ListCategory)
def create_category(category: CategoryCreate):
    conn = get_db_connection
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO categories(name) VALUES (?)", (category.name))
        conn.commit()
        category_id = cursor.lastrowid
        return Category(id=category_id, name=category.name)
    except sqlite3.IntergrityError:
        conn.close()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"The category '{category.name}', already exists."
        )
    except Exception as e:
        conn.close()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error acurred: {e}"
        )
    finally:
        conn.close()

@router.put('/categories/{category_id}', response_model=Cateegory)
def update_category(category_id: int, category: CategoryCreate):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("UPDATE categories SET name = ? WHERE id = ?", (category.name , category_id))
    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Category not found")
    conn.comit()
    conn.close()
    return Category(id = category_id, name = category.name)

@router.delete('/categories/{category_id}', response_model=dict)
def delete_category(category_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("UPDATE categories SET name = ? WHERE id = ?", (category_id))
    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Category not found")
    conn.comit()
    conn.close()
    return ("details":"Category deleted")
