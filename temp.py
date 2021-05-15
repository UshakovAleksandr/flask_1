
import requests

url = "https://api-blog-flask.herokuapp.com/users"
resp = requests.get(url)
print(resp.json())


#
# resp = requests.get(f"{url}/alive")
# print(resp.status_code)
# print(resp.json())

# resp = requests.get(f"{url}/notes/8")
# print(resp.status_code)
# print(resp.json())

# data = {
#     "header": "note2",
#     "note_text":"text2",
#     "author": "admin2"
# }
# resp = requests.post(f"{url}/notes", json=data)
# print(resp.status_code)
# print(resp.json())

# resp = requests.get(f"{url}/notes")
# print(resp.status_code)
# print(resp.json())

# resp = requests.put(f"{url}/notes/3",
#                     json={"header": "new",
#                           "author": "admin"})
# print(resp.status_code)
# print(resp.json())

# resp = requests.delete(f"{url}/notes/6")
# print(resp.status_code)
# print(resp.json())