# import requests
# import time
# import json
# import random
# import urllib.parse

# import base64
   

    
# login_url= "https://qa-admin.zolv.health/api/v1/user/login"
# logout_url="https://qa-admin.zolv.health/api/v1/user/logout"

# # Login TestCase : 

# login_payload = {
#         "loginId":"AutotestAdmin",
#         "password":"Smm@1234"
# }


# def Admin_login_test(login_url,login_payload):
#     # global token1
  
#     print("\033[1;34m LOGIN TESTCASE! Document ID: TP_001\033[0m")

#     response_login = requests.post(login_url,json=login_payload)
#     if response_login.status_code == 200:
#         response_json = response_login.json()
#         name=response_json.get('name')
#         # print(f"\033[91m✅ Login successful! Welcome, {loginId} | Name: {name} | Status: {response_login.status_code}\033[0m",{"loginId":loginId,"password":pwd})
#         print("Response JSON : ",json.dumps(response_json,indent=4))
#         token1= response_json.get('token',{}).get('token')
#         # print(f"\033[92m✅  Login successful for: {loginid} | Name: {name} | Status: {response_login.status_code}\033[0m")
#         print(f"\033[92m✅  TEST PASSED...!: Test Case ID - 001 \033[0m") # login success so test failed becoz in oms logged with oms in other 3 credentials kds,go,testoms

#         # print(f"Token (Login): {token1}") 
#         return response_json,token1  

#     else:
#         # print(f"\033[91m❌ Login failed with status code {response_login.status_code}\033[0m",{"loginId":loginid,"password":pwd})
#         print(f"\033[91m❌ TEST FAILED...! - Test Case ID : 001 \033[0m") # login failed so test passed

#         # print("Response:", response_login.json())
#         # print(f"\033[92m✅ TEST PASSED...!\033[0m") # login failed so test passed

# Admin_login_test(login_url,login_payload)








# #Login from Device B using same credentials while Device A login is active (multiple device Login behaviour) :


# # # print("\n")

# print("\033[1;34m System must not allow simultaneous logins from multiple devices using same credentialsT!\033[0m")


# login = {
#     "loginId": "AutotestAdmin",
#     "password": "Smm@1234"
# }
# # headers = {"Content-Type": "application/json"}

# # Step 2: Login from Device A
# print("🔐 Logging in from Device A...")
# response_a = requests.post("https://qa-oms.zolv.health/api/v1/user/oms-login", json=login)

# if response_a.status_code == 200:
#     response_json = response_a.json()
#     # print("Response JSON:", json.dumps(response_json, indent=4))

#     token_a = response_a.json()["token"]
#     company_id=response_json["company"]["id"]
#     rest_id=response_json["restaurant"]["id"]
#     print("\033[92m✅ Device A Login Successful.\033[0m",response_a.status_code)
#     # print("Token A:", token_a)
# else:
#     print("\033[91m❌ Device A Login Failed.\033[0m")
#     print("Status Code:", response_a.status_code)
#     print("Response:", response_a.text)
#     print("\033[91m❌ TEST RESULT: FAILED — Could not login from Device A\033[0m")
#     exit()

# # Step 3: Login from Device B using same credentials
# print("\n🔐3: Attempting login from Device B (same credentials)...")
# response_b = requests.post("https://qa-oms.zolv.health/api/v1/user/oms-login", json=login)

# if response_b.status_code != 200:
#     print("\033[92m✅ Device B Login correctly blocked.\033[0m")
#     print("Status Code:", response_b.status_code)
#     print("Response:", response_b.text)
#     print("\033[92m✅ TEST RESULT: PASSED — Multiple-device login is not allowed.\033[0m")
# else:
#     token_b = response_b.json()["token"]
#     print("\033[91m❌ Device B Login succeeded, which should not be allowed.\033[0m",response_b.status_code)
#     # print("Token B:", token_b)


#     # Try to use Device A token (assume token is validated on a protected endpoint)
#     # protected_url = "https://qa-oms.zolv.health/api/v1/food/menu-item/web/{company_id}/{restaurant_id}/get-menu-item-counts"  # replace with real protected endpoint
#     headers = {
#         "Authorization": f"Bearer {token_a}",
#         "Content-Type": "application/json"
#     }
#     # https://qa-oms.zolv.health/api/v1/menu-item-library/web/get-menu-item-library
#     response_check = requests.get("https://qa-oms.zolv.health/api/v1/dashboard/orders/web/{company_id}/{68709372293ae6389032a05f}/get-order-progress", headers=headers)

#     if response_check.status_code != 403:  # 401 - invalid, expired , 403 - token is valid
#         print("✅ Device A token is now invalid — previous session was terminated.")
#         print("\033[92m✅ TEST RESULT: PASSED — Second login invalidated the first session.\033[0m", response_check.status_code)
#         print("Response:", response_check.text)
#     else:
#         print("\033[91m❌ Device A token is still valid — concurrent login is allowed.\033[0m")
#         print("\033[91m❌ TEST RESULT: FAILED — Multiple device login should be blocked.\033[0m", response_check.status_code)
#         # print("Response:", response_check.text)










# # Un Authorized User (Privilege) :

# choose = input("Select the Credential : ")


# if choose == "1":
#     print("Selected Credential : \033[1;34m AutotestAdmin \033[0m")

#     payload = {"loginId":"AutotestAdmin","password":"Smm@1234"}

# elif choose == "2":
#     print("Selected Credential : \033[1;34m AutotestOMS \033[0m")

#     payload = {"loginId":"AutotestOMS","password":"Smm@1234"}
   
# elif choose == "3":
#     print("Selected Credential : \033[1;34m AutotestKDS \033[0m")

#     payload =  {"loginId":"AutotestKDS","password":"Smm@1234"}   

# elif choose == "4":
        
#     print("Selected Credential : \033[1;34m AutotestZolvGo \033[0m")

#     payload = {"loginId":"AutotestZolvGo","password":"Smm@1234"}


# login_Auth = requests.post(login_url,json=payload)
# print(payload,login_Auth)
# if login_Auth.status_code == 200:
#     admin_json = login_Auth.json()
#     admin_token = admin_json['token']['token']
#     name = admin_json['name']
#     company_id = admin_json['company']['id']
#     print("\033[91m❌  TEST FAILED..\033[0m", name, company_id)
# else:
#     print("\033[92m✅TEST PASSED..")










# #  Invalid API endpoint (intentionally wrong) : 

#     print("\033[1;34mLOGIN TESTCASE - Invalid Endpoint, Minimal Payload\033[0m")

#     invalidlogin_url = "https://qa-admin.zolv.health/api/v1/user/invalid_login"  # Example: endpoint is incorrect



#         # Send POST request to invalid endpoint

#     response = requests.post(invalidlogin_url, json={"loginId": loginid, "password": pwd})

#     # Check if response is successful or has a response code
#     if response.status_code:
#         print(f"Status Code: {response.status_code}")

#         # Check if response content-type is JSON
#         content_type = response.headers.get('Content-Type', '')
#         if 'application/json' in content_type:
#             print("Response JSON:")
#             # print(json.dumps(response.json(), indent=4))
#             print("\033[92m✅ Test Passed: Received JSON response\033[0m")
#         else:
#             print("\033[91m❌ Response is not valid JSON:\033[0m")
#             print(response.text)
#     else:
#         print("\033[91m❗ Request failed, no valid status code received.\033[0m")








# # Test login rate limiting (multiple attempts in quick succession) : 

# print("\033[1;34mRate limiting (multiple attempts in quick succession) Test\033[0m")

# username = "testuser"
# wrong_password = "wrongPass"
# invalid_login_payload={"loginId": username, "password": wrong_password}

# print("\nTesting rate limiting protection...")
# for i in range(100):
#     response_rate_limit = requests.post(login_url, json=invalid_login_payload)
#     print(f"Attempt {i+1} status code: {response_rate_limit.status_code}")
#     if response_rate_limit.status_code == 429:
#         print("\033[1;92mRate limiting correctly implemented!\033[0m")
#         break
#     # time.sleep(0.1)  # Small delay between requests





# #Simultaneously Login Attempts : 



# print("\033[1;34mSIMULATED LOGIN BLOCK TEST\033[0m")

# # Static credentials
# correct_username = "TestOMS"
# correct_password = "Smm@1234"


# # Simulate repeated login attempts
# blocked = False
# username = "testuser"
# password = "wrongpass"  # Always wrong

# for login_attempts in range(10):
#     print("Attempt", login_attempts + 1)

#     if blocked:
#         print("\033[91m🚫 Blocked: Too many failed attempts.\033[0m")
#     else:
#         if username == correct_username and password == correct_password:
#             print("\033[92m✅ Login successful\033[0m")
#         else:
#             print("\033[91m❌ Login failed: Incorrect credentials\033[0m")
#             if login_attempts >= 2:  # since attempts count starts from 0, block after 3 attempts
#                 blocked = True
#                 print("\033[91m🚫 User is now blocked after 3 failed attempts.\033[0m")

#     time.sleep(1)





# # Login Test with invalid HTTP method : 

# print("\033[1;34mLOGIN TESTCASE - Invalid Endpoint, Minimal Payload\033[0m")

# response_invalid_method = requests.put(login_url,json={"loginId": "TestOMS", "password": "Smm@1234"})
# if response_invalid_method.status_code != 200:
#     print("\033[1;92mTest for invalid HTTP method passed!\033[0m")
#     print("Status code:", response_invalid_method.status_code)
# else:
#     print("\033[1;31mTest for invalid HTTP method failed! Server accepted PUT for POST endpoint.\033[0m")






# # Login with Deleted User Credentials : 



# print("\033[1;34m LOGIN DELETED USER TESTCASE!\033[0m")


# admin_url = "https://qa-admin.zolv.health/api/v1/user/login"
# admin_logout = "https://qa-admin.zolv.health/api/v1/user/logout"


# login_id = "TestDelete"
# password= "TestDelete@1234"

# # ----------------------
# # Login as test user
# # ----------------------
# user1 = requests.post(login_url, json={"loginId":login_id, "password":password})

# if user1.status_code == 200:
#     user1_json = user1.json()
#     name_user1 = user1_json['name']
#     company_id = user1_json['company']['id']
#     token1 = user1_json['token']['token']
#     user_id = user1_json['id']

#     print("\033[92m✅ User login successful\033[0m")
#     print("Company ID:", company_id)
#     print("Response JSON:")
#     print(json.dumps(user1_json, indent=4))

#     # Step 2: Logout test user
#     headers = {"Authorization": f"Bearer {token1}"}
#     logout_response = requests.put(logout_url, headers=headers)
#     if logout_response.status_code == 200:
#         print("\033[92m✅ Test user logout successful\033[0m")
#     else:
#         print("\033[91m❌ Test user logout failed with status code:\033[0m", logout_response.status_code)
#         print(logout_response.text)

# else:
#     print("\033[91m❌ Test user login failed with status code:\033[0m", user1.status_code)
#     print(user1.text)
#     exit()

# # ----------------------
# # Step 3: Admin login
# # ----------------------
# admin_login = requests.post(admin_url, json={"loginId": "AutotestAdmin", "password": "Smm@1234"})
# if admin_login.status_code == 200:
#     admin_json = admin_login.json()
#     admin_token = admin_json['token']['token']
#     name = admin_json['name']

#     print("\033[92m✅ Admin login successful:\033[0m", name)

#     # Step 4: Delete the user
#     delete_url = "https://qa-admin.zolv.health/api/v1/masters/user/web/{company_id}/delete-user/{user_id}"

#     delete_urls = delete_url.format(company_id=company_id, user_id=user_id)
#     headers = {"Authorization": f"Bearer {admin_token}"}
#     delete_response = requests.patch(delete_urls, headers=headers)

#     if delete_response.status_code == 200:
#         print("\033[92m✅ Test user deleted successfully\033[0m")

#         # Step 5: Logout admin
#         logout_admin_response = requests.put(admin_logout, headers=headers)
#         if logout_admin_response.status_code == 200:
#             print("\033[92m✅ Admin logout successful\033[0m")
#         else:
#             print("\033[91m❌ Admin logout failed with status code:\033[0m", logout_admin_response.status_code)
#             print(logout_admin_response.text)

#         # Step 6: Try to log in as deleted user
#         deleted_login = requests.post(login_url, json={"loginId": loginid, "password": pwd})
#         if deleted_login.status_code == 401:
#             print("\033[92m✅ Deleted user login correctly blocked (401 Unauthorized)\033[0m")
#         else:
#             print("\033[91m❌ Unexpected login status for deleted user:\033[0m", deleted_login.status_code)
#             print(deleted_login.text)

#     else:
#         print("\033[91m❌ Failed to delete test user. Status:\033[0m", delete_response.status_code)
#         print(delete_response.text)

# else:
#     print("\033[91m❌ Admin login failed with status code:\033[0m", admin_login.status_code)
#     print(admin_login.text)





# # # lOGIN WITH INACTIVE USER

# print("\033[1;34m LOGIN WITH INACTIVE USER TEST!\033[0m")

# username_input = "TestOMS"
# password_input = "Smm@1234"

# # Stored user data
# stored_username = "TestOMS"
# stored_password = "Smm@1234"


# #  Admin login
# # # ----------------------
# admin_login = requests.post(login_url, json={"loginId": "AutotestAdmin", "password": "Smm@1234"})
# if admin_login.status_code == 200:
#     admin_json = admin_login.json()
#     admin_token = admin_json['token']['token']
#     name = admin_json['name']
#     company_id = admin_json['company']['id']
#     print("\033[92m✅ Admin login successful:\033[0m", name,company_id)

#     # get user active status : 
#     user_url=f"https://qa-admin.zolv.health/api/v1/masters/user/web/{company_id}/get-user-list"
#     user_headers = {"Authorization": f"Bearer {admin_token}"}
#     user_payload = {"username": username_input,"password_input":password_input}

#     user_response=requests.get(user_url,headers=user_headers)

#     if user_response.status_code == 200:
#         # Parse the user list JSON
#         user_json = user_response.json()
#         user_list = user_json['users']
#         print("Sample user object:", user_list[0])  # 👈 Check actual keys

#         found = False
#         for user in user_list:
#             # Try matching by loginId instead of username
#             if user["loginId"] == username_input:
#                 isActive = user["isActive"]
#                 found = True

#                 if username_input == stored_username and password_input == stored_password:
#                     if isActive:
#                         print("\033[92m✅ Login successful (User is active)\033[0m",username_input)
#                     else:
#                         print("\033[91m🚫 Login failed: User is currently inactive\033[0m",username_input)
#                 else:
#                     print("\033[91m❌ Login failed: Incorrect username or password\033[0m")

#         if not found:
#             print("\033[91m❌ User not found in user list\033[0m")




print("haiiiiii welcome to the admin world.....................!")
