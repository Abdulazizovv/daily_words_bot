# import psycopg2
from collections import namedtuple
from typing import NamedTuple

# con = psycopg2.connect(
#     host='localhost',
#     dbname='mydb',
#     user='postgres',
#     password='11111'
# )

# cur = con.cursor()
# con.autocommit = True
# cur.execute("""CREATE TABLE IF NOT EXISTS car(
#             id SERIAL PRIMARY KEY,
#             car_name VARCHAR(255) not null,
#             car_model VARCHAR(255) not null,
#             car_color VARCHAR(255) not null,
#             car_power VARCHAR(255) not null

# )""")

# car_name = input("car_name:")
# car_model = input("car_model:")
# car_color = input("car_color:")
# car_power = input("car_power:")

# car = namedtuple("car", ["name", "model", "color", "power"])


# car1 = car(car_name, car_model, car_color, car_power)

# print(car1)

# cur.execute("""INSERT INTO car (car_name, car_model, car_color, car_power) VALUES (%s, %s, %s, %s)""", (car1.name, car1.model, car1.color, car1.power))

# print("successfully inserted")

# cur.execute("select * from car")
# print(cur.fetchall())

# class Coordinates(NamedTuple):
#     long: float
#     lat: float

# coor = Coordinates(12.3, 16.5)
# print(coor)

# from pydantic import BaseModel

# class User(BaseModel):
#     username: str
#     age: int
#     email: str
#     password: str

# user = User(username="abdulazizovv", age="21", email="abdulazizovv@gmail.com", password="u123456u")
# print(user)


class Home(NamedTuple):
    price: float
    rooms: int
    address: str
    size: int

home1 = Home(30000, 5, "Ferghana", 95)
print(home1)



