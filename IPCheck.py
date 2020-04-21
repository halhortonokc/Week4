import json

def ipCheck(candidateIPString):
    candidateIPList = candidateIPString.split(".")
    octetCount = len(candidateIPList)
    if octetCount != 4:
        isValidIP = False
    elif int(candidateIPList[0])<=255 and int(candidateIPList[1])<=255 and int(candidateIPList[2])<=255 and int(candidateIPList[3])<=255:
        isValidIP = True
    else:
        isValidIP = False
    return(isValidIP)


serialData = open ('jsonData', "r")
data = json.load(serialData)



for record in data:
    candidateIPString = record['lanIp']
    deviceSerialNumber = record["serial"]
    if ipCheck(candidateIPString) == True:
        print(f"{candidateIPString} is a Valid IP Address for Serial {deviceSerialNumber}")
    else:
        print(f"{candidateIPString} is Not a Valid IP Address for Serial {deviceSerialNumber}")










