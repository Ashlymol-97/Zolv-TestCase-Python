# import requests

# print("\033[1;34mRate limiting (multiple attempts in quick succession) Test\033[0m")

# login_url="https://qa-oms.zolv.health/api/v1/user/login"

# # Headers: required for JSON payload
# headers = {
#     "Content-Type": "application/json"
# }

# # Payload with correct field names
# invalid_login_payload = {
#     "loginId": "AutotestOMS",   # ✅ Use "loginId" only if this is accepted by the API (otherwise use "username")
#     "password": "Smm@1234"
# }

# print("\033[1;34mRate limiting (multiple attempts in quick succession) Test\033[0m\n")
# print("Testing rate limiting protection...")

# # Loop for repeated login attempts
# for i in range(20):
#     response = requests.post(login_url, json=invalid_login_payload)
#     print(f"Attempt {i + 1} status code: {response.status_code}")
#     print(response.text)

#     if response.status_code == 429:
#         print("\033[1;92m✅ Rate limiting correctly implemented!\033[0m",response.status_code)
#         break
#     elif response.status_code == 200:
#         print("\033[1;91m❌ Unexpected success — wrong credentials accepted.\033[0m")
#         break
#     elif response.status_code == 400:
#         print("\033[1;91m❌ Request format is invalid (400 Bad Request). Fix payload.\033[0m")
#         break
#     elif response.status_code >= 500:
#         print("\033[1;91m❌ Server error — something is wrong on the backend.\033[0m")
#         break



# import requests
# import time
# import json
# import random
# import urllib.parse

# import base64
   

    
# login_url= "https://qa-oms.zolv.health/api/v1/user/oms-login"
# logout_url="https://qa-oms.zolv.health/api/v1/user/logout"




# # 1 : Login TestCase : Login with valid Login Credentials

# # print("\033[1;34m LOGIN TESTCASE! Document ID: TP_001\033[0m")
# # print("\033[1;34m Login with valid Login Credentials! Document ID: TP_001\033[0m")


# # login_payload = {
# #         "loginId":"AutotestOMS",
# #         "password":"Smm@1234"
# # }

  
# # response_login = requests.post(login_url,json=login_payload)
# # if response_login.status_code == 200:
# #     response_json = response_login.json()
# #     name=response_json.get('name')
# #     # print(f"\033[91m✅ Login successful! Welcome, {loginId} | Name: {name} | Status: {response_login.status_code}\033[0m",{"loginId":loginId,"password":pwd})
# #     # print("Response JSON : ",json.dumps(response_json,indent=4))
# #     token1= response_json.get('token',{}).get('token')
# #     # print(f"\033[92m✅  Login successful for: {loginid} | Name: {name} | Status: {response_login.status_code}\033[0m")
# #     print(f"\033[92m✅  TEST PASSED...!: Test Case ID - 001 \033[0m") # login success so test failed becoz in oms logged with oms in other 3 credentials kds,go,testoms

# #     # print(f"Token (Login): {token1}") 

# # else:
# #     # print(f"\033[91m❌ Login failed with status code {response_login.status_code}\033[0m",{"loginId":loginid,"password":pwd})
# #     print(f"\033[91m❌ TEST FAILED...! - Test Case ID : 001 \033[0m") # login failed so test passed

# #     print("Response:", response_login.json())
# #     # print(f"\033[92m✅ TEST PASSED...!\033[0m") # login failed so test passed



# # print(" "*200) # for space 






# # 2 :  Login with invalid credentials :

# # print("\033[1;34m Login with Invalid Login Credentials! \033[0m")


   
# # Invalid_login_payload = {
# #         "login_id":"TestOMS",
# #         "password":"Smm@1234"
# # }

# # response_invalidlogin = requests.post(login_url,json=Invalid_login_payload)
# # if response_invalidlogin.status_code == 200:
# #     invalid_json = response_invalidlogin.json()
# #     name=invalid_json.get('name')
# #     # print(f"\033[91m✅ Login successful! Welcome, {loginId} | Name: {name} | Status: {response_login.status_code}\033[0m",{"loginId":loginId,"password":pwd})
# #     # print("Response JSON : ",json.dumps(response_json,indent=4))
# #     token1= invalid_json.get('token',{}).get('token')
# #     # print(f"\033[91m❌  Login successful for: {loginid} | Name: {name} | Status: {response_login.status_code}\033[0m")
# #     print(f"\033[91m❌TEST FAILED...!: Test Case ID - 002 \033[0m") # login success so test failed becoz in oms logged with oms in other 3 credentials kds,go,testoms

# #     # print(f"Token (Login): {token1}") 

# # else:
# #     # print(f"\033[92m✅  Login failed with status code {response_login.status_code}\033[0m",{"loginId":loginid,"password":pwd})
# #     print(f"\033[92m✅  TEST PASSED...! - Test Case ID : 002 \033[0m",response_invalidlogin.status_code) # login failed so test passed

# #     # print("Response:", response_invalidlogin.json())
# #     # print(f"\033[92m✅ TEST PASSED...!\033[0m") # login failed so test passed



# # print(" "*200) # for space 






# # 3 : Login with missing Login ID :

# # print("\033[1;34m Login with missing Login ID\033[0m")

# # Missing_login_payload = {
# #         "loginId":None,
# #         "password":"Smm@1234"
# # }


# # response_login = requests.post(login_url,json=Missing_login_payload)
# # if response_login.status_code == 200:
# #     response_json = response_login.json()
# #     name=response_json.get('name')
# #     # print(f"\033[91m✅ Login successful! Welcome, {loginId} | Name: {name} | Status: {response_login.status_code}\033[0m",{"loginId":loginId,"password":pwd})
# #     # print("Response JSON : ",json.dumps(response_json,indent=4))
# #     token1= response_json.get('token',{}).get('token')
# #     # print(f"\033[91m❌  Login successful for: {loginid} | Name: {name} | Status: {response_login.status_code}\033[0m")
# #     print(f"\033[91m❌ TEST FAILED...!: Test Case ID - 003 \033[0m",response_login.status_code) # login success so test failed becoz in oms logged with oms in other 3 credentials kds,go,testoms

# #     # print(f"Token (Login): {token1}") 

# # else:
# #     # print(f"\033[92m✅ Login failed with status code {response_login.status_code}\033[0m",{"loginId":loginid,"password":pwd})
# #     print(f"\033[92m✅ TEST PASSED...! - Test Case ID : 003 \033[0m",response_login.status_code) # login failed so test passed

# #     # print("Response:", response_login.json())
# #     # print(f"\033[92m✅ TEST PASSED...!\033[0m") # login failed so test passed



# # print(" "*200) # for space 



 
# # 4 : Login with missing password :


# # print("\033[1;34m Login with missing password\033[0m")

# # Missingpwd_login_payload = {
# #         "loginId":"AutotestOMS",
# #         "password":None
# # }


# # response_login = requests.post(login_url,json=Missingpwd_login_payload)
# # if response_login.status_code == 200:
# #     response_json = response_login.json()
# #     name=response_json.get('name')
# #     # print(f"\033[91m✅ Login successful! Welcome, {loginId} | Name: {name} | Status: {response_login.status_code}\033[0m",{"loginId":loginId,"password":pwd})
# #     # print("Response JSON : ",json.dumps(response_json,indent=4))
# #     token1= response_json.get('token',{}).get('token')
# #     # print(f"\033[91m❌  Login successful for: {loginid} | Name: {name} | Status: {response_login.status_code}\033[0m")
# #     print(f"\033[91m❌ TEST FAILED...!: Test Case ID - 004 \033[0m",response_login.status_code) # login success so test failed becoz in oms logged with oms in other 3 credentials kds,go,testoms

# #     # print(f"Token (Login): {token1}") 

# # else:
# #     # print(f"\033[92m✅ Login failed with status code {response_login.status_code}\033[0m",{"loginId":loginid,"password":pwd})
# #     print(f"\033[92m✅ TEST PASSED...! - Test Case ID : 004 \033[0m",response_login.status_code) # login failed so test passed

# #     # print("Response:", response_login.json())
# #     # print(f"\033[92m✅ TEST PASSED...!\033[0m") # login failed so test passed



# # print(" "*200) # for space 







# # 5 : Un Authorized User (Privilege) :


# # # print("\033[1;34m Un Authorized User (Privilege)![0m")
# # # print("\033[1;34m  Document ID: TP_001 \033\033[0m")
# # print(" "*200) # for space 


# # Unauthorized_payload = [
# #     {"loginId": "AutotestKDS", "password": "Smm@1234"},
# #     {"loginId": "AutotestZolvGo", "password": "Smm@1234"},
# #     {"loginId": "TestOMS", "password": "Smm@1234"},
# #     {"loginId": "user@example.com","password": "userpassword","userType": ""}, 
# #     {"loginId": "Testdeleteuser","password": "Testdeleteuser@1234"}
# # ]
# # for user in Unauthorized_payload:
# #     login_Auth = requests.post(login_url,json=user)
# #     # print(Unauthorized_payload,login_Auth)
# #     if login_Auth.status_code == 200:
# #         print("\033[91m❌  TEST FAILED..: Test Case ID - 005 \033[0m",login_Auth.status_code)
# #     else:
# #         print("\033[92m✅TEST PASSED..: Test Case ID - 005 \033[0m",login_Auth.status_code)

#     # time.sleep(0.1)  # Small delay between requests





# # 6 : Login with null field in payload : 


# # print("\033[1;34m Login with null field in payload\033[0m")

# # null_login_payload = {
# #         "loginId":None,
# #         "password": None
# # }


# # response_login = requests.post(login_url,json=null_login_payload)
# # if response_login.status_code == 200:
# #     response_json = response_login.json()
# #     name=response_json.get('name')
# #     # print(f"\033[91m✅ Login successful! Welcome, {loginId} | Name: {name} | Status: {response_login.status_code}\033[0m",{"loginId":loginId,"password":pwd})
# #     # print("Response JSON : ",json.dumps(response_json,indent=4))
# #     token1= response_json.get('token',{}).get('token')
# #     # print(f"\033[91m❌  Login successful for: {loginid} | Name: {name} | Status: {response_login.status_code}\033[0m")
# #     print(f"\033[91m❌ TEST FAILED...!: Test Case ID - 006 \033[0m",response_login.status_code) # login success so test failed becoz in oms logged with oms in other 3 credentials kds,go,testoms

# #     # print(f"Token (Login): {token1}") 

# # else:
# #     # print(f"\033[92m✅ Login failed with status code {response_login.status_code}\033[0m",{"loginId":loginid,"password":pwd})
# #     print(f"\033[92m✅ TEST PASSED...! - Test Case ID : 006 \033[0m",response_login.status_code) # login failed so test passed
# #     # print("Response:", response_login.json())
# #     # print(f"\033[92m✅ TEST PASSED...!\033[0m") # login failed so test passed



# # print(" "*200) # for space 







# # 7 : Concurrent Login Attempts : doubt

# # Test login rate limiting (multiple attempts in quick succession) : 
# headers = {
#     "Content-Type": "application/json"
# }

# # Payload with correct field names
# invalid_login_payload = {
#     "loginId": "AutotestOMS",   # ✅ Use "loginId" only if this is accepted by the API (otherwise use "username")
#     "password": "Smm@1234"
# }

# print("\033[1;34mRate limiting (multiple attempts in quick succession) Test\033[0m\n")
# print("Testing rate limiting protection...")

# # Loop for repeated login attempts
# for i in range(20):
#     response = requests.post(login_url, json=invalid_login_payload, headers=headers)
#     print(f"Attempt {i + 1} status code: {response.status_code}")
#     print(response.text)
#     print(response.status_code)

#     if response.status_code == 429:
#         print("\033[1;92m✅ Rate limiting correctly implemented!\033[0m")
#         break
#     elif response.status_code == 200:
#         print("\033[1;91m❌ Unexpected success — wrong credentials accepted.\033[0m")
#         break
#     elif response.status_code == 400:
#         print("\033[1;91m❌ Request format is invalid (400 Bad Request). Fix payload.\033[0m")
#         break
#     elif response.status_code >= 500:
#         print("\033[1;91m❌ Server error — something is wrong on the backend.\033[0m")
#         break




# # 8 : Login with Inactive User  :

# # print("\033[1;34mLogin with Inactive User\033[0m")



# # # 🔐 Target user credentials
# # username_input = "TestOMS"
# # password_input = "Smm@1234"

# # # 🔒 Stored correct credentials (mocked for comparison)
# # stored_username = "TestOMS"
# # stored_password = "Smm@1234"

# # # 🔑 Admin credentials and login URL
# # admin_url = "https://qa-admin.zolv.health/api/v1/user/login"

# # # 🔐 Admin login
# # admin_login = requests.post(admin_url, json={"loginId": "AutotestAdmin", "password": "Smm@1234"})

# # if admin_login.status_code == 200:
# #     admin_json = admin_login.json()
# #     admin_token = admin_json['token']['token']
# #     name = admin_json['name']
# #     company_id = admin_json['company']['id']

# #     # print("\033[92m✅ Admin login successful:\033[0m", name, company_id)

# #     # 📋 Get user list
# #     user_url = f"https://qa-admin.zolv.health/api/v1/masters/user/web/{company_id}/get-user-list"
# #     user_headers = {"Authorization": f"Bearer {admin_token}"}

# #     user_response = requests.get(user_url, headers=user_headers)

# #     if user_response.status_code == 200:
# #         user_list = user_response.json().get('users', [])
# #         # print("🔎 Sample user object:", user_list[0])  # For debugging structure

# #         user_found = False

# #         for user in user_list:
# #             if user["loginId"] == username_input:
# #                 user_found = True
# #                 is_active = user["isActive"]

# #                 if is_active:
# #                     # print(f"\033[92m✅ User {username_input} is active. Attempting login...\033[0m")

# #                     # Try to log in as the user
# #                     user_login = requests.post(login_url, json={"loginId": username_input, "password": password_input})

# #                     if user_login.status_code == 200:
# #                         # print(f"\033[92m✅ Login successful for active user: {username_input}\033[0m")
# #                        print(f"\033[92m✅ Test Passed: - Test Case ID : 008\033[0m")

# #                     else:
# #                         print(f"\033[91m❌ Test Failed:- Test Case ID : 008\033[0m")
# #                         # print(f"\033[91m❌ Login failed for active user: {username_input} (unexpected)\033[0m",user_login.text)
# #                         user_login.status_code


# #                 else:
# #                     print(f"\033[93m⚠️ User {username_input} is inactive. Attempting login to verify block...\033[0m")

# #                     # Attempt login for inactive user (should fail)
# #                     user_login = requests.post(login_url, json={"loginId": username_input, "password": password_input})

# #                     if user_login.status_code != 200:
# #                         # print(f"\033[92m✅ Test Passed: Inactive user {username_input} was blocked from login.\033[0m") 
# #                         print(f"\033[92m✅ Test Passed: - Test Case ID : 008\033[0m")

# #                     else:
# #                         # print(f"\033[91m❌ Test Failed: Inactive user {username_input} was able to login!\033[0m")
# #                         print(f"\033[91m❌ Test Failed:- Test Case ID : 008\033[0m")

# #         if not user_found:
# #             print(f"\033[91m❌ User {username_input} not found in user list\033[0m")

# #     else:
# #         print("\033[91m❌ Failed to fetch user list.\033[0m", user_response.status_code)

# # else:
# #     print("\033[91m❌ Admin login failed.\033[0m", admin_login.status_code)








# # 9 :  Login with Deleted User Credentials : 



# # # print("\033[1;34m LOGIN DELETED USER TESTCASE!\033[0m")


# # admin_url = "https://qa-admin.zolv.health/api/v1/user/login"
# # admin_logout = "https://qa-admin.zolv.health/api/v1/user/logout"


# # login_id = "TestDelete"
# # password= "TestDelete@1234"

# # # ----------------------
# # # Login as test user
# # # ----------------------
# # user1 = requests.post(login_url, json={"loginId":login_id, "password":password})

# # if user1.status_code == 200:
# #     user1_json = user1.json()
# #     name_user1 = user1_json['name']
# #     company_id = user1_json['company']['id']
# #     token1 = user1_json['token']['token']
# #     user_id = user1_json['id']

# #     # print("\033[92m✅ User login successful\033[0m")
# #     # print("Company ID:", company_id)
# #     # print("Response JSON:")
# #     # print(json.dumps(user1_json, indent=4))

# #     # Step 2: Logout test user
# #     headers = {"Authorization": f"Bearer {token1}"}
# #     logout_response = requests.put(logout_url, headers=headers)
# #     if logout_response.status_code == 200:
# #         print("\033[92m✅ Test user logout successful\033[0m")
# #     else:
# #         print("\033[91m❌ Test user logout failed with status code:\033[0m", logout_response.status_code)
# #         # print(logout_response.text)

# # else:
# #     print("\033[92m✅ TEST PASSED : Test user login failed with status code: Test Case ID - 009 \033[0m", user1.status_code)
# #     # print(user1.text)
# #     exit()

# # # ----------------------
# # # Step 3: Admin login
# # # ----------------------
# # admin_login = requests.post(admin_url, json={"loginId": "AutotestAdmin", "password": "Smm@1234"})
# # if admin_login.status_code == 200:
# #     admin_json = admin_login.json()
# #     admin_token = admin_json['token']['token']
# #     name = admin_json['name']

# #     # print("\033[92m✅ Admin login successful:\033[0m", name)

# #     # Step 4: Delete the user
# #     delete_url = "https://qa-admin.zolv.health/api/v1/masters/user/web/{company_id}/delete-user/{user_id}"

# #     delete_urls = delete_url.format(company_id=company_id, user_id=user_id)
# #     headers = {"Authorization": f"Bearer {admin_token}"}
# #     delete_response = requests.patch(delete_urls, headers=headers)

# #     if delete_response.status_code == 200:
# #         # print("\033[92m✅ Test user deleted successfully\033[0m")

# #         # Step 5: Logout admin
# #         logout_admin_response = requests.put(admin_logout, headers=headers)
# #         if logout_admin_response.status_code == 200:
# #            logout_res=logout_admin_response.json()
# #             # print("\033[92m✅ Admin logout successful\033[0m")
# #         else:
# #             # print("\033[91m❌ Admin logout failed with status code:\033[0m", logout_admin_response.status_code)
# #             # print(logout_admin_response.text)
# #             msg=logout_admin_response.text


# #         # Step 6: Try to log in as deleted user
# #         deleted_login = requests.post(login_url, json={"loginId": login_id, "password": password})
# #         if deleted_login.status_code == 401:
# #             print("\033[92m✅ TEST PASSED :  Deleted user login correctly blocked (401 Unauthorized) : Test Case ID - 009\033[0m")
# #         else:
# #             print("\033[91m❌ TEST FAILED : Unexpected login status for deleted user: Test Case ID - 009 \033[0m", deleted_login.status_code)
# #             # print(deleted_login.text)

# #     else:
# #         print("\033[91m❌ Failed to delete test user. Status:\033[0m", delete_response.status_code)
# #         # print(delete_response.text)

# # else:
# #     print("\033[91m❌ Admin login failed with status code:\033[0m", admin_login.status_code)
# #     # print(admin_login.text)














# # 11 :   Invalid API endpoint (intentionally wrong) : 

# # print("\033[1;34mLOGIN TESTCASE - Invalid Endpoint, Minimal Payload\033[0m")

# # invalidlogin_url = "https://qa-admin.zolv.health/api/v1/user/invalid_login"  # Example: endpoint is incorrect



# #     # Send POST request to invalid endpoint

# # response = requests.post(invalidlogin_url, json=login_payload)

# # # Check if response is successful or has a response code
# # if response.status_code:
# #     # print(f"Status Code: {response.status_code}")

# #     # Check if response content-type is JSON
# #     content_type = response.headers.get('Content-Type', '')
# #     if 'application/json' in content_type:
# #         print("Response JSON:")
# #         # print(json.dumps(response.json(), indent=4))
# #         print("\033[91m❌ TEST FAILED : Received JSON response : Test Case ID - 011\033[0m")
# #     else:
# #         print("\033[92m✅ TEST PASSED :  Response is not valid JSON : Test Case ID - 011\033[0m")
# #         # print(response.text)
# # else:
# #     print("\033[91m❗ Request failed, no valid status code received. : Test Case ID - 011\033[0m")







# # 12 : Invalid Parameters :

# # print("\033[1;34mLOGIN TESTCASE - Invalid Parameters\033[0m")


# # Invalidparams_login_payload = [
# #     {"loginId": "abcd@123", "password": "asdasdasd"}, # Small delay between requests
# #     {"loginId": "12345", "password": ""},
# #     {"loginId": "12345", "password": "6543"},
# #     {"loginId": "asdf@#$12", "password": 12344}, 
# #     {"loginId": "", "password": "Smm@1234"},
# #     {"loginId": True, "password": False},                                              #Boolean Value Attempts
# #     {"loginId": "用户名😊", "password": "密码🔒"},                                     #Emoji value Attempts
# #     {"loginId": "12345", "password": ""},
# #     {"loginId": { "$ne": None },"password": { "$ne": None }},                           #NoSQL injection Attempts 
# #     {"loginId": "' OR '1'='1", "password": "anything"},                                 #SQL Injection Attempt
# #     {"loginId": "<![CDATA[admin]]>","password": "<![CDATA[password]]>"},                #XML Injection Attempt 

# #     {"loginId": "' OR '1'='1", "password": "test123"},                                  #    #// Malicious query parameter
# #     {"loginId": "<script>alert('XSS')</script>", "password": "test123"},
# #     {"loginId": "'; DROP TABLE users; --", "password": "test123"},
# #     {"loginId": "../../../../etc/passwd", "password": "test123"},
# #     {"loginId": "\" OR \"\" = \"", "password": "test123"},
# #     {"loginId": "reboot", "password": "test123"},
# #     {"loginId": "${7*7}", "password": "test123"},
# #     {"loginId": "%3Cscript%3Ealert('XSS')%3C/script%3E", "password": "test123"},
# # ]


# # for invalid in Invalidparams_login_payload:

# #     response_invalidlogin = requests.post(login_url,json=Invalidparams_login_payload)
# #     if response_invalidlogin.status_code == 200:
# #         invalid_json = response_invalidlogin.json()
# #         name=invalid_json.get('name')
# #         # print(f"\033[91m❌ Login successful! Welcome, {loginId} | Name: {name} | Status: {response_login.status_code}\033[0m",{"loginId":loginId,"password":pwd})
# #         # print("Response JSON : ",json.dumps(response_json,indent=4))
# #         token1= invalid_json.get('token',{}).get('token')
# #         # print(f"\033[91m❌  Login successful for: {loginid} | Name: {name} | Status: {response_login.status_code}\033[0m")
# #         print(f"\033[91m❌TEST FAILED...!: Test Case ID - 012 \033[0m") # login success so test failed becoz in oms logged with oms in other 3 credentials kds,go,testoms

# #         # print(f"Token (Login): {token1}") 

# #     else:
# #         # print(f"\033[92m✅  Login failed with status code {response_login.status_code}\033[0m",{"loginId":loginid,"password":pwd})
# #         print(f"\033[92m✅  TEST PASSED...! - Test Case ID : 012 \033[0m",response_invalidlogin.status_code) # login failed so test passed

# #         # print("Response:", response_invalidlogin.json())
# #         # print(f"\033[92m✅ TEST PASSED...!\033[0m") # login failed so test passed



# # print(" "*200) # for space 





# # 13 : Login with empty field in payload  : 


# # print("\033[1;34m Login with empty field in payload\033[0m")

# # empty_login_payload = {
# #         "loginId":" ",
# #         "password":" "
# # }


# # response_login = requests.post(login_url,json=empty_login_payload)
# # if response_login.status_code == 200:
# #     response_json = response_login.json()
# #     name=response_json.get('name')
# #     # print(f"\033[91m✅ Login successful! Welcome, {loginId} | Name: {name} | Status: {response_login.status_code}\033[0m",{"loginId":loginId,"password":pwd})
# #     # print("Response JSON : ",json.dumps(response_json,indent=4))
# #     token1= response_json.get('token',{}).get('token')
# #     # print(f"\033[91m❌  Login successful for: {loginid} | Name: {name} | Status: {response_login.status_code}\033[0m")
# #     print(f"\033[91m❌ TEST FAILED...!: Test Case ID - 013 \033[0m",response_login.status_code) # login success so test failed becoz in oms logged with oms in other 3 credentials kds,go,testoms

# #     # print(f"Token (Login): {token1}") 

# # else:
# #     # print(f"\033[92m✅ Login failed with status code {response_login.status_code}\033[0m",{"loginId":loginid,"password":pwd})
# #     print(f"\033[92m✅ TEST PASSED...! - Test Case ID : 013 \033[0m",response_login.status_code) # login failed so test passed

# #     # print("Response:", response_login.json())
# #     # print(f"\033[92m✅ TEST PASSED...!\033[0m") # login failed so test passed



# # print(" "*200) # for space 







# # 14 : SQL Injection Attempt : 


# # print("\033[1;34m SQL Injection Attempt\033[0m")

# # sql_injection_payload = {
# #             "loginId": "' OR 1=1 --",
# #             "password": "anypassword"
# # }
# # response_login = requests.post(login_url,json=sql_injection_payload)
# # if response_login.status_code != 200:
# #     print("\033[1;92m✅ TEST PASSED...! : Test for SQL injection protection passed! - Test Case ID : 014 \033[0m")
# #     # print("Response:", response_login.json())
# # else:
# #     print("TEST PASSED : Test for SQL injection protection failed! SQL injection might be possible.014")
# #     print(f"\033[91m❌ TEST FAILED...! - Test Case ID : 014 \033[0m") # login failed so test passed



# # print(" "*200) # for space 





# # 15 : XML Injection Attempt : 

# # print("\033[1;34m XML Injection Attempt \033[0m")


# # xml_injection_payload = {
# #     "loginId": "<script>alert(1)</script>",
# #     "password": "anypassword"
# # }
# # response_xml_injection = requests.post(login_url,json=xml_injection_payload)
# # if response_xml_injection.status_code != 200:
#     # print("\033[1;92m ✅ TEST PASSED : Test for XML/XSS injection protection passed..!  - Test Case ID : 015 \033[0m")
# #     print("\033[1;92m ✅ TEST PASSED : - Test Case ID : 015 \033[0m")

# #     # print("Response:", response_xml_injection.json())
# # else:
# #     print("\033[91m❌ TEST FAILED...! Test for XML/XSS injection protection failed! XML/XSS injection might be possible.  - Test Case ID : 015 \033[0m")
# #     print("\033[91m❌ TEST FAILED...!- Test Case ID : 015 \033[0m")
# # #     print(f") # login failed so test passed



# # print(" "*200) # for space 





# # # 16 : Login with additional field in payload : 

# # print("\033[1;34m Login with additional field in payload \033[0m")

# # extrafield_payload ={
# #     "loginId": "AutotestOMS",
# #     "password": "Smm@1234", 
# #     "extraField": "unexpected"
# # }
# # response_login = requests.post(login_url,json=extrafield_payload)
# # if response_login.status_code == 200:
# #     token = response_login.json()["token"]["token"]
# #     # print(token,"...")
# #     response_json = response_login.json()
# #     # print("Response JSON : ",json.dumps(response_json,indent=4))
# #     # print("\033[1;91m❌  Login successful with extra field.! - Test Case ID : 016 \033[0m")
# #     print(f"\033[91m❌ TEST FAILED...! :- Test Case ID : 016 \033[0m",response_login.status_code) # login failed so test passed

# # else:
# #     # print(f"\033[92m✅ Login failed due to extra field — API enforces strict schema. \033[0m",response_login.status_code) # login failed so test passed
# #     print("\033[1;92m✅ TEST PASSED...! :  - Test Case ID : 016 \033[0m")
# #     print("Response:", response_login.json())




# # print(" "*200) # for space 


# #  17 : Login with extremely long payload :

# # print("\033[1;34m Login with extremely long payload \033[0m")

# # long_payload ={
# #     "loginId":"AutotestOMS" + "a" * 1000, 
# #     "password":"smm@1234" + "b" * 10000
# # }                                  #extremely long inputs (potential buffer overflow)
# # response_login = requests.post(login_url,json=long_payload)
# # if response_login.status_code != 200:
# #     # print("\033[1;92m✅ API couldn't handle long payload.! \033[0m",response_login.status_code)
# #     print("\033[1;92m✅ TEST PASSED...! : - Test Case ID : 017 \033[0m")

# #     # print("Response:", response_login.json())
# # else:
# #     # print(f"\033[91m❌ Login succeeded with long credentials. \033[0m",response_login.status_code) # login failed so test passed
# #     print(f"\033[91m❌ TEST FAILED...! :- Test Case ID : 017 \033[0m") # login failed so test passed






# # print(" "*200) # for space 


# # 18 :  Login Test with invalid HTTP method : 

# # print("\033[1;34mLOGIN TESTCASE - Invalid Endpoint, Minimal Payload\033[0m")

# # response_invalid_method = requests.put(login_url,json=login_payload)
# # if response_invalid_method.status_code != 200:
# #     # print("\033[1;92mTest for invalid HTTP method passed!\033[0m")
# #     print("\033[1;92mTEST PASSED : Test Case ID - 018 \033[0m", response_invalid_method.status_code)
# # else:
# #     print("\033[1;91m TEST FAILED : Test for invalid HTTP method failed! Server accepted PUT for POST endpoint.: Test Case ID -  018 \033[0m")















# # print(" "*200) # for space 



# #20 : Login from Device B using same credentials while Device A login is active (multiple device Login behaviour) :


# # print("\n")


# # print("\033[1;34m System must allow simultaneous logins from multiple devices using same credentials! \033[0m")

# # login_url= "https://qa-oms.zolv.health/api/v1/user/oms-login"

# # login = {
# #     "loginId": "AutotestOMS",
# #     "password": "Smm@1234"
# # }

# # # Step 1: Login from Device A
# # # print("🔐 Logging in from Device A...")
# # response_a = requests.post(login_url, json=login)

# # if response_a.status_code == 200:
# #     response_json = response_a.json()
# #     token_a = response_json["token"]["token"]
# #     company_id = response_json["company"]["id"]
# #     rest_id = response_json["restaurant"]["id"]
# #     # print("\033[92m✅ Device A Login Successful.!\033[0m", response_a.status_code)
# #     # print("Token A:", token_a)
# # else:
# #     # print("\033[91m❌ Device A Login Failed.\033[0m")
# #     exit()

# # # Step 2: Login from Device B using same credentials
# # # print("\n🔐 Logging in from Device B (same credentials)...")
# # response_b = requests.post(login_url, json=login)

# # if response_b.status_code == 200:
# #     token_b = response_b.json()["token"]["token"]
# #     print("\033[92m✅ Device B Login Successful.!\033[0m", response_b.status_code)
# #     # print("Token B:", token_b)
# # else:
# #     # print("\033[91m❌ Device B Login Failed — multiple login incorrectly blocked.\033[0m")
# #     exit()

# # # Step 3: Use Device A token to access protected endpoint
# # # print("\n🔄 Verifying Device A token is still valid...")
# # headers_a = {
# #     "Authorization": f"Bearer {token_a}",
# #     "Content-Type": "application/json"
# # }
# # url = f"https://qa-oms.zolv.health/api/v1/dashboard/orders/web/{company_id}/{rest_id}/get-order-progress"

# # response_check_a = requests.get(url, headers=headers_a)

# # if response_check_a.status_code == 200:
# #     print("\033[91m❌ Device A token is still valid after Device B login — simultaneous login allowed. : Test Case ID - 020 \033[0m")
# # else:
# #     print("\033[92m✅ Device A token was rejected after Device B login. : Test Case ID - 020 \033[0m")
# #     print("Status Code:", response_check_a.status_code)
# #     # print("Response:", response_check_a.text)




# # print(" "*200) # for space 



# # 24 : Simultaneously Login Attempts : Multiple login attempt with invalid/wrong password




# import time

# print("\033[1;34mMultiple login attempt with invalid/wrong password\033[0m")

# # Simulate repeated login attempts
# blocked = False
# MAX_FAILED_ATTEMPTS = 2
# failed_attempts = 0


# invalid_credentials = {
#     "loginId": "AutotestOMS",
#     "password": "wrongpa33555"
# }

# for attempt in range(10):
#     if blocked:
#         print(f"Attempt {attempt + 1}")
#         print("\033[91m🚫 Blocked: Too many failed attempts. - Test Case ID : 024\033[0m")
#         time.sleep(1)
#         continue

#     print(f"Attempt {attempt + 1}")
#     response = requests.post(login_url, json=invalid_credentials)
#     print("Status Code:", response.status_code)

#     if response.status_code == 200:
#         print("\033[92m✅ Login successful\033[0m  - Test Case ID : 024")
#         failed_attempts = 0  # Reset on success (not expected in this test)
#     else:
#         failed_attempts += 1
#         print("\033[91m❌ Invalid credentials\033[0m")

#         if failed_attempts > MAX_FAILED_ATTEMPTS:
#             blocked = True
#             print("\033[91m🚫 User is now blocked after 3 failed attempts. - Test Case ID : 024\033[0m")

#     time.sleep(1)  # simulate delay between attempts

# print(" " * 200)  # For spacing





# #21 : Login with user having only KDS privilege  : 

# # print("\033[1;34mLogin with user having only KDS privilege\033[0m")

# # kds_privilege_payload ={
# #     "loginId": "AutotestKDS",
# #     "password": "Smm@1234"
# # }

# # response_login = requests.post(login_url,json=kds_privilege_payload)
# # if response_login.status_code == 200:
# #     response_json = response_login.json()
# #     # print("Response JSON : ",json.dumps(response_json,indent=4))

# #     print("\033[91m❌  TEST FAILED..: Test Case ID - 021 \033[0m",response_login.status_code)
# # else:
# #     print("\033[92m✅TEST PASSED..: Test Case ID - 021 \033[0m",response_login.status_code)


# # print(" "*200) # for space 






# # 22 : Login with user having only Go privilege :

# # print("\033[1;34mLogin with user having only Go privilege\033[0m")

# # go_privilege_payload ={
# #     "loginId": "AutotestZolvGo", 
# #     "password": "Smm@1234"
# # }

# # response_login = requests.post(login_url,json=go_privilege_payload)
# # if response_login.status_code == 200:
# #     response_json = response_login.json()
# #     # print("Response JSON : ",json.dumps(response_json,indent=4))
# #     print("\033[91m❌  TEST FAILED..: Test Case ID - 022 \033[0m",response_login.status_code)
# # else:
# #     print("\033[92m✅TEST PASSED..: Test Case ID - 022 \033[0m",response_login.status_code)



# # # 11 :   Invalid API endpoint (intentionally wrong) : 

# # print("\033[1;34mLOGIN TESTCASE - Invalid Endpoint, Minimal Payload\033[0m")

# # invalidlogin_url = "https://qa-oms.zolv.health/api/v1/user/invalid_login"  # Example: endpoint is incorrect

# # login_payload = {
# #         "loginId":"AutotestOMS",
# #         "password":"Smm@1234"
# # }


# #     # Send POST request to invalid endpoint

# # response = requests.post(invalidlogin_url, json=login_payload)
# # # print(f"Status Code: {response.status_code}")

# # # Check if response is successful or has a response code
# # if response.status_code == 200:
# #     # print(response.text,"Login with Invalid API endpoint")
# #     print("\033[91m❌ TEST FAILED..! Test Case ID - 011\033[0m")
# # else:
# #     print("\033[92m✅ TEST PASSED..! Test Case ID - 011\033[0m")
# #     # print(response.text,"Invalid API endpoint")
# #     # print(response.status_code)





# # 24 : Simultaneously Login Attempts : Multiple login attempt with invalid/wrong password



# print("\033[1;34mMultiple login attempt with invalid/wrong password\033[0m")


# # Simulate repeated login attempts
# blocked = False


# invalid_attempts = {
#     "loginId": "AutotestOMS",
#     "password": "wrongpa33555"
# }
# for login_attempts in range(10):
#     print("Attempt", login_attempts + 1)
#     response=requests.post(login_url,invalid_attempts)
#     print(response.status_code)
#     if response.status_code == 200 : 
#         print("\033[92m✅ Login successful\033[0m  - Test Case ID : 024 ")
#     else :
#         if login_attempts >= 2:  # since attempts count starts from 0, block after 3 attempts      
#             blocked = True
#             print("\033[92m🚫 User is now blocked after 3 failed attempts. - Test Case ID : 024 \033[0m")

    
#     if blocked:
#         print("\033[92m🚫 Blocked: Too many failed attempts. - Test Case ID : 024 \033[0m")
#     else:
#         print("\033[92m✅ Login successful\033[0m  - Test Case ID : 024 ")
        
       
#     time.sleep(1)


# print(" "*200) # for space 




