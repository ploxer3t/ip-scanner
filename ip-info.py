import requests


ip_address = input("Enter IP address: ")


url = f"http://ip-api.com/json/{ip_address}"


response = requests.get(url)


if response.status_code == 200:
    data = response.json()
    print(f"Country: {data['country']}")
    print(f"City: {data['city']}")
    print(f"Region: {data['regionName']}")
    print(f"ISP: {data['isp']}")
    print(f"Latitude: {data['lat']}")
    print(f"Longitude: {data['lon']}")

else:
    print("Error getting location data.")
