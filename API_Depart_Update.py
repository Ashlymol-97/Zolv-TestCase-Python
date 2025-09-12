
import requests
import time
import json
import random
import urllib.parse

import base64



failed_count=0
total_count=18

base_url= "https://qa-admin.zolv.health/"
login_url= "https://qa-admin.zolv.health/api/v1/user/login"
logout_url="https://qa-admin.zolv.health/api/v1/user/logout"

test_case_id=0


# 1 : Login TestCase : Login with valid Login Credentials


print("\033[1;34m ADMIN LOGIN TESTCASE! Document ID: TP_001\033[0m")
# print("\033[1;34m Login with valid Login Credentials! Document ID: TP_001\033[0m")


login_payload = {
        "loginId":"ZolvQAAdmin",
        "password":"Smm@1234"
}


     
response_login = requests.post(login_url,json=login_payload)
if response_login.status_code != 200:
    failed_count+=1
    # print(f"\033[91m❌ Login failed with status code {response_login.text}\033[0m")
    print(f"\033[91m❌  Test Case ID - 001 : Login       : TEST FAILED...! :  Error - Invalid Credentials \033[0m") # login failed so test passed
else:
    response_json = response_login.json()
    names=response_json.get('name')
    # print("...",response_login.text)
    valid_token= response_json.get('token',{}).get('token')
    company_id=response_json['company']['id']

    headers= {
        "Authorization": f"Bearer {valid_token}",
        "Content-Type": "application/json"
    }
    # print(f"\033[91m✅ Login successful! Welcome, {loginId} | Name: {name} | Status: {response_login.status_code}\033[0m",{"loginId":loginId,"password":pwd})
    # print("Response JSON : ",json.dumps(response_json,indent=4))
    print(f"\033[92m✅ Test Case ID - 001 : Login         : TEST PASSED...! \033[0m") # login success so test failed becoz in oms logged with oms in other 3 credentials kds,go,testoms










# 2 : Get Department : Get list
dep_id = 0
get_response = requests.get(base_url + f"api/v1/masters/department/web/68709372293ae6389032a050/get-department-list?isActive=&name=&ignorePaging=false&size=10&sort=1&page=1",headers=headers)
if get_response.status_code == 200:
#     print("Listed..Success")
    dep_json=get_response.json()
#     print("Response JSON : ",json.dumps(dep_json,indent=4))
    for dep_id in dep_json:
        dep_id = dep_json['departments'][-1]['id']
#     print(dep_id)
# print("Failed list")



print("\033[1;34m  Department Updation with Name Field ! Document ID: TP_002\033[0m")


#  Department Update : Valid Name Field : 
test_case_id=2
valid_value="Staff Dep"

Update_name_payload={
    "name":valid_value,
    "isActive": True
}
response_update_name=requests.put(base_url + f"api/v1/masters/department/web/{company_id}/update-department/{dep_id}",headers=headers,json=Update_name_payload)



def valid_test_case(response, company_id, headers, failed_count):
    if response_update_name.status_code == 200:
        update_json = response_update_name.json()
        print(f"\033[92m✅ Test Case ID - 00{test_case_id} : Valid value : TEST PASSED...! \033[0m")
        # print("...",response_update_name.text)

        # print(response_update_name.status_code,names,"=================")

        # dep_id = update_json.get('id')
        # if dep_id:
        #     del_response = requests.patch(
        #         base_url + f"api/v1/masters/department/web/{company_id}/delete-department/{dep_id}",
        #         headers=headers
        #     )
        #     if del_response.status_code == 200:
        #         del_response.status_code
        #         # print("Deleted Successfully")
    else:
        print(f"\033[91m❌ Test Case ID - 00{test_case_id} : Valid value : TEST FAILED...! \033[0m")
        failed_count += 1
        # print("...",response_update_name.status_code,response_update_name.text)
        # print(response_update_name.status_code)
valid_test_case(Update_name_payload, company_id, headers, failed_count)








# 3 : Update Department with invalid Name field : 



test_case_id=2



test_cases = [
    (22, "Integer Value"),                      # Test Case ID - 003
    ("@%&#+-+=54a%", "Special Characters"),     # Test Case ID - 004
    (None, "Null"),                             # Test Case ID - 005
    (True, "Boolean"),                          # Test Case ID - 006
    ("  AreaStart", "Leading Space"),           # Test Case ID - 007
    ("AreaEnd  ", "Trailing Space"),            # Test Case ID - 008
    ("", "Empty String"),                       # Test Case ID - 009
    ("   ", "Only Spaces"),                     # Test Case ID - 010
    ("testname"+ "a" * 1000, "large input values"),         # Test Case ID - 011
    ("用户名😊", "Emoji / Unicode"),              # Test Case ID - 012
    ("' OR '1'='1", "SQL Injection Attempt"),   # Test Case ID - 013
    ("CSE", "Duplicate Value"),        # Test Case ID - 014
]


for test,description in test_cases:
    
     Update_name_invalid_payload={
       "name":test,
       "isActive": True
     }
     test_case_id += 1
     response_update_invalid_name=requests.put(base_url + f"api/v1/masters/department/web/{company_id}/update-department/{dep_id}",headers=headers,json=Update_name_invalid_payload)

     def test_case(response,company_id, headers, failed_count):

         if response.status_code == 200: 

             update_invalid__json = response.json()
             print(f"\033[91m❌ Test Case ID - 00{test_case_id} : {description}             :           TEST FAILED...! : Invalid data or missing fields \033[0m ")
        #      print(response.text, test)
             print(response.status_code)
             failed_count+=1


        #     dep_id = update_invalid__json.get('id')
        #     if dep_id:
        #         del_response = requests.patch(
        #             base_url + f"api/v1/masters/department/web/{company_id}/delete-department/{dep_id}",
        #             headers=headers
        #         )
        #         if del_response.status_code == 200:
        #             del_response.text
        #             # print("🗑️ Department Deleted")
         else:
             print(f"\033[92m✅ Test Case ID - 00{test_case_id} : {description}           :            TEST PASSED...! \033[0m ")
        #      print(response.text, test)
        #      print(response.status_code)


     test_case(response_update_invalid_name, company_id, headers, failed_count)









# 4 : Update departmnt : Isactive field : Valid :

print("\033[1;34m  Department Updation with IsActive Field ! Document ID: TP_002\033[0m")

#  Department Update : Valid Name Field : 
test_case_id=2
valid_value=True

Update_name_payload={
    "name":valid_value,
    "isActive": valid_value
}
response_update_isactive=requests.put(base_url + f"api/v1/masters/department/web/{company_id}/update-department/{dep_id}",headers=headers,json=Update_name_payload)



def valid_test_case(response, company_id, headers, failed_count):
    if response_update_name.status_code == 200:
        update_json = response_update_name.json()
        print(f"\033[92m✅ Test Case ID - 00{test_case_id} : Valid value : TEST PASSED...! \033[0m")
        # print("...",response_update_name.text)

        # print(response_update_name.status_code,names,"=================")

        # dep_id = update_json.get('id')
        # if dep_id:
        #     del_response = requests.patch(
        #         base_url + f"api/v1/masters/department/web/{company_id}/delete-department/{dep_id}",
        #         headers=headers
        #     )
        #     if del_response.status_code == 200:
        #         del_response.status_code
        #         # print("Deleted Successfully")
    else:
        print(f"\033[91m❌ Test Case ID - 00{test_case_id} : Valid value : TEST FAILED...! \033[0m")
        failed_count += 1
        # print("...",response_update_name.status_code,response_update_name.text)
        # print(response_update_name.status_code)
valid_test_case(response_update_isactive, company_id, headers, failed_count)






# 3 : Update Department with invalid Name field : 



test_case_id=2



test_cases = [
    (22, "Integer Value"),                      # Test Case ID - 003
    ("*@%&#+-+=54a%", "Special Characters"),     # Test Case ID - 004
    (None, "Null"),                             # Test Case ID - 005
    ("  AreaStart", "Leading Space"),           # Test Case ID - 006
    ("AreaEnd  ", "Trailing Space"),            # Test Case ID - 007
    ("", "Empty String"),                       # Test Case ID - 008
    ("   ", "Only Spaces"),                     # Test Case ID - 009
    ("testname"+ "a" * 1000, "large input values"),         # Test Case ID - 010
    ("用户名😊", "Emoji / Unicode"),              # Test Case ID - 011
    ("' OR '1'='1", "SQL Injection Attempt"),   # Test Case ID - 012
    ("CSE", "Duplicate Value"),        # Test Case ID - 013
]


for test,description in test_cases:
    
     Update_name_invalid_payload={
       "name":"Staff Department",
       "isActive": test
     }
     test_case_id += 1
     response_update_invalid_isactive=requests.put(base_url + f"api/v1/masters/department/web/{company_id}/update-department/{dep_id}",headers=headers,json=Update_name_invalid_payload)

     def test_case(response,company_id, headers, failed_count):

         if response.status_code == 200: 

             update_invalid__json = response.json()
             print(f"\033[91m❌ Test Case ID - 00{test_case_id} : {description}             :           TEST FAILED...! : Invalid data or missing fields \033[0m ")
        #      print(response.text, test)
        #      print(response.status_code)
             failed_count+=1


        #     dep_id = update_invalid__json.get('id')
        #     if dep_id:
        #         del_response = requests.patch(
        #             base_url + f"api/v1/masters/department/web/{company_id}/delete-department/{dep_id}",
        #             headers=headers
        #         )
        #         if del_response.status_code == 200:
        #             del_response.text
        #             # print("🗑️ Department Deleted")
         else:
             print(f"\033[92m✅ Test Case ID - 00{test_case_id} : {description}           :            TEST PASSED...! \033[0m ")
        #      print(response.text, test)
        #      print(response.status_code)


     test_case(response_update_invalid_isactive, company_id, headers, failed_count)










# # 4 : Update department with OMS user token : 
# print("\033[1;34m  Department Updation with OMS USER Privilege ! Document ID: TP_002\033[0m")
# test_case_id=14

# OMS_login_payload = {
#         "loginId":"AutotestOMS",
#         "password":"Smm@1234"
# }
# valid_value="Head Dep"

# Update_name_payload={
#     "name":valid_value,
#     "isActive": True
# }
# response_OMS_login = requests.post(login_url,json=OMS_login_payload)
# if response_OMS_login.status_code == 200:
#     response_update_isactive=requests.put(base_url + f"api/v1/masters/department/web/{company_id}/update-department/{dep_id}",headers=headers,json=Update_name_payload)
#     token1= response_json.get('token',{}).get('token')
#     user_headers = {
#         "Authorization": f"Bearer {token1}",
#         "Content-Type": "application/json"
#     }
#     valid_test_case(response_update_isactive, company_id, headers, failed_count)
