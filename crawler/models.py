from typing import Optional
from pydantic import BaseModel
from jsondata import *

# open the data.json file


# Pydantic models for handling the data type of each field
class AdditionalAccountsModel(BaseModel):
    client_account: str
    agency_account : str
    # check these types

class Address(BaseModel):
    street: str
    additionalInfo: Optional[str]
    state: str
    city: str
    zip: Optional[str]
    country: str    

class Email(BaseModel):
    address: str
    isVerified: bool
    unverifiedAddress: Optional[str]

class Portrait(BaseModel):
    bigPortrait: str
    originalPortrait: str

class Freelancer(BaseModel):
    rid: int
    userRid: int
    nid: str
    firstName: str
    lastName: str
    email: Email
    address: Address
    phone: int
    smsEmail: Optional[str]
    portrait: Portrait
    invoiceAddress: Optional[str]
    timezone: str
    isNameReviewPending: bool
    isIdVerificationPending: bool

class UserModel(BaseModel):
    freelancer: Freelancer = None

class CallUserModel():
    def __init__(self, data):
        self.data = data

    def show_user_model(self):
        user = UserModel(**self.data)
        print(f"User informations: \n\n{user}")
