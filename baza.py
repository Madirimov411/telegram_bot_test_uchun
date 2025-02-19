import os
import psycopg2
from dotenv import load_dotenv
import random

# .env fayldan ma'lumotlarni yuklash
load_dotenv()

conn = psycopg2.connect(
    host=os.getenv("db_ho   st"),
    database=os.getenv("db_name"),
    user=os.getenv("db_user"),
    password=os.getenv("db_password"),
    port=os.getenv("db_port"),
)

cur = conn.cursor()
print("Databazaga muvaffaqiyatli ulandi")

def get_dasturlash_tillari():
    cur.execute("SELECT * FROM til")
    return cur.fetchall()

def get_savollar_by_id_15(id):
    cur.execute(f"SELECT * FROM testlar WHERE til_id={id}")
    savollar = cur.fetchall()
    random.shuffle(savollar)
    return savollar[:15]

def create_user(telegram_id, user_name, first_name, last_name, date_membership):
    cur.execute(
        f"""INSERT INTO users(telegram_id, user_name, first_name, last_name, date_membership) 
            VALUES ({telegram_id}, '{user_name}', '{first_name}', '{last_name}', '{date_membership}');
        """
    )
    conn.commit()
    print("Yangi foydalanuvchi qo'shildi ✅")
