from typing import List, optional
import sqlite3
from models import Item
from database import get_db_connection

def create_item(item: item) -> item:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("insert into items (name, description) values (?,?)", (item.name, item.description)
    conn.commit()
    item.id = cursor.lastrowid
    conn.close()
    return item

def get_items()-> List[item]:
    conn = get_db_connection()
    item = conn.execute("select * from items").fetchall()
    conn.close()
    return [item(**dict(item)for item in items)]

def get_item(item_id: int) -> optional[item]:
    conn = get_db_connection()
    item = conn.execute("select * from items where id =?", (item_id,)).fetchall()
    conn.close()
    return [item(**dict(item)for item in items)]