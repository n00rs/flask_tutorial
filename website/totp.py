import time
import pyotp
from pyotp import HOTP,TOTP
import qrcode 


str_secert_key = "QAZWSXEDCRFVTGBYHNujmikolp"

dict_totp = TOTP(str_secert_key)

# print(dict_totp.now())

# create uri
str_uri = pyotp.TOTP(str_secert_key).provisioning_uri(name="jane doe",issuer_name="flask app")

# genrate Qr and save
str = qrcode.make(str_uri).save("totp.png")
# time.sleep(30)

while True:
    print(dict_totp.verify(input("Enter 2FA code: ")))

'''
HTOP example
'''
int_counter = 0
dict_hotp = HOTP(str_secert_key)

print(dict_hotp.at(0))
print(dict_hotp.at(1))
print(dict_hotp.at(2))
print(dict_hotp.at(3))
print(dict_hotp.at(4))
print(dict_hotp.at(5))

for _ in range(5) : 
    print(dict_hotp.verify(input("Enter OTP: "),int_counter))
    int_counter += 1
    
    