
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


def login_test(login_url,login_payload,failed_count):
     
    response_login = requests.post(login_url,json=login_payload)
    if response_login.status_code != 200:
        failed_count+=1
        # print(f"\033[91m❌ Login failed with status code {response_login.text}\033[0m")
        print(f"\033[91m❌  Test Case ID - 001 : Login                     : TEST FAILED...! :  Error - Invalid Credentials \033[0m") # login failed so test passed
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
        print(f"\033[92m✅ Test Case ID - 001 : Login                       : TEST PASSED...! \033[0m") # login success so test failed becoz in oms logged with oms in other 3 credentials kds,go,testoms
        return headers, company_id, failed_count   # ✅ return values

headers, company_id, failed_count = login_test(login_url, login_payload,failed_count)






print("\033[1;34m ADMIN DEPARTMENT CREATION TESTCASE! Document ID: TP_003\033[0m")

print("\033[1;34m  Department Creation with Name Field !\033[0m")

# 2 : Create : Department : Valid name Field :

test_case_id=2
valid_value="Cstest"


dep_payload = {
    "name": valid_value,
    "isActive": True
}
response = requests.post(
    base_url + f"api/v1/masters/department/web/{company_id}/create-department",
    json=dep_payload,
    headers=headers
)

def valid_test_case(response, company_id, headers, failed_count):


    if response.status_code == 201 and 200:
        create_json = response.json()
        print(f"\033[92m✅ Test Case ID - 00{test_case_id} : Valid value : TEST PASSED...! \033[0m")
        # print("...",response.text)
        names=create_json.get('name')

        # print(response.status_code,names,"=================")

        dep_id = create_json.get('id')
        if dep_id:
            del_response = requests.patch(
                base_url + f"api/v1/masters/department/web/{company_id}/delete-department/{dep_id}",
                headers=headers
            )
            if del_response.status_code == 200:
                del_response.status_code
                # print("Deleted Successfully")
    else:
        print(f"\033[91m❌ Test Case ID - 00{test_case_id} : Valid value : TEST FAILED...! \033[0m")
        failed_count += 1
        # print("...",response.status_code,response.text)
        # print(response.status_code)
valid_test_case(response, company_id, headers, failed_count)









# 3 : Create Department  with Invalid name value : 


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
    ("Menu Dep", "Duplicate Value"),        # Test Case ID - 014
]


for test,description in test_cases:
    
    invalid_dep_payload = {
        "name": test,
        "isActive": True  
    }

    test_case_id += 1
    response= requests.post(base_url + f"api/v1/masters/department/web/{company_id}/create-department",json=invalid_dep_payload,headers=headers)

    def test_case(response,company_id, headers, failed_count):



        if response.status_code == 201 or response.status_code == 500:

            create_json = response.json()
            print(f"\033[91m❌ Test Case ID - 00{test_case_id} : {description}             :           TEST FAILED...! : Invalid data or missing fields \033[0m ")
            # print(response.text, test)
            # print(response.status_code)
            failed_count+=1


            dep_id = create_json.get('id')
            if dep_id:
                del_response = requests.patch(
                    base_url + f"api/v1/masters/department/web/{company_id}/delete-department/{dep_id}",
                    headers=headers
                )
                if del_response.status_code == 200:
                    del_response.text
                    # print("🗑️ Department Deleted")
        else:
            print(f"\033[92m✅ Test Case ID - 00{test_case_id} : {description}           :            TEST PASSED...! \033[0m ")
            # print(response.text, test)
            # print(response.status_code)


    test_case(response, company_id, headers, failed_count)





# 4 : Create Department  with valid Isactive  : 

print("\033[1;34m  Department Creation with Isactive Field !\033[0m")

valid_value=True

test_case_id=15

valid_dep_payload = {
    "name": "TestDepart",
    "isActive": valid_value
}
response = requests.post(base_url + f"api/v1/masters/department/web/{company_id}/create-department",json=valid_dep_payload,headers=headers)

valid_test_case(response, company_id, headers, failed_count)







# 5 : Create Department  with invalid Isactive :



test_case_id=15



test_cases = [
    (22, "Integer Value"),                      # Test Case ID - 003
    ("@%&#+-+=54a%", "Special Characters"),     # Test Case ID - 004
    (None, "Null"),                             # Test Case ID - 005
    ("  AreaStart", "Leading Space"),           # Test Case ID - 006
    ("AreaEnd  ", "Trailing Space"),            # Test Case ID - 007
    ("", "Empty String"),                       # Test Case ID - 008
    ("   ", "Only Spaces"),                     # Test Case ID - 009
    ("testname"+ "a" * 1000, "large input values"),         # Test Case ID - 010
    ("用户名😊", "Emoji / Unicode"),              # Test Case ID - 011
    ("' OR '1'='1", "SQL Injection Attempt"),   # Test Case ID - 012
    ("Menu Dep", "Duplicate Value"),        # Test Case ID - 013
    ( "Areanametest".upper(), "Case Sensitivity"),       # Test Case ID - 014
]


for test,description in test_cases:
    invalid_is_dep_payload = {
        "name":"CSE",
        "isActive": test  
    }
    test_case_id += 1
    response = requests.post(base_url + f"api/v1/masters/department/web/{company_id}/create-department",json=invalid_is_dep_payload,headers=headers)
    test_case(response, company_id, headers, failed_count)






