import requests
from data import StellarBurgersUrl as Url, EndPoint
from helpers import sign_up_data


class StellarBurgersAPI:
    def __init__(self):
        self.MY_LOGIN = None
        self.MY_PASSWORD = None
        self.MY_NAME = None

    @property
    def sign_up_data(self):
        return sign_up_data(self)

    @staticmethod
    def create_new_user(sign_up_data):
        new_user_response = requests.post(f"{Url.URL_MAIN}{EndPoint.registration_user}", data=sign_up_data)
        return new_user_response

    def get_login(self):
        return self.MY_LOGIN

    def get_password(self):
        return self.MY_PASSWORD

    @staticmethod
    def verification_user(user_data):
        response = requests.post(f"{Url.URL_MAIN}{EndPoint.verification_user}",
                                 data=user_data)
        return response

    @staticmethod
    def get_access_token(new_user_response):
        access_token = new_user_response.json().get("accessToken")
        return access_token

    @staticmethod
    def delete_user(access_token):
        headers = {"Authorization": f"Bearer{access_token}"}
        response = requests.delete(f"{Url.URL_MAIN}{EndPoint.delete_user}", headers=headers)
        return response
