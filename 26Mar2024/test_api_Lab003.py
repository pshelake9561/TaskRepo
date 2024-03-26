import requests
import pytest


def test_create_token():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/auth"
    URL = base_url + base_path
    headers = {"Content-Type": "application/json"}
    payload = {"username": "admin",
               "password": "password123"}
    response = requests.post(url=URL, headers=headers, json=payload)
    response_json = response.json()
    token = response_json["token"]
    assert response.status_code == 200
    assert token is not None
    return token


def test_get_booking_ids():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    response = requests.get(URL)
    response_json = response.json()
    assert response.status_code == 200


def test_create_booking():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    payload = {"firstname": "Pramod", "lastname": "Shelke", "totalprice": 501, "depositpaid": 'true',
               "bookingdates": {"checkin": "2024-04-14", "checkout": "2024-04-16"}, "additionalneeds": ""}
    header = {"Content-Type": "application/json"}
    response = requests.post(url=URL, json=payload, headers=header)
    response_json = response.json()
    booking_id = response_json["bookingid"]
    firstname = response_json["booking"]["firstname"]
    checkin = response_json["booking"]["bookingdates"]["checkin"]
    assert response.status_code == 200
    assert booking_id is not None
    assert booking_id > 0
    assert type(booking_id) == int
    assert firstname == "Pramod"
    assert checkin == "2024-04-14"
    return booking_id


def test_get_booking():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/"
    id = test_create_booking()
    URL = base_url + base_path + str(id)
    response = requests.get(URL)
    response_json = response.json()
    firstname = response_json["firstname"]
    assert response.status_code == 200
    assert firstname == "Pramod"


def test_update_booking():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/"
    bookingid = test_create_booking()
    PUT_URL = base_url + base_path + str(bookingid)
    auth = "token=" + test_create_token()
    header = {"Content-Type": "application/json",
              "Cookie": auth}
    payload = {
        "firstname": "Prem",
        "lastname": "shelke",
        "totalprice": 1000,
        "depositpaid": 'true',
        "bookingdates": {
            "checkin": "2024-04-09",
            "checkout": "2024-04-22"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.put(url=PUT_URL, headers=header, json=payload)
    response_json = response.json()
    firstname = response_json["firstname"]
    assert response.status_code == 200
    assert firstname == "Prem", "Failed - Incorrect First name"


def test_partial_update_booking():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/"
    bookingid = test_create_booking()
    PATCH_URL = base_url + base_path + str(bookingid)
    auth = "token=" + test_create_token()
    header = {"Content-Type": "application/json",
              "Cookie": auth}
    payload = {
        "firstname": "Vaishnavi",
        "lastname": "Shelke"
    }
    response = requests.patch(url=PATCH_URL, headers=header, json=payload)
    response_json = response.json()
    firstname = response_json["firstname"]
    assert response.status_code == 200
    assert firstname == "Vaishnavi", "Failed Message - Incorrect firstname"


def test_delete_booking():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/"
    id = test_create_booking()
    auth = "token=" + test_create_token()
    header = {"Cookie": auth}
    DELETE_URL = base_url + base_path + str(id)
    response = requests.delete(url=DELETE_URL, headers=header)
    assert response.status_code == 200
