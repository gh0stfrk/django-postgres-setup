import requests

base_url = "http://localhost:8000"


def create_user(username, password, email):
    url = f"{base_url}/user/"
    data = {"username": username, "password": password, "email": email}
    response = requests.post(url, json=data)
    return response


if __name__ == "__main__":
    user = {
        "username": "gh0stfrk",
        "password": "namlas",
        "email": "gh0stfrk@namlas.com",
    }

    res = create_user(user["username"], user["password"], user["email"])
    if res.status_code == 200:
        response = res.json()
        print(response)
