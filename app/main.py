from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, database
from typing import List


app = FastAPI()

@app.get("/recipes/search", response_model=List[schemas.RecipeBase])
def search_recipes(ingredients: str, db: Session = Depends(database.get_db)):
    ingredient_names = [name.strip().lower() for name in ingredients.split(",")]

    db_ingredients = db.query(models.Ingredient).filter(models.Ingredient.name.in_(ingredient_names)).all()

    if not db_ingredients:
        raise HTTPException(status_code=404, detail="No ingredients found")

    recipes = db.query(models.Recipe).join(models.Recipe.ingredients).filter(
        models.Ingredient.id.in_([i.id for i in db_ingredients])).all()

    if not recipes:
        raise HTTPException(status_code=404, detail="No recipes found")

    return recipes


@app.get("/")
def read_root():
    return {"message": "Welcome to the Recipe Finder API!"}