from fastapi import FastAPI, Depends, HTTPExption
from typing import list
from crud import create_item, get_item,update_item,delete_item
from security import get_api_key
from database import init_db

from projekt.app import response

app = FastAPI()

init_db()

@app.post("/items/",response_model=item)
def create_new_item(item: item, api_key:str=depends(get_api_key)):
    return create_item()

@app.get("/items/", response_model=List[item])
def read_items(api_key:str=depends(get_api_key)):
    return get_item()

@app.get("/items/{item_id}", response_model=item)
def read_item(item_id: int, api_key: str=Depends(get_api_key)):
    item = get_item(item_id)
    if item is None:
        raise HTTPExption(status_code=404, detail="Item not found")
    else:
        return item

    @app.put(f"/items/{item_id}", response_model=item)
    def update_existing_item(item_id: int,item: item , api_key: str=Depends(get_api_key))
        update_item = update_item(item_id, item)
        if item is None:
            raise HTTPExption(status_code=404, detail="Item not found")
            else:
            return update_item

     @app.delete("/items/{item_id}")
    def delete_existing_item(item_id: int, item: item, api_key: str = Depends(get_api_key))
      update_item = update_item(item_id, item)
      if not result:
            raise HTTPExption(status_code=404, detail="Item not found")
      else:
           return {"detail":"item deleted successfully"}