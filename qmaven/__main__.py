from .maven import MavenAPI
from pprint import pprint
import json

response = MavenAPI.search("rxjava")
if response.encoding:
    decoded_content = response.content.decode(response.encoding)
else:
    decoded_content = response.content.decode("utf-8")

json_response = json.loads(decoded_content)
array_results = json_response["response"]["docs"]
pprint(array_results)

for result in array_results:
    print(result["g"])
    print(result["id"])
