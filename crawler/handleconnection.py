from credentials import *
import httpx
import re

class HandleConnection():
    credentials_obj = Credentials()
    def set_auth_headers(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0",
            "Accept-Encoding": "gzip, deflate",
            "Referer": "https://www.upwork.com/ab/account-security/login",
            "X-Requested-With": "XMLHttpRequest",
            "Content-Type": "application/json",
            "X-Odesk-Csrf-Token": "77a3580ba2b836e38dc186b179b4fe69",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Origin": "https://www.upwork.com",
            "Sec-Fetch-Site": "same-origin",
            "Te": "trailers"
        }
        return headers

    # set the default data to be sent
    def set_auth_data(self):
        data = {
            "login": {
                "mode" : "password",
                "iovation": "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;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",
                "username": "".join(self.credentials_obj.USERNAME),
                "elapsedTime": "158619",
                "forterToken":"fbd415fda17d4e3f8c3ca71178bd956d_1667012917398__UDF43-m4_14ck_tt",
                "password": "".join(self.credentials_obj.PASSWORD)
            }
        }
        return data

    # get the master access token from request
    def get_master_access_token(self, request):
        cookieName = request.headers.get("Set-Cookie")
        master_access_token = (((re.search("master_access_token=(.*)", cookieName)).group()).split(";")[0]).split("=")[1]
        return master_access_token

    # set the required cookies
    def set_cookies(self, request):
        master_access_token = self.get_master_access_token(request)
        cookies = {
            "XSRF-TOKEN": "764f8239ba5c90a83c3e0ebdce6b8248",
            "master_access_token": "".join(master_access_token)
        } 
        return cookies
        
    # test if request is 200. If not, check if it was a session expired issue.
    # yet, if it's not the case and it has tried ~5 times, the program quits
    def login_success(self, jsonResponse, connection_attempts):
        if (jsonResponse.status_code == httpx.codes.OK): return True
        elif (jsonResponse.status_code == "401" and "Session is expired" in jsonResponse): 
            print("Trying to establish your connection (", connection_attempts, ")... \nPlease wait.")
            return False
        elif (connection_attempts >= 5):
            print("Too many connection attemps! Please, try again later.")
            exit(0)

    # and the following method is called together
    def connection_error(self, exc):
        print("Sorry! We've had an internal error:")
        print(f"Error response {exc.response.status_code} while requesting {exc.request.url!r}.")
        print("Exiting...")
        exit(0)