import os
from dotenv import load_dotenv
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, database
from typing import List
from app.database import get_db

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

print(f"DATABASE_URL: {DATABASE_URL}")

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


@app.post("/add_ingredient_to_recipe")
def add_ingredient_to_recipe(recipe_id: int, ingredient_name: str, quantity: str, db: Session = Depends(database.get_db)):
    recipe = db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")

    ingredient = db.query(models.Ingredient).filter(models.Ingredient.name == ingredient_name).first()
    if not ingredient:
        raise HTTPException(status_code=404, detail="Ingredient not found")

    recipe_ingredient = models.RecipeIngredient(
        recipe_id=recipe.id,
        ingredient_id=ingredient.id,
        quantity=quantity
    )

    db.add(recipe_ingredient)
    db.commit()

    return {"message": "Ingredient added to recipe successfully"}


@app.get("/test_db")
def test_db(db: Session = Depends(get_db)):
    ingredients = db.query(models.Ingredient).all()
    if not ingredients:
        raise HTTPException(status_code=404, detail="No ingredients found")
    return ingredients


@app.get("/")
def read_root():
    return {"message": "Welcome to the Recipe Finder API!"}