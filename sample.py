
import requests
import time
import json
import random
import urllib.parse

import base64
  


# failed_count=0
# total_count=18

# base_url= "https://qa-admin.zolv.health/"
# login_url= "https://qa-admin.zolv.health/api/v1/user/login"
# logout_url="https://qa-admin.zolv.health/api/v1/user/logout"



# # 1 : Login TestCase : Login with valid Login Credentials

# print("\033[1;34m ADMIN LOGIN TESTCASE! Document ID: TP_001\033[0m")
# # print("\033[1;34m Login with valid Login Credentials! Document ID: TP_001\033[0m")


# login_payload = {
#         "loginId":"AutotestAdmin",
#         "password":"Smm@1234"
# }

  
# response_login = requests.post(login_url,json=login_payload)
# if response_login.status_code != 200:
#     failed_count+=1
#     # print(f"\033[91m❌ Login failed with status code {response_login.text}\033[0m")
#     print(f"\033[91m❌ TEST FAILED...! : Test Case ID - 001                                                      : Error - Invalid Credentials \033[0m") # login failed so test passed
# else:
#     response_json = response_login.json()
#     name=response_json.get('name')
#     # print("...",response_login.text)
#     valid_token= response_json.get('token',{}).get('token')
#     company_id=response_json['company']['id']

#     headers= {
#         "Authorization": f"Bearer {valid_token}",
#         "Content-Type": "application/json"
#     }
#     # print(f"\033[91m✅ Login successful! Welcome, {loginId} | Name: {name} | Status: {response_login.status_code}\033[0m",{"loginId":loginId,"password":pwd})
#     # print("Response JSON : ",json.dumps(response_json,indent=4))
#     print(f"\033[92m✅ Test Case ID - 001 : Login                                                                  : TEST PASSED...! \033[0m") # login success so test failed becoz in oms logged with oms in other 3 credentials kds,go,testoms


   










# # ***************************************Create Area ****************************************************************** 



# # 2 : Create : Area : Valid name Field :



#     create_parentarea_payload = {
#         "name": "AreaTestCase",
#         "code":606,
#         "areaType": "parent",
#         "parentAreaId":"", #if choose child area in area type, parentarea id field is mandatory .
#         "buildingId": "68709372293ae6389032a058",
#         "floorId": "68709372293ae6389032a05a",
#         "isActive": True,
#         "moduleGroupId": "68709372293ae6389032a05b",
#         "paymentModes": [
#               {
#                   "name": "paymentGateway",
#                   "enabled": True
#               },
#               {
#                   "name": "payOnDelivery",
#                   "enabled": True
#               },
#               # // {
#               # //     "name": "employeeCredit",
#               # //     "enabled": false
#               # // },
#               {
#                   "name": "roomCredit",
#                   "enabled": True
#               }
#           ],
#         "deliveryModes":[
#               {
#                   "name": "roomDelivery",
#                   "enabled": True
#               },
#               {
#                   "name": "takeAway",
#                   "enabled": True
#               },
#               {
#                   "name": "dineIn",
#                   "enabled": True
#               }
#           ],
#         "preOrderStatus": False
        
#     }
#     create_parentarea = requests.post(base_url + f"api/v1/masters/area/web/{company_id}/create-area",json=create_parentarea_payload,headers=headers)
#     if create_parentarea.status_code == 200:
#        createparent_json=create_parentarea.json()
#        area_id = createparent_json['id']

#     #   print("Parent Area Created Successfully..!",create_parentarea.text)
#     #    print("Response JSON : ",json.dumps(createparent_json,indent=4))
#        print(f"\033[92m✅ Test Case ID - 002 : Area Creation (Parent)                                                 : TEST PASSED...!  \033[0m")
#     else:
#        failed_count+=1
       
#        print(f"\033[91m❌ Test Case ID - 002 : Area Creation (Parent)                                                 : TEST FAILED...! : Invalid data or missing fields  \033[0m")
 
#     #    print("Failed Creation.",create_parentarea.text) 







# # 3 : Create : Area : integer name input :



#     create_int_parentarea_payload = {
#         "name": 44,
#         "code":656,
#         "areaType": "parent",
#         "parentAreaId":"", #if choose child area in area type, parentarea id field is mandatory .
#         "buildingId": "68709372293ae6389032a058",
#         "floorId": "68709372293ae6389032a05a",
#         "isActive": True,
#         "moduleGroupId": "68709372293ae6389032a05b",
#         "paymentModes": [
#               {
#                   "name": "paymentGateway",
#                   "enabled": True
#               },
#               {
#                   "name": "payOnDelivery",
#                   "enabled": True
#               },
#               # // {
#               # //     "name": "employeeCredit",
#               # //     "enabled": false
#               # // },
#               {
#                   "name": "roomCredit",
#                   "enabled": True
#               }
#           ],
#         "deliveryModes":[
#               {
#                   "name": "roomDelivery",
#                   "enabled": True
#               },
#               {
#                   "name": "takeAway",
#                   "enabled": True
#               },
#               {
#                   "name": "dineIn",
#                   "enabled": True
#               }
#           ],
#         "preOrderStatus": False
        
#     }
#     create_int_parentarea = requests.post(base_url + f"api/v1/masters/area/web/{company_id}/create-area",json=create_int_parentarea_payload,headers=headers)
#     if create_int_parentarea.status_code != 200:
#        #    print("Failed Creation.",create_int_parentarea.text) 
#        print(f"\033[92m✅ Test Case ID - 003 : Area Creation (Parent) with Integer value                              : TEST PASSED...!  \033[0m")
#     else:
#        failed_count+=1
#        create_int_parent_json=create_int_parentarea.json()
#        print(f"\033[91m❌ Test Case ID - 003 : Area Creation (Parent) Integer value                                   : TEST FAILED...! : Invalid data or missing fields  \033[0m")
#   #   print("Parent Area Created Successfully..!",create_int_parentarea.text)
#     #    print("Response JSON : ",json.dumps(create_int_parent_json,indent=4))










# # 4 : Create : Area : name with Special Character input :



#     create_specialcharacters_parentarea_payload = {
#         "name":"+@1234&%%$$***",
#         "code":546,
#         "areaType": "parent",
#         "parentAreaId":"", #if choose child area in area type, parentarea id field is mandatory .
#         "buildingId": "68709372293ae6389032a058",
#         "floorId": "68709372293ae6389032a05a",
#         "isActive": True,
#         "moduleGroupId": "68709372293ae6389032a05b",
#         "paymentModes": [
#               {
#                   "name": "paymentGateway",
#                   "enabled": True
#               },
#               {
#                   "name": "payOnDelivery",
#                   "enabled": True
#               },
#               # // {
#               # //     "name": "employeeCredit",
#               # //     "enabled": false
#               # // },
#               {
#                   "name": "roomCredit",
#                   "enabled": True
#               }
#           ],
#         "deliveryModes":[
#               {
#                   "name": "roomDelivery",
#                   "enabled": True
#               },
#               {
#                   "name": "takeAway",
#                   "enabled": True
#               },
#               {
#                   "name": "dineIn",
#                   "enabled": True
#               }
#           ],
#         "preOrderStatus": False
        
#     }
#     create_special_parentarea = requests.post(base_url + f"api/v1/masters/area/web/{company_id}/create-area",json=create_specialcharacters_parentarea_payload,headers=headers)
#     if create_special_parentarea.status_code != 200:
#        #    print("Failed Creation.",create_special_parentarea.text) 
#        print(f"\033[92m✅ Test Case ID - 004 : Area Creation (Parent) with Special Character                          : TEST PASSED...!  \033[0m")
#     else:
#        failed_count+=1
#        create_special_parent_json=create_special_parentarea.json()
#        print(f"\033[91m❌ Test Case ID - 004 : Area Creation (Parent) with Special Character                          : TEST FAILED...! : Invalid data or missing fields  \033[0m")
#   #   print("Parent Area Created Successfully..!",create_special_parentarea.text)
#     #    print("Response JSON : ",json.dumps(create_special_parent_json,indent=4))











# # 5 : Create : Area : name with null value :



#     create_null_parentarea_payload = {
#         "name": " ",
#         "code":86,
#         "areaType": "parent",
#         "parentAreaId":"", #if choose child area in area type, parentarea id field is mandatory .
#         "buildingId": "68709372293ae6389032a058",
#         "floorId": "68709372293ae6389032a05a",
#         "isActive": True,
#         "moduleGroupId": "68709372293ae6389032a05b",
#         "paymentModes": [
#               {
#                   "name": "paymentGateway",
#                   "enabled": True
#               },
#               {
#                   "name": "payOnDelivery",
#                   "enabled": True
#               },
#               # // {
#               # //     "name": "employeeCredit",
#               # //     "enabled": false
#               # // },
#               {
#                   "name": "roomCredit",
#                   "enabled": True
#               }
#           ],
#         "deliveryModes":[
#               {
#                   "name": "roomDelivery",
#                   "enabled": True
#               },
#               {
#                   "name": "takeAway",
#                   "enabled": True
#               },
#               {
#                   "name": "dineIn",
#                   "enabled": True
#               }
#           ],
#         "preOrderStatus": False
        
#     }
#     create_null_parentarea = requests.post(base_url + f"api/v1/masters/area/web/{company_id}/create-area",json=create_null_parentarea_payload,headers=headers)
#     if create_null_parentarea.status_code != 200:
#        #    print("Failed Creation.",create_null_parentarea.text) 
#        print(f"\033[92m✅ Test Case ID - 005 : Area Creation (Parent) with null value                                 : TEST PASSED...!  \033[0m")
#     else:
#        failed_count+=1
#        create_null_parent_json=create_null_parentarea.json()
#        print(f"\033[91m❌ Test Case ID - 005 : Area Creation (Parent) with null value                                 : TEST FAILED...! : Invalid data or missing fields  \033[0m")
#   #   print("Parent Area Created Successfully..!",create_null_parentarea.text)
#     #    print("Response JSON : ",json.dumps(create_null_parent_json,indent=4))










# # 6 : Create : Area : name with Boolean value :



#     create_boolean_parentarea_payload = {
#         "name": True,
#         "code":86,
#         "areaType": "parent",
#         "parentAreaId":"", #if choose child area in area type, parentarea id field is mandatory .
#         "buildingId": "68709372293ae6389032a058",
#         "floorId": "68709372293ae6389032a05a",
#         "isActive": True,
#         "moduleGroupId": "68709372293ae6389032a05b",
#         "paymentModes": [
#               {
#                   "name": "paymentGateway",
#                   "enabled": True
#               },
#               {
#                   "name": "payOnDelivery",
#                   "enabled": True
#               },
#               # // {
#               # //     "name": "employeeCredit",
#               # //     "enabled": false
#               # // },
#               {
#                   "name": "roomCredit",
#                   "enabled": True
#               }
#           ],
#         "deliveryModes":[
#               {
#                   "name": "roomDelivery",
#                   "enabled": True
#               },
#               {
#                   "name": "takeAway",
#                   "enabled": True
#               },
#               {
#                   "name": "dineIn",
#                   "enabled": True
#               }
#           ],
#         "preOrderStatus": False
        
#     }
#     create_boolean_parentarea = requests.post(base_url + f"api/v1/masters/area/web/{company_id}/create-area",json=create_boolean_parentarea_payload,headers=headers)
#     if create_boolean_parentarea.status_code != 200:
#        #    print("Failed Creation.",create_boolean_parentarea.text) 
#        print(f"\033[92m✅ Test Case ID - 006 : Area Creation (Parent) with Boolean value                              : TEST PASSED...!  \033[0m")
#     else:
#        failed_count+=1
#        create_boolean_parent_json=create_boolean_parentarea.json()
#        print(f"\033[91m❌ Test Case ID - 006 : Area Creation (Parent) with Boolean value                              : TEST FAILED...! : Invalid data or missing fields  \033[0m")
#   #   print("Parent Area Created Successfully..!",create_boolean_parentarea.text)
#     #    print("Response JSON : ",json.dumps(create_boolean_parent_json,indent=4))











# #  7 : Create : Area : name with leading (left-side) spaces from a string. :



#     create_lstrip_parentarea_payload = {
#         "name": "  strip",
#         "code":600,
#         "areaType": "parent",
#         "parentAreaId":"", #if choose child area in area type, parentarea id field is mandatory .
#         "buildingId": "68709372293ae6389032a058",
#         "floorId": "68709372293ae6389032a05a",
#         "isActive": True,
#         "moduleGroupId": "68709372293ae6389032a05b",
#         "paymentModes": [
#               {
#                   "name": "paymentGateway",
#                   "enabled": True
#               },
#               {
#                   "name": "payOnDelivery",
#                   "enabled": True
#               },
#               # // {
#               # //     "name": "employeeCredit",
#               # //     "enabled": false
#               # // },
#               {
#                   "name": "roomCredit",
#                   "enabled": True
#               }
#           ],
#         "deliveryModes":[
#               {
#                   "name": "roomDelivery",
#                   "enabled": True
#               },
#               {
#                   "name": "takeAway",
#                   "enabled": True
#               },
#               {
#                   "name": "dineIn",
#                   "enabled": True
#               }
#           ],
#         "preOrderStatus": False
        
#     }
#     create_lstrip_parentarea = requests.post(base_url + f"api/v1/masters/area/web/{company_id}/create-area",json=create_lstrip_parentarea_payload,headers=headers)
#     if create_lstrip_parentarea.status_code != 200:
#        #    print("Failed Creation.",create_lstrip_parentarea.text) 
#        print(f"\033[92m✅ Test Case ID - 007 : Area Creation (Parent) with leading (left-side) spaces from a string   : TEST PASSED...!  \033[0m")
#     else:
#        failed_count+=1
#        create_lstrip_parent_json=create_lstrip_parentarea.json()
#        print(f"\033[91m❌ Test Case ID - 007 : Area Creation (Parent) with leading (left-side) spaces from a string   : TEST FAILED...! : Invalid data or missing fields  \033[0m")
#   #   print("Parent Area Created Successfully..!",create_lstrip_parentarea.text)
#     #    print("Response JSON : ",json.dumps(create_lstrip_parent_json,indent=4))










    



# #  8 : Create : Area : name with trailing (right-side) spaces from a string :



#     create_rstrip_parentarea_payload = {
#         "name": "strip   ",
#         "code":700,
#         "areaType": "parent",
#         "parentAreaId":"", #if choose child area in area type, parentarea id field is mandatory .
#         "buildingId": "68709372293ae6389032a058",
#         "floorId": "68709372293ae6389032a05a",
#         "isActive": True,
#         "moduleGroupId": "68709372293ae6389032a05b",
#         "paymentModes": [
#               {
#                   "name": "paymentGateway",
#                   "enabled": True
#               },
#               {
#                   "name": "payOnDelivery",
#                   "enabled": True
#               },
#               # // {
#               # //     "name": "employeeCredit",
#               # //     "enabled": false
#               # // },
#               {
#                   "name": "roomCredit",
#                   "enabled": True
#               }
#           ],
#         "deliveryModes":[
#               {
#                   "name": "roomDelivery",
#                   "enabled": True
#               },
#               {
#                   "name": "takeAway",
#                   "enabled": True
#               },
#               {
#                   "name": "dineIn",
#                   "enabled": True
#               }
#           ],
#         "preOrderStatus": False
        
#     }
#     create_rstrip_parentarea = requests.post(base_url + f"api/v1/masters/area/web/{company_id}/create-area",json=create_rstrip_parentarea_payload,headers=headers)
#     if create_rstrip_parentarea.status_code != 200:
#        #    print("Failed Creation.",create_rstrip_parentarea.text) 
#        print(f"\033[92m✅ Test Case ID - 008 : Area Creation (Parent) with trailing (right-side) spaces from a string : TEST PASSED...!  \033[0m",create_rstrip_parentarea.text)
#     else:
#        failed_count+=1
#        create_rstrip_parent_json=create_rstrip_parentarea.json()
#        print(f"\033[91m❌ Test Case ID - 008 : Area Creation (Parent) with trailing (right-side) spaces from a string : TEST FAILED...! : Invalid data or missing fields  \033[0m")
#   #   print("Parent Area Created Successfully..!",create_rstrip_parentarea.text)
#     #    print("Response JSON : ",json.dumps(create_rstrip_parent_json,indent=4))






def to_bool(value):
    """Converts value into a strict boolean True/False."""
    if isinstance(value, bool):   # Already a boolean
        return value
    if isinstance(value, str): 
        if str in ["True","False","true","false"]:  # Strings like "true", "false", "1", "0"
           return value.strip().lower() in ("true", "1", "yes", "y", "t")
        

    if isinstance(value, (int, float)):  # Numbers: 1 → True, 0 → False
        return value == 1
    return False  # Anything else defaults to False

    # value=["True","False","true","false"]
    # if "True" or "true" or "False" or "false" in value:
    #     return value
    # return False







from Funtions import login_test,run_test_case
import requests
import json

    
failed_count = 0
test_case_id=0
base_url = "https://qa-admin.zolv.health/"
login_url= "https://qa-admin.zolv.health/api/v1/user/login"

login_payload = {
    "loginId": "ZolvQAAdmin",
    "password": "Smm@1234"
}


headers, failed_count, company_id = login_test(
    base_url,
    login_url,
    login_payload,
    test_case_id=test_case_id,
    failed_count=failed_count
)




# #  2:

base_payload = {
        "name": valid_name,
        "code": code,
        "areaType": areatype,
        "parentAreaId": parent_id, 
        "buildingId": building_id,
        "floorId": floor_id,
        "isActive": to_bool(isactive),   # ✅ converted boolean
        "moduleGroupId": modulegroup_id,
        "paymentModes": [
            {"name": paymentmode_name1, "enabled": to_bool(paymentMode1)},
            {"name": paymentmode_name2, "enabled": to_bool(paymentMode2)},
            {"name": paymentmode_name3, "enabled": to_bool(paymentMode3)},
        ],
        "deliveryModes": [
            {"name": delivery_mode_name1, "enabled": to_bool(delivery_mode1)},
            {"name": delivery_mode_name2, "enabled": to_bool(delivery_mode2)},
            {"name": delivery_mode_name3, "enabled": to_bool(delivery_mode3)},
        ],
        "preOrderStatus": to_bool(preorder)  # ✅ converted boolean
    }


# main.py


# Utili

# Example input values




def build_base_payload(
        valid_data, code, areatype, parent_id, building_id, floor_id, isactive,
        modulegroup_id, paymentmode_name1, paymentMode1, paymentmode_name2, paymentMode2, paymentmode_name3, paymentMode3,
        delivery_mode_name1, delivery_mode1, delivery_mode_name2, delivery_mode2,
        delivery_mode_name3, delivery_mode3, preorder):
    return {
        "name": valid_data,
        "code": code,
        "areaType": areatype,
        "parentAreaId": parent_id,
        "buildingId": building_id,
        "floorId": floor_id,
        "isActive": to_bool(isactive),
        "moduleGroupId": modulegroup_id,
        "paymentModes": [
            {"name": paymentmode_name1, "enabled": to_bool(paymentMode1)},
            {"name": paymentmode_name2, "enabled": to_bool(paymentMode2)},
            {"name": paymentmode_name3, "enabled": to_bool(paymentMode3)},
        ],
        "deliveryModes": [
            {"name": delivery_mode_name1, "enabled": to_bool(delivery_mode1)},
            {"name": delivery_mode_name2, "enabled": to_bool(delivery_mode2)},
            {"name": delivery_mode_name3, "enabled": to_bool(delivery_mode3)},
        ],
        "preOrderStatus": to_bool(preorder) 
    }

valid_data = {"name": "Test Area Modified"}

base_url = "https://qa-admin.zolv.health/"
company_id = company_id 
endpoint = f"api/v1/masters/area/web/{company_id}/create-area"
headers = headers
failed_count = 0
test_case_id = 1


base_payload = build_base_payload(
    valid_data, 33, "parent", "", "68709372293ae6389032a058",
    "68709372293ae6389032a05a",to_bool(True), "68709372293ae6389032a05b",
    "paymentGateway", to_bool(True),"payOnDelivery",to_bool(True), "roomCredit",to_bool(True),
    "roomDelivery",to_bool(True), "takeAway",to_bool(True), "dineIn",to_bool(True),to_bool(False),
    base_url, company_id, headers,failed_count
)

# Example override: change only "name"

# Run test
failed_count = run_test_case(
    base_payload, base_url, endpoint, company_id, headers, test_case_id, failed_count)

print(f"\nTotal failed test cases: {failed_count}")


