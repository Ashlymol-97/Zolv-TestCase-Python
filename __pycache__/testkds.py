import requests
import time
import json
import random
import urllib.parse

import base64
   


base_url = "https://qa-kds.zolv.health/"
login_url= "https://qa-kds.zolv.health/api/v1/user/kds-login"
logout_url = "https://qa-kds.zolv.health/api/v1/user/logout"


# # 11 :  Login with Deleted User Credentials : 



# # print("\033[1;34m LOGIN DELETED USER TESTCASE!\033[0m")


# admin_url = "https://qa-admin.zolv.health/api/v1/user/login"
# admin_logout = "https://qa-admin.zolv.health/api/v1/user/logout"

# admin_login = requests.post(admin_url, json={"loginId": "AutotestAdmin", "password": "Smm@1234"})
# if admin_login.status_code == 200:
#     admin_json = admin_login.json()
#     admin_token = admin_json['token']['token']
#     company_json = admin_login.json()

#     companys_id = company_json["company"]["id"]
#     # print("Response JSON :", json.dumps(company_json, indent=4))

#     # print("Logged ")
    

#     login_id = "TestdeleteaQ"
#     password= "Smm@1234"

#     create_user_payload= {
#     "name": "TestdeleteaQ",
#     "email": "",
#     "phone": "",
#     "loginId": "TestdeleteaQ",
#     "employeeCode": "TQ",
#     "type": "module_user",
#     "departmentId": "68709372293ae6389032a053",
#     "privilegedAreas": [],
#     "isActive": True,
#     "isEmployee": True,
#     "employeeCreditApplicable": False,
#     "employeeWalletApplicable": False,
#     "restaurantId": "68709372293ae6389032a05f",
#     "accessLevel": [
#     {
#         "module": "686f510c6e7e978b9132a03c",
#         "role": "68709372293ae6389032a054"
#     }
#     ],
#     "password": "Smm@1234"
#     }






#     create_user_url = f"https://qa-admin.zolv.health/api/v1/masters/user/web/{companys_id}/create-user"
#     headers_admin = {
#         "Authorization": f"Bearer {admin_token}",
#         "Content-Type": "application/json"
#     }
#     response_creates=requests.post(create_user_url,json=create_user_payload,headers=headers_admin)
#     print(response_creates)

#     if response_creates.status_code != 201:
    
#         print("Failed user creation...",response_creates.text)
#         print(response_creates.text,"................")
#         response_creates.status_code
#     else:
#         user_token = admin_json['token']['token']
#         ceateuser_json = response_creates.json()
#         print("User Creation successfull...")
#         # print("Response JSON :", json.dumps(ceateuser_json, indent=4))


    

#         # ----------------------
#         # Login as test user
#         # ----------------------
#         user2 = requests.post(login_url, create_user_payload)
#         users_id=None
#         if user2.status_code == 200:
#             user2_json = user2.json()
#             # print("Response JSON :", json.dumps(user1_json, indent=4))
#             name_user1 = user2_json['name']
#             companys_id = user2_json['company']['id']
#             toke = user2_json['token']['token']
#             users_id = user2_json['id']

#             print("\033[92m✅User login successful\033[0m")
#             # print("Company ID:", company_id)
#             # print("Response JSON:")
            

#             # Step 2: Logout test user
#             headers_log = {"Authorization": f"Bearer {toke}",
#                        "Content-Type": "application/json"
#             }
#             logout_response = requests.put(logout_url, headers=headers_log)
#             users_id=users_id
#             if logout_response.status_code == 200:
#                 S=logout_response.status_code
#                 print("\033[92m✅ Test user logout successful\033[0m")
#             else:
#                 print("\033[91m❌ Test user logout failed with status code:\033[0m")
#                 logout_response.text
#                 print(users_id)


#         else:
#             print("\033[92m✅ Test user login failed with status code: Test Case ID - 009 \033[0m")
#             user2.text
        
#         # ----------------------
#         # Step 3: Admin login
#         # ----------------------
#             admin_login = requests.post(admin_url, json={"loginId": "AutotestAdmin", "password": "Smm@1234"})
#             if admin_login.status_code == 200:
#                 admin_json = admin_login.json()
#                 ad_token = admin_json['token']['token']
#                 name = admin_json['name']
               
#                 print("\033[92m✅ Admin login successful:\033[0m", name)
#                 headers_userdel = {
#                     "Authorization": f"Bearer {ad_token}",
#                     "Content-Type": "application/json"
#                 }
#                 # Step 4: Delete the user
#                 delete_url = f"https://qa-admin.zolv.health/api/v1/masters/user/web/{companys_id}/delete-user/{users_id}?"

#                 delete_urls = delete_url.format(companys_id=companys_id,users_id=users_id)
                
#                 delete_response = requests.patch(delete_urls, headers=headers_userdel)

#                 if delete_response.status_code == 200:
#                     print("\033[92m✅ Test user deleted successfully\033[0m")

#                     # Step 5: Logout admin
#                     logout_admin_response = requests.put(admin_logout, headers=headers_userdel)
#                     if logout_admin_response.status_code == 200:
#                         logout_res=logout_admin_response.json()
#                         print("\033[92m✅ Admin logout successful\033[0m")
#                     else:
#                         print("\033[91m❌ Admin logout failed with status code:\033[0m")
#                         # print(logout_admin_response.text)
#                         msg=logout_admin_response.text


#                         # Step 6: Try to log in as deleted user
#                         deleted_login = requests.post(login_url, json=create_user_payload)
#                         if deleted_login.status_code != 200:
#                             print("\033[92m✅ TEST PASSED...! : Test Case ID - 011\033[0m")
#                             # print("\033[92m✅ TEST PASSED :  Deleted user login correctly blocked (401 Unauthorized) : Test Case ID - 009\033[0m")
#                         else:
#                             print("\033[91m❌ TEST FAILED...! : Test Case ID - 011 : Error - User not found \033[0m")

#                             # print("\033[91m❌ TEST FAILED : Unexpected login status for deleted user: Test Case ID - 009 \033[0m")
#                             # print(deleted_login.text)

#                 else:
#                     print("\033[91m❌ Failed to delete test user. Status:\033[0m")
#                     # print(delete_response.text)

#             else:
#                 print("\033[91m❌ Admin login failed with status code:\033[0m")
#                 # print(admin_login.text)


#         # print(" "*200) # for space 







import requests
import json

# ---------------------------
# Admin Login
# ---------------------------
admin_url = "https://qa-admin.zolv.health/api/v1/user/login"
admin_logout = "https://qa-admin.zolv.health/api/v1/user/logout"
login_url = "https://qa-admin.zolv.health/api/v1/user/login"
logout_url = "https://qa-admin.zolv.health/api/v1/user/logout"

admin_login = requests.post(admin_url, json={"loginId": "AutotestAdmin", "password": "Smm@1234"})

if admin_login.status_code == 200:
    admin_json = admin_login.json()
    admin_toke = admin_json["token"]["token"]
    company_id = admin_json["company"]["id"]

    print("✅ Admin login successful")

    # ---------------------------
    # Create New Test User
    # ---------------------------
    create_user_payload = {
        "name": "Kdstest",
        "email": "",
        "phone": "",
        "loginId": "Kdstest",
        "employeeCode": "Kds",
        "type": "module_user",
        "departmentId": "68709372293ae6389032a053",
        "privilegedAreas": [
            "68709372293ae6389032a05e"
        ],
        "isActive": True,
        "isEmployee": True,
        "employeeCreditApplicable": False,
        "employeeWalletApplicable": False,
        "restaurantId": "68709372293ae6389032a05f",
        "accessLevel": [
            {
            "module": "686f510c6e7e978b9132a03c",
            "role": "68709372293ae6389032a056"
            }
        ],
        "password": "Smm@1234"
    }
        

    create_user_url = f"https://qa-admin.zolv.health/api/v1/masters/user/web/{company_id}/create-user"
    header1_admin = {
        "Authorization": f"Bearer {admin_toke}",
        "Content-Type": "application/json"
    }

    responses_create = requests.post(create_user_url, json=create_user_payload, headers=header1_admin)

    if responses_create.status_code == 201:
        print("✅ Test user created successfully")

        # ---------------------------
        # Login as the new test user
        # ---------------------------
        user_login = requests.post(login_url, json=create_user_payload)

        if user_login.status_code == 200:
            user_json = user_login.json()
            user_token = user_json["token"]["token"]
            user_id = user_json["id"]

            print("✅User login successful")

            # ---------------------------
            # Logout test user
            # ---------------------------
            header_user = {
                "Authorization": f"Bearer {user_token}",
                "Content-Type": "application/json"
            }

            logout_user_response = requests.put(logout_url, headers=header_user)

            if logout_user_response.status_code == 200:
                print("✅ Test user logout successful")

                # ---------------------------
                # Admin logs in again
                # ---------------------------
                admin_login = requests.post(admin_url, json={"loginId": "AutotestAdmin", "password": "Smm@1234"})
                if admin_login.status_code == 200:
                    admin_json = admin_login.json()
                    admin_t = admin_json["token"]["token"]
                    print("✅ Admin login successful: Autotest Admin")

                    # ---------------------------
                    # Delete test user
                    # ---------------------------
                    delete_url = f"https://qa-admin.zolv.health/api/v1/masters/user/web/{company_id}/delete-user/{user_id}?"
                    headers_a = {
                        "Authorization": f"Bearer {admin_t}",
                        "Content-Type": "application/json"
                    }

                    delete_response = requests.patch(delete_url, headers=headers_a)

                    if delete_response.status_code == 200:
                        print("✅ Test user deleted successfully")

                        # ---------------------------
                        # Admin logout
                        # ---------------------------
                        logout_admin_response = requests.put(admin_logout, headers=headers_a)

                        if logout_admin_response.status_code == 200:
                            print("✅ Admin logout successful")

                            # ---------------------------
                            # Try login as deleted user
                            # ---------------------------
                            deleted_login = requests.post(login_url, json={
                                "loginId": "kdstest",
                                "password": "Smm@1234"
                            })

                            if deleted_login.status_code != 200:
                                print("\033[92m✅ TEST PASSED...! : Test Case ID - 011\033[0m")
                            else:
                                print("\033[91m❌ TEST FAILED...! : Test Case ID - 011 : Deleted user was able to login\033[0m")

                        else:
                            print("❌ Admin logout failed")
                    else:
                        print("❌ Failed to delete test user")
                else:
                    print("❌ Admin re-login failed")
            else:
                print("❌ Test user logout failed")
        else:
            print("❌ Test user login failed")
    else:
        print("❌ Test user creation failed")
else:
    print("❌ Admin login failed")







# # # 11 :  Login with Deleted User Credentials : 



# # print("\033[1;34m LOGIN DELETED USER TESTCASE!\033[0m")


# admin_url = "https://qa-admin.zolv.health/api/v1/user/login"
# admin_logout = "https://qa-admin.zolv.health/api/v1/user/logout"

# admin_login = requests.post(admin_url, json={"loginId": "AutotestAdmin", "password": "Smm@1234"})
# if admin_login.status_code == 200:
#     admin_json = admin_login.json()
#     admin_token = admin_json['token']['token']
#     company_json = admin_login.json()

#     companys_id = company_json["company"]["id"]
#     # print("Response JSON :", json.dumps(company_json, indent=4))

#     # print("Logged ")
    

#     # login_id = "TestdeleteaQ"
#     # password= "Smm@1234"

#     create_user_payload= {
#     "name": "TestdeleteaQ",
#     "email": "",
#     "phone": "",
#     "loginId": "TestdeleteaQ",
#     "employeeCode": "TQ",
#     "type": "module_user",
#     "departmentId": "68709372293ae6389032a053",
#     "privilegedAreas": [],
#     "isActive": True,
#     "isEmployee": True,
#     "employeeCreditApplicable": False,
#     "employeeWalletApplicable": False,
#     "restaurantId": "68709372293ae6389032a05f",
#     "accessLevel": [
#     {
#         "module": "686f510c6e7e978b9132a03c",
#         "role": "68709372293ae6389032a054"
#     }
#     ],
#     "password": "Smm@1234"
#     }






#     create_user_url = f"https://qa-admin.zolv.health/api/v1/masters/user/web/{companys_id}/create-user"
#     headers_admin = {
#         "Authorization": f"Bearer {admin_token}",
#         "Content-Type": "application/json"
#     }
#     response_creates=requests.post(create_user_url,json=create_user_payload,headers=headers_admin)
#     print(response_creates)

#     if response_creates.status_code != 201:
    
#         print("Failed user creation...",response_creates.text)
#         print(response_creates.text,"................")
#         response_creates.status_code
#     else:
#         user_token = admin_json['token']['token']
#         ceateuser_json = response_creates.json()
#         print("User Creation successfull...")
#         # print("Response JSON :", json.dumps(ceateuser_json, indent=4))


    

#         # ----------------------
#         # Login as test user
#         # ----------------------
#         user2 = requests.post(login_url, create_user_payload)
#         users_id=None

#         if user2.status_code == 200:
#             user2_json = user2.json()
#             # print("Response JSON :", json.dumps(user1_json, indent=4))
#             name_user1 = user2_json['name']
#             companys_id = user2_json['company']['id']
#             toke = user2_json['token']['token']
#             users_id = user2_json['id']

#             print("\033[92m✅User login successful\033[0m")
#             # print("Company ID:", company_id)
#             # print("Response JSON:")
            

#             # Step 2: Logout test user
#             headers_log = {"Authorization": f"Bearer {toke}",
#                        "Content-Type": "application/json"
#             }
#             logout_response = requests.put(logout_url, headers=headers_log)
#             users_id=users_id

#             if logout_response.status_code == 200:
#                 S=logout_response.status_code
#                 print("\033[92m✅ Test user logout successful\033[0m")
#             else:
#                 print("\033[91m❌ Test user logout failed with status code:\033[0m")
#                 logout_response.text

#         else:
#             print("\033[92m✅ Test user login failed with status code: Test Case ID - 009 \033[0m")
#             user2.text

#         # ----------------------
#         # Step 3: Admin login
#         # ----------------------
#             admin_login = requests.post(admin_url, json={"loginId": "AutotestAdmin", "password": "Smm@1234"})
#             if admin_login.status_code == 200:
#                 admin_json = admin_login.json()
#                 admin_token = admin_json['token']['token']
#                 name = admin_json['name']

#                 print("\033[92m✅ Admin login successful:\033[0m", name)

#                 # Step 4: Delete the user
#                 # if 'users_id' in locals():

#                 delete_url = "https://qa-admin.zolv.health/api/v1/masters/user/web/{companys_id}/delete-user/{users_id}?"

#                 delete_urls = delete_url.format(companys_id=companys_id,users_id=users_id)
#                 headers_userdel = {"Authorization": f"Bearer {admin_token}"}
#                 delete_response = requests.patch(delete_urls, headers=headers_userdel)

#                 if delete_response.status_code == 200:
#                     print("\033[92m✅ Test user deleted successfully\033[0m")

#                     # Step 5: Logout admin
#                     logout_admin_response = requests.put(admin_logout, headers=headers_userdel)
#                     if logout_admin_response.status_code == 200:
#                         logout_res=logout_admin_response.json()
#                         print("\033[92m✅ Admin logout successful\033[0m")
#                     else:
#                         print("\033[91m❌ Admin logout failed with status code:\033[0m")
#                         # print(logout_admin_response.text)
#                         msg=logout_admin_response.text


#                         # Step 6: Try to log in as deleted user
#                         deleted_login = requests.post(login_url, json=create_user_payload)
#                         if deleted_login.status_code != 200:
#                             print("\033[92m✅ TEST PASSED...! : Test Case ID - 011\033[0m")
#                             # print("\033[92m✅ TEST PASSED :  Deleted user login correctly blocked (401 Unauthorized) : Test Case ID - 009\033[0m")
#                         else:
#                             print("\033[91m❌ TEST FAILED...! : Test Case ID - 011 : Error - User not found \033[0m")

#                             # print("\033[91m❌ TEST FAILED : Unexpected login status for deleted user: Test Case ID - 009 \033[0m")
#                             # print(deleted_login.text)

#                 else:
#                     print("\033[91m❌ Failed to delete test user. Status:\033[0m",delete_response.status_code)
#                     # print(delete_response.text)

#             else:
#                 print("\033[91m❌ Admin login failed with status code:\033[0m")
#                 # print(admin_login.text)


#         # print(" "*200) # for space 

