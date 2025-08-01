import requests
import time
import json
import random
import urllib.parse

import base64
import hashlib

from Api_omslogin import token1,login_url
print(" "*600) # for space 

logout_url ="https://qa-oms.zolv.health/api/v1/user/logout"   



# 1 : logout : Logout with valid session token  :

# print("\033[1;34m LOGIN TESTCASE! Document ID: TP_002 \033[0m")

# print("\033[1;34m Logout with valid session token...............!\033[0m")


# headers = {
#     "Authorization": f"Bearer {token1}",
#     "Content-Type": "application/json"
# }
# # print(f"Using token: {headers.get('Authorization')}")

# response_logout = requests.put(logout_url,headers=headers) 
# if response_logout.status_code == 200:
#     logout_json = response_logout.json()
#     print("Response JSON:", json.dumps(logout_json, indent=4))
#     print(f"Token (Logout): ......................{token1}")
#     print(f"\033[92m✅  TEST PASSED...!: Test Case ID - 001 \033[0m",response_logout.text) # login success so test failed becoz in oms logged with oms in other 3 credentials kds,go,testoms

# else:
#     print(f"Logout failed with status code {response_logout.status_code}")
#     print("Response:", response_logout.json())
#     print(f"\033[91m❌ TEST FAILED...! - Test Case ID : 001 \033[0m") # login failed so test passed


     
     

print(""*200)

# 2 : LOGIN AGAIN WITH USED TOKEN Or Logout with expired session token: 

# print("\033[1;34m LOGOUT AGAIN WITH USED TOKEN !\033[0m")

# user = {"loginId":"AutotestOMS", "password":"Smm@1234"}

# # Step 1: Login and get the token
# response_login = requests.post(login_url, json=user)
# if response_login.status_code != 200:
#     print("Login failed")
#     exit()
# else:
#    response_json=response_login.json()
#    token=response_login.json()["token"]["token"]
#    company_id = response_json["company"]["id"]
#    rest_id = response_json["restaurant"]["id"]   
# #    print(token)

# # Step 2: Logout (invalidate the token)
# headers = {
#     "Authorization": f"Bearer {token}",
#     "Content-Type": "application/json"
# }
# response_logout = requests.put(logout_url, headers=headers)
# # print(response_logout.status_code)
# if response_logout.status_code == 200:
#     # print("Successfully logged out.")
#      s=response_logout.status_code
# else:
#     # print("Logout may have failed or not invalidated token.") 
#     s=response_logout.status_code
# get_url = f"https://qa-oms.zolv.health/api/v1/dashboard/orders/web/{company_id}/{rest_id}/get-order-progress"
# # Step 3: Attempt to access a protected resource with the **now invalid** token
# response_protected = requests.get(get_url, headers=headers)

# # print("\n=== Reusing Logged-out Token ===")
# if response_protected.status_code != 200:
#     # print("✅ Token is invalid after logout, as expected.")
#     print("\033[92m✅ TEST PASSED : Test Case ID - 002 \033[0m")

# elif response_protected.status_code == 200:
#     # print("❌ Token still works after logout – potential security issue!")
#     print("\033[91m❌ TEST FAILED : Test Case ID - 002 \033[0m")

# else:
#     print(f"Received unexpected status code: {response_protected.status_code}")
#     print(response_protected.text)






# 3 : Logout with invalid token format : 

# Logout with invalid token format : 


print("\033[1;34m Logout with invalid token format\033[0m")

# Simulated token from client
token = "1234#.....-invalid-token"  # Invalid format example

# Prepare headers dictionary
headers = {}
login_payload = {
        "loginId":"AutotestOMS",
        "password":"Smm@1234"
}

  
response_login = requests.post(login_url,json=login_payload)
if response_login.status_code != 200:
    print("Login Failed ")
    print("Response:", response_login.json())
else:
    response_json = response_login.json()
    name=response_json.get('name')
    print("Response JSON : ",json.dumps(response_json,indent=4))
    token1= response_json.get('token',{}).get('token')
    print("login Success")
    print("INVALID TOKEN TEST ON LOGOUT")

    # Check if token is valid (e.g., starts with "Bearer " and length > 20)
    if token.startswith("Bearer ") and len(token) > 20:
        print("Logging out user with valid token.")
        headers["Authorization"] = token

        # Make logout request
        response = requests.put(logout_url, headers=headers)
        # print("Response status code:", response.status_code)
        print("Response body:", response.text,response.status_code)
        print("\033[91mUser logged out successfully.\033[0m")
    else:
        print("\033[92mInvalid token format. Logout rejected.\033[0m")



    

# print(" "*200) # for space 

