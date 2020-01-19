# ip address is of the format: x.x.x.x; where x is from 0 to 255

import random
import requests as rq
import json 

def random_ip_address():
    return str(random.randint(0, 256)) + "." + str(random.randint(0, 256)) + "." + str(random.randrange(0, 256)) + "." + str(random.randint(0, 256))

def main():
    while True:
        rand_ip = random_ip_address()
        response = rq.get("http://ip-api.com/json/" + rand_ip)
        x = response.json()
        if x['status'] == "fail":
            continue
        print(x["regionName"] + ", " + x["country"] + " : " + rand_ip)
        proceed = input("Proceed?(y/n) ")
        if proceed == 'n' or proceed == 'N':
            print("\nThank you for using Suyash's random Location and IP generator!")
            break

main()