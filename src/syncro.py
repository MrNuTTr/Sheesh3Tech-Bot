import json
import requests
from requests.structures import CaseInsensitiveDict

# See https://reqbin.com/req/python/c-xgafmluu/convert-curl-to-python-requests

# Load the file containing needed tokens
token_file = open("tokens.json")
# Parse the json into a python object
tokens = json.load(token_file)
# Close the file
token_file.close()

baseurl = "https://myc3.syncromsp.com/api/v1/"

def get_ticket_number():
    page_num = 1
    url = baseurl + "tickets?status=Not%20Resolved&page=" + str(page_num)

    headers = CaseInsensitiveDict()
    headers["accept"] = "application/json"
    headers["Authorization"] = tokens["syncro"]

    response = requests.get(url, headers=headers)
    print(response.json())

get_ticket_number()