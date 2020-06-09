"""
This module is for getting information of cars from cars.com
by using BeautifulSoup library and storing the data into MySQL database.
"""

import requests
from bs4 import BeautifulSoup
import re
from peewee import *
from models import Car
import settings as s


def make_request(url):
    """Make request to web page and return the response."""
    return requests.get(url)


def get_page_content(page):
    """Extract HTML content of the page and return."""
    return page.content


def create_soup_object(page_content, parser):
    """Create beautiful soup object and return."""
    return BeautifulSoup(page_content, parser)


def get_list_of_cars(url):
    """Get the list of cars from given url address and return."""
    page = make_request(url)
    content = get_page_content(page)  # get content of page
    soup = create_soup_object(content, "html.parser")

    # return list of information of cars
    return soup.findAll("div", {"class": "listing-row__details"})


def extract_information_of_cars(car_list):
    """Extract information for each car in the car list"""

    # information of cars will be stored as list
    cars = []

    # get information of each car in the list
    for car in car_list:
        title = car.find("h2", class_="listing-row__title")
        title = title.text.strip()
        year = title.split(" ")[0]  # extract year from title
        brand = title.split(" ")[1]  # extract brand from title
        model = title.split(" ", 2)[2]  # extract model from title

        price = car.find("span", class_="listing-row__price")
        price = price.text.strip()
        price = re.sub("[$]", "", price)  # removing $ character from price
        price = re.sub("[,]", ".", price)  # switch ',' character with '.'

        try:
            price = float(price)
        except Exception as e:
            print(e)
            price = 0

        # get meta data that contains ext_color, int_color and transmission
        listing_row_meta = car.find("ul", class_="listing-row__meta")

        listing_row_meta = listing_row_meta.text
        listing_row_meta = re.sub(r"[\n\t]*", "", listing_row_meta)
        listing_row_meta = re.sub(" +", " ", listing_row_meta)

        ext_color = listing_row_meta.split(" ")[2]
        int_color = listing_row_meta.split(" ")[5]
        transmission = listing_row_meta.split(" ")[7]

        # get phone number of dealer
        phone = car.find("div", class_="listing-row__phone obscure")

        try:
            phone = phone.text.strip()
            phone = phone.split("\n")[1]
            phone = re.sub("[-() ]", "", phone)  # removing characters from phone number

        except Exception as e:
            print(e)
            phone = "private"  # if phone number is private

        # create new car object
        car = {
            "brand": brand,
            "model": model,
            "year": year,
            "price": price,
            "ext_color": ext_color,
            "int_color": int_color,
            "transmission": transmission,
            "phone": phone
        }
        cars.append(car)

    return cars


def store_car_data(cars):
    """Stores information of all cars into car table."""

    # Create a MySQL database connector object and connect
    mysql_db = MySQLDatabase(database=s.SCHEMA, user=s.USER, password=s.PASSWORD, host=s.HOST, port=s.PORT)
    mysql_db.connect()

    for car in cars:
        # create new car record
        new_car = Car(
                        brand=car.get("brand"),
                        model=car.get("model"),
                        year=car.get("year"),
                        price=car.get("price"),
                        ext_color=car.get("ext_color"),
                        int_color=car.get("int_color"),
                        transmission=car.get("transmission"),
                        phone=car.get("phone")
                     )

        new_car.save()  # car is stored into database

    mysql_db.close()
    print("All data saved successfully.")