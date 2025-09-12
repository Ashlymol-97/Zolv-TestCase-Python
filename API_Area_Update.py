
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

# login_test(login_url, login_payload, failed_count)






# 2 : Area Update : Valid Area Name : 


def area_test_case(test_case_id, action, payload, base_url, company_id, headers, failed_count, area_id=None):
    """
    Reusable function for both create and update area.
    :param action: "create" or "update"
    :param payload: dict (the JSON payload)
    :param area_id: required for update
    """

    if action == "create":
        url = base_url + f"api/v1/masters/area/web/{company_id}/create-area"
        response = requests.post(url, json=payload, headers=headers)
    elif action == "update":
        if not area_id:
            print("\033[91m❌ Update requires area_id!\033[0m")
            return
        url = base_url + f"api/v1/masters/area/web/{company_id}/update-area/{area_id}"
        response = requests.patch(url, json=payload, headers=headers)
    else:
        print("\033[91m❌ Invalid action! Must be 'create' or 'update'\033[0m")
        return

    if response.status_code == 200:
        result = response.json()
        print(f"\033[92m✅ Test Case ID - 00{test_case_id} : {action.upper()} SUCCESS\033[0m")
        return result.get("id")  # return area_id for reuse
    else:
        print(f"\033[91m❌ Test Case ID - 00{test_case_id} : {action.upper()} FAILED : {response.text}\033[0m")
        failed_count += 1
        return None












# create_payload = {
#     "name": "Areanametest",
#     "code": 33,
#     "areaType": "parent",
#     "parentAreaId": "",
#     "buildingId": "68709372293ae6389032a058",
#     "floorId": "68709372293ae6389032a05a",
#     "isActive": True,
#     "moduleGroupId": "68709372293ae6389032a05b",
#     "paymentModes": [
#         {"name": "paymentGateway", "enabled": True},
#         {"name": "payOnDelivery", "enabled": True},
#         {"name": "roomCredit", "enabled": True}
#     ],
#     "deliveryModes": [
#         {"name": "roomDelivery", "enabled": True},
#         {"name": "takeAway", "enabled": True},
#         {"name": "dineIn", "enabled": True}
#     ],
#     "preOrderStatus": False
# }

# area_id = area_test_case(
#     test_case_id=2, action="create",
#     payload=create_payload,
#     base_url=base_url, company_id=company_id, headers=headers,
#     failed_count=0
# )




# update_payload = {
#     "name": "Casuality",
#     "code": 212,
#     "areaType": "child",
#     "parentAreaId": "67da8adb9ac9dd502edd0e99",
#     "buildingId": "67d166a556850730f60a8b0a",
#     "floorId": "67d3ccd36a26b12fb436b97d",
#     "isActive": True,
#     "moduleGroupId": "67da52349ac9dd502edd0e88",
#     "paymentModes": [
#         {"name": "paymentGateway", "enabled": True},
#         {"name": "cashOnDelivery", "enabled": False},
#         {"name": "roomCredit", "enabled": True}
#     ],
#     "deliveryModes": [
#         {"name": "roomDelivery", "enabled": True},
#         {"name": "takeAway", "enabled": False},
#         {"name": "dineIn", "enabled": True}
#     ],
#     "preOrderStatus": False,
#     "qrKey": "ABC123XYZ",
#     "qrImage": "base64_encoded_image_string",
#     "languageId": "60b1a233cd2b2c72e9e8d89b"
# }

# area_test_case(
#     test_case_id=3, action="update",
#     payload=update_payload,
#     base_url=base_url, company_id=company_id, headers=headers,
#     failed_count=0,
#     area_id=area_id   # from create step
# )

