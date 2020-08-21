import requests

#Part A - Pull timetamp of now

TIMEURL = "http://date.jsontest.com"
IPURL = "http://ip.jsontest.com"

def main():
    dateresp = requests.post(TIMEURL)
    ipresp = requests.post(IPURL)
    print(dateresp)

    datejson = dateresp.json()
    print(f"Time now is {datejson['time']}")
    
    ipjson = ipresp.json()
    print(f"My IP address is {ipjson['ip']}")

    with open("myservers.txt", "r") as sfile:
        servers = sfile.readlines()
        print("My servers are: ")
        for x in servers:
            print(f"-{x}")

    print(jsonstring)





if __name__ == "__main__":
    main()
