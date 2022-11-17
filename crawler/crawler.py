
from handleconnection import *
from jsondata import *
from otp import *
import httpx
import asyncio

class Crawler():
    # Instances
    otp_obj = OTP()
    handle_conn_obj = HandleConnection()
    json_data_obj = JsonData()

    # Set headers and data
    headers = handle_conn_obj.set_auth_headers()
    data = handle_conn_obj.set_auth_data()

    # Initialisation of the class variables
    cookies = ""
    connection_attempts = 0

    # Authetication method
    async def authenticate(self):
        with httpx.Client(base_url="https://www.upwork.com", follow_redirects=True) as client:
            while(True):
                try:
                    request = client.post("/ab/account-security/login", json=self.data, headers=self.headers)
                    self.connection_attempts += 1
                    print("Authenticating: " + str(self.connection_attempts) + "st. Attempt!")
                    if(self.handle_conn_obj.login_success(request, self.connection_attempts)): 
                        # print("User successfully authenticated.")
                        break
                except httpx.HTTPStatusError as exc:
                    self.handle_conn_obj.connection_error(self, exc)
            
            cookies = self.handle_conn_obj.set_cookies(request)


            self.otp_obj.insert_otp(client, cookies) # call the insert the OTP code method
                    
            # wait until the task to retrieve the profile informations finishes
            self.task_get_profile_info = asyncio.create_task(coro=self.get_profile_info(client))
            await self.task_get_profile_info
        return client
    
    async def get_profile_info(self, client):
        response = (client.get("/freelancers/settings/api/v1/contactInfo", headers=self.headers)).json()
        self.json_data_obj.save_to_json_file(response)
