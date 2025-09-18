

import requests
import time
import json
import random
import urllib.parse

import base64




failed_count=0
total_count=272

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




print("\033[1;34m ADMIN AREA CREATION TESTCASE! Document ID: TP_002\033[0m")

print("\033[1;34m  Area Creation with Name Field ! Document ID: TP_002\033[0m")

# 2 : Create : Area : Valid name Field :

test_case_id=0+2
valid_data="Areanametest"
def valid_test_case(valid_name, code, areatype, parent_id, building_id, floor_id,isactive,
                          modulegroup_id, paymentmode_name1,paymentMode1,paymentmode_name2,paymentMode2,paymentmode_name3,paymentMode3,
                          delivery_mode_name1,delivery_mode1, delivery_mode_name2,delivery_mode2,
                          delivery_mode_name3,delivery_mode3,preorder, base_url, company_id, headers,failed_count):
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
            print(f"\033[92m✅ Test Case ID - 00{test_case_id}  :  Valid value    :        TEST PASSED...! \033[0m ")
            # print(response.text)
            # print(response.status_code)
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
            print(f"\033[91m❌ Test Case ID - 00{test_case_id} : Invalid value        :       TEST FAILED...!  :  Invalid data or missing fields \033[0m")
            # print(response.status_code, valid_data)
            # print(response.text,"{response.text} {valid_name}")
            failed_count+=1






valid_test_case(
    valid_data, 83, "parent", "", "68709372293ae6389032a058",
    "68709372293ae6389032a05a",to_bool(True), "68709372293ae6389032a05b",
    "paymentGateway", to_bool(True),"payOnDelivery",to_bool(True), "roomCredit",to_bool(True),
    "roomDelivery",to_bool(True), "takeAway",to_bool(True), "dineIn",to_bool(True),to_bool(False),
    base_url, company_id, headers,failed_count)








# 3 : Create Area name with Invalid input values : 


test_case_id=0+2


count=0
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
    # ("' OR '1'='1", "SQL Injection Attempt"),   
]


for test,description in test_cases:
    test_case_id += 1

    def common_test_cases(name, code, areatype, parent_id, building_id, floor_id,isactive,
                          modulegroup_id, paymentmode_name1,paymentMode1,paymentmode_name2,paymentMode2,paymentmode_name3,paymentMode3,
                          delivery_mode_name1,delivery_mode1, delivery_mode_name2,delivery_mode2,
                          delivery_mode_name3,delivery_mode3,preorder, base_url, company_id, headers,test,description,failed_count,count
):

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

        response_test = requests.post(
            base_url + f"api/v1/masters/area/web/{company_id}/create-area",
            json=common_payload,
            headers=headers
        )

        if response_test.status_code == 200:
            create_json = response_test.json()
            print(f"\033[91m❌ Test Case ID - 00{test_case_id} : {description}                                 :           TEST FAILED...! : Invalid data or missing fields \033[0m ")
            # print(response_test.text, test)
            # print(response_test.status_code)
            failed_count+=1


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
            print(f"\033[92m✅ Test Case ID - 00{test_case_id} : {description}                                 :            TEST PASSED...! \033[0m ")
            # print(response_test.text, test)
            # print(response_test.status_code,test)



    common_test_cases(
        test, 33, "parent", "", "68709372293ae6389032a058",
        "68709372293ae6389032a05a",to_bool(True), "68709372293ae6389032a05b",
        "paymentGateway", to_bool(True),"payOnDelivery",to_bool(True), "roomCredit",to_bool(True),
        "roomDelivery",to_bool(True), "takeAway",to_bool(True), "dineIn",to_bool(True),to_bool(False),
        base_url, company_id, headers,test,description,failed_count,count
 
    )

if count in [0,10]:
    failed_count+=1
    print(failed_count)









#  #******************************************************** Create Area : code ************************************************


print("\033[1;34m  Area Creation with Code Field ! Document ID: TP_002\033[0m")


# 4 : Create : Area : Valid Code Field :


test_case_id = 14

valid_code=37
count=0

valid_test_case(
    "Invalid code", valid_code, "parent", "", "68709372293ae6389032a058",
    "68709372293ae6389032a05a",to_bool(True), "68709372293ae6389032a05b",
    "paymentGateway", to_bool(True),"payOnDelivery",to_bool(True), "roomCredit",to_bool(True),
    "roomDelivery",to_bool(True), "takeAway",to_bool(True), "dineIn",to_bool(True),to_bool(False),
    base_url, company_id, headers,failed_count
)

if count in [0,3]:
    failed_count+=1
    print(failed_count)



# 5  : Create Area : code with invalid input : 

test_case_id=14



invalid_code_values = [
    ("abc", "String"),                             # Test Case ID - 015
    ("@#$%", "Special Characters"),                # Test Case ID - 016
    (None, "Null"),                                # Test Case ID - 017
    ("", "Empty String"),                          # Test Case ID - 018
    ("   ", "Only Spaces"),                        # Test Case ID - 019
    (-7, "Negative Value"),                        # Test Case ID - 020
    (123.456, "Decimal Value"),                    # Test Case ID - 021
    (0, "Zero Value"),                             # Test Case ID - 022
    (886666666666666660000009999 * 1000, "Large Number"),  # Test Case ID - 023
    (12e34, "Invalid Format (Exponential)"),       # Test Case ID - 024
    (True, "Boolean Value"),                       # Test Case ID - 025
    # ("' OR '1'='1", "SQL Injection Attempt"),      # Test Case ID - 026
    (5, "Duplicate Value"),                        # Test Case ID - 027
]



for testcode,descriptions  in invalid_code_values:
    test_case_id += 1
    testcode
    common_test_cases(
        "Invalid code", testcode, "parent", "", "68709372293ae6389032a058",
        "68709372293ae6389032a05a",to_bool(True), "68709372293ae6389032a05b",
        "paymentGateway", to_bool(True),"payOnDelivery",to_bool(True), "roomCredit",to_bool(True),
        "roomDelivery",to_bool(True), "takeAway",to_bool(True), "dineIn",to_bool(True),to_bool(False),
        base_url, company_id, headers,testcode,description,failed_count,count 
    )








# # ********************************************************Create Area : Area Type *******************************************************************


# # 6 : Create area with valid area type :  Parent  :
# print("\033[1;34m  Area Creation with Area Type Field ! Document ID: TP_002\033[0m")


# test_case_id=27
# valid_data="parent"

# valid_test_case(
#     "areastype", 45, valid_data, "", "68709372293ae6389032a058",
#     "68709372293ae6389032a05a",to_bool(True), "68709372293ae6389032a05b",
#     "paymentGateway", to_bool(True),"payOnDelivery",to_bool(True), "roomCredit",to_bool(True),
#     "roomDelivery",to_bool(True), "takeAway",to_bool(True), "dineIn",to_bool(True),to_bool(False),
#     base_url, company_id, headers,failed_count
# )






# # 7 : Create area with valid area type :  Child  :



# test_case_id=31
# valid_data="child"

# valid_test_case(
#     "areatype", 47, valid_data, "68709372293ae6389032a05e", "68709372293ae6389032a058",
#     "68709372293ae6389032a05a",to_bool(True), "68709372293ae6389032a05b",
#     "paymentGateway", to_bool(True),"payOnDelivery",to_bool(True), "roomCredit",to_bool(True),
#     "roomDelivery",to_bool(True), "takeAway",to_bool(True), "dineIn",to_bool(True),to_bool(False),
#     base_url, company_id, headers,failed_count
# )





# # 8 : Create area with invalid area type : 

# test_case_id=31

# for test,description in test_cases:
#     test_case_id += 1
#     common_test_cases(
#             "AreaType", 53, test, "", "68709372293ae6389032a058",
#             "68709372293ae6389032a05a",to_bool(True), "68709372293ae6389032a05b",
#             "paymentGateway", to_bool(True),"payOnDelivery",to_bool(True), "roomCredit",to_bool(True),
#             "roomDelivery",to_bool(True), "takeAway",to_bool(True), "dineIn",to_bool(True),to_bool(False),
#             base_url, company_id, headers,description,failed_count,count
#     )







# # ********************************************************Create Area : Building ID *******************************************************************





# print("\033[1;34m  Area Creation with Building ID Field ! Document ID: TP_002\033[0m")

# # 9 : Create area with valid Building Id : 

# test_case_id=45
# valid_data="68709372293ae6389032a058"

# valid_test_case(
#     "Buildtest", 470,"parent","", valid_data,
#     "68709372293ae6389032a05a",to_bool(True), "68709372293ae6389032a05b",
#     "paymentGateway", to_bool(True),"payOnDelivery",to_bool(True), "roomCredit",to_bool(True),
#     "roomDelivery",to_bool(True), "takeAway",to_bool(True), "dineIn",to_bool(True),to_bool(False),
#     base_url, company_id, headers,failed_count
# )







# # 10 : Create area with invalid Building Id : 

# test_cases = [
#     ("68709372293ae6389032a057", "Invalid Building ID"),    # Test Case ID - 044
#     (22, "Integer Value"),                                  # Test Case ID - 045
#     ("@%&#+-+=54a%", "Special Characters"),                 # Test Case ID - 046
#     (None, "Null"),                                         # Test Case ID - 047
#     (True, "Boolean"),                                      # Test Case ID - 048
#     ("  AreaStart", "Leading Space"),                       # Test Case ID - 049
#     ("AreaEnd  ", "Trailing Space"),                        # Test Case ID - 050
#     ("", "Empty String"),                                   # Test Case ID - 051
#     ("   ", "Only Spaces"),                                 # Test Case ID - 052
#     ("用户名😊", "Emoji / Unicode"),                        # Test Case ID - 053
#     ("' OR '1'='1", "SQL Injection Attempt"),               # Test Case ID - 054
#     ( "Areanametest".upper(), "Case Sensitivity"),           # Test Case ID - 055
# ]

# test_case_id=45

# for test,description in test_cases:
#     test_case_id += 1
#     common_test_cases(
#             "Buildtest", 536,"parent","", test,
#             "68709372293ae6389032a05a",to_bool(True), "68709372293ae6389032a05b",
#             "paymentGateway", to_bool(True),"payOnDelivery",to_bool(True), "roomCredit",to_bool(True),
#             "roomDelivery",to_bool(True), "takeAway",to_bool(True), "dineIn",to_bool(True),to_bool(False),
#             base_url, company_id, headers,description,failed_count,count 
#     )









# # ********************************************************Create Area : Floor ID *******************************************************************





# print("\033[1;34m  Area Creation with Floor ID Field ! Document ID: TP_002\033[0m")

# # 11 : Create area with valid Floor Id : 

# test_case_id=58
# valid_data="68709372293ae6389032a05a"

# valid_test_case(
#     "Buildtest", 470,"parent","", "68709372293ae6389032a058",
#     valid_data,to_bool(True), "68709372293ae6389032a05b",
#     "paymentGateway", to_bool(True),"payOnDelivery",to_bool(True), "roomCredit",to_bool(True),
#     "roomDelivery",to_bool(True), "takeAway",to_bool(True), "dineIn",to_bool(True),to_bool(False),
#     base_url, company_id, headers,failed_count
# )












# # 12 : Create area with invalid Floor Id : 

# test_cases = [
#     ("68709372293ae6389032abb", "Invalid Floor ID"),       # Test Case ID - 056
#     (22, "Integer Value"),                                  # Test Case ID - 057
#     ("@%&#+-+=54a%", "Special Characters"),                 # Test Case ID - 058
#     (None, "Null"),                                         # Test Case ID - 059
#     (True, "Boolean"),                                      # Test Case ID - 060
#     ("  AreaStart", "Leading Space"),                       # Test Case ID - 061
#     ("AreaEnd  ", "Trailing Space"),                        # Test Case ID - 062
#     ("", "Empty String"),                                   # Test Case ID - 063
#     ("   ", "Only Spaces"),                                 # Test Case ID - 064
#     ("用户名😊", "Emoji / Unicode"),                        # Test Case ID - 065
#     ("' OR '1'='1", "SQL Injection Attempt"),               # Test Case ID - 066
#     ( "Areanametest".upper(), "Case Sensitivity"),           # Test Case ID - 067
# ]

# test_case_id=58

# for test,description in test_cases:
#     test_case_id += 1
#     common_test_cases(
#             "Buildtest", 536,"parent","","68709372293ae6389032a058" ,
#             test,to_bool(True), "68709372293ae6389032a05b",
#             "paymentGateway", to_bool(True),"payOnDelivery",to_bool(True), "roomCredit",to_bool(True),
#             "roomDelivery",to_bool(True), "takeAway",to_bool(True), "dineIn",to_bool(True),to_bool(False),
#             base_url, company_id, headers,description,failed_count,count 
#     )










# # ********************************************************Create Area : Is active Field *******************************************************************





# print("\033[38;5;208mm  Area Creation with  Is Active Field ! Document ID: TP_002\033[0m")

# # 13 : Create area with valid  Is Active  : 

# test_case_id=71
# valid_data=to_bool(True)

# valid_test_case(
#     "Buildtest", 490,"parent","", "68709372293ae6389032a058",
#     "68709372293ae6389032a05a",valid_data, "68709372293ae6389032a05b",
#     "paymentGateway", to_bool(True),"payOnDelivery",to_bool(True), "roomCredit",to_bool(True),
#     "roomDelivery",to_bool(True), "takeAway",to_bool(True), "dineIn",to_bool(True),to_bool(False),
#     base_url, company_id, headers,failed_count
# )





# # 14 : Create area with invalid Is Active  : 

# test_case = [
#     (27, "Integer Values"),                                  # Test Case ID - 070
#     ("@%&#+-+=54a%", "Special Characters"),                 # Test Case ID - 071
#     (None, "Null"),                                         # Test Case ID - 072
#     (True, "Boolean"),                                      # Test Case ID - 073
#     ("  AreaStart", "Leading Space"),                       # Test Case ID - 074
#     ("AreaEnd  ", "Trailing Space"),                        # Test Case ID - 075
#     ("", "Empty String"),                                   # Test Case ID - 076
#     ("   ", "Only Spaces"),                                 # Test Case ID - 077
#     ("用户名😊", "Emoji / Unicode"),                        # Test Case ID - 078
#     ("' OR '1'='1", "SQL Injection Attempt"),               # Test Case ID - 079
#     ( "Areanametest".upper(), "Case Sensitivity"),          # Test Case ID - 080
# ]

# test_case_id=71

# for t,description in test_case:
#     test_case_id += 1
#     test=t
#     common_test_cases(
#             "Isactive", 536,"parent","","68709372293ae6389032a058" ,
#             "68709372293ae6389032a05a",test, "68709372293ae6389032a05b",
#             "paymentGateway", to_bool(True),"payOnDelivery",to_bool(True), "roomCredit",to_bool(True),
#             "roomDelivery",to_bool(True), "takeAway",to_bool(True), "dineIn",to_bool(True),to_bool(False),
#             base_url, company_id, headers,description,failed_count,count 
#     )





# # ********************************************************Create Area : Module Group ID *******************************************************************




# # doubt : boolean
# print("\033[1;34m  Area Creation with   Module Group ID  Field ! Document ID: TP_002\033[0m")

# # 15 : Create area with valid  Module Group ID  : 

# test_case_id=83
# valid_data="68709372293ae6389032a05b"

# valid_test_case(
#     "Buildtest", 490,"parent","", "68709372293ae6389032a058",
#     "68709372293ae6389032a05a",to_bool(True), valid_data,
#     "paymentGateway", to_bool(True),"payOnDelivery",to_bool(True), "roomCredit",to_bool(True),
#     "roomDelivery",to_bool(True), "takeAway",to_bool(True), "dineIn",to_bool(True),to_bool(False),
#     base_url, company_id, headers,failed_count
# )








# # 16 : Create area with invalid  Module Group ID  : 



# test_case = [
#     (27, "Integer Values"),                                  # Test Case ID - 082
#     ("@%&#+-+=54a%", "Special Characters"),                 # Test Case ID - 083
#     (None, "Null"),                                         # Test Case ID - 084
#     (True, "Boolean"),                                      # Test Case ID - 085
#     ("  AreaStart", "Leading Space"),                       # Test Case ID - 086
#     ("AreaEnd  ", "Trailing Space"),                        # Test Case ID - 087
#     ("", "Empty String"),                                   # Test Case ID - 088
#     ("   ", "Only Spaces"),                                 # Test Case ID - 089
#     ("用户名😊", "Emoji / Unicode"),                        # Test Case ID - 090
#     ("' OR '1'='1", "SQL Injection Attempt"),               # Test Case ID - 100
#     ( "Areanametest".upper(), "Case Sensitivity"),          # Test Case ID - 101
# ]

# test_case_id=83

# for t,description in test_case:
#     test_case_id += 1
#     test=t
#     common_test_cases(
#             "Isactive", 536,"parent","","68709372293ae6389032a058" ,
#             "68709372293ae6389032a05a",to_bool(True),test,
#             "paymentGateway", to_bool(True),"payOnDelivery",to_bool(True), "roomCredit",to_bool(True),
#             "roomDelivery",to_bool(True), "takeAway",to_bool(True), "dineIn",to_bool(True),to_bool(False),
#             base_url, company_id, headers,description,failed_count,count 
#     )







#  # ********************************************************Create Area : Payment Modes *******************************************************************





# print("\033[1;34m  Area Creation with   Payment Modes  Field ! Document ID: TP_002\033[0m")
# print("\033[1;34m  Area Creation with   Payment Mode 1 Name Field  \033[0m")

# # 17 : Create area with valid Payment Modes 1 name : 

# test_case_id=95
# valid_data="paymentGateway"
# valid_test_case(
#     "Paymentmode", 490,"parent","", "68709372293ae6389032a058",
#     "68709372293ae6389032a05a",to_bool(True), "68709372293ae6389032a05b",
#     valid_data, to_bool(True),"payOnDelivery",to_bool(True), "roomCredit",to_bool(True),
#     "roomDelivery",to_bool(True), "takeAway",to_bool(True), "dineIn",to_bool(True),to_bool(False),
#     base_url, company_id, headers,failed_count
# )




# # 18 : Create area with invalid Payment Modes 1 name : 





# test_case_id=95

# for t,description in test_case:
#     test_case_id += 1
#     test=t
#     common_test_cases(
#             "Paymentmode", 536,"parent","","68709372293ae6389032a058" ,
#             "68709372293ae6389032a05a",to_bool(True),"68709372293ae6389032a05b",
#             t, to_bool(True),"payOnDelivery",to_bool(True), "roomCredit",to_bool(True),
#             "roomDelivery",to_bool(True), "takeAway",to_bool(True), "dineIn",to_bool(True),to_bool(False),
#             base_url, company_id, headers,description,failed_count,count 
#     )







# # 19 : Create area with valid Payment Modes 1 enabled : 

# print("\033[1;34m  Area Creation with   Payment Mode 1 Enabled Field  \033[0m")

# test_case_id=118
# valid_data=to_bool(True)

# valid_test_case(
#     "Paymentmode", 490,"parent","", "68709372293ae6389032a058",
#     "68709372293ae6389032a05a",to_bool(True), "68709372293ae6389032a05b",
#     "paymentGateway",valid_data,"payOnDelivery",to_bool(True), "roomCredit",to_bool(True),
#     "roomDelivery",to_bool(True), "takeAway",to_bool(True), "dineIn",to_bool(True),to_bool(False),
#     base_url, company_id, headers,failed_count
# )




# # 20 : Create area with invalid Payment Modes 1 enabled : 





# test_case_id=118

# for t,description in test_case:
#     test_case_id += 1
#     test=t
#     common_test_cases(
#             "Paymentmode", 636,"parent","","68709372293ae6389032a058" ,
#             "68709372293ae6389032a05a",to_bool(True),"68709372293ae6389032a05b",
#             "paymentGateway",to_bool(test),"payOnDelivery",to_bool(True), "roomCredit",to_bool(True),
#             "roomDelivery",to_bool(True), "takeAway",to_bool(True), "dineIn",to_bool(True),to_bool(False),
#             base_url, company_id, headers,description,failed_count,count 
#     )






# # # 21 : Create area with valid Payment Modes 2 name : 
# print("\033[1;34m  Area Creation with   Payment Mode 2 Name Field \033[0m")

# test_case_id=130
# valid_data="payOnDelivery"
# valid_test_case(
#     "Paymentmode", 490,"parent","", "68709372293ae6389032a058",
#     "68709372293ae6389032a05a",to_bool(True), "68709372293ae6389032a05b",
#     "paymentGateway", to_bool(True),valid_data,to_bool(True), "roomCredit",to_bool(True),
#     "roomDelivery",to_bool(True), "takeAway",to_bool(True), "dineIn",to_bool(True),to_bool(False),
#     base_url, company_id, headers,failed_count
# )




# # 22 : Create area with invalid Payment Modes 2 name : 





# test_case_id=130

# for t,description in test_case:
#     test_case_id += 1
#     test=t
#     common_test_cases(
#             "Paymentmode", 536,"parent","","68709372293ae6389032a058" ,
#             "68709372293ae6389032a05a",to_bool(True),"68709372293ae6389032a05b",
#             "paymentGateway", to_bool(True),test,to_bool(True), "roomCredit",to_bool(True),
#             "roomDelivery",to_bool(True), "takeAway",to_bool(True), "dineIn",to_bool(True),to_bool(False),
#             base_url, company_id, headers,description,failed_count,count 
#     )










# # 23 : Create area with valid Payment Modes 2 enabled : 


# print("\033[1;34m  Area Creation with   Payment Mode 2 Enabled Field  \033[0m")

# test_case_id=142
# valid_data=to_bool(True)
# valid_test_case(
#     "Paymentmode", 490,"parent","", "68709372293ae6389032a058",
#     "68709372293ae6389032a05a",to_bool(True), "68709372293ae6389032a05b",
#     "paymentGateway",to_bool(True),"payOnDelivery",valid_data, "roomCredit",to_bool(True),
#     "roomDelivery",to_bool(True), "takeAway",to_bool(True), "dineIn",to_bool(True),to_bool(False),
#     base_url, company_id, headers,failed_count
# )




# # 24 : Create area with invalid Payment Modes 2 enabled : 





# test_case_id=142

# for t,description in test_case:
#     test_case_id += 1
#     test=t
#     common_test_cases(
#             "Paymentmode", 636,"parent","","68709372293ae6389032a058" ,
#             "68709372293ae6389032a05a",to_bool(True),"68709372293ae6389032a05b",
#             "paymentGateway",to_bool(True),"payOnDelivery",to_bool(test), "roomCredit",to_bool(True),
#             "roomDelivery",to_bool(True), "takeAway",to_bool(True), "dineIn",to_bool(True),to_bool(False),
#             base_url, company_id, headers,description,failed_count,count 
#     )









# # 25 : Create area with valid Payment Modes 3 name : 

# print("\033[1;34m  Area Creation with   Payment Mode 3 Name Field \033[0m")

# test_case_id=154
# valid_data="roomCredit"
# valid_test_case(
#     "Paymentmode", 490,"parent","", "68709372293ae6389032a058",
#     "68709372293ae6389032a05a",to_bool(True), "68709372293ae6389032a05b",
#     "paymentGateway", to_bool(True),"payOnDelivery",to_bool(True), valid_data,to_bool(True),
#     "roomDelivery",to_bool(True), "takeAway",to_bool(True), "dineIn",to_bool(True),to_bool(False),
#     base_url, company_id, headers,failed_count
# )




# # 26 : Create area with invalid Payment Modes 3 name : 





# test_case_id=154

# for t,description in test_case:
#     test_case_id += 1
#     test=t
#     common_test_cases(
#             "Paymentmode", 536,"parent","","68709372293ae6389032a058" ,
#             "68709372293ae6389032a05a",to_bool(True),"68709372293ae6389032a05b",
#             "paymentGateway", to_bool(True),"payOnDelivery",to_bool(True), t,to_bool(True),
#             "roomDelivery",to_bool(True), "takeAway",to_bool(True), "dineIn",to_bool(True),to_bool(False),
#             base_url, company_id, headers,description,failed_count,count 
#     )







# # 27 : Create area with valid Payment Modes 3 enabled : 

# print("\033[1;34m  Area Creation with   Payment Mode 3 Enabled Field  \033[0m")

# test_case_id=166
# valid_data=to_bool(True)
# valid_test_case(
#     "Paymentmode", 490,"parent","", "68709372293ae6389032a058",
#     "68709372293ae6389032a05a",to_bool(True), "68709372293ae6389032a05b",
#     "paymentGateway",to_bool(True),"payOnDelivery",to_bool(True), "roomCredit",valid_data,
#     "roomDelivery",to_bool(True), "takeAway",to_bool(True), "dineIn",to_bool(True),to_bool(False),
#     base_url, company_id, headers,failed_count
# )




# # 28 : Create area with invalid Payment Modes 3 enabled : 





# test_case_id=166

# for t,description in test_case:
#     test_case_id += 1
#     test=t
#     common_test_cases(
#             "Paymentmode", 636,"parent","","68709372293ae6389032a058" ,
#             "68709372293ae6389032a05a",to_bool(True),"68709372293ae6389032a05b",
#             "paymentGateway",to_bool(True),"payOnDelivery",to_bool(True), "roomCredit",to_bool(test),
#             "roomDelivery",to_bool(True), "takeAway",to_bool(True), "dineIn",to_bool(True),to_bool(False),
#             base_url, company_id, headers,description,failed_count,count 
#     )











#  # ********************************************************Create Area : Delivery Modes *******************************************************************



# # 29 : Create area with valid Delivery Modes 1 Name :

# print("\033[1;34m  Area Creation with   Delivery Modes  Field ! Document ID: TP_002\033[0m")

# print("\033[1;34m  Area Creation with   Delivery Mode 1 Name Field  \033[0m")



# test_case_id=178
# valid_data="roomDelivery"
# valid_test_case(
#     "Deliverymode", 490,"parent","", "68709372293ae6389032a058",
#     "68709372293ae6389032a05a",to_bool(True), "68709372293ae6389032a05b",
#     "paymentGateway", to_bool(True),"payOnDelivery",to_bool(True), "roomCredit",to_bool(True),
#     valid_data,to_bool(True), "takeAway",to_bool(True), "dineIn",to_bool(True),to_bool(False),
#     base_url, company_id, headers,failed_count
# )




# # 30 : Create area with invalid Delivery Modes 1 name : 





# test_case_id=178

# for t,description in test_case:
#     test_case_id += 1
#     test=t
#     common_test_cases(
#             "Deliverymode", 536,"parent","","68709372293ae6389032a058" ,
#             "68709372293ae6389032a05a",to_bool(True),"68709372293ae6389032a05b",
#             "paymentGateway", to_bool(True),"payOnDelivery",to_bool(True), "roomCredit",to_bool(True),
#             test,to_bool(True), "takeAway",to_bool(True), "dineIn",to_bool(True),to_bool(False),
#             base_url, company_id, headers,description,failed_count,count 
#     )






# # 31 : Create area with valid Delivery Mode 1 enabled : 

# print("\033[1;34m  Area Creation with   Delivery Mode 1 Enabled Field  \033[0m")

# test_case_id=190
# valid_data=to_bool(True)
# valid_test_case(
#     "Deliverymode", 490,"parent","", "68709372293ae6389032a058",
#     "68709372293ae6389032a05a",to_bool(True), "68709372293ae6389032a05b",
#     "paymentGateway",to_bool(True),"payOnDelivery",to_bool(True), "roomCredit",to_bool(True),
#     "roomDelivery",valid_data,"takeAway",to_bool(True), "dineIn",to_bool(True),to_bool(False),
#     base_url, company_id, headers,failed_count
# )




# # 32 : Create area with invalid Delivery Mode 1 enabled : 





# test_case_id=190

# for t,description in test_case:
#     test_case_id += 1
#     test=t
#     common_test_cases(
#             "Deliverymode", 636,"parent","","68709372293ae6389032a058" ,
#             "68709372293ae6389032a05a",to_bool(True),"68709372293ae6389032a05b",
#             "paymentGateway",to_bool(True),"payOnDelivery",to_bool(True), "roomCredit",to_bool(True),
#             "roomDelivery",to_bool(test), "takeAway",to_bool(True), "dineIn",to_bool(True),to_bool(False),
#             base_url, company_id, headers,description,failed_count ,count
#     )











# # 33  : Create area with valid Delivery Mode 2 name : 





# print("\033[1;34m  Area Creation with   Delivery Mode 2 Name Field \033[0m")

# test_case_id=201
# valid_data="takeAway"
# valid_test_case(
#     "Deliverymode", 490,"parent","", "68709372293ae6389032a058",
#     "68709372293ae6389032a05a",to_bool(True), "68709372293ae6389032a05b",
#     "paymentGateway", to_bool(True),"payOnDelivery",to_bool(True), "roomCredit",to_bool(True),
#     "roomDelivery",to_bool(True),valid_data,to_bool(True), "dineIn",to_bool(True),to_bool(False),
#     base_url, company_id, headers,failed_count
# )




# # 34 : Create area with invalid Delivery Mode 2 name : 





# test_case_id=201

# for t,description in test_case:
#     test_case_id += 1
#     test=t
#     common_test_cases(
#             "Deliverymode", 536,"parent","","68709372293ae6389032a058" ,
#             "68709372293ae6389032a05a",to_bool(True),"68709372293ae6389032a05b",
#             "paymentGateway", to_bool(True),"payOnDelivery",to_bool(True), "roomCredit",to_bool(True),
#             "roomDelivery",to_bool(True),test,to_bool(True), "dineIn",to_bool(True),to_bool(False),
#             base_url, company_id, headers,description,failed_count,count 
#     )










# # 35 : Create area with valid Delivery Mode 2 enabled : 


# print("\033[1;34m  Area Creation with   Delivery Mode 2 Enabled Field  \033[0m")

# test_case_id=213
# valid_data=to_bool(True)
# valid_test_case(
#     "Deliverymode", 490,"parent","", "68709372293ae6389032a058",
#     "68709372293ae6389032a05a",to_bool(True), "68709372293ae6389032a05b",
#     "paymentGateway",to_bool(True),"payOnDelivery",to_bool(True), "roomCredit",to_bool(True),
#     "roomDelivery",to_bool(True), "takeAway",valid_data, "dineIn",to_bool(True),to_bool(False),
#     base_url, company_id, headers,failed_count
# )




# # 36 : Create area with invalid Delivery Mode 2 enabled : 





# test_case_id=213

# for t,description in test_case:
#     test_case_id += 1
#     test=t
#     common_test_cases(
#             "Deliverymode", 636,"parent","","68709372293ae6389032a058" ,
#             "68709372293ae6389032a05a",to_bool(True),"68709372293ae6389032a05b",
#             "paymentGateway",to_bool(True),"payOnDelivery",to_bool(True), "roomCredit",to_bool(True),
#             "roomDelivery",to_bool(True), "takeAway",to_bool(test), "dineIn",to_bool(True),to_bool(False),
#             base_url, company_id, headers,description,failed_count,count 
#     )










# # 37  : Create area with valid Delivery Mode 3 name : 





# print("\033[1;34m  Area Creation with   Delivery Mode 3  Name Field \033[0m")

# test_case_id=224
# valid_data="dineIn"
# valid_test_case(
#     "Deliverymode", 490,"parent","", "68709372293ae6389032a058",
#     "68709372293ae6389032a05a",to_bool(True), "68709372293ae6389032a05b",
#     "paymentGateway", to_bool(True),"payOnDelivery",to_bool(True), "roomCredit",to_bool(True),
#     "roomDelivery",to_bool(True),"takeAway",to_bool(True),valid_data,to_bool(True),to_bool(False),
#     base_url, company_id, headers,failed_count
# )




# # 38 : Create area with invalid Delivery Modes 3 name : 





# test_case_id=224

# for t,description in test_case:
#     test_case_id += 1
#     test=t
#     common_test_cases(
#             "Deliverymode", 536,"parent","","68709372293ae6389032a058" ,
#             "68709372293ae6389032a05a",to_bool(True),"68709372293ae6389032a05b",
#             "paymentGateway", to_bool(True),"payOnDelivery",to_bool(True), "roomCredit",to_bool(True),
#             "roomDelivery",to_bool(True),"takeAway",to_bool(True),test,to_bool(True),to_bool(False),
#             base_url, company_id, headers,description,failed_count,count 
#     )










# # 39 : Create area with valid Delivery Mode 3 enabled : 


# print("\033[1;34m  Area Creation with   Delivery Mode 3 Enabled Field  \033[0m")

# test_case_id=236
# valid_data=to_bool(True)
# valid_test_case(
#     "Deliverymode", 490,"parent","", "68709372293ae6389032a058",
#     "68709372293ae6389032a05a",to_bool(True), "68709372293ae6389032a05b",
#     "paymentGateway",to_bool(True),"payOnDelivery",to_bool(True), "roomCredit",to_bool(True),
#     "roomDelivery",to_bool(True), "takeAway",to_bool(True), "dineIn",valid_data,to_bool(False),
#     base_url, company_id, headers,failed_count
# )




# # 40 : Create area with invalid Delivery Modes 3 enabled : 





# test_case_id=236

# for t,description in test_case:
#     test_case_id += 1
#     test=t
#     common_test_cases(
#             "Deliverymode", 636,"parent","","68709372293ae6389032a058" ,
#             "68709372293ae6389032a05a",to_bool(True),"68709372293ae6389032a05b",
#             "paymentGateway",to_bool(True),"payOnDelivery",to_bool(True), "roomCredit",to_bool(True),
#             "roomDelivery",to_bool(True), "takeAway",to_bool(True), "dineIn",to_bool(test),to_bool(False),
#             base_url, company_id, headers,description,failed_count,count 
#     )








#  # ********************************************************Create Area : Preorder  status *******************************************************************







# # 41 : Create area with valid Preorder status  : 

# print("\033[1;34m  Area Creation with Preorder status Field  \033[0m")

# test_case_id=248
# valid_data=to_bool(False)
# valid_test_case(
#     "preorder", 490,"parent","", "68709372293ae6389032a058",
#     "68709372293ae6389032a05a",to_bool(True), "68709372293ae6389032a05b",
#     "paymentGateway",to_bool(True),"payOnDelivery",to_bool(True), "roomCredit",to_bool(True),
#     "roomDelivery",to_bool(True),"takeAway",to_bool(True), "dineIn",to_bool(True),valid_data,
#     base_url, company_id, headers,failed_count
# )




# # 42 : Create area with invalid Preorder status Field : 





# test_case_id=248

# for t,description in test_case:
#     test_case_id += 1
#     test=t
#     common_test_cases(
#             "preorder", 636,"parent","","68709372293ae6389032a058" ,
#             "68709372293ae6389032a05a",to_bool(True),"68709372293ae6389032a05b",
#             "paymentGateway",to_bool(True),"payOnDelivery",to_bool(True), "roomCredit",to_bool(True),
#             "roomDelivery",to_bool(True), "takeAway",to_bool(True), "dineIn",to_bool(True),to_bool(test),
#             base_url, company_id, headers,description,failed_count,count 
#     )











#  # ********************************************************Create Area : Parent Area ID  *******************************************************************



# # 43 : Create area with valid Parent Area ID   :


# print("\033[1;34m  Area Creation with Parent ID Field  \033[0m")


# test_case_id=260
# valid_data="68709372293ae6389032a05e"

# valid_test_case(
#     "parent", 47, "child", valid_data, "68709372293ae6389032a058",
#     "68709372293ae6389032a05a",to_bool(True), "68709372293ae6389032a05b",
#     "paymentGateway", to_bool(True),"payOnDelivery",to_bool(True), "roomCredit",to_bool(True),
#     "roomDelivery",to_bool(True), "takeAway",to_bool(True), "dineIn",to_bool(True),to_bool(False),
#     base_url, company_id, headers,failed_count
# )










# # 44 : Create area with invalid ParentArea ID Field : 





# test_case_id=260

# for t,description in test_case:
#     test_case_id += 1
#     test=t
#     common_test_cases(
#             "parentid", 636,"child",test,"68709372293ae6389032a058" ,
#             "68709372293ae6389032a05a",to_bool(True),"68709372293ae6389032a05b",
#             "paymentGateway",to_bool(True),"payOnDelivery",to_bool(True), "roomCredit",to_bool(True),
#             "roomDelivery",to_bool(True), "takeAway",to_bool(True), "dineIn",to_bool(True),to_bool(False),
#             base_url, company_id, headers,description,failed_count,count 
#     )





# # 45 : Logout : 

# print("\033[1;34m  Logout  \033[0m")

# response_logout = requests.put(logout_url,headers=headers) 
# if response_logout.status_code == 200:
#     logout_json = response_logout.json()

#     # print("Response JSON:", json.dumps(logout_json, indent=4))
#     # print(f"Token (Logout): {valid_token}")
#     print(f"\033[92m✅ Test Case ID - 272 : Logout       :        TEST PASSED...! \033[0m ")

# else:
#     failed_count+=1
#     # print(f"Logout failed with status code {response_logout.status_code}")
#     # print("Response:", response_logout.json())
#     print(f"\033[91m❌ TEST FAILED...! : Test Case ID - 272 : Error -  Invalid or expired session token. \033[0m") # login failed so test passed
#     print(f"\033[91m❌ Test Case ID - 272 : Logout       :       TEST FAILED...! :\033[0m ")

     



# print(f"\033[1;34mTotal Test Failed  : {failed_count}/{total_count}\033[0m")

# if failed_count == 0:
#     print("\033[92m ✅ All TEST PASSED \033[0m")

