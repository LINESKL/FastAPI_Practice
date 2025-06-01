from typing import Annotated
from fastapi import APIRouter, Path

router = APIRouter(prefix="/items", tags=["items"])


@router.get("/")
def list_items():
    return {
        "Item 1",
        "Item 2",
        "Item 3"
    }

@router.get("/latest")
def get_latest_item():
    return {
        "Item": {
            "id": 1,
            "name": "latest item"
        }
    }

@router.get("/{item_id}")
def get_item_by_id(item_id: Annotated[int, Path(ge=1, le=1_000)]):
    return {
        "Item": {
            "id": item_id,
        }
    }
