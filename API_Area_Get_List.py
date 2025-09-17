
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

print("\033[1;34m GET AREA LIST  TESTCASE! Document ID: \033[0m")


login_payload = {
    "loginId":"ZolvQAAdmin",
    "password":"Smm@1234"
}



# 1 : Get Area  : Get Area list with valid company ID :


print("\033[1;34m Get Area List with valid company ID \033[0m")


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
    header_dep = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    Get_url=base_url + f"api/v1/masters/area/web/{company_id}/get-area-list?page=1&size=10&sort=1&name=&buildingId=&floorId=&moduleGroupId=&ignorePaging=false"
    response_get_dep=requests.get(Get_url,headers=header_dep)
    if response_get_dep.status_code == 200:
        get_dep_json = response_get_dep.json()
        # print("Response JSON : ",json.dumps(get_dep_json,indent=4))
        print("\033[1;92m✅ Test Case ID - 001   :  TEST PASSED...! \033[0m")   
    else:
        failed_count+=1

        print(f"\033[1;91m❌ Test Case ID - 001   :  Invalid Company Id  : TEST FAILED...! \033[0m") # login failed so test passed

        







# 2 : Get Area list with invalid company ID :


    print("\033[1;34m Get Area List with invalid company ID \033[0m")

    invalid_company_id="68709372293ae6389032a0588"

    # print(" Login successful")
  
    Get_url_invalid_company=base_url + f"api/v1/masters/area/web/{invalid_company_id}/get-area-list?page=1&size=10&sort=1&name=&buildingId=&floorId=&moduleGroupId=&ignorePaging=false"
    response_get_dep=requests.get(Get_url_invalid_company,headers=header_dep)
    if response_get_dep.status_code == 200:
        get_dep_json = response_get_dep.json()
        failed_count+=1
        print("\033[1;91m❌ Test Case ID - 002   :  Invalid Company Id :  TEST FAILED...!\033[0m")   
    else:
        print(f"\033[1;92m✅ Test Case ID - 002   :  TEST PASSED...! \033[0m") # login failed so test passed
        # print(response_get_dep.status_code)









# 3 :  Get Area list with  Invalid API end point : 


    print("\033[1;34m Get Area List Invalid API end point \033[0m")

    invalid_api_url = base_url + f"api/v1/masters/area/web/{invalid_company_id}/get-area-list?page=1&size=10&sort=1&name=&buildingId=&floorId=&moduleGroupId=&ignorePaging=false/invalid" 

    response_invalid_APi = requests.get(invalid_api_url,headers=header_dep)
    # print(f"Status Code: {response_login.status_code}")

    # Check if response is successful or has a response code
    if response_invalid_APi.status_code == 200:
        print(response_login.text,"Login with Invalid API endpoint")
        failed_count+=1
        print("\033[91m❌ Test Case ID - 003   :  Error - Invalid API endpoint :  TEST FAILED...!\033[0m")
    else:
        print("\033[1;92m✅ Test Case ID - 003   :  TEST PASSED...!\033[0m")
      













# 5 :  Get Area list with invalid HTTP method : 

    print("\033[1;34m Get Area List with Invalid HTTP Method \033[0m")


    # print("Response JSON : ",json.dumps(unauth_json,indent=4))
    response_invalid_method = requests.put(Get_url,header_dep)
    if response_invalid_method.status_code != 200:
        # print("\033[1;92mTest for invalid HTTP method passed!\033[0m",response_invalid_method.status_code)
        print("\033[1;92m✅ Test Case ID - 005   :  TEST PASSED...!\033[0m")
    else:
        failed_count+=1
        print("\033[1;91m❌ Test Case ID -  005   :  Error - API should only allow PUT for login :  TEST FAILED...!\033[0m")







# 6 : Get Area with Empty token : 
    Empty_token=""
    header_Empty = {
        "Authorization": f"Bearer {Empty_token}",
        "Content-Type": "application/json"
    }
    print("\033[1;34m Get Area List with Empty token \033[0m")


    response_empty_token = requests.get(Get_url,header_Empty)
    if response_empty_token.status_code == 200:
        failed_count+=1
        empty_json=response_empty_token.json()
        # print("Response JSON : ",json.dumps(empty_json,indent=4))
        print("\033[1;91m❌ Test Case ID -  006   :  Empty Token :  TEST FAILED...!\033[0m")
    else:
        print("\033[1;92m✅ Test Case ID - 006   :  TEST PASSED...!\033[0m")








# 7 : Get Area List with invalid token format : 

    print("\033[1;34m Get Area List with invalid token format \033[0m")

    invalid_token = "@1234eas%%%%%77&&&&&77"
    header_invalid_token = {
        "Authorization": f"Bearer {invalid_token}",
        "Content-Type": "application/json"
    }
    response_get_dep=requests.get(Get_url,headers=header_invalid_token)
    if response_get_dep.status_code != 200:
        print("\033[1;92m✅ Test Case ID - 007   :  TEST PASSED...!\033[0m")   
    else:
        failed_count+=1

        print(f"\033[1;91m❌ Test Case ID - 007   :  Invalid Token Format :  TEST FAILED...!\033[0m") # login failed so test passed

        











# 8 :  Get Area List with Unexpected parameter values for valid params :

    print("\033[1;34m Get Area List with  Invalid parameter values  \033[0m")

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

    unexp_para_url=f"https://qa-admin.zolv.health/api/v1/masters/area/web/{company_id}/get-area-list?"
    response_invalidparams = requests.get(unexp_para_url,params=unexp_params,headers=header_dep)
    if response_invalidparams.status_code == 200:
        invalid_json = response_invalidparams.json()
        # print("Response JSON : ",json.dumps(invalid_json,indent=4))
        token1= invalid_json.get('token',{}).get('token')
        print(f"\033[1;91m❌ Test Case ID - 008   :  Error - Un-Expected Field Format :  TEST FAILED...!\033[0m") # login success so test failed becoz in oms logged with oms in other 3 credentials kds,go,testoms
        failed_count+=1


    else:
        print(f"\033[1;92m✅ Test Case ID - 008   :  TEST PASSED...!\033[0m") 






# 9 : Get Area list with  Valid parameter values :

print("\033[1;34m Get Area with  Valid parameter values  \033[0m")

valid_params = {
        "page": 1,                  # negative page number (invalid)
        "ignorePaging":False,
        "size": 2,          # not expected by API
        "name":"TestDep",
        "sort":-1,
        "isActive":True
        # "search": "f",   

    }


valid_para_url=f"https://qa-admin.zolv.health/api/v1/masters/area/web/{company_id}/get-area-list?"
response_validparams = requests.get(Get_url,params=valid_params,headers=header_dep)
if response_validparams.status_code == 200:
    valid_json = response_validparams.json()
    # print("Response JSON : ",json.dumps(valid_json,indent=4))
    token1= valid_json.get('token',{}).get('token')
    print(f"\033[1;92m✅ Test Case ID - 009   :  TEST PASSED...!\033[0m") 
    response_valid_logout = requests.put(logout_url,headers=header_dep) 
    if response_valid_logout.status_code == 200:
        response_valid_logout.text
        # print("Logout Successfully ")
    else:
        response_valid_logout.text
        # print("Logout Failed")
else:
    print(f"\033[1;91m❌ Test Case ID - 009   :  Error - Invalid Input Parameter :  TEST FAILED...!\033[0m")










# # 10 : get Area list with Unauthorized User privilege  :

# print("\033[1;34m Get Area Unauthorized User privilege  \033[0m")
# count=0
# Test_case_id=0+9
# user_payload = [
#     {"loginId":"AutotestOMS",  "password":"Smm@1234"},
#     {"loginId":"AutotestKDS",  "password":"Smm@1234"},
#     {"loginId":"AutotestZolvGo",  "password":"Smm@1234"}

# ]
# for user in user_payload:
#     Test_case_id+=1
#     loginid=user["loginId"]
#     pwd=user["password"]

#     user_login = requests.post(login_url,json={"loginId":loginid,"password":pwd})
#     if user_login.status_code != 200:
#         print(f"\033[1;91m❌ TEST FAILED...! : Test Case ID - 0{Test_case_id} : Error - \033[0m") 
#     else:
#         print(f"\033[1;91m❌ TEST FAILED...! : Test Case ID - 0{Test_case_id} : Error - \033[0m") 
#         user_privil_json = user_login.json()
#         print("Response JSON : ",json.dumps(user_privil_json,indent=4))
#         user_valid_token= user_privil_json.get('token',{}).get('token')
#         company_id_valid=user_privil_json['company']['id']
#         print(" login Success..")
#         user_valid_header = {
#             "Authorization": f"Bearer {user_valid_token}",
#             "Content-Type": "application/json"
#         }
#         get_valid_user=requests.get(Get_url,headers=user_valid_header)
#         if get_valid_user.status_code == 200:
#             print(f"\033[1;91m❌ TEST FAILED...! : Test Case ID - 010 : Error - \033[0m") 
#         else:
#             print(f"\033[1;92m✅ TEST PASSED...! : Test Case ID - 0{Test_case_id} \033[0m") 
#             count+=1



# if count in [0,3]:
#     failed_count+=1
#     print(failed_count)







# 10 : get Area list with OMS User privilege  :

print("\033[1;34m Get Area OMS User privilege  \033[0m")
user_OMS = {"loginId":"AutotestOMS",  "password":"Smm@1234"}

user_OMS_login = requests.post(login_url,json=user_OMS)
if user_OMS_login.status_code != 200:
    print(f"\033[1;92m✅ Test Case ID - 010   :  TEST PASSED...!\033[0m") 
else:
    print(f"\033[1;91m❌ Test Case ID - 010   :  TEST FAILED...!  : Error - OMS User privilege\033[0m")

    user_OMS_json = user_OMS_login.json()
    # print("Response JSON : ",json.dumps(user_OMS_json,indent=4))
    OMSuser_valid_token= user_OMS_json.get('token',{}).get('token')
    # print(" login Success..")
    user_OMS_header = {
        "Authorization": f"Bearer {OMSuser_valid_token}",
        "Content-Type": "application/json"
    }
    get_OMS_user=requests.get(Get_url,headers=user_OMS_header)
    if get_OMS_user.status_code == 200:
        print(f"\033[1;91m❌ Test Case ID - 010     :  Error - OMS Privileged User :  TEST FAILED...!\033[0m") 
    else:
        print(f"\033[1;92m✅ Test Case ID - 010     :  TEST PASSED...!\033[0m") 










# 11 : get Area list with KDS User privilege  :

print("\033[1;34m Get Area KDS User privilege  \033[0m")

user_KDS_payload = {"loginId":"AutotestKDS",  "password":"Smm@1234"},

user_KDS_login = requests.post(login_url,json=user_KDS_payload)
if user_KDS_login.status_code != 200:
    print(f"\033[1;92m✅ Test Case ID - 011   :  TEST PASSED...!\033[0m") 
else:
    print(f"\033[1;91m❌ Test Case ID - 011   :  Error - KDS User privilege :  TEST FAILED...!\033[0m")

    user_KDS_json = user_KDS_login.json()
    # print("Response JSON : ",json.dumps(user_privil_json,indent=4))
    user_KDS_token= user_KDS_json.get('token',{}).get('token')
    # print(" login Success..")
    user_KDS_header = {
        "Authorization": f"Bearer {user_KDS_token}",
        "Content-Type": "application/json"
    }
    get_KDS_user=requests.get(Get_url,headers=user_KDS_header)
    if get_KDS_user.status_code == 200:
        print(f"\033[1;91m❌ Test Case ID - 011     :  Error - KDS Privileged User :  TEST FAILED...!\033[0m") 
    else:
        print(f"\033[1;92m✅ Test Case ID - 011     :  TEST PASSED...!\033[0m") 









# 12 : get Area list with ZOLVGO User privilege  :

print("\033[1;34m Get Area ZOLVGO User privilege  \033[0m")

user_G0_payload = {"loginId":"AutotestZolvGo",  "password":"Smm@1234"}

user_Go_login = requests.post(login_url,json=user_G0_payload)
if user_Go_login.status_code != 200:
    print(f"\033[1;92m✅ Test Case ID - 012   :  TEST PASSED...!\033[0m") 
else:
    print(f"\033[1;91m❌ Test Case ID - 012 :  Error - ZOLVGO User privilege :  TEST FAILED...!\033[0m")

    user_Go_json = user_Go_login.json()
    # print("Response JSON : ",json.dumps(user_Go_json,indent=4))
    user_Go_token= user_Go_json.get('token',{}).get('token')
    # print(" login Success..")
    user_Go_header = {
        "Authorization": f"Bearer {user_Go_token}",
        "Content-Type": "application/json"
    }
    get_Go_user=requests.get(Get_url,headers=user_Go_header)
    if get_Go_user.status_code == 200:
        print(f"\033[1;91m❌ Test Case ID - 012    :  Error - ZolvGo Privileged User :  TEST FAILED...!\033[0m") 
    else:
        print(f"\033[1;92m✅ Test Case ID - 012    :  TEST PASSED...!\033[0m") 









# 13 : Get Area with after session already terminated :


print("\033[1;34m Get Area with after session already terminated\033[0m")

response_login_session = requests.post(login_url, json=login_payload)
if response_login_session.status_code != 200:
    print("Login failed")
else:
    response_session_json=response_login_session.json()
    token_session= response_session_json.get('token',{}).get('token')
#    print(f"Token obtained: {token_session}")
    headers_session = {
        "Authorization": f"Bearer {token_session}",
        "Content-Type": "application/json"
    }

    response_logout = requests.put(logout_url, headers=headers_session)
    # print("Status code:", response_login_session.status_code)
    # print("Response body:", response_login_session.text)

    # print("-" * 50)
    relogin=requests.post(login_url, json=login_payload)
    if relogin.status_code != 200:
        print("Login failed")
    else:
        relogin_json=relogin.json()
        response_afterlogin_session = requests.get(Get_url, headers=headers_session)

        if response_afterlogin_session.status_code != 200:
            # print("\033[92m✅ Token expired or session already terminated .\033[0m")
            print(f"\033[1;92m✅Test Case ID - 013    :  TEST PASSED...!\033[0m") 

        elif response_afterlogin_session.status_code == 200:
            failed_count+=1
            print(f"\033[91m❌ Test Case ID - 013    :  Error -  Session expired :  TEST FAILED...!\033[0m") 
        else:
            print("\033[91m❌ Unexpected response.\033[0m")

        # print("Status code:", response_afterlogin_session.status_code)
        # print("Response body:", response_afterlogin_session.text or "(empty)")








# 14 : Get Area with disabled module ( eg .disabled the module F&B ):

print("\033[1;34m Get Area with disabled module\033[0m")

diable_module_login=requests.post(login_url,json=login_payload)
if diable_module_login.status_code != 200:
    print("Login Failed")
else:
    disable_module_json=diable_module_login.json()
    # print("login success")
    company_id=disable_module_json['company']['id']
    token_disable = disable_module_json["token"]["token"]
    header_disable = {
        "Authorization": f"Bearer {token_disable}",
        "Content-Type": "application/json"
    }
    module_get_list=requests.get(base_url + f"api/v1/company/web/get-module-list/{company_id}",headers=header_disable)
    if module_get_list.status_code == 200:
        module_get_json=module_get_list.json()
        # print("Module Listed Successfully")
        # print("Response JSON : ",json.dumps(module_get_json,indent=4))
       
        update_payload={
            "modules": [
        {
        "id": "686f510c6e7e978b9132a03c",
        "enabled": False
        },
        {
        "id": "686f510c6e7e978b9132a03d",
        "enabled": False
        },
        {
        "id": "686f510c6e7e978b9132a043",
        "enabled": False
        },
        {
        "id": "686f510c6e7e978b9132a044",
        "enabled": False
        },
        {
        "id": "686f510c6e7e978b9132a045",
        "enabled": False
        }
        ]
        }
        module_update=requests.patch(base_url + f"api/v1/company/web/update-configuration/{company_id}",json=update_payload,headers=header_disable)
        if module_update.status_code == 200:
            # print("Update Success")
            response_get_area=requests.get(Get_url,headers=header_disable)
            if response_get_area.status_code == 200:
                get_area_json = response_get_area.json()
                # print("Response Get Area  : ",json.dumps(get_area_json,indent=4))
                print(f"\033[1;91m❌ Test Case ID - 012    :  Error - Get Area with disabled module :  TEST FAILED...!\033[0m") 
                failed_count+=1
                update_payload={
                    "modules": [
                {
                "id": "686f510c6e7e978b9132a03c",
                "enabled": True
                },
                {
                "id": "686f510c6e7e978b9132a03d",
                "enabled": False
                },
                {
                "id": "686f510c6e7e978b9132a043",
                "enabled": False
                },
                {
                "id": "686f510c6e7e978b9132a044",
                "enabled": False
                },
                {
                "id": "686f510c6e7e978b9132a045",
                "enabled": False
                }
                ]
                }
                module_update=requests.patch(base_url + f"api/v1/company/web/update-configuration/{company_id}",json=update_payload,headers=header_disable)


            else: 
                print(f"\033[1;92m✅Test Case ID - 013    :  TEST PASSED...!\033[0m") 
 
        else: 
            print("Update Failed")

    else:
        print("Module Listed Failed",module_get_list.status_code)








# 4 : Get Area list with Unexpected Parameters :

# 4.1 : Get Area list with Unexpected Parameters in Page Params:
print("\033[1;34m Get Area List with Invalid Parameters \033[0m")

print("\033[1;34m Get Area List with Invalid Parameters in Page Params\033[0m")
count=0
invalid_para_url=None
invalid_params=None
test_cases = [
        (22, "Integer Value"),                     
        ("@%&#+-+=54a%", "Special Characters"),     
        (None, "Null"),                            
        (" abc123", "Leading Space"),          
        ("-5", "Negative value"),           
        ("", "Empty String"),                       
        ("   ", "Only Spaces"),                    
        ("testname"+ "a" * 1000, "large input values"),         
        ("test", "String"),
    ]
test_cases_boolean = [
        (22, "Integer Value"),                     
        ("@%&#+-+=54a%", "Special Characters"),     
        (None, "Null"),                            
        (" abc123", "Leading Space"),          
        ("-5", "Negative value"),           
        ("", "Empty String"),                       
        ("   ", "Only Spaces"),                    
        ("testname"+ "a" * 1000, "large input values"),         
        ("test", "String"),
        (True,"Boolean")              
    ]
def invalidparams(invalid_para_url,invalid_params,test_cases,header_disable,count):
    
   
    for test,description in test_cases_boolean:
        invalid_params = {
        "page": test,                  
        "ignorePaging":False,
        "size": 2,          
        "name":"TestDep",
        "sort":-1,
        "isActive":True
        # "search": "f",   

    }

        # invalid_params = {
        #     "departmentId": "abc123",   
        #     "page": -5,                  
        #     "limit": "twenty",          
        #     "unknownParam": "test",          
        #     "ignorePaging":"abcd",
        #     "name":"xyz",
        #     "sort":"a",
        #     "moduleId":"a"
        # }

     
        invalid_para_url=f"https://qa-admin.zolv.health/api/v1/masters/area/web/{company_id}/get-area-list?"
        response_invalidparams = requests.get(invalid_para_url,invalid_params,headers=header_disable)
        if response_invalidparams.status_code == 200:
            invalid_json = response_invalidparams.json()
            # print(invalid_para_url)
            # print("Response JSON : ",json.dumps(invalid_json,indent=4))
            token1= invalid_json.get('token',{}).get('token')
            count+=1
            print(f"\033[91m❌ Test Case ID - 004   : {description}  :  Error - Invalid Input Format :  TEST FAILED...!\033[0m") # login success so test failed becoz in oms logged with oms in other 3 credentials kds,go,testoms

        
        else:
            print(f"\033[1;92m✅ Test Case ID - 004   : {description}  :  TEST PASSED...!\033[0m") 



   
    
invalidparams(invalid_para_url,invalid_params,test_cases,header_disable,count)

if count in [0,10]:
    failed_count+=1
    # print(failed_count)

# 4.2 :Get Area List with Invalid Parameters in ignorePaging  Params :
count=0
for test,description in test_cases:
        invalid_params = {
        "page": 1,                  
        "ignorePaging":test,
        "size": 2,          
        "name":"TestDep",
        "sort":-1,
        "isActive":True
        # "search": "f",   

}
print("\033[1;34m Get Area List with Invalid Parameters in ignorePaging  Params\033[0m")

invalidparams(invalid_para_url,invalid_params,test_cases,header_disable,count)
if count in [0,10]:
    failed_count+=1



# 4.3 :Get Area List with Invalid Parameters in size  Params :

for test,description in test_cases_boolean:
        invalid_params = {
        "page": 1,                  
        "ignorePaging":False,
        "size": test,          
        "name":"TestDep",
        "sort":-1,
        "isActive":True
        # "search": "f",   

}
print("\033[1;34m Get Area List with Invalid Parameters in Size  Params\033[0m")

invalidparams(invalid_para_url,invalid_params,test_cases,header_disable,count)
if count in [0,10]:
    failed_count+=1




# 4.4  :Get Area List with Invalid Parameters in Name  Params :

for test,description in test_cases_boolean:
        invalid_params = {
        "page": 1,                  
        "ignorePaging":False,
        "size": 2,          
        "name":test,
        "sort":-1,
        "isActive":True
        # "search": "f",   

}
print("\033[1;34m Get Area List with Invalid Parameters in Name  Params\033[0m")

invalidparams(invalid_para_url,invalid_params,test_cases,header_disable,count)
if count in [0,10]:
    failed_count+=1




# 4.5  :Get Area List with Invalid Parameters in Sort  Params :

for test,description in test_cases_boolean:
        invalid_params = {
        "page": 1,                  
        "ignorePaging":False,
        "size": 2,          
        "name":"TestDep",
        "sort":test,
        "isActive":True
        # "search": "f",   

}
print("\033[1;34m Get Area List with Invalid Parameters in Sort  Params\033[0m")

invalidparams(invalid_para_url,invalid_params,test_cases,header_disable,count)
if count in [0,10]:
    failed_count+=1






# 4.6  :Get Area List with Invalid Parameters in Isactive  Params :

for test,description in test_cases:
        invalid_params = {
        "page": 1,                  
        "ignorePaging":False,
        "size": 2,          
        "name":"TestDep",
        "sort":-1,
        "isActive":test
        # "search": "f",   

}
print("\033[1;34m Get Area List with Invalid Parameters in Isactive  Params\033[0m")

invalidparams(invalid_para_url,invalid_params,test_cases,header_disable,count)

if count in [0,10]:
    failed_count+=1





# 4.7  :Get Area List with Invalid Parameters in Search  Params :

for test,description in test_cases:
        invalid_params = {
        # "page": 1,                  
        # "ignorePaging":False,
        # "size": 2,          
        # "name":"TestDep",
        # "sort":-1,
        # "isActive":test
        "search": test,   

}
print("\033[1;34m Get Area List with Invalid Parameters in Search  Params\033[0m")

invalidparams(invalid_para_url,invalid_params,test_cases,header_disable,count)

if count in [0,10]:
    failed_count+=1



#    Logout : 

response_logout = requests.put(logout_url,headers=header_disable) 
if response_logout.status_code == 200:
    logout_json = response_logout.json()
    # print("Response JSON:", json.dumps(logout_json, indent=4))
    # print(f"Token (Logout): {token}")

else:
    failed_count+=1
    # print(f"Logout failed with status code {response_logout.status_code}")
    # print("Response:", response_logout.json())









print(f"\033[1;34mTotal Test Failed  : {failed_count}/{total_count}\033[0m")

if failed_count == 0:
    print("\033[92m ✅ All TEST PASSED \033[0m")

