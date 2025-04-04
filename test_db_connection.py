import os
from dotenv import load_dotenv
import psycopg2
from psycopg2 import OperationalError
import time

print(" Script started")

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
print(f"loaded DATABASE_URL: {DATABASE_URL}")

print("Trying to connect...")

try:
    start = time.time()
    conn = psycopg2.connect(DATABASE_URL, connect_timeout=5)
    print("✅ Connection successful!")
    conn.close()
    end = time.time()
    print(f"⏱️ Time taken: {round(end - start, 2)} seconds")

except OperationalError as e:
    print("❌ Connection failed:")
    print(e)