import requests
 
# POST isteğini göndermek için URL

url = "http://10.36.5.44:5000/webhook"
 
# JSON verisi (istekte boş JSON gönderiyorsunuz)

data = {}
 
# Header bilgisi

headers = {

    "Content-Type": "application/json"

}
 
# POST isteği gönderme

try:

    response = requests.post(url, json=data, headers=headers)
 
    # Yanıtın durum kodunu ve içeriğini yazdırma

    print(f"Status Code: {response.status_code}")

    print(f"Response Text: {response.text}")

except requests.exceptions.RequestException as e:

    print(f"Error: {e}")

 