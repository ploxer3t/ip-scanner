import requests
from termcolor import colored

def get_ip_info(ip_address):
    """Gets the IP address information."""

    # Make a request to the IP address info API.
    response = requests.get("https://ipinfo.io/{}/json".format(ip_address))

    # Parse the JSON response.
    data = response.json()

    # Return the IP address information.
    return data

def main():
    """Gets the IP address information and prints it to the console."""

    # Get the IP address from the user.
    ip_address = input("Enter an IP address: ")

    # Get the IP address information.
    ip_info = get_ip_info(ip_address)

    # Print the IP address information to the console.
    print(colored("IP", "red"), "->", colored(ip_info["ip"], "yellow"))
    print(colored("City", "red"), "->", colored(ip_info["city"], "yellow"))
    print(colored("Region", "red"), "->", colored(ip_info["region"], "yellow"))
    print(colored("Country", "red"), "->", colored(ip_info["country"], "yellow"))
    print(colored("Postal Code", "red"), "->", colored(ip_info["postal"], "yellow"))
    print(colored("Timezone", "red"), "->", colored(ip_info["timezone"], "yellow"))
    print(colored("Coordinates", "red"), "->", colored(ip_info["loc"], "yellow"))
    print(colored("By: @Ploxeret Happy H4CK1NG", "blue"))
if __name__ == "__main__":
    main()
