from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
import database

app = FastAPI()

@app.get("/test-db")
def test_db_connection(db: Session = Depends(database.get_db)):
    try:
        db.execute("SELECT 1")
        return {"message": "Database connection successful"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database connection failed: {e}")