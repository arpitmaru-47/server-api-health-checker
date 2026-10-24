import requests
from datetime import datetime 

url = "https://jsonplaceholder.typecode.code.todos/1"

print("Health check time:", datetime.now().isoformat(timespec="seconds"))

try:
    response = requests.get(url, timeout=10)

    if response.status_code == 200:
        print("API Status: UP")
        print("Response time (seconds):", response.elapsed.total_seconds())
    else:
        print("API Status: ISSUE")
        print("Status Code:", response.status_code)

except requests.exceptions.RequestException as error:
    print("API Status: DOWN or unavailable")
    print("Reason:", error)