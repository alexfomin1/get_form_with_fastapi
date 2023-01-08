import re

from fastapi import FastAPI, Request
from pydantic import BaseModel, validator
from tinydb import TinyDB

app = FastAPI()

# models section


class Date(BaseModel):
    date: str

    @validator("date")
    def date_validator(cls, v):
        if not re.match(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", v) and not re.match(
                r"^[0-9]{2}(\.)[0-9]{2}(\.)[0-9]{4}$", v):
            raise ValueError("Invalid date format")
        return v


class Phone_number(BaseModel):
    phone_number: str

    @validator("phone_number")
    def phone_number_validator(cls, v):
        if not re.match(
                r"^(\+|\s)7\s?\(?[0-9]{3}\)?\s?[0-9]{3}\s?[0-9]{2}\s?[0-9]{2}$",
                v,
        ):
            raise ValueError("Invalid phone number")
        return v


class Email(BaseModel):
    email: str

    @validator("email")
    def email_validator(cls, v):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", v):
            raise ValueError("Incorrect email")
        return "email"


class Text(BaseModel):
    text: str

    @validator("text")
    def text_validator(cls, v):
        if type(v) != str:
            raise ValueError("Incorrect text")
        return "text"


db = TinyDB("db.json")


def get_list_of_patterns(data: dict) -> list:
    all_patterns = db.all()
    list_of_patterns = []
    for pattern in all_patterns:
        status = True
        for key, value in pattern.items():
            if key == "name":
                pass
            elif key in data:
                if data[key] == value:
                    pass
                else:
                    status = False
            else:
                status = False
        if status:
            list_of_patterns.append(pattern["name"])
    return list_of_patterns


# db section
def init_db_table_booking():
    db.insert({
        "name": "table_booking",
        "visitor_phone_number": "phone_number",
        "visitor_name": "text",
        "visitor_email": "email",
        "date": "date",
    })


def init_db_restaurant_info():
    db.insert({
        "name": "restaurant_info",
        "restaurant_name": "text",
        "restaurant_phone_number": "phone_number",
        "restaurant_address": "text",
    })


def init_db_dish_info():
    db.insert({
        "name": "dish_info",
        "dish_name": "text",
        "dish_price": "text",
        "dish_description": "text",
    })


@app.on_event("startup")
def start_checkup():
    all_patterns = db.all()
    if not all_patterns:
        init_db_table_booking()
        init_db_restaurant_info()
        init_db_dish_info()


@app.post("/get_form")
def get_form(data_input: Request):
    dict_data = {}
    data = data_input.query_params
    for key, value in data.items():
        try:
            Date(date=value)
            dict_data[key] = "date"
        except ValueError:
            dict_data[key] = "text"
            try:
                Phone_number(phone_number=value)
                dict_data[key] = "phone_number"
            except ValueError:
                dict_data[key] = "text"
                try:
                    Email(email=value)
                    dict_data[key] = "email"
                except ValueError:
                    dict_data[key] = "text"
    list_of_patterns = get_list_of_patterns(dict_data)
    if not list_of_patterns:
        return dict_data
    elif len(list_of_patterns) == 1:
        return list_of_patterns[0]
    else:
        return list_of_patterns
