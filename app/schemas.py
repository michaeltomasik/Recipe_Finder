from pydantic import BaseModel
from typing import List

class IngredientBase(BaseModel):
    name: str

class RecipeBase(BaseModel):
    title: str
    instructions: str
    ingredients: List[IngredientBase]

    class Config:
        orm_mode = True
