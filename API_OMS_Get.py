import requests
import time
import json
import random
import urllib.parse

import base64
   

base_url = "https://qa-oms.zolv.health/"

login_url= "https://qa-oms.zolv.health/api/v1/user/oms-login"
logout_url="https://qa-oms.zolv.health/api/v1/user/logout"

failed_count=0
total_count=25

print("\033[1;34m GET DEPARTMENT LIST  TESTCASE! Document ID: \033[0m")


login_payload = {
    "loginId":"AutotestOMS",
    "password":"Smm@1234"
}



# 1 : Get Department TestCase : Get Department list with valid company ID :


print("\033[1;34m GET DEPARTMENT LIST with valid company ID \033[0m")


response_login = requests.post(login_url,json=login_payload)
if response_login.status_code == 200:
    response_json = response_login.json()
    # print("Response JSON : ",json.dumps(response_json,indent=4))
    token1= response_json.get('token',{}).get('token')
    company_id=response_json['company']['id']
    restaurant_id=response_json['restaurant']['id']
    token_dep = response_json["token"]["token"]

    # print(" Login successful")
    header_dep = {
        "Authorization": f"Bearer {token_dep}",
        "Content-Type": "application/json"
    }
    Get_url=base_url + f"api/v1/masters/department/web/{company_id}/get-department-list"
    response_get_dep=requests.get(Get_url,headers=header_dep)
    if response_get_dep.status_code == 200:
        get_dep_json = response_get_dep.json()
        # print("Response JSON : ",json.dumps(get_dep_json,indent=4))
        print("\033[1;92m✅ TEST PASSED...! : Test Case ID - 001 \033[0m")   
    else:
        failed_count+=1

        print(f"\033[91m❌ TEST FAILED...! : Test Case ID - 001 : Invalid Company Id  \033[0m") # login failed so test passed

        
else:
 
    print(" Login failed ")






# 2 : Get Department list with invalid company ID :


print("\033[1;34m GET DEPARTMENT LIST with invalid company ID \033[0m")

response_login = requests.post(login_url,json=login_payload)
if response_login.status_code == 200:
    inval_json = response_login.json()
    # print("Response JSON : ",json.dumps(response_json,indent=4))
    token1= inval_json.get('token',{}).get('token')
    invalid_company_id="68709372293ae6389032a051"
    token_dep2 = inval_json["token"]["token"]

    # print(" Login successful")
    header_dep2 = {
        "Authorization": f"Bearer {token_dep2}",
        "Content-Type": "application/json"
    }
    Get_url=base_url + f"api/v1/masters/department/web/{invalid_company_id}/get-department-list"
    response_get_dep=requests.get(Get_url,headers=header_dep2)
    if response_get_dep.status_code == 200:
        get_dep_json = response_get_dep.json()
        failed_count+=1

        # print("Response JSON : ",json.dumps(get_dep_json,indent=4))
        print("\033[1;91m❌ TEST FAILED...! : Test Case ID - 002 : Invalid Company Id \033[0m")   
    else:
        print(f"\033[92m✅ TEST PASSED...! : Test Case ID - 002 \033[0m") # login failed so test passed

        
else:
    print(" Login failed ")













# 3 :  Get Department list with  Invalid API end point : 


print("\033[1;34m GET DEPARTMENT LIST Invalid API end point \033[0m")

response_login = requests.post(login_url,json=login_payload)
if response_login.status_code == 200:
    res_json = response_login.json()
    # print("Response JSON : ",json.dumps(unauth_json,indent=4))
    token1= res_json.get('token',{}).get('token')
    company_id2=res_json['company']['id']
    token_dep4 = res_json["token"]["token"]
    privileges=res_json["id"]


    # print("..",response_json)
    header_dep4 = {
        "Authorization": f"Bearer {token_dep4}",
        "Content-Type": "application/json"
    }
    invalidlogin_url = base_url + f"api/v1/masters/department/web/{company_id2}/invalid" 


        # Send POST request to invalid endpoint

    response_invalid_APi = requests.get(invalidlogin_url,headers=header_dep4)
    # print(f"Status Code: {response_login.status_code}")

    # Check if response is successful or has a response code
    if response_invalid_APi.status_code == 200:
        # print(response_login.text,"Login with Invalid API endpoint")
        failed_count+=1
        print("\033[91m❌ TEST FAILED...! : Test Case ID - 003 : Error - Invalid API endpoint\033[0m")
    else:
        print("\033[1;92m✅ TEST PASSED...! : Test Case ID - 003\033[0m")
      
else:
    print("Login Failed ")






# 4 : Get Department list with Unexpected Parameters :

print("\033[1;34m GET DEPARTMENT LIST with Invalid Parameters \033[0m")

response_invalid_login = requests.post(login_url,json=login_payload)
if response_invalid_login.status_code == 200:
    res_para_json = response_invalid_login.json()
    # print("Response JSON : ",json.dumps(unauth_json,indent=4))
    token_dep5 = res_para_json["token"]["token"]
    company_id3=res_para_json['company']['id']


    # print("..",response_json)
    header_dep5 = {
        "Authorization": f"Bearer {token_dep5}",
        "Content-Type": "application/json"
    }
    invalid_params = {
        "departmentId": "abc123",   # should be numeric
        "page": -5,                  # negative page number (invalid)
        "limit": "twenty",           # should be an integer
        "unknownParam": "test",          # not expected by API
        "ignorePaging":"abcd",
        "name":"xyz",
        "sort":"a",
        "moduleId":"a"
    }

    Get_url=base_url + f"api/v1/masters/department/web/{company_id3}/get-department-list"
    response_invalidparams = requests.get(Get_url,params=invalid_params,headers=header_dep5)
    if response_invalidparams.status_code == 200:
        invalid_json = response_invalidparams.json()
        # print("Response JSON : ",json.dumps(invalid_json,indent=4))
        token1= invalid_json.get('token',{}).get('token')
        print(f"\033[91m❌ TEST FAILED...! : Test Case ID - 004 : Error - Invalid Input Format\033[0m") # login success so test failed becoz in oms logged with oms in other 3 credentials kds,go,testoms
        failed_count+=1


    else:
        print(f"\033[1;92m✅ TEST PASSED...! : Test Case ID - 004 \033[0m") 

else:
    print("Login Failed")





# 5 :  Get Deapartment list with invalid HTTP method : 

print("\033[1;34m GET DEPARTMENT LIST with Invalid HTTP Method \033[0m")

invalid_http_login = requests.post(login_url,json=login_payload)
if invalid_http_login.status_code == 200:
    invalid_json = invalid_http_login.json()
    company_id4=invalid_json['company']['id']

    token_dep6=invalid_json.get('token',{}).get('token')
    header_dep6 = {
        "Authorization": f"Bearer {token_dep6}",
        "Content-Type": "application/json"
    }
    Get_url=base_url + f"api/v1/masters/department/web/{company_id4}/get-department-list"

    # print("Response JSON : ",json.dumps(unauth_json,indent=4))
    response_invalid_method = requests.put(Get_url,header_dep6)
    if response_invalid_method.status_code != 200:
        # print("\033[1;92mTest for invalid HTTP method passed!\033[0m",response_invalid_method.status_code)
        print("\033[1;92m✅ TEST PASSED...! : Test Case ID - 005 \033[0m")
    else:
        failed_count+=1
        print("\033[1;91m❌ TEST FAILED...! : Test Case ID -  005  : Error - API should only allow PUT for login \033[0m")

else:
    print("Login Failed")




# 6 : Get Department with Empty token : 


print("\033[1;34m GET DEPARTMENT LIST with Empty token \033[0m")

invalid_empty_login = requests.post(login_url,json=login_payload)
if invalid_empty_login.status_code == 200:
    resp_json = invalid_empty_login.json()
    company_id5=resp_json['company']['id']

    token_dep7=" "
    header_dep7 = {
        "Authorization": f"Bearer {token_dep7}",
        "Content-Type": "application/json"
    }
    Get_url=base_url + f"api/v1/masters/department/web/{company_id5}/get-department-list"

    # print("Response JSON : ",json.dumps(resp_json,indent=4))
    response_empty_token = requests.get(Get_url,header_dep7)
    if response_empty_token.status_code == 200:
        print("\033[1;91m❌ TEST FAILED...! : Test Case ID -  006  : Empty Token \033[0m")
    else:
        failed_count+=1
        print("\033[1;92m✅ TEST PASSED...! : Test Case ID - 006 \033[0m")

else:
    print("Login Failed")






# 7 : Get Department with invalid token format : 

print("\033[1;34m GET DEPARTMENT LIST with invalid token format \033[0m")

invalid_token = requests.post(login_url,json=login_payload)
if response_login.status_code == 200:
    token_inval_json = response_login.json()
    # print("Response JSON : ",json.dumps(response_json,indent=4))
    invalid_token = "@1234eas%%%%%77&&&&&77"
    # print(" Login successful")
    company_id6=token_inval_json['company']['id']

    header_dep8 = {
        "Authorization": f"Bearer {invalid_token}",
        "Content-Type": "application/json"
    }
    Get_url=base_url + f"api/v1/masters/department/web/{company_id6}/get-department-list"
    response_get_dep=requests.get(Get_url,headers=header_dep8)
    if response_get_dep.status_code != 200:
        print("\033[1;92m✅ TEST PASSED...! : Test Case ID - 007 \033[0m")   
    else:
        failed_count+=1

        print(f"\033[1;91m❌ TEST FAILED...! : Test Case ID - 007 : Invalid Token Format \033[0m") # login failed so test passed

        
else:
 
    print(" Login failed ")








# 8 : Unexpected parameter values for valid params :

print("\033[1;34m Get Department with  Invalid parameter values  \033[0m")

invalid_login = requests.post(login_url,json=login_payload)
if invalid_login.status_code == 200:
    inval_params_json = invalid_login.json()
    # print("Response JSON : ",json.dumps(unauth_json,indent=4))
    token_dep5 = inval_params_json["token"]["token"]
    company_id3=inval_params_json['company']['id']


    # print("..",response_json)
    header_dep5 = {
        "Authorization": f"Bearer {token_dep5}",
        "Content-Type": "application/json"
    }
    invalid_params = {
        "page": -1,                  # negative page number (invalid)
        "ignorePaging":True,
        "size": 2,          # not expected by API
        "name":"xyz",
        "sort":-1,
        "moduleId":"a",
        "departmentId": "abc123",   # should be numeric
        "limit": "twenty",           # should be an integer
        "unexpected":"abcd"

    }

    Get_url=base_url + f"api/v1/masters/department/web/{company_id3}/get-department-list"
    response_invalidparams = requests.get(Get_url,params=invalid_params,headers=header_dep5)
    if response_invalidparams.status_code == 200:
        invalid_json = response_invalidparams.json()
        # print("Response JSON : ",json.dumps(invalid_json,indent=4))
        token1= invalid_json.get('token',{}).get('token')
        print(f"\033[1;91m❌ TEST FAILED...! : Test Case ID - 008 : Error - Invalid Input Format\033[0m") # login success so test failed becoz in oms logged with oms in other 3 credentials kds,go,testoms
        failed_count+=1


    else:
        print(f"\033[1;92m✅ TEST PASSED...! : Test Case ID - 008 \033[0m") 

else:
    print("Login Failed")





# 9 : Get Department with  Valid parameter values :

print("\033[1;34m Get Department with  Valid parameter values  \033[0m")

valid_params = {
        "page": 1,                  # negative page number (invalid)
        "ignorePaging":False,
        "size": 2,          # not expected by API
        "name":"TestDep",
        "sort":-1,
        "isActive":True
        # "search": "f",   

    }

valid_para_login = requests.post(login_url,json=login_payload)
if valid_para_login.status_code == 200:
    val_params_json = valid_para_login.json()
    # print("Response JSON : ",json.dumps(unauth_json,indent=4))
    token_valid_para = val_params_json["token"]["token"]
    company_valid=val_params_json['company']['id']


    # print("..",response_json)
    header_valid_para = {
        "Authorization": f"Bearer {token_valid_para}",
        "Content-Type": "application/json"
    }



    Get_url=base_url + f"api/v1/masters/department/web/{company_valid}/get-department-list"
    response_validparams = requests.get(Get_url,params=valid_params,headers=header_valid_para)
    if response_validparams.status_code == 200:
        valid_json = response_validparams.json()
        # print("Response JSON : ",json.dumps(valid_json,indent=4))
        token1= valid_json.get('token',{}).get('token')
        print(f"\033[1;92m✅ TEST PASSED...! : Test Case ID - 009 \033[0m") 

    else:
        print(f"\033[1;91m❌ TEST FAILED...! : Test Case ID - 009 : Error - Invalid Input Parameter\033[0m")
else:
    print("Login Failed")






# 10 : get list with report privilege user :

# print("\033[1;34m GET LIST REPORT PRIVILEGE USER \033[0m")



user_payload = {
    "loginId":"testreport",
    "password":"Smm@1234"
}

user_login = requests.post(login_url,json=user_payload)
if user_login.status_code != 200:
    print("OMS login Failed..")
else:
    user_privil_json = user_login.json()
    print("Response JSON : ",json.dumps(user_privil_json,indent=4))
    user_valid_token= user_privil_json.get('token',{}).get('token')
    company_id_valid=user_privil_json['company']['id']
    print("OMS login Success..")
    user_valid_header = {
        "Authorization": f"Bearer {user_valid_token}",
        "Content-Type": "application/json"
    }
    get_valid_user=requests.get(base_url + f"v1/masters/department/web/{company_id_valid}/get-departments-list",headers=user_valid_header)
    if get_valid_user.status_code == 200:
        print(f"\033[1;92m✅ TEST PASSED...! : Test Case ID - 010 \033[0m") 
    else:
        print(f"\033[1;91m❌ TEST FAILED...! : Test Case ID - 010 : Error - \033[0m") 
        failed_count+=1








# 11 : Get Department list with unauthorized user token : doubts


print("\033[1;34m GET DEPARTMENT LIST unauthorized user token \033[0m")



user_privil_payload = {
    "loginId":"testreport",
    "password":"Smm@1234"
}
   
privilege_user = requests.post(login_url,json=user_privil_payload)
if privilege_user.status_code == 200:
    print("logined")
    comp_json=privilege_user.json()
    comp_id=comp_json['company']['id']
    rest_id=comp_json['restaurant']['id']
    token_privl=comp_json.get('token',{}).get('token')
    header_privil = {
        "Authorization": f"Bearer {token_privl}",
        "Content-Type": "application/json"
    }

    get_url_privil=requests.get(base_url + f"api/v1/dashboard/orders/web/{comp_id}/{rest_id}/get-order-progress",headers=header_privil)
    if get_url_privil.status_code == 200:
        # privil_json=get_url_privil.json()   
        # print("Response JSON : ",json.dumps(privil_json,indent=4))

        print(f"\033[1;91m❌ TEST FAILED...! : Test Case ID - 011 : Error - \033[0m",get_url_privil.text) 
        failed_count+=1
    else:
        print(f"\033[1;92m✅ TEST PASSED...! : Test Case ID - 011 ..........\033[0m") 
else:

    print("login Failed")






# user_privil_payload = {
#     "loginId": "testreport",
#     "password": "Smm@1234"
# }

# privilege_user = requests.post(login_url, json=user_privil_payload)
# if privilege_user.status_code == 200:
#     print("logined")
#     comp_json = privilege_user.json()
#     comp_id = comp_json['company']['id']
#     rest_id = comp_json['restaurant']['id']
#     token_privl = comp_json.get('token', {}).get('token')

#     header_privil = {
#         "Authorization": f"Bearer {token_privl}",
#         "Content-Type": "application/json"
#     }

#     get_url_privil = requests.get(
#         base_url + f"v1/dashboard/orders/web/{comp_id}/{rest_id}/get-order-progress",
#         headers=header_privil
#     )

#     print("Status Code:", get_url_privil.status_code)
#     print("Content-Type:", get_url_privil.headers.get("Content-Type"))
#     # print("Response Body (truncated):", get_url_privil.text[:200])

#     if "application/json" in get_url_privil.headers.get("Content-Type", ""):
#         print(f"\033[1;91m❌ TEST FAILED...! : Test Case ID - 011 : Unauthorized user still received JSON\033[0m")
#         failed_count += 1
#     else:
#         print("❌ Response is not JSON (probably HTML login page)")
#         print(f"\033[1;92m✅ TEST PASSED...! : Test Case ID - 011 (Unauthorized user blocked)\033[0m")

# else:
#     print("login Failed")







# 12 : Get Department with after session already terminated :


print("\033[1;34m Get Department with after session already terminated\033[0m")

response_login4 = requests.post(login_url, json=login_payload)
if response_login4.status_code != 200:
    print("Login failed")
    exit()
else:
    response_json4=response_login4.json()
    token_session= response_json4.get('token',{}).get('token')
#    print(f"Token obtained: {token_session}")
    headers4 = {
        "Authorization": f"Bearer {token_session}",
        "Content-Type": "application/json"
    }

    response4 = requests.put(logout_url, headers=headers4)
    # print("Status code:", response4.status_code)
    # print("Response body:", response4.text)

    # print("-" * 50)

    response4 = requests.get(Get_url, headers=headers4)

    if response4.status_code != 200:
        # print("\033[92m✅ Token expired or session already terminated .\033[0m")
        print(f"\033[1;92m✅ TEST PASSED...! : Test Case ID - 012 \033[0m") 

    elif response4.status_code == 200:
        failed_count+=1
        print(f"\033[91m❌ TEST FAILED...! : Test Case ID - 012 : Error -  Session expired. \033[0m") 
    else:
        print("\033[91m❌ Unexpected response.\033[0m")

    # print("Status code:", response4.status_code)
    # print("Response body:", response4.text or "(empty)")



 


# 13 : 