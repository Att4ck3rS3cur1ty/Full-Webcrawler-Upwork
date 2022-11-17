import os
from dotenv import load_dotenv
from os.path import join, dirname

class Credentials():
    def __init__(self):
        dotenv_path = "./env/.env" # path to the env dir
        dotenv_path = join(dirname(dotenv_path), ".env") # load the dotenv from the .env file
        load_dotenv(dotenv_path)

        self.USERNAME = os.getenv("USERNAME") # retrieve USERNAME
        self.PASSWORD = os.getenv("PASSWORD") # retrieve PASSWORD
        self.SECRET_ANSWER = os.getenv("SECRET_ANSWER") # retrieve SECRET ANSWER
        self.OTP_SECRET_KEY = os.getenv("OTP_SECRET_KEY") # retrieve OTP SECRET KEY
        # print(USERNAME, PASSWORD, SECRET_ANSWER)
