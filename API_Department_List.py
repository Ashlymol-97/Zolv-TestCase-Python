
import requests
import time
import json
import random
import urllib.parse

import base64


base_url= "https://qa-admin.zolv.health/"
login_url= "https://qa-admin.zolv.health/api/v1/user/login"
logout_url="https://qa-admin.zolv.health/api/v1/user/logout"

failed_count=0
total_count=10

print("\033[1;34m Get Department LIST  TESTCASE! Document ID: \033[0m")


login_payload = {
    "loginId":"ZolvQAAdmin",
    "password":"Smm@1234"
}



# 1 : Get Area  : Get Department list with valid company ID :


print("\033[1;34m Get Department List with valid company ID \033[0m")


response_login = requests.post(login_url,json=login_payload)
if response_login.status_code != 200:
    print(" Login failed ")

else:
    response_json = response_login.json()
    # print("Response JSON : ",json.dumps(response_json,indent=4))
    # token1= response_json.get('token',{}).get('token')
    company_id=response_json['company']['id']
    token = response_json["token"]["token"]

    # print(" Login successful")
    header_deplist = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    Get_url=base_url + f"api/v1/masters/department/web/{company_id}/get-department-list?isActive=&name=&ignorePaging=false&size=10&sort=1&page=1"
    response_get_dep=requests.get(Get_url,headers=header_deplist)
    if response_get_dep.status_code == 200:
        get_dep_json = response_get_dep.json()
        # print("Response JSON : ",json.dumps(get_dep_json,indent=4))
        print("\033[1;92m✅ Test Case ID - 001   :  TEST PASSED...! \033[0m")   
    else:
        failed_count+=1

        print(f"\033[1;91m❌ Test Case ID - 001   :  Invalid Company Id  : TEST FAILED...! \033[0m") # login failed so test passed

        







# 2 : Get Department list with invalid company ID :


    print("\033[1;34m Get Department List with invalid company ID \033[0m")

    invalid_company_id="68709372293ae6389032a0588"

    # print(" Login successful")
  
    Get_url_invalid_company=base_url + f"api/v1/masters/department/web/{invalid_company_id}/get-department-list?isActive=&name=&ignorePaging=false&size=10&sort=1&page=1"
    response_get_dep=requests.get(Get_url_invalid_company,headers=header_deplist)
    if response_get_dep.status_code == 200:
        get_dep_json = response_get_dep.json()
        failed_count+=1
        print("\033[1;91m❌ Test Case ID - 002   :  Invalid Company Id :  TEST FAILED...!\033[0m")   
    else:
        print(f"\033[1;92m✅ Test Case ID - 002   :  TEST PASSED...! \033[0m") # login failed so test passed
        # print(response_get_dep.status_code)






# 3 :  Get Department list with  Invalid API end point : 


    print("\033[1;34m Get Department List Invalid API end point \033[0m")

    invalid_api_url = base_url + f"api/v1/masters/department/web/{company_id}/get-department-list/invalid" 

    response_invalid_APi = requests.get(invalid_api_url,headers=header_deplist)
    # print(f"Status Code: {response_invalid_APi.status_code}")

    # Check if response is successful or has a response code
    if response_invalid_APi.status_code == 200:
        print(response_login.text,"Login with Invalid API endpoint")
        failed_count+=1
        print("\033[91m❌ Test Case ID - 003   :  Error - Invalid API endpoint :  TEST FAILED...!\033[0m")
    else:
        print("\033[1;92m✅ Test Case ID - 003   :  TEST PASSED...!\033[0m")
      













# 4 :  Get Department list with invalid HTTP method : 

    print("\033[1;34m Get Department List with Invalid HTTP Method \033[0m")


    response_invalid_method = requests.put(Get_url,header_deplist)
    if response_invalid_method.status_code != 200:
        print("\033[1;92mTest for invalid HTTP method passed!\033[0m",response_invalid_method.status_code)
        print("\033[1;92m✅ Test Case ID - 004   :  TEST PASSED...!\033[0m")
    else:
        failed_count+=1
        print("\033[1;91m❌ Test Case ID -  004   :  Error - API should only allow PUT for login :  TEST FAILED...!\033[0m")







# 5 : Get Department with Empty token : 
    Empty_token=""
    header_Empty = {
        "Authorization": f"Bearer {Empty_token}",
        "Content-Type": "application/json"
    }
    print("\033[1;34m Get Deaprtment List with Empty token \033[0m")


    response_empty_token = requests.get(Get_url,header_Empty)
    if response_empty_token.status_code == 200:
        failed_count+=1
        empty_json=response_empty_token.json()
        # print("Response JSON : ",json.dumps(empty_json,indent=4))
        print("\033[1;91m❌ Test Case ID -  005   :  Empty Token :  TEST FAILED...!\033[0m")
    else:
        print("\033[1;92m✅ Test Case ID - 005   :  TEST PASSED...!\033[0m")








# 6 : Get Department List with invalid token format : 

    print("\033[1;34m Get Area List with invalid token format \033[0m")

    invalid_token = "@1234eas%%%%%77&&&&&77"
    header_invalid_token = {
        "Authorization": f"Bearer {invalid_token}",
        "Content-Type": "application/json"
    }
    response_get_dep=requests.get(Get_url,headers=header_invalid_token)
    if response_get_dep.status_code != 200:
        print("\033[1;92m✅ Test Case ID - 006   :  TEST PASSED...!\033[0m")   
    else:
        failed_count+=1

        print(f"\033[1;91m❌ Test Case ID - 006   :  Invalid Token Format :  TEST FAILED...!\033[0m") # login failed so test passed

        






# still vere cheyth : 












# 7 :  Get Deaprtment List with Unexpected parameter values for valid params :

    print("\033[1;34m Get Deaprtment List with  Invalid parameter values  \033[0m")

    unexp_params = {
        "page": -1,                  
        "ignorePaging":True,
        "size": 2,          
        "name":"xyz",
        "sort":-1,
        "moduleId":"a",
        "departmentId": "abc123",   
        "limit": "twenty",          
        "unexpected":"abcd"

    }

    unexp_para_url=f"api/v1/masters/department/web/{company_id}/get-department-list?"
    response_invalidparams = requests.get(unexp_para_url,params=unexp_params,headers=header_deplist)
    if response_invalidparams.status_code == 200:
        invalid_json = response_invalidparams.json()
        # print("Response JSON : ",json.dumps(invalid_json,indent=4))
        token1= invalid_json.get('token',{}).get('token')
        print(f"\033[1;91m❌ Test Case ID - 008   :  Error - Un-Expected Field Format :  TEST FAILED...!\033[0m") # login success so test failed becoz in oms logged with oms in other 3 credentials kds,go,testoms
        failed_count+=1


    else:
        print(f"\033[1;92m✅ Test Case ID - 008   :  TEST PASSED...!\033[0m") 






# 8 : Get Deaprtment list with  Valid parameter values :

print("\033[1;34m Get Deaprtment with  Valid parameter values  \033[0m")

valid_params = {
        "page": 1,                  # negative page number (invalid)
        "ignorePaging":False,
        "size": 2,          # not expected by API
        "name":"TestDep",
        "sort":-1,
        "isActive":True
        # "search": "f",   

    }


valid_para_url=f"api/v1/masters/department/web/{company_id}/get-department-list?"
response_validparams = requests.get(Get_url,params=valid_params,headers=header_deplist)
if response_validparams.status_code == 200:
    valid_json = response_validparams.json()
    # print("Response JSON : ",json.dumps(valid_json,indent=4))
    token1= valid_json.get('token',{}).get('token')
    print(f"\033[1;92m✅ Test Case ID - 009   :  TEST PASSED...!\033[0m") 
    response_valid_logout = requests.put(logout_url,headers=header_deplist) 
    if response_valid_logout.status_code == 200:
        response_valid_logout.text
        # print("Logout Successfully ")
    else:
        response_valid_logout.text
        # print("Logout Failed")
else:
    print(f"\033[1;91m❌ Test Case ID - 009   :  Error - Invalid Input Parameter :  TEST FAILED...!\033[0m")






