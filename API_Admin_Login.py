
import requests
import time
import json
import random
import urllib.parse

import base64
  


failed_count=0
total_count=25

base_url= "https://qa-admin.zolv.health/"
login_url= "https://qa-admin.zolv.health/api/v1/user/login"
logout_url="https://qa-admin.zolv.health/api/v1/user/logout"



# 1 : Login TestCase : Login with valid Login Credentials

print("\033[1;34m ADMIN LOGIN TESTCASE! Document ID: TP_001\033[0m")
# print("\033[1;34m Login with valid Login Credentials! Document ID: TP_001\033[0m")


login_payload = {
        "loginId":"ZolvQAAdmin",
        "password":"Smm@1234"
}

  
response_login = requests.post(login_url,json=login_payload)
if response_login.status_code == 200:
    response_json = response_login.json()
    name=response_json.get('name')
    # print("...",response_login.text)
    valid_token= response_json.get('token',{}).get('token')

    headers= {
        "Authorization": f"Bearer {valid_token}",
        "Content-Type": "application/json"
    }
    # print(f"\033[91m✅ Login successful! Welcome, {loginId} | Name: {name} | Status: {response_login.status_code}\033[0m",{"loginId":loginId,"password":pwd})
    # print("Response JSON : ",json.dumps(response_json,indent=4))
    # print(f"\033[92m✅  Login successful for: {loginid} | Name: {name} | Status: {response_login.status_code}\033[0m")
    print(f"\033[92m✅ TEST PASSED...! : Test Case ID - 001 \033[0m") # login success so test failed becoz in oms logged with oms in other 3 credentials kds,go,testoms

    # print(f"Token (Login): {token1}") 

else:

    failed_count+=1
    # print(f"\033[91m❌ Login failed with status code {response_login.text}\033[0m")
    print(f"\033[91m❌ TEST FAILED...! : Test Case ID - 001 : Error - Invalid Credentials \033[0m") # login failed so test passed

    # print("Response:", response_login.json())








# 2 :  Login with invalid credentials :

# print("\033[1;34m Login with Invalid Login Credentials! \033[0m")

  
Invalid_login_payload = {
        "login_id":"abcd",
        "password":"1234"
}

response_invalidlogin = requests.post(login_url,json=Invalid_login_payload)
if response_invalidlogin.status_code == 200:
    invalid_json = response_invalidlogin.json()
    name=invalid_json.get('name')
    failed_count+=1
    # print(failed_count,"f")
  
    # print(f"\033[91m✅ Login successful! Welcome, {loginId} | Name: {name} | Status: {response_login.status_code}\033[0m",{"loginId":loginId,"password":pwd})
    # print("Response JSON : ",json.dumps(response_json,indent=4))
    token1= invalid_json.get('token',{}).get('token')
    # print(f"\033[91m❌  Login successful for: {loginid} | Name: {name} | Status: {response_login.status_code}\033[0m")
    print(f"\033[91m❌ TEST FAILED...! : Test Case ID - 002 : Error - Invalid Credentials \033[0m") # login success so test failed becoz in oms logged with oms in other 3 credentials kds,go,testoms

    # print(f"Token (Login): {token1}") 

else:
    # print(f"\033[92m✅  Login failed with status code {response_login.status_code}\033[0m",{"loginId":loginid,"password":pwd})
    print(f"\033[92m✅ TEST PASSED...! : Test Case ID - 002 \033[0m") # login failed so test passed

    # print("Response:", response_invalidlogin.json())
    # print(f"\033[92m✅ TEST PASSED...!\033[0m") # login failed so test passed



# print(" "*200) # for space 






# 3 : Login with missing Login ID :

# print("\033[1;34m Login with missing Login ID\033[0m")

Missing_login_payload = {
    "loginId":None,
    "password":"Smm@1234"
}


response_login = requests.post(login_url,json=Missing_login_payload)
if response_login.status_code == 200:
    response_json = response_login.json()
    name=response_json.get('name')
    failed_count+=1

    # print(f"\033[91m✅ Login successful! Welcome, {loginId} | Name: {name} | Status: {response_login.status_code}\033[0m",{"loginId":loginId,"password":pwd})
    # print("Response JSON : ",json.dumps(response_json,indent=4))
    token1= response_json.get('token',{}).get('token')
    # print(f"\033[91m❌  Login successful for: {loginid} | Name: {name} | Status: {response_login.status_code}\033[0m")
    print(f"\033[91m❌ TEST FAILED...! : Test Case ID - 003 : Error - Login ID required \033[0m") # login success so test failed becoz in oms logged with oms in other 3 credentials kds,go,testoms

    # print(f"Token (Login): {token1}") 

else:
    # print(f"\033[92m✅ Login failed with status code {response_login.status_code}\033[0m",{"loginId":loginid,"password":pwd})
    print(f"\033[92m✅ TEST PASSED...! : Test Case ID - 003 \033[0m") # login failed so test passed

    # print("Response:", response_login.json())
    # print(f"\033[92m✅ TEST PASSED...!\033[0m") # login failed so test passed







# 4 : Login with missing password :


# print("\033[1;34m Login with missing password\033[0m")

Missingpwd_login_payload = {
    "loginId":"AutotestAdmin",
    "password":None
}


response_login = requests.post(login_url,json=Missingpwd_login_payload)
if response_login.status_code == 200:
    response_json = response_login.json()
    name=response_json.get('name')
    # print(f"\033[91m✅ Login successful! Welcome, {loginId} | Name: {name} | Status: {response_login.status_code}\033[0m",{"loginId":loginId,"password":pwd})
    # print("Response JSON : ",json.dumps(response_json,indent=4))
    token1= response_json.get('token',{}).get('token')
    failed_count+=1

    # print(f"\033[91m❌  Login successful for: {loginid} | Name: {name} | Status: {response_login.status_code}\033[0m")
    print(f"\033[91m❌ TEST FAILED...! : Test Case ID - 004 : Error - Password required \033[0m") # login success so test failed becoz in oms logged with oms in other 3 credentials kds,go,testoms

    # print(f"Token (Login): {token1}") 

else:
    # print(f"\033[92m✅ Login failed with status code {response_login.status_code}\033[0m",{"loginId":loginid,"password":pwd})
    print(f"\033[92m✅ TEST PASSED...! : Test Case ID - 004 \033[0m") # login failed so test passed

    # print("Response:", response_login.json())
    # print(f"\033[92m✅ TEST PASSED...!\033[0m") # login failed so test passed











#5 : Login with user having only KDS privilege  : 

# print("\033[1;34mLogin with user having only KDS privilege\033[0m")

kds_privilege_payload ={
    "loginId": "AutotestKDS",
    "password": "Smm@1234"
}

response_login = requests.post(login_url,json=kds_privilege_payload)
if response_login.status_code == 201:
    response_json = response_login.json()
    failed_count+=1
    # print(failed_count,"f")


    # print("Response JSON : ",json.dumps(response_json,indent=4))

    print("\033[91m❌ TEST FAILED...! : Test Case ID - 005 : Error - Unauthorized user \033[0m")
else:
    print("\033[92m✅ TEST PASSED...! : Test Case ID - 005 \033[0m")









# 6 : Login with user having only Go privilege :

# print("\033[1;34mLogin with user having only Go privilege\033[0m")

go_privilege_payload ={
    "loginId": "AutotestZolvGo", 
    "password": "Smm@1234"
}

response_login = requests.post(login_url,json=go_privilege_payload)
if response_login.status_code == 200:
    response_json = response_login.json()
    failed_count+=1
    # print(failed_count,"f")


    # print("Response JSON : ",json.dumps(response_json,indent=4))
    print("\033[91m❌ TEST FAILED...! : Test Case ID - 006 : Error - Unauthorized user  \033[0m")
else:
    print("\033[92m✅ TEST PASSED...! : Test Case ID - 006 \033[0m")











# 7 : Concurrent Login Attempts : 

# print("\033[1;34m Concurrent Login Attempts : rate limiting (multiple attempts in quick succession)\033[0m")
c=0
# Test login rate limiting (multiple attempts in quick succession) : 
headers = {
    "Content-Type": "application/json"
}

# Payload with correct field names
invalid_login_payload = {
    "loginId": "ZolvQAAdmin",   # ✅ Use "loginId" only if this is accepted by the API (otherwise use "username")
    "password": "Smm@1234"
}

# print("\033[1;34mRate limiting (multiple attempts in quick succession) Test\033[0m\n")
# print("Testing rate limiting protection...")

# Loop for repeated login attempts
for i in range(10):
    response = requests.post(login_url, json=invalid_login_payload)
    # print(f"Attempt {i + 1} status code: {response.status_code}")
    # print(response.text)
    # print(response.status_code)

    if response.status_code == 429:
        # print("\033[1;92m  Rate limiting correctly implemented!\033[0m")
        print("\033[1;92m✅ TEST PASSED...! : Test Case ID - 007 \033[0m")

        break
    elif response.status_code == 200:
        c+=1
        
        # print(c)

        print(f"\033[91m❌ TEST FAILED...! : Test Case ID - 007 : Error - Concurrent login attempt denied for user.  \033[0m")
    elif response.status_code == 400:
        print("\033[1;91m❌ Request format is invalid (400 Bad Request). Fix payload.\033[0m")
    
    elif response.status_code >= 500:
        print("\033[1;91m❌ Server error — something is wrong on the backend.\033[0m")

        
if c!=0 and c<=10:
    failed_count+=1
time.sleep(0.1 )








# 8 : Login with Inactive User  :

# print("\033[1;34mLogin with Inactive User\033[0m")

time.sleep(0.1 )


# 🔐 Target user credentials
username_input = "Testinactive"
password_input = "Smm@1234"

# 🔒 Stored correct credentials (mocked for comparison)
stored_username = "Testinactive"
stored_password = "Smm@1234"

# 🔑 Admin credentials and login URL
admin_url = "https://qa-admin.zolv.health/api/v1/user/login"

# 🔐 Admin login
admin_login = requests.post(login_url, json={"loginId": "ZolvQAAdmin", "password": "Smm@1234"})

if admin_login.status_code == 200:
    admin_json = admin_login.json()
    token_admin = admin_json['token']['token']
    name = admin_json['name']
    company_id = admin_json['company']['id']

    # print("\033[92m✅ Admin login successful:\033[0m", name, company_id)

    # 📋 Get user list
    user_url = f"https://qa-admin.zolv.health/api/v1/masters/user/web/{company_id}/get-user-list?page=2&size=10&sort=1&ignorePaging=false&roleId=&name=&isActive="
    user_header = {
        "Authorization": f"Bearer {token_admin}",
        "Content-Type": "application/json"
    }

    user_responses = requests.get(user_url,headers=user_header)
    # print(user_responses.status_code)
    if user_responses.status_code == 200:
        user_list = user_responses.json().get('users', [])
        # print("🔎 Sample user object:", user_list[-1])  # For debugging structure

        user_found = False

        for user in user_list:
            if user["loginId"] == username_input:
                user_found = True
                is_active = user["isActive"]

                if is_active:
                    print(f"\033[92m✅ User {username_input} is active. Attempting login...\033[0m")

                    # Try to log in as the user
                    user_login = requests.post(login_url, json={"loginId": username_input, "password": password_input})

                    if user_login.status_code == 200:
                        print(f"\033[92m✅ Login successful for active user: {username_input}\033[0m")
                    #    print(f"\033[92m✅ Test Passed: - Test Case ID : 010\033[0m")

                    else:
                        # print(f"\033[91m❌ Test Failed:- Test Case ID : 010\033[0m")
                        print(f"\033[91m❌ Login failed for active user: {username_input} (unexpected)\033[0m")
                        # print(user_login.text)


                else:
                    # print(f"\033[93m⚠️ User {username_input} is inactive. Attempting login to verify block...\033[0m")

                    # Attempt login for inactive user (should fail)
                    user_login = requests.post(login_url, json={"loginId": username_input, "password": password_input})

                    if user_login.status_code != 200:
                        # print(f"\033[92m✅ Test Passed: Inactive user {username_input} was blocked from login.\033[0m") 
                        print(f"\033[92m✅ TEST PASSED...! : Test Case ID - 008 \033[0m")
                        # print(user_login.text)

                    else:
                        # print(f"\033[91m❌ Test Failed: Inactive user {username_input} was able to login!\033[0m")
                        failed_count+=1
                        print(f"\033[91m❌ TEST FAILED...! : Test Case ID - 008 : Error - The user is currently inactive\033[0m")
                        # print(user_login.text)

        if not user_found:
            print(f"\033[91m❌ User {username_input} not found in user list\033[0m")

    else:
        print("\033[91m❌ Failed to fetch user list.\033[0m", user_responses.status_code)

else:
    print("\033[91m❌ Admin login failed.\033[0m", admin_login.status_code)









# # 9 :  Login with Deleted User Credentials : 



# print("\033[1;34m LOGIN DELETED USER TESTCASE!\033[0m")


# admin_url = "https://qa-admin.zolv.health/api/v1/user/login"
admin_logout = "https://qa-admin.zolv.health/api/v1/user/logout"

admin_login = requests.post(login_url, json={"loginId": "ZolvQAAdmin", "password": "Smm@1234"})
if admin_login.status_code == 200:
    admin_json = admin_login.json()
    admin_tokens = admin_json['token']['token']
    company_json = admin_login.json()

    company_id = company_json["company"]["id"]
    # print("Response JSON :", json.dumps(company_json, indent=4))

    # print("Logged ")
    
    login_id = "Testdeladmin"
    password= "Smm@1234"



    create_user_payload =  {
        "name": "Testdeladmin",
        "email": "",
        "phone": "",
        "loginId": "Testdeladmin",
        "employeeCode": "td4",
        "type": "admin_user",
        "departmentId": "68709372293ae6389032a052",
        "privilegedAreas": [
            "68ac344d386d2a3a01cc05a3"
        ],
        "isActive": True,
        "isEmployee": True,
        "isStudent": False,
        "subscriptionEnabled": True,
        "employeeCreditApplicable": False,
        "employeeWalletApplicable": False,
        "subscriptionGroup": "68a59e1403cfe84816ecd0ca",
        "password": "Smm@1234"
    }



    # create_user_url = f"https://qa-admin.zolv.health/api/v1/masters/user/web/{company_id}/create-user"
    headers_admin =  {
        "Authorization": f"Bearer {admin_tokens}",
        "Content-Type": "application/json"
    }

    response_create=requests.post(base_url + f"api/v1/masters/user/web/{company_id}/create-user",json=create_user_payload,headers=headers_admin)
    if response_create.status_code != 201:
    
        # print("Failed user creation...")
        print(response_create.text,"................")
        response_create.status_code
    else:
        user_token = admin_json['token']['token']
        ceateuser_json = response_create.json()
        # print("User Creation successfull...")
        # print("Response JSON :", json.dumps(ceateuser_json, indent=4))


    

        # ----------------------
        # Login as test user
        # ----------------------
        user1 = requests.post(login_url, json={"loginId": login_id, "password": password})

        if user1.status_code == 200:
            user1_json = user1.json()
            # print("Response JSON :", json.dumps(user1_json, indent=4))
            name_user1 = user1_json['name']
            company_id = user1_json['company']['id']
            toke = user1_json['token']['token']
            user_id = user1_json['id']

            # print("\033[92m✅User login successful\033[0m")
            # print("Company ID:", company_id)
            # print("Response JSON:")
            

            # Step 2: Logout test user
            headers = {"Authorization": f"Bearer {toke}"}
            logout_response = requests.put(logout_url, headers=headers)
            if logout_response.status_code == 200:
                S=logout_response.status_code
                # print("\033[92m✅ Test user logout successful\033[0m")
            else:
                # print("\033[91m❌ Test user logout failed with status code:\033[0m")
                logout_response.text

        else:
            # print("\033[92m✅ Test user login failed with status code: Test Case ID - 009 \033[0m")
            user1.text

        # ----------------------
        # Step 3: Admin login
        # ----------------------
        admin_login = requests.post(admin_url, json={"loginId": "ZolvQAAdmin", "password": "Smm@1234"})
        if admin_login.status_code == 200:
            admin_json = admin_login.json()
            admin_token = admin_json['token']['token']
            name = admin_json['name']

            # print("\033[92m✅ Admin login successful:\033[0m", name)

            # Step 4: Delete the user
            delete_url = "https://qa-admin.zolv.health/api/v1/masters/user/web/{company_id}/delete-user/{user_id}"

            delete_urls = delete_url.format(company_id=company_id, user_id=user_id)
            headers = {"Authorization": f"Bearer {admin_token}"}
            delete_response = requests.patch(delete_urls, headers=headers)

            if delete_response.status_code == 200:
                # print("\033[92m✅ Test user deleted successfully\033[0m")

                # Step 5: Logout admin
                logout_admin_response = requests.put(admin_logout, headers=headers)
                if logout_admin_response.status_code == 200:
                    logout_res=logout_admin_response.json()
                    # print("\033[92m✅ Admin logout successful\033[0m")
                else:
                    # print("\033[91m❌ Admin logout failed with status code:\033[0m")
                    # print(logout_admin_response.text)
                    msg=logout_admin_response.text


                # Step 6: Try to log in as deleted user
                deleted_login = requests.post(login_url, json=create_user_payload)
                if deleted_login.status_code != 200:
                    print("\033[92m✅ TEST PASSED...! : Test Case ID - 009\033[0m")
                    # print("\033[92m✅ TEST PASSED :  Deleted user login correctly blocked (401 Unauthorized) : Test Case ID - 009\033[0m")
                else:
                    failed_count+=1
                    print("\033[91m❌ TEST FAILED...! : Test Case ID - 009 : Error - User not found \033[0m")

                    # print("\033[91m❌ TEST FAILED : Unexpected login status for deleted user: Test Case ID - 009 \033[0m")
                    # print(deleted_login.text)

            else:
                print("\033[91m❌ Failed to delete test user. Status:\033[0m")
                # print(delete_response.text)

        else:
            print("\033[91m❌ Admin login failed with status code:\033[0m")
            # print(admin_login.text)


        # print(" "*200) # for space 






# # 10 : Login with additional field in payload : 

# print("\033[1;34m Login with additional field in payload \033[0m")

extrafield_payload ={
    "loginId": "AutotestAdmin",
    "password": "Smm@1234", 
    "extraField": "unexpected"
}
response_login = requests.post(login_url,json=extrafield_payload)
if response_login.status_code == 200:
    token = response_login.json()["token"]["token"]
    # print(token,"...")
    response_json = response_login.json()
    failed_count+=1
    # print(failed_count,"f")


    # print("Response JSON : ",json.dumps(response_json,indent=4))
    # print("\033[1;91m❌  Login successful with extra field.! - Test Case ID : 016 \033[0m")
    print(f"\033[91m❌ TEST FAILED...! : Test Case ID - 010 : Error - Unexpected fields in payload \033[0m") # login failed so test passed

else:
    # print(f"\033[92m✅ Login failed due to extra field — API enforces strict schema. \033[0m",response_login.status_code) # login failed so test passed
    print("\033[1;92m✅ TEST PASSED...! : Test Case ID - 010 \033[0m")
    # print("Response:", response_login.json())






#  11 : Login with extremely long payload :

# print("\033[1;34m Login with extremely long payload \033[0m")

long_payload ={
    "loginId":"AutotestAdmin" + "a" * 1000, 
    "password":"Smm@1234" + "b" * 10000
}                                  #extremely long inputs (potential buffer overflow)
response_login = requests.post(login_url,json=long_payload)
if response_login.status_code != 200:
    # print("\033[1;92m✅ API couldn't handle long payload.! \033[0m",response_login.status_code)
    print("\033[1;92m✅ TEST PASSED...! : Test Case ID - 011 \033[0m")

    # print("Response:", response_login.json())
else:
    failed_count+=1
    # print(f"\033[91m❌ Login succeeded with long credentials. \033[0m",response_login.status_code) # login failed so test passed
    print(f"\033[91m❌ TEST FAILED...! : Test Case ID - 011 : Error - Payload too large \033[0m") # login failed so test passed







#12 : Login from Device B using same credentials while Device A login is active (multiple device Login behaviour) :


# print("\n")


# print("\033[1;34m System must allow simultaneous logins from multiple devices using same credentials! \033[0m")



login = {
    "loginId": "ZolvQAAdmin",
    "password": "Smm@1234"
}

# Step 1: Login from Device A
# print("🔐 Logging in from Device A...")
response_a = requests.post(login_url, json=login)

if response_a.status_code == 200:
    response_json = response_a.json()
    token_a = response_json["token"]["token"]
    company_id = response_json["company"]["id"]
    headers_a = {
    "Authorization": f"Bearer {token_a}",
    "Content-Type": "application/json"
    }
    # rest_id = response_json["restaurant"]["id"]
    # print("\033[92m✅ Device A Login Successful.!\033[0m", response_a.status_code)
    # print("Token A:", token_a)
else:
    # print("\033[91m❌ Device A Login Failed.\033[0m")
      response_a.status_code

# Step 2: Login from Device B using same credentials
# print("\n🔐 Logging in from Device B (same credentials)...")
response_b = requests.post(login_url, json=login)

if response_b.status_code == 200:
    token_b = response_b.json()["token"]["token"]
    # print("\033[92m✅ Device B Login Successful.!\033[0m", response_b.status_code)
    # print("Token B:", token_b)
else:
    # print("\033[91m❌ Device B Login Failed — multiple login incorrectly blocked.\033[0m")
    exit()

# Step 3: Use Device A token to access protected endpoint
# print("\n🔄 Verifying Device A token is still valid...")

url= f"https://qa-admin.zolv.health/api/v1/company/web/get-module-list/{company_id}"
response_check_a = requests.get(url, headers=headers_a)

if response_check_a.status_code == 200:
    failed_count+=1
    # print(failed_count,"f")

    # print("\033[91m❌ Device A token is still valid after Device B login — simultaneous login allowed. : Test Case ID - 020 \033[0m")
    print("\033[91m❌ TEST FAILED...! : Test Case ID - 012  :  Error - Unauthorized \033[0m")

else:
    # print("\033[92m✅ Device A token was rejected after Device B login. : Test Case ID - 020 \033[0m")
    print("\033[92m✅ TEST PASSED...! : Test Case ID - 012 \033[0m")

    # print("Status Code:", response_check_a.status_code)
    # print("Response:", response_check_a.text)





# 13 : Login with special characters input in Login ID (username):

# print("\033[1;34m Login with special characters input in Login ID (username)! \033[0m")

special_chars_username_payload = {
    "loginId": "user@#$%^&*()",
    "password": "Smm@1234"
}

  
response_special_chars = requests.post(login_url,json=special_chars_username_payload)
if response_special_chars.status_code != 200:
    special_chars_json = response_special_chars.json()
    name=special_chars_json.get('name')
    # print("\033[1;92mTest for special characters in username passed!\033[0m")
    # print("Response:", response_special_chars.json())

    # print("...",response_special_chars.text)
    # print("Response JSON : ",json.dumps(special_chars_json,indent=4))
    special_chars_token= special_chars_json.get('token',{}).get('token')
    print(f"\033[92m✅ TEST PASSED...! : Test Case ID - 013 \033[0m") 
    # print(f"Token (Login): {special_chars_token}") 

else:

    failed_count+=1
    # print(f"\033[91m❌ Login failed with status code {response_special_chars.text}\033[0m")
    print(f"\033[91m❌ TEST FAILED...! : Test Case ID - 013  :  Error - Special characters not allowed in Login Id \033[0m") # login failed so test passed
    # print("Test for special characters in username failed! Login succeeded with special characters.")








# 14 : Login with malformed JSON request : 


# print("\033[1;34m  Login with malformed JSON request! \033[0m")


headers_without_content_type = {"Authorization": ""}
response_malformed_json = requests.post(
    login_url + "/api/v1/user/login",
    data="This is not valid JSON",
    headers=headers_without_content_type
)
if response_malformed_json.status_code != 200:
    # print("\033[1;92mTest for malformed JSON passed!\033[0m")
    print(f"\033[92m✅ TEST PASSED...! : Test Case ID - 014 \033[0m") 
    # print("Status code:................", response_malformed_json.status_code)
else:
    failed_count+=1
    # print("\033[1;91mTest for malformed JSON failed! Server accepted malformed input.\033[0m")
    print(f"\033[91m❌ TEST FAILED...! : Test Case ID - 014  :  Error - Invalid JSON \033[0m") # login failed so test passed








# 15 :Login with emoji characters input : 


# print("\033[1;34m  Login with emoji characters input! \033[0m")


unicode_payload = {
    "loginId": "用户名😊",
    "password": "密码🔒"
}

response_unicode = requests.post(login_url,json=unicode_payload)
if response_unicode.status_code != 200:
    response_unicode_json = response_unicode.json()
    # print("\033[1;92mTest for Unicode/emoji handling passed!\033[0m")
    # print("Response JSON : ",json.dumps(response_unicode_json,indent=4))
    response_unicode_token= response_unicode_json.get('token',{}).get('token')
    print(f"\033[92m✅ TEST PASSED...! : Test Case ID - 015 \033[0m") 
    # print(f"Token (Login): {response_unicode_token}") 

else:

    failed_count+=1
    # print("\033[1;31mTest for Unicode/emoji handling failed! Login succeeded with unusual characters.\033[0m")
    print(f"\033[91m❌ TEST FAILED...! : Test Case ID - 015  :  Error - Invalid characters \033[0m") # login failed so test passed









# 16 : Case sensitivity in Login :


# print("\033[1;34m  ase Case sensitivity in Login! \033[0m")


case_sensitivity_payload = {
    "loginId": "ZolvQAAdmin".upper(),
    "password": "Smm@1234"
}

  
response_case_sensitivity = requests.post(login_url,json=case_sensitivity_payload)
if response_case_sensitivity.status_code != 200:
    case_sensitivity_json = response_case_sensitivity.json()
    # print("\033[1;93mUsername appears to be case-insensitive.\033[0m")
    # print("Response JSON : ",json.dumps(case_sensitivity_json,indent=4))
    case_sensitivity_token= special_chars_json.get('token',{}).get('token')
    print(f"\033[92m✅ TEST PASSED...! : Test Case ID - 016 \033[0m") 
    # print(f"Token (Login): {case_sensitivity_token}") 

else:

    failed_count+=1
    # print("\033[1;93mUsername appears to be case-sensitive.\033[0m")
    print(f"\033[91m❌ TEST FAILED...! : Test Case ID - 016  :  Error - Username appears to be case-insensitive  \033[0m") # login failed so test passed
    # print("Test for case sensitivity in username failed! Login succeeded with case sensitivity.")











# General Considerations :




# 1 : Un Authorized User (Privilege) :


# print("\033[1;34m Un Authorized User (Privilege)![0m")

c=0
Unauthorized_payload = [
    {"loginId": "AutotestZolvGo", "password": "Smm@1234"},
    {"loginId": "TestOMS", "password": "Smm@1234"},
    {"loginId": "user@example.com","password": "userpassword","userType": ""}, 
    {"loginId": "Testdeleteuser","password": "Testdeleteuser@1234"}
]
for user in Unauthorized_payload:
    login_Auth = requests.post(login_url,json=user)
    # print(Unauthorized_payload,login_Auth)
    if login_Auth.status_code != 200:
        print("\033[92m✅ TEST PASSED...! : Test Case ID - 111 \033[0m")
      
    else:
        c+=1
          
        if c!=0 and c<=1:
          failed_count+=1
          error_message={"Un"}
        #   print(failed_count,"f")
        print("\033[91m❌ TEST FAILED...! : Test Case ID - 111 : Error - Unauthorized user \033[0m")



    # time.sleep(0.1)  # Small delay between requests







# 2 :   Invalid API endpoint (intentionally wrong) : 

# print("\033[1;34mLOGIN TESTCASE - Invalid Endpoint, Minimal Payload\033[0m")

invalidlogin_url = "https://qa-admin.zolv.health/api/v1/user/invalid_login"  # Example: endpoint is incorrect

login_payload = {
        "loginId":"ZolvQAAdmin",
        "password":"Smm@1234"
}


    # Send POST request to invalid endpoint

response = requests.post(invalidlogin_url, json=login_payload)
# print(f"Status Code: {response.status_code}")

# Check if response is successful or has a response code
if response.status_code == 200:
    # print(response.text,"Login with Invalid API endpoint")
    failed_count+=1
    print("\033[91m❌ TEST FAILED...! : Test Case ID - 112 : Error - Invalid API endpoint\033[0m")
else:
    print("\033[92m✅ TEST PASSED...! : Test Case ID - 112 \033[0m")
    # print(response.text,"Invalid API endpoint")
    # print(response.status_code)







# 3 : Invalid Parameters :

# print("\033[1;34mLOGIN TESTCASE - Invalid Parameters\033[0m")

c=0
Invalidparams_login_payload = [
    {"loginId": "abcd@123", "password": "asdasdasd"}, # Small delay between requests
    {"loginId": "12345", "password": ""},
    {"loginId": "12345", "password": "6543"},
    {"loginId": "asdf@#$12", "password": 12344}, 
    {"loginId": "", "password": "Smm@1234"},
    {"loginId": True, "password": False},                                              #Boolean Value Attempts
    {"loginId": "用户名😊", "password": "密码🔒"},                                     #Emoji value Attempts
    {"loginId": "12345", "password": ""},
    {"loginId": { "$ne": None },"password": { "$ne": None }},                           #NoSQL injection Attempts 
    {"loginId": "' OR '1'='1", "password": "anything"},                                 #SQL Injection Attempt
    {"loginId": "<![CDATA[admin]]>","password": "<![CDATA[password]]>"},                #XML Injection Attempt 

    {"loginId": "' OR '1'='1", "password": "test123"},                                  #    #// Malicious query parameter
    {"loginId": "<script>alert('XSS')</script>", "password": "test123"},
    {"loginId": "'; DROP TABLE users; --", "password": "test123"},
    {"loginId": "../../../../etc/passwd", "password": "test123"},
    {"loginId": "\" OR \"\" = \"", "password": "test123"},
    {"loginId": "reboot", "password": "test123"},
    {"loginId": "${7*7}", "password": "test123"},
    {"loginId": "%3Cscript%3Ealert('XSS')%3C/script%3E", "password": "test123"},
]


for invalid in Invalidparams_login_payload:

    response_invalidlogin = requests.post(login_url,json=Invalidparams_login_payload)
    if response_invalidlogin.status_code == 200:
        invalid_json = response_invalidlogin.json()
        name=invalid_json.get('name')    
        c+=1
        # print(f"\033[91m❌ Login successful! Welcome, {loginId} | Name: {name} | Status: {response_login.status_code}\033[0m",{"loginId":loginId,"password":pwd})
        # print("Response JSON : ",json.dumps(response_json,indent=4))
        token1= invalid_json.get('token',{}).get('token')
        # print(f"\033[91m❌  Login successful for: {loginid} | Name: {name} | Status: {response_login.status_code}\033[0m")
        print(f"\033[91m❌ TEST FAILED...! : Test Case ID - 113 : Error - Invalid Input Format\033[0m") # login success so test failed becoz in oms logged with oms in other 3 credentials kds,go,testoms

        # print(f"Token (Login): {token1}") 

    else:
        # print(f"\033[92m✅  Login failed with status code {response_login.status_code}\033[0m",{"loginId":loginid,"password":pwd})
        print(f"\033[92m✅ TEST PASSED...! : Test Case ID - 113 \033[0m") # login failed so test passed

        # print("Response:", response_invalidlogin.json())
        # print(f"\033[92m✅ TEST PASSED...!\033[0m") # login failed so test passed

  
if c!=0 and c<=1:
    failed_count+=1










# 4 : Login with empty field in payload  : 


# print("\033[1;34m Login with empty field in payload\033[0m")

empty_login_payload = {
        "loginId":" ",
        "password":" "
}


response_login = requests.post(login_url,json=empty_login_payload)
if response_login.status_code == 200:
    response_json = response_login.json()
    name=response_json.get('name')
    failed_count+=1

    # print(f"\033[91m✅ Login successful! Welcome, {loginId} | Name: {name} | Status: {response_login.status_code}\033[0m",{"loginId":loginId,"password":pwd})
    # print("Response JSON : ",json.dumps(response_json,indent=4))
    token1= response_json.get('token',{}).get('token')
    # print(f"\033[91m❌  Login successful for: {loginid} | Name: {name} | Status: {response_login.status_code}\033[0m")
    print(f"\033[91m❌ TEST FAILED...! : Test Case ID - 114 : Error -  Fields cannot be empty \033[0m") # login success so test failed becoz in oms logged with oms in other 3 credentials kds,go,testoms

    # print(f"Token (Login): {token1}") 

else:
    # print(f"\033[92m✅ Login failed with status code {response_login.status_code}\033[0m",{"loginId":loginid,"password":pwd})
    print(f"\033[92m✅ TEST PASSED...! : Test Case ID - 114 \033[0m") # login failed so test passed

    # print("Response:", response_login.json())
    # print(f"\033[92m✅ TEST PASSED...!\033[0m") # login failed so test passed











# 5 : SQL Injection Attempt : 


# print("\033[1;34m SQL Injection Attempt\033[0m")

sql_injection_payload = {
            "loginId": "' OR 1=1 --",
            "password": "anypassword"
}
response_login = requests.post(login_url,json=sql_injection_payload)
if response_login.status_code != 200:
    print("\033[1;92m✅ TEST PASSED...! : Test Case ID - 115 \033[0m")
    # print("Response:", response_login.json())
else:
    failed_count+=1
    # print("TEST PASSED : Test for SQL injection protection failed! SQL injection might be possible.014")
    print(f"\033[91m❌ TEST FAILED...! : Test Case ID - 115 : Error - SQL injection detected \033[0m") # login failed so test passed



# print(" "*200) # for space 






# 6 : No SQL Injection Attempt : 

# print("\033[1;34m No SQL Injection Attempt! \033[0m")

no_sql_injection= {
  "username": "oms' || 1==1 //",
  "password": "anything"
}
response_no_sql_injection = requests.post(login_url,json=no_sql_injection)
if response_no_sql_injection.status_code != 200:
    no_sql_injection_json = response_no_sql_injection.json()
    # print("...",response_no_sql_injection.text)
    # print("Response JSON : ",json.dumps(response_no_sql_injection_json,indent=4))
    no_sql_injection_token= no_sql_injection_json.get('token',{}).get('token')
    print(f"\033[92m✅ TEST PASSED...! : Test Case ID - 116 \033[0m") 
else:

    failed_count+=1
    # print(f"\033[91m❌ Login failed with status code {response_no_sql_injection.text}\033[0m")
    print(f"\033[91m❌ TEST FAILED...! : Test Case ID : 116  :  Error - Suspicious input detected \033[0m") # login failed so test passed
    # print("Test for special characters in username failed! Login succeeded with special characters.")








# 7 : Login with null field in payload : 


# print("\033[1;34m Login with null field in payload\033[0m")

null_login_payload = {
        "loginId":None,
        "password": None
}


response_login = requests.post(login_url,json=null_login_payload)
if response_login.status_code == 200:
    response_json = response_login.json()
    name=response_json.get('name')
    # print(f"\033[91m✅ Login successful! Welcome, {loginId} | Name: {name} | Status: {response_login.status_code}\033[0m",{"loginId":loginId,"password":pwd})
    # print("Response JSON : ",json.dumps(response_json,indent=4))
    token1= response_json.get('token',{}).get('token')
    failed_count+=1
    # print(f"\033[91m❌  Login successful for: {loginid} | Name: {name} | Status: {response_login.status_code}\033[0m")
    print(f"\033[91m❌ TEST FAILED...! : Test Case ID - 117 : Error -  Username and Password fields are required\033[0m") # login success so test failed becoz in oms logged with oms in other 3 credentials kds,go,testoms

    # print(f"Token (Login): {token1}") 

else:
    # print(f"\033[92m✅ Login failed with status code {response_login.status_code}\033[0m",{"loginId":loginid,"password":pwd})
    print(f"\033[92m✅ TEST PASSED...! : Test Case ID - 117 \033[0m") # login failed so test passed
    # print("Response:", response_login.json())
    # print(f"\033[92m✅ TEST PASSED...!\033[0m") # login failed so test passed






# 8 :  Login Test with invalid HTTP method : 

# print("\033[1;34mLOGIN TESTCASE - Invalid  HTTP method\033[0m")

response_invalid_method = requests.put(login_url,json=login_payload)
if response_invalid_method.status_code != 200:
    # print("\033[1;92mTest for invalid HTTP method passed!\033[0m",response_invalid_method.status_code)
    print("\033[1;92m✅ TEST PASSED...! : Test Case ID - 118 \033[0m")
else:
    failed_count+=1
    print("\033[1;91m❌ TEST FAILED...! : Test Case ID -  118  : Error - API should only allow POST for login \033[0m")





# 9 : XML Injection Attempt : 

# print("\033[1;34m XML Injection Attempt \033[0m")


xml_injection_payload = {
    "loginId": "<script>alert(1)</script>",
    "password": "anypassword"
}
response_xml_injection = requests.post(login_url,json=xml_injection_payload)
if response_xml_injection.status_code != 200:
    # print("\033[1;92m ✅ TEST PASSED : Test for XML/XSS injection protection passed..!  - Test Case ID : 015 \033[0m")
    print("\033[1;92m✅ TEST PASSED...! : Test Case ID - 119 \033[0m")

    # print("Response:", response_xml_injection.json())
else:
    failed_count+=1
    # print("\033[91m❌ TEST FAILED...! Test for XML/XSS injection protection failed! XML/XSS injection might be possible.  - Test Case ID : 015 \033[0m")
    print("\033[91m❌ TEST FAILED...! : Test Case ID - 119 : Error - XML injection detected \033[0m")
#     print(f") # login failed so test passed






# 9 : Database down during login 

print("\033[1;93mTest Case ID -  120 :  Skipping DB Availability....\033[0m")






# 10 : Login when Redis is Down
        
print("\033[1;93mTest Case ID -  121 : Skipping Cache...\033[0m")










print(f"\033[1;34mTotal TEST FAILEDS  : {failed_count}/{total_count}\033[0m")

if failed_count == 0:
    print("\033[92m ✅ All TEST PASSED \033[0m")





time.sleep(0.1)
print("\n")