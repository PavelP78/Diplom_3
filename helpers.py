from faker import Faker


def sign_up_data(self):
    fake = Faker()
    self.MY_LOGIN = fake.email()
    self.MY_PASSWORD = fake.password()
    self.MY_NAME = fake.name()
    user_data = {"email": self.MY_LOGIN, "password": self.MY_PASSWORD, "name": self.MY_NAME}
    return user_data
