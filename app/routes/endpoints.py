from fastapi import APIRouter
from app import database
from app.config import openapi_key
from app.queries import queries as queries
from app.models import models
import requests

router = APIRouter()



@router.get("/")
def root():
    return {"message": "Hello World"}

# ************************************
# EXAMPLES
# ************************************


# @router.get("/city")
# def get_all_cities_by_postalcode(postalcode: str):
#     query = queries.city_by_postalcode
#     cities = database.execute_sql_query(query, (
#         postalcode,
#     ))
#     if isinstance(cities, Exception):
#         return cities, 500
#     cities_to_return = []
#     for city in cities:
#         cities_to_return.append(city[0])
#     return({'cities': cities_to_return})
#
# @router.get("/packages")
# def get_all_packages():
#     query = queries.package_by_name
#     packages = database.execute_sql_query(query)
#     if isinstance(packages, Exception):
#         return packages, 500
#     packages_to_return = []
#     for package in packages:
#         packages_to_return.append(package[0])
#     return({'packages': packages_to_return})
#
# @router.post("/clients")
# def create_client(client: student1_models.Client):
#     query = queries.insert_clients_query
#     success = database.execute_sql_query(query, (
#         client.name,
#         client.email,
#         client.street,
#         client.postalcode,
#         client.city,
#         client.package,
#         client.referral,
#         client.othersource,
#     ))
#     if success:
#         return client
#     else:
#         return {"error": "Something went wrong. Check the terminal for more information."}
#
#
#
# @router.get("/weather")
# def get_weather(city: str):
#     try:
#         url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={openapi_key}&units=metric"
#         response = requests.get(url)
#         data = response.json()
#
#         if response.status_code != 200 or "main" not in data:
#             return {"error": "Weather info not available"}, 400
#
#         return {
#             "city": city,
#             "temperature": data["main"]["temp"],
#             "description": data["weather"][0]["description"],
#         }
#
#     except Exception as e:
#         return {"error": str(e)}, 500

