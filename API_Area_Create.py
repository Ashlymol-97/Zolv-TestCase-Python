

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
    print(f"\033[91m❌  Test Case ID - 001 : Login        : TEST FAILED...! :  Error - Invalid Credentials \033[0m") # login failed so test passed
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
    print(f"\033[92m✅ Test Case ID - 001 : Login          : TEST PASSED...! \033[0m") # login success so test failed becoz in oms logged with oms in other 3 credentials kds,go,testoms





    


# # 2 : Get Area Detailed List : 

# def get_area_list(base_url, company_id, headers):
#     print("...............")
#     get_response=requests.get(base_url + f"api/v1/masters/area/web/{company_id}/get-area-list?page=1&size=10&sort=1&name=&buildingId=&floorId=&moduleGroupId=&ignorePaging=false",headers=headers)
#     if get_response.status_code == 200:
#         area_json=get_response.json()
#         for area in area_json.get("areas", []):
#             # area_id = area["areas"][0]["id"]
#             floor_id = area.get("floor", {}).get("id")   # floor is nested
#             # print(f"Area Name: {area['name']}, Area ID: {area_id}, Floor ID: {floor_id}")
#         # area_name = area_json['areas']['id']

#         # print(area_name,"............................")
#         print("Response JSON : ",json.dumps(area_json,indent=4))


# get_area_list(base_url, company_id, headers)











def to_bool(value):
    """Converts value into a strict boolean True/False."""
    if isinstance(value, bool):   # Already a boolean
        return value
    if isinstance(value, str):    # Strings like "true", "false", "1", "0"
        return value.strip().lower() in ("true", "1", "yes", "y", "t")
    if isinstance(value, (int, float)):  # Numbers: 1 → True, 0 → False
        return value == 1
    return False  # Anything else defaults to False




print("\n")
print("\033[1;34m ADMIN AREA CREATION TESTCASE! Document ID: TP_002\033[0m")


# 2 : Create : Area : Valid name Field :

test_case_id=2
valid_name="Areanametest"
def valid_test_case(valid_name, code, areatype, parent_id, building_id, floor_id,isactive,
                          modulegroup_id, paymentmode_name1,paymentMode1,paymentmode_name2,paymentMode2,paymentmode_name3,paymentMode3,
                          delivery_mode_name1,delivery_mode1, delivery_mode_name2,delivery_mode2,
                          delivery_mode_name3,delivery_mode3,preorder, base_url, company_id, headers):

        common_payload = {
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

        response = requests.post(
            base_url + f"api/v1/masters/area/web/{company_id}/create-area",
            json=common_payload,
            headers=headers
        )

        if response.status_code == 200:
            create_json = response.json()
            print(f"\033[92m✅ Test Case ID - 00{test_case_id} : Valid value                 : TEST PASSED...! \033[0m ")
            # print(response.text, valid_name)
            area_id = create_json.get('id')
            if area_id:
                del_response = requests.patch(
                    base_url + f"api/v1/masters/area/web/{company_id}/delete-area/{area_id}",
                    headers=headers
                )
                if del_response.status_code == 200:
                    del_response.text
                    # print("🗑️ Area Deleted")
        else:
            print(f"\033[91m❌ Test Case ID - 00{test_case_id} : Valid value                  : TEST FAILED...!  : : Invalid data or missing fields \033[0m {response.text} {valid_name}")


valid_test_case(
    valid_name, 33, "parent", "", "68709372293ae6389032a058",
    "68709372293ae6389032a05a",to_bool(True), "68709372293ae6389032a05b",
    "paymentGateway", to_bool(True),"payOnDelivery",to_bool(True), "roomCredit",to_bool(True),
    "roomDelivery",to_bool(True), "takeAway",to_bool(True), "dineIn",to_bool(True),to_bool(False),
    base_url, company_id, headers
)








# 3 : Create Area name with Invalid input values : 


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
    ("用户名😊", "Emoji / Unicode"),              # Test Case ID - 011
    ("' OR '1'='1", "SQL Injection Attempt"),   # Test Case ID - 012
    ("Areanametest", "Duplicate Value"),        # Test Case ID - 013
    ( "Areanametest".upper(), "Case Sensitivity"),       # Test Case ID - 014
]


for test,description in test_cases:
    test_case_id += 1

    def common_test_cases(name, code, areatype, parent_id, building_id, floor_id,isactive,
                          modulegroup_id, paymentmode_name1,paymentMode1,paymentmode_name2,paymentMode2,paymentmode_name3,paymentMode3,
                          delivery_mode_name1,delivery_mode1, delivery_mode_name2,delivery_mode2,
                          delivery_mode_name3,delivery_mode3,preorder, base_url, company_id, headers,description):

        common_payload = {
            "name": name,
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

        response = requests.post(
            base_url + f"api/v1/masters/area/web/{company_id}/create-area",
            json=common_payload,
            headers=headers
        )

        if response.status_code == 200:
            create_json = response.json()
            print(f"\033[91m❌ Test Case ID - 00{test_case_id} : {description}                  :   TEST FAILED...!   : Invalid data or missing fields \033[0m ")
            # print(response.text, test)

            area_id = create_json.get('id')
            if area_id:
                del_response = requests.patch(
                    base_url + f"api/v1/masters/area/web/{company_id}/delete-area/{area_id}",
                    headers=headers
                )
                if del_response.status_code == 200:
                    del_response.text
                    # print("🗑️ Area Deleted")
        else:
            print(f"\033[92m✅ Test Case ID - 00{test_case_id} : {description}                 : TEST PASSED...! \033[0m ")
            # print(response.text, test)

    common_test_cases(
        test, 33, "parent", "", "68709372293ae6389032a058",
        "68709372293ae6389032a05a",to_bool(True), "68709372293ae6389032a05b",
        "paymentGateway", to_bool(True),"payOnDelivery",to_bool(True), "roomCredit",to_bool(True),
        "roomDelivery",to_bool(True), "takeAway",to_bool(True), "dineIn",to_bool(True),to_bool(False),
        base_url, company_id, headers,description 
    )











 #******************************************************** Create Area : code ************************************************




# 4 : Create : Area : Valid Code Field :


test_case_id=15
valid_code=37

valid_test_case(
    "Invalid code", valid_code, "parent", "", "68709372293ae6389032a058",
    "68709372293ae6389032a05a",to_bool(True), "68709372293ae6389032a05b",
    "paymentGateway", to_bool(True),"payOnDelivery",to_bool(True), "roomCredit",to_bool(True),
    "roomDelivery",to_bool(True), "takeAway",to_bool(True), "dineIn",to_bool(True),to_bool(False),
    base_url, company_id, headers
)





# 5  : Create Area : code with invalid input : 

test_case_id=15

# invalid_code_values = [
#         "abc",                                # String                             Test Case ID - 016
#         "@#$%",                               # Special characters                 Test Case ID - 017
#         None,                                 # Null                               Test Case ID - 018
#         "",                                   # Empty                              Test Case ID - 019
#         "   ",                                # Space                              Test Case ID - 020
#         -7,                                   # Negative value                     Test Case ID - 021
#         123.456,                              # Decimal value                      Test Case ID - 022
#         0,                                    # Zero value                         Test Case ID - 023  
#         886666666666666660000009999*1000,      # Large Number                      Test Case ID - 024
#         12e34,                                # Invalid format                     Test Case ID - 025
#         True,                                 # Boolean                            Test Case ID - 026
#         "' OR '1'='1" ,                       # SQL Injection                      Test Case ID - 027
#         5                                    # duplicates                          Test Case ID - 028
#     ]



invalid_code_values = [
    ("abc", "String"),                             # Test Case ID - 016
    ("@#$%", "Special Characters"),                # Test Case ID - 017
    (None, "Null"),                                # Test Case ID - 018
    ("", "Empty String"),                          # Test Case ID - 019
    ("   ", "Only Spaces"),                        # Test Case ID - 020
    (-7, "Negative Value"),                        # Test Case ID - 021
    (123.456, "Decimal Value"),                    # Test Case ID - 022
    (0, "Zero Value"),                             # Test Case ID - 023
    (886666666666666660000009999 * 1000, "Large Number"),  # Test Case ID - 024
    (12e34, "Invalid Format (Exponential)"),       # Test Case ID - 025
    (True, "Boolean Value"),                       # Test Case ID - 026
    ("' OR '1'='1", "SQL Injection Attempt"),      # Test Case ID - 027
    (5, "Duplicate Value"),                        # Test Case ID - 028
]



for invalid_code,descriptions  in invalid_code_values:
    test_case_id += 1
    test=invalid_code
    common_test_cases(
        "Invalid code", invalid_code, "parent", "", "68709372293ae6389032a058",
        "68709372293ae6389032a05a",to_bool(True), "68709372293ae6389032a05b",
        "paymentGateway", to_bool(True),"payOnDelivery",to_bool(True), "roomCredit",to_bool(True),
        "roomDelivery",to_bool(True), "takeAway",to_bool(True), "dineIn",to_bool(True),to_bool(False),
        base_url, company_id, headers,descriptions 
    )








# ********************************************************Create Area : Area Type *******************************************************************


# 6 : Create area with valid area type :  Parent  :


test_case_id=29
valid_area_type="parent"

valid_test_case(
    "Invalid areatype", 45, valid_area_type, "", "68709372293ae6389032a058",
    "68709372293ae6389032a05a",to_bool(True), "68709372293ae6389032a05b",
    "paymentGateway", to_bool(True),"payOnDelivery",to_bool(True), "roomCredit",to_bool(True),
    "roomDelivery",to_bool(True), "takeAway",to_bool(True), "dineIn",to_bool(True),to_bool(False),
    base_url, company_id, headers
)






# 7 : Create area with valid area type :  Child  :



















