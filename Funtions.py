import requests
import time
import json
import random
import urllib.parse

import base64


# 1 : login funtion 

def login_test(base_url, login_url, login_payload, test_case_id,failed_count):

    print(f"\033[1;34m ADMIN LOGIN TESTCASE! Document ID: TP_{test_case_id:03d}\033[0m")
    test_case_id += 1
    try:
        response = requests.post(login_url, json=login_payload)

        if response.status_code == 200:
            response_json = response.json()
            name = response_json.get("name")
            valid_token = response_json.get("token", {}).get("token")
            company_id=response_json['company']['id']

            headers = {
                "Authorization": f"Bearer {valid_token}",
                "Content-Type": "application/json"
            }

            print(f"\033[92m✅ TEST PASSED...! : Test Case ID - {test_case_id:03d} | Name: {name} /{company_id}\033[0m")
            return headers, failed_count,company_id

        else:
            failed_count += 1
            print(f"\033[91m❌ TEST FAILED...! : Test Case ID - {test_case_id:03d} | Error - Invalid Credentials\033[0m")
            return None, failed_count

    except Exception as e:
        failed_count += 1
        print(f"\033[91m❌ TEST ERROR...! : Test Case ID - {test_case_id:03d} | Exception - {str(e)}\033[0m")
        return None, failed_count
    













# 2 : String Field testcase : 




def run_test_case(base_payload, overrides, base_url,endpoint, company_id, headers, test_case_id, failed_count):
    """
    Common reusable test function.
    
    :param base_payload: dict -> valid default payload for area creation
    :param overrides: dict -> fields you want to override for this test
    :param base_url: str -> API base url
    :param company_id: str -> Company ID
    :param headers: dict -> Auth headers
    :param test_case_id: int -> ID for tracking
    :param failed_count: int -> failure counter
    """
    
    # merge base payload with overrides
    payload = {**base_payload, **overrides}
    test_case_id += 1

    response = requests.post(base_url + {endpoint},json=payload,headers=headers)

    if response.status_code == 200:
        create_json = response.json()
        print(f"\033[92m✅ Test Case ID - 00{test_case_id} : {overrides} : TEST PASSED...!\033[0m")

        # delete created record (cleanup)
        area_id = create_json.get("id")
        # if area_id:
        #     requests.patch(f"{base_url}{endpoint.format(company_id=company_id,area_id=area_id)}",headers=headers)
    else:
        print(f"\033[91m❌ Test Case ID - 00{test_case_id} : {overrides} : TEST FAILED...!\033[0m",response.status_code)
        failed_count += 1
    
    return failed_count


# # failed_count=run_test_case(base_payload, overrides, base_url,endpoint, company_id, headers, test_case_id, failed_count)





# def valid_test_case(valid_name, code, areatype, parent_id, building_id, floor_id,isactive,
#                           modulegroup_id, paymentmode_name1,paymentMode1,paymentmode_name2,paymentMode2,paymentmode_name3,paymentMode3,
#                           delivery_mode_name1,delivery_mode1, delivery_mode_name2,delivery_mode2,
#                           delivery_mode_name3,delivery_mode3,preorder, base_url, company_id, headers,failed_count):

#         common_payload = {
#             "name": valid_name,
#             "code": code,
#             "areaType": areatype,
#             "parentAreaId": parent_id, 
#             "buildingId": building_id,
#             "floorId": floor_id,
#             "isActive": to_bool(isactive),   # ✅ converted boolean
#             "moduleGroupId": modulegroup_id,
#             "paymentModes": [
#                 {"name": paymentmode_name1, "enabled": to_bool(paymentMode1)},
#                 {"name": paymentmode_name2, "enabled": to_bool(paymentMode2)},
#                 {"name": paymentmode_name3, "enabled": to_bool(paymentMode3)},
#             ],
#             "deliveryModes": [
#                 {"name": delivery_mode_name1, "enabled": to_bool(delivery_mode1)},
#                 {"name": delivery_mode_name2, "enabled": to_bool(delivery_mode2)},
#                 {"name": delivery_mode_name3, "enabled": to_bool(delivery_mode3)},
#             ],
#             "preOrderStatus": to_bool(preorder)  # ✅ converted boolean
#         }

#         response = requests.post(
#             base_url + f"api/v1/masters/area/web/{company_id}/create-area",
#             json=common_payload,
#             headers=headers
#         )

#         if response.status_code == 200:
#             create_json = response.json()
#             print(f"\033[92m✅ Test Case ID - 00{test_case_id} : Valid value        :        TEST PASSED...! \033[0m ")
#             # print(response.text)
#             # print(response.status_code)
#             area_id = create_json.get('id')
#             if area_id:
#                 del_response = requests.patch(
#                     base_url + f"api/v1/masters/area/web/{company_id}/delete-area/{area_id}",
#                     headers=headers
#                 )
#                 if del_response.status_code == 200:
#                     del_response.text
#                     # print("🗑️ Area Deleted")
#         else:
#             print(f"\033[91m❌ Test Case ID - 00{test_case_id} : Valid value        :       TEST FAILED...!  : : Invalid data or missing fields \033[0m")
#             # print(response.status_code, valid_data)
#             # print(response.text,"{response.text} {valid_name}")
#             failed_count+=1


# valid_test_case(
#     valid_data, 33, "parent", "", "68709372293ae6389032a058",
#     "68709372293ae6389032a05a",to_bool(True), "68709372293ae6389032a05b",
#     "paymentGateway", to_bool(True),"payOnDelivery",to_bool(True), "roomCredit",to_bool(True),
#     "roomDelivery",to_bool(True), "takeAway",to_bool(True), "dineIn",to_bool(True),to_bool(False),
#     base_url, company_id, headers,failed_count
# )

failed_count=0
count=0
invalid_para_url=None
invalid_params=None
test_cases=None
headers=None
company_id=None
def invalidparamstest(invalid_para_url,invalid_params,test_cases,headers,count,failed_count):
    
   
    for test,description in test_cases:
        invalid_params = {
        "page": 1,                  
        "ignorePaging":False,
        "size": 2,          
        "name":"TestDep",
        "sort":-1,
        "isActive":True
        # "search": "f",   

    }


     
        invalid_para_url=f"https://qa-admin.zolv.health/api/v1/masters/area/web/{company_id}/get-area-list?"
        response_invalidparams = requests.get(invalid_para_url,invalid_params,headers=headers)
        if response_invalidparams.status_code == 200:
            invalid_json = response_invalidparams.json()
            # print(invalid_para_url)
            # print("Response JSON : ",json.dumps(invalid_json,indent=4))
            token1= invalid_json.get('token',{}).get('token')
            count+=1
            print(f"\033[91m❌ Test Case ID - 004   : {description}  :  Error - Invalid Input Format :  TEST FAILED...!\033[0m") # login success so test failed becoz in oms logged with oms in other 3 credentials kds,go,testoms
            failed_count+=1

        
        else:
            print(f"\033[1;92m✅ Test Case ID - 004   : {description}  :  TEST PASSED...!\033[0m",response_invalidparams.status_code) 


   
    # if count in [0,10]:
    #     failed_count+=1
    
# invalidparams(invalid_para_url,invalid_params,test_cases,headers,count,failed_count)


