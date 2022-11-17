from credentials import *
import pyotp
from jsondata import *

class OTP():
    # Generate the OTP code 
    def generate_otp(self):      
        c1 = Credentials()
        totp = pyotp.TOTP(c1.OTP_SECRET_KEY)
        print("Current OTP:", totp.now())
        return totp.now()
        # send a POST request to insert the OTP code
    def insert_otp(self, client, cookies):
        otp_headers = {
                'Host': 'www.upwork.com',
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0',
                'Accept': '*/*',
                'Accept-Language': 'pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3',
                'Referer': 'https://www.upwork.com/ab/account-security/device-authorization?szRedir=https%3A%2F%2Fwww.upwork.com%2Ffreelancers%2Fsettings%2FcontactInfo',
                'X-Requested-With': 'XMLHttpRequest',
                'X-Odesk-Csrf-Token': '764f8239ba5c90a83c3e0ebdce6b8248',
                'Origin': 'https://www.upwork.com',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'Te': 'trailers'
        }

        # Input the OTP code
        otp_data = {
            "deviceAuthOtp[otp]": "".join(self.generate_otp()),
            "deviceAuthOtp[remember]": "true",
            "deviceAuthOtp[uid]": "1586511888781832192",
            "deviceAuthOtp[name]":"totp"
        }
        
        # Set the OTP request params
        params = {
            'szRedir': 'https://www.upwork.com/freelancers/settings/contactInfo',
        }
        
        # Send the post request
        client.post("https://www.upwork.com/ab/account-security/api/device-authorization/check-otp", json=otp_data, headers=otp_headers, cookies=cookies, params=params)