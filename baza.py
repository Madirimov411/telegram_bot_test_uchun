import os
import psycopg2
from dotenv import load_dotenv
import random

# .env fayldan ma'lumotlarni yuklash
load_dotenv()

conn = psycopg2.connect(
    host=os.getenv("db_host"),
    database=os.getenv("db_name"),
    user=os.getenv("db_user"),
    password=os.getenv("db_password"),
    port=os.getenv("db_port"),
)

cur = conn.cursor()
print("Databazaga muvaffaqiyatli ulandi")

insert_query = "INSERT INTO public.til (id, name) VALUES (%s, %s)"

data_list = [
    (1, 'Python','python','https://img.ixbt.site/live/topics/preview/00/04/43/61/4c83e99030.jpg'),
    (2, 'JavaScript','java_script','https://blog.enterprisedna.co/wp-content/uploads/2024/04/Javascript-Content-Article.png'),
    (3, 'Java','java','https://infostart.ru/upload/iblock/f54/f548efe1cf81eeab4473aa8b403a7204.png'),
    (4, 'C++','c_plus_plus','https://overclockers.ru/st/legacy/blog/413340/336432_O.jpg'),
    (5, 'C#','c_sharp','https://the-tech.kz/wp-content/uploads/2024/04/photo_2024-04-29_12-46-54.jpg'),
    (6, 'Go','go_lang','https://miro.medium.com/v2/resize:fit:1358/1*xofqkz49chC9XliDAuH1Qw.png'),
    (7, 'Swift','swift','https://i.pinimg.com/originals/df/b9/7a/dfb97a69381655c60569c2d653dbefc0.png'),
    (8, 'Kotlin','kotlin','https://media.proglib.io/wp-uploads/2017/06/mainkotlin.jpg'),
    (9, 'PHP','php','https://repository-images.githubusercontent.com/286744205/eccf6100-dbec-11ea-8094-6995de8227ea'),
    (10, 'Dart','dart','https://pic.rutubelist.ru/video/52/b4/52b4e52f7c9329d0178cbd80bb4d402e.jpg'),
    (11, 'Scala','scala','https://cdn.otus.ru/media/public/24/49/1_1801_4f11cf_1-1801-244974.png'),
]