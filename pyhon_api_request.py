import requests
# from requests.exceptions import HTTPError
import json


api_url = "https://tahura.rw/api/users/login.php"
user_email = "eugen4e@gmail.com"
password = "kigali2921"

#construct auth user object
#send a post request 
auth_user = {"e_mail":user_email,"password":password}
# print(auth_user)
# response = requests.post(api_url, json=auth_user)
# print(api_url)

# #check the status code
# if response.status_code == 200:
#     resp_data = response.json()
#     print({
#         "message":"welcome, user logged in succcesfully ",
#         "data":resp_data,
#         "status":response.status_code,
#         "headers": response.headers['content-type'],
#         "request-body": response.request.body
#         })
# else:
#     print({
#         "message":"unable to log in. please try again or register",
#         "status":response.status_code,
#         "headers": response.headers['content-type']
#     })
## constract the schedule obj
# schedule_0bj = {
#     "el_id": "f3c5b275f9",
#     "user_id": "JpySxZJkvBtT"
#     }

# schedule_url = "https://tahura.rw/schedule"
# jwt_token = "yourToken"

# #send a schedule wth a post request

# response = requests.post(schedule_url, json=auth_user)
try:
    response = requests.post(api_url, json=auth_user)
    # print(api_url)

#check the status code
# if response.status_code == 200:
    resp_data = response.json()
    print({
        "message":"welcome, user logged in succcesfully ",
        "data":resp_data,
        "status":response.status_code,
        "headers": response.headers['content-type'],
        # "request-body": response.request.body
        })

except Exception as err:
    print({
        "message":"unable to log in. please try again or register",
        # "status":response.status_code,
        "error": err
    })
