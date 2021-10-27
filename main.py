#!/usr/bin/python3
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new User --")
my_user = User()
my_user.first_name = "Betty"
my_user.last_name = "Bar"
my_user.email = "airbnb@mail.com"
my_user.password = "root"
my_user.save()
print(my_user)

print("-- Create a new State --")
my_state = State()
my_state.name = "Deez Nuts"
my_state.save()
print(my_state)

print("-- Create a new City --")
my_city = City()
my_city.name = "Tulsa"
print(my_city)

print("-- Create a new Amenity --")
my_amenity = Amenity()
my_amenity.name = "Garglon Bofa"
print(my_amenity)
