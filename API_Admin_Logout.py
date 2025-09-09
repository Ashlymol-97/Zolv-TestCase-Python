import requests
import time
import json
import random
import urllib.parse

import base64
import hashlib



failed_count=0
total_count=20  

print(" "*600) # for space


base_url= "https://qa-admin.zolv.health/"
login_url= "https://qa-admin.zolv.health/api/v1/user/login"
logout_url="https://qa-admin.zolv.health/api/v1/user/logout"


# 1 : logout : Logout with valid session token  :

print("\033[1;34m ADMIN LOGOUT TESTCASE! Document ID: TP_002 \033[0m")

# print("\033[1;34m Logout with valid session token...............!\033[0m")


login_payload = {
        "loginId":"ZolvQAAdmin",
        "password":"Smm@1234"
}

  
response_login = requests.post(login_url,json=login_payload)
if response_login.status_code == 200:
    response_json = response_login.json()
    name=response_json.get('name')
    # print(f"\033[91m✅ Login successful! Welcome, {loginId} | Name: {name} | Status: {response_login.status_code}\033[0m",{"loginId":loginId,"password":pwd})
    # print("Response JSON : ",json.dumps(response_json,indent=4))
    token= response_json.get('token',{}).get('token')


    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    # print(f"Using token: {headers.get('Authorization')}")

    response_logout = requests.put(logout_url,headers=headers) 
    if response_logout.status_code == 200:
        logout_json = response_logout.json()
        # print("Response JSON:", json.dumps(logout_json, indent=4))
        # print(f"Token (Logout): {token}")
        print(f"\033[92m✅ TEST PASSED...! : Test Case ID - 001 \033[0m") # login success so test failed becoz in oms logged with oms in other 3 credentials kds,go,testoms

    else:
        failed_count+=1
        # print(f"Logout failed with status code {response_logout.status_code}")
        # print("Response:", response_logout.json())
        print(f"\033[91m❌ TEST FAILED...! : Test Case ID - 001 : Error -  Invalid or expired session token. \033[0m") # login failed so test passed

else:
    print(f"\033[91m❌ Login failed with status code {response_login.status_code}\033[0m")
   
     





# 2 : LOGIN AGAIN WITH USED TOKEN Or Logout with expired session token: 

# print("\033[1;34m LOGOUT AGAIN WITH USED TOKEN !\033[0m")
user = {
    "loginId":"ZolvQAAdmin",
    "password":"Smm@1234"
}

# Step 1: Login and get the token
response_login1 = requests.post(login_url, json=user)
if response_login1.status_code != 200:
    s=response_login1.status_code
    # print("Login failed")
else:
    response_json1=response_login1.json()
    token1= response_json1.get('token',{}).get('token')
    company_id = response_json1["company"]["id"]
    # rest_id = response_json1["restaurant"]["id"]
    
# Step 2: Logout (invalidate the token)
    headers1 = {
        "Authorization": f"Bearer {token1}",
        "Content-Type": "application/json"
    }
    response_logout1 = requests.put(logout_url, headers=headers1)
    if response_logout1.status_code != 200:
        response_logout1.status_code
        # print("Logout may have failed or not invalidated token.")
    else:
        response_logout1.status_code

        # print("Successfully logged out.")

Get_url = f"https://qa-admin.zolv.health/api/v1/masters/user/web/{company_id}/get-user-list"

# Step 3: Attempt to access a protected resource with the **now invalid** token
response_protected = requests.get(Get_url, headers=headers1)

# print("\n=== Reusing Logged-out Token ===")
if response_protected.status_code != 200:
    print(f"\033[92m✅ TEST PASSED...! : Test Case ID - 002 \033[0m") 

    # print("✅ Token is invalid after logout, as expected.",response_protected.status_code)
elif response_protected.status_code == 200:
    failed_count+=1
    # print("❌ Token still works after logout – potential security issue!")
    print(f"\033[91m❌ TEST FAILED...! : Test Case ID - 002 : Error - Session expired. \033[0m") # login failed so test passed

else:
    print(f"Received unexpected status code: {response_protected.status_code}")
    print(response_protected.text)






# 3 : Logout with invalid token format : 


# print("\033[1;34m Logout with invalid token format\033[0m")

# Simulated token from client
invalid_token = "23434=rr=..#//.....-invalid-token"  # Invalid format example

# Prepare headers dictionary
headers2 = {}
login_payload = {
        "loginId":"ZolvQAAdmin",
        "password":"Smm@1234"
}

  
response_login2 = requests.post(login_url,json=login_payload)
if response_login2.status_code != 200:
    print("Login Failed ")
    # print("Response:", response_login.json())
else:
    response_json2 = response_login2.json()
    name=response_json2.get('name')
    # print("Response JSON : ",json.dumps(response_json,indent=4))
    # print("login Success")
    # print("INVALID TOKEN TEST ON LOGOUT")


    headers2 = {
        "Authorization": f"Bearer {invalid_token}",
        "Content-Type": "application/json"
    }
    response2 = requests.put(logout_url, headers=headers2)
    if response2.status_code != 200:
        # print("\033[92mInvalid token format. Logout rejected.\033[0m")
        print(f"\033[92m✅ TEST PASSED...! : Test Case ID - 003 \033[0m") 
    else:
        failed_count+=1
        print(f"\033[91m❌ TEST FAILED...! : Test Case ID - 003 : Error - Invalid token. \033[0m") # login failed so test passed
 




    

#4 :  lOGOUT  WITH WITHOUT TOKEN or Logout with missing token : 

# print("\033[1;34m LOGOUT WITH WITHOUT TOKEN !\033[0m")

response_login3 = requests.post(login_url, json=user)
if response_login3.status_code != 200:
    print("Login failed")
    exit()
else:
    empty_token = " "
#    print(f"Token obtained: {token}")
    headers3 = {
        "Authorization": f"Bearer {empty_token}",
        "Content-Type": "application/json"
    }

    # Step: Attempt logout with no token
    response3 = requests.put(logout_url,headers=headers3)

    # print("\n=== Logout Attempt Without Token ===")
    # print(f"Status Code: {response.status_code}")
    # print(f"Response Body: {response.text}")

    # Expected: 401 Unauthorized or 403 Forbidden
    if response3.status_code == 401 or response3.status_code == 403:
        print(f"\033[92m✅ TEST PASSED...! : Test Case ID - 004 \033[0m") 
        # print("✅ Logout blocked without token, as expected.")
    elif response3.status_code == 200:
        failed_count+=1
        # print("❌ Logout succeeded without token – potential security issue!")
        print(f"\033[91m❌ TEST FAILED...! : Test Case ID - 004 : Error -  Authentication required. \033[0m") # login failed so test passed
    else:
        print(f"Received unexpected status code: {response3.status_code}")







# 5 : Logout after session already terminated : 


# print("\033[1;34m Logout after session already terminated\033[0m")

response_login4 = requests.post(login_url, json=user)
if response_login4.status_code != 200:
    print("Login failed")
    exit()
else:
    response_json4=response_login4.json()
    token3= response_json4.get('token',{}).get('token')
#    print(f"Token obtained: {token}")
    headers4 = {
        "Authorization": f"Bearer {token3}",
        "Content-Type": "application/json"
    }

    # First logout attempt (session still valid)
    # print("\033[1;34mFirst logout attempt:\033[0m")
    response4 = requests.put(logout_url, headers=headers4)
    # print("Status code:", response4.status_code)
    # print("Response body:", response4.text)

    # print("-" * 50)

    # Second logout attempt (session already terminated)
    # print("\033[1;34mSecond logout attempt (same token):\033[0m")
    response4 = requests.put(logout_url, headers=headers4)

    # Check how the server handles repeat logout
    if response4.status_code != 200:
        # print("\033[92m✅ Token expired or session already terminated — Unauthorized.\033[0m")
        print(f"\033[92m✅ TEST PASSED...! : Test Case ID - 005 \033[0m") 

    elif response4.status_code == 200:
        failed_count+=1
        print(f"\033[91m❌ TEST FAILED...! : Test Case ID - 005 : Error -  Session expired. \033[0m") # login failed so test passed
        # print("\033[91mℹ️ Logout successful again — API may allow repeat logout.\033[0m")
    else:
        print("\033[91m❌ Unexpected response.\033[0m")

    # print("Status code:", response4.status_code)
    # print("Response body:", response4.text or "(empty)")







# 6 :  Access protected resource after logout  :



# print("\033[1;34m  Access protected resource after logout...................................\033[0m")

protected_url = f"https://qa-admin.zolv.health/api/v1/masters/user/web/{company_id}/get-user-list"

response_login5 = requests.post(login_url,json=login_payload)
if response_login5.status_code == 200:
    response_json5 = response_login5.json()
    # print("Login Successfully..")
    name=response_json5.get('name')

    token4= response_json5.get('token',{}).get('token')


# Authorization headers
    headers5 = {
        "Authorization": f"Bearer {token4}",
        "Content-Type": "application/json"
    }
    # print("Response JSON : ",json.dumps(response_json5,indent=4))


    # Step 1: Perform Logout
    # print("\033[1;34m[Step 1] Performing logout request...\033[0m")

    response_logout5 = requests.put(logout_url, headers=headers4)
    # print("Logout Status Code:", response_logout5.status_code)
    # print("Logout Response Body:", response_logout5.text)
    # print("\033[38;5;208m-\033[0m" * 100)

    # Step 2: Try to access protected resource after logout
    # print("\033[1;34m[Step 2] Attempting to access protected resource after logout...\033[0m")
    response_protected5 = requests.get(protected_url, headers=headers4)
    # print("Protected Resource Status Code:", response_protected.status_code)
    # print("Protected Resource Response Body:", response_protected.text)
    # print("\033[38;5;208m-\033[0m" * 100)

    # Step 3: Validate outcome
    if response_protected5.status_code == 401 or response_protected.status_code == 403:
        # print("\033[92m✅ Test Passed: Access denied as expected after logout.\033[0m",response_protected.status_code)
        print("\033[92m✅ Test Passed...! : Test Case ID - 006 \033[0m")

    else:
        failed_count+=1
        # print("\033[91m❌ Test Failed: Access still granted after logout.\033[0m")
        print("\033[91m❌ Test Failed...! : Test Case ID - 006 : Error -  Token invalid or expired. \033[0m")







# 7 : Client-side session/token cleanup logout : 


print("\033[1;93mTest Case ID -  007 :  Skipping  Token Cleanup....\033[0m")





# 8 : CSRF validation (if applicable) logout : 
 

print("\033[1;93mTest Case ID -  008 :  Skipping CSRF Validation....\033[0m")









# 9 :  Prevent back navigation post-logout : 

# print("\033[1;34m Prevent back navigation post-logout\033[0m")

protected_url = f"https://qa-admin.zolv.health/api/v1/masters/user/web/{company_id}/get-user-list"



response_login8 = requests.post(login_url,json=login_payload)
if response_login8.status_code == 200:
    response_json8 = response_login8.json()
    # print(f"\033[91m✅ Login successful! Welcome, {loginId} )
    # print("Response JSON : ",json.dumps(response_json,indent=4))
    token7= response_json.get('token',{}).get('token')

    headers8 = {
        "Authorization": f"Bearer {token7}",
        "Content-Type": "application/json"
    }


    # print("Performing logout request:")
    response_logout8 = requests.put(logout_url, headers=headers)
    # print("Logout Status Code:", response_logout8.status_code)
    # print("Logout Response Body:", response_logout8.text)
    # print("-" * 50)

    # print("Attempting to access protected resource after logout (simulate back navigation):")
    response_protected8 = requests.get(protected_url, headers=headers)
    # print("Access Status Code:", response_protected8.status_code)
    # print("Access Response Body:", response_protected8.text)
    # print("-" * 50)

    if response_protected8.status_code == 401 or response_protected8.status_code == 403:
        # print("\033[92m✅ Access denied after logout — back navigation prevented.\033[0m")
        print("\033[92m✅ Test Passed...! : Test Case ID - 009 \033[0m")

    else:
        failed_count+=1
        # print("\033[91m❌ Access granted — back navigation NOT prevented.\033[0m")
        print("\033[91m❌ Test Failed...! : Test Case ID - 009 : Error - Redirects to login screen. \033[0m")





#10 : Logging verification : doubt

print("\033[1;93mTest Case ID -  010 :  Skipping Logging verification....\033[0m")







#11 : Concurrent logout requests : 

# print("\033[1;34m Concurrent logout requests\033[0m")

c=0
responsecon_login = requests.post(login_url,json=login_payload)
if responsecon_login.status_code == 200:
    responsecon_json = responsecon_login.json()
    # print(f"\033[91m✅ Login successful! Welcome, {loginId} )
    # print("Response JSON : ",json.dumps(response_json,indent=4))
    concur_token= responsecon_json.get('token',{}).get('token')

    headers9 = {
        "Authorization": f"Bearer {concur_token}",
        "Content-Type": "application/json"
    }




    # Run 5 logout attempts using a for loop
    for i in range(1, 6):
        # print(f"Logout Request {i}")
        concurrent_response = requests.put(logout_url, headers=headers9)
        status = concurrent_response.status_code
        body = concurrent_response.text

        # print("Status Code:", status)
        # print("Response Body:", body)

        # Validation logic
        if i == 1:
            if status == 200:
                # print("\033[92m✅ Logout succeeded as expected.\033[0m")
                # print("\033[92m✅ Test Passed...!: Test Case ID - 011 \033[0m")
                status=response_login.status_code

            else:
                print("\033[91m❌ First logout should succeed, but it failed.\033[0m",status)
        else:
            if status in [401, 403]:
                print("\033[92m✅ Test Passed...! : Test Case ID - 011 \033[0m")
                # print("\033[92m✅ Logout attempt rejected as expected (session already terminated).\033[0m")
            elif status == 200:
                c+=1
                if c!=0 and c<=1:
                    failed_count+=1
                # print("\033[91mℹ️ Logout allowed again (API is idempotent).\033[0m")
                print("\033[91m❌ Test Failed...! : Test Case ID - 011 : Error - Token remained active after concurrent logout. \033[0m")
            else:
                print("\033[91m❌ Unexpected status code on repeated logout.\033[0m")

        # print("-" * 50)

    # print("All logout validation completed.")






print("\033[1;93mTest Case ID -  012 :  Skipping Logout during poor internet connection....\033[0m")




# 13 : # #logout With Invalid parameters : 


# print("\033[1;34mINVALID PARAMETERS TEST ON LOGOUT\033[0m")

c=0
response_login9 = requests.post(login_url,json=login_payload)
if response_login9.status_code == 200:
    response_json9 = response_login9.json()
    # print(f"\033[91m✅ Login successful! Welcome, {loginId} )
    # print("Response JSON : ",json.dumps(response_json,indent=4))
    invalid_token= response_json.get('token',{}).get('token')

    headers8 = {
        "Authorization": f"Bearer {invalid_token}",
        "Content-Type": "application/json"
    }


    # List of invalid logout payloads
    invalid_logout_payloads = [
        {},
        {"session": "fake_session_id"},
        {"Authorization": ""},
        {"Authorization": None},
        {"auth": "Bearer abc123"},
        {"token": "invalid_token_value"},
        {"Authorization": "Bearer  "},
        {"Authorization": 12345},
        {"Authorization": True},
        {"Authorization": {"key": "value"}}

    ]

    # Loop using enumerate for cleaner indexing
    for index, payload in enumerate(invalid_logout_payloads, start=1):
        # print("Test Case", index)
        # print("Payload:", payload)

        headers9 = {}

        if "Authorization" in payload:
            auth = payload["Authorization"]

            if type(auth) == str:
                auth = auth.strip()
                if auth.startswith("Bearer ") and len(auth) > 7:
                    headers9["Authorization"] = auth
                    # print("Attempting logout with Authorization header...")
                    print("\033[91m❌ Test Failed...! : Test Case ID - 013 : Error - Invalid parameter.\033[0m")

                else:
                    print("\033[92m✅ Test Passed...! : Test Case ID - 013 \033[0m")
                    # print("Invalid Authorization format. Logout not attempted.")
            else:
                    print("\033[92m✅ Test Passed...! : Test Case ID - 013 \033[0m")
                # print("Authorization value is not a string. Logout not attempted.")
        else:
                    print("\033[92m✅ Test Passed...! : Test Case ID - 013 \033[0m")
            # print("'Authorization' header missing. Logout not attempted.")

        if "Authorization" in headers9:
            response9 = requests.put(logout_url, headers=headers9)
            # print("Response status code:", response9.status_code)
            # print("Response body:", response9.text)
            if response9.status_code == 200: 
                c+=1
                if c!=0 and c<=1:
                    failed_count+=1
                # print("\033[92mYou have been successfully logged out..\033[0m")
                print("\033[91m❌ Test Failed...! : Test Case ID - 013 : Error - Invalid parameter. \033[0m")

            else:
                # print("\033[91mRequest not sent due to invalid or missing Authorization.\033[0m")
                print("\033[92m✅ Test Passed...! : Test Case ID - 013 \033[0m")
   


        # print("-" * 50)







# 14 : Logout using unsupported/ Invalid HTTP Method :

# # print("\033[1;34m Logout using unsupported/ Invalid HTTP Method\033[0m")

  
response_login10 = requests.post(login_url,json=login_payload)
if response_login10.status_code == 200:
    response_json10 = response_login.json()
    # print(f"\033[91m✅ Login successful! Welcome, {loginId} | Name: {name} | Status: {response_login.status_code}\033[0m",{"loginId":loginId,"password":pwd})
    # print("Response JSON : ",json.dumps(response_json,indent=4))
    token10= response_json10.get('token',{}).get('token')

    headers10 = {
        "Authorization": f"Bearer {token10}",
        "Content-Type": "application/json"
    }
    response_logout = requests.get(logout_url,headers=headers) 
    if response_logout.status_code == 200:
        logout_json = response_logout.json()
        # print("Response JSON:", json.dumps(logout_json, indent=4))
        # print(f"Token (Logout): {token}")
        failed_count+=1
        print(f"\033[91m❌ TEST FAILED...! : Test Case ID - 014 : Error - Invalid HTTP method. \033[0m") # login success so test failed becoz in oms logged with oms in other 3 credentials kds,go,testoms

    else:
        # print(f"Logout failed with status code {response_logout.status_code}")
        # print("Response:", response_logout.json())
        print(f"\033[92m✅ TEST PASSED...! : Test Case ID - 014 \033[0m") # login failed so test passed

else:
    print(f"\033[91m❌ Login failed with status code {response_login.status_code}\033[0m")
   








# 15 : Logout behavior when user is logged in across multiple devices (Logout from Device x after logging out from Device y )




# print("\033[1;34m  Logout behavior when user is logged in across multiple devices (Logout from Device x after logging out from Device y!\033[0m")


logins = {
    "loginId": "ZolvQAAdmin",
    "password": "Smm@1234"
}

# Step 2: Login from Device x
# print("🔐 Step 2: Logging in from Device x...")
response_x = requests.post(login_url,json=logins)

if response_x.status_code == 200:
    json_x=response_x.json()
    token_x = json_x.get('token',{}).get('token')
    company_id = json_x['company']['id']


    # token_x = response_x.json()["token"]
    # print("\033[92m✅ Device x Login Successful.\033[0m")
    # print("Token x:", token_x)
else:
    # print("\033[91m❌ Device x Login Failed.\033[0m")
    # print("Status Code:", response_x.status_code)
    response_x.text
    # exit()



# Step 3: Login from Device y
# print("\n🔐 Step 3: Logging in from Device y...")
response_y = requests.post(login_url, json=logins)

if response_y.status_code == 200:
    json_y=response_y.json()
    token_y = json_y.get('token',{}).get('token')
    # token_y = response_y.json()["token"]
    # print("\033[92m✅ Device y Login Successful.\033[0m")
    # print("Token B:", token_b)
else:
    # print("\033[91m❌ Device y Login Failed.\033[0m")
    # print("Status Code:", response_y.status_code)
    response_y.text
    # exit()



# Step 4: Logout from Device y
# print("\n🚪 Step 4: Logging out from Device y...")
logout_headers_y={
        "Authorization": f"Bearer {token_y}",
        "Content-Type": "application/json"
    }
response_logout_y = requests.put(logout_url, headers=logout_headers_y)

if response_logout_y.status_code == 200:
    response_logout_y.status_code
    # print("\033[92m✅ Device y logout successful.\033[0m",logout_url)

    # print("\033[92m✅ Device y logout successful.\033[0m",logout_url)
else:
    # print("\033[91m❌ Device y logout failed.\033[0m",response_logout_y.text)
    response_logout_y.status_code
    # print("Response:", response_logout_y.text)
    # exit()

# Step 5: Attempt Logout from Device x
# print("\n🚪 Step 5: Attempting logout from Device x after Device y logout...")
headers_x = {
        "Authorization": f"Bearer {token_x}",
        "Content-Type": "application/json"
    }
response_logout_x = requests.get(Get_url, headers=headers_x)

if response_logout_x.status_code == 200:
    failed_count+=1
    # print("\033[91m ❌Device x logout successful — Session remained valid after Device y logout.\033[0m")
    print("\033[91m❌ Test Failed...! : Test Case ID - 015 : Error - Session already expired. \033[0m")

else:
    # print("\033[92m✅ Device x logout failed — Session may have been Expired by Device y logout.\033[0m")
    # print("Status Code:", response_logout_x.status_code)
    # print("Response:", response_logout_x.text)
    print("\033[92m✅ Test Passed...! : Test Case ID - 015 \033[0m")



print(f"\033[1;34mTotal TEST FAILEDS  : {failed_count}/{total_count}\033[0m")




if failed_count == 0:
    print("\033[92m ✅ All TEST PASSED \033[0m")



time.sleep(0.1)
print("\n")