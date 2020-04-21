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

recordCount = len(data)
loopCount = 0
while loopCount < recordCount:
    candidateIPString = (data[loopCount]['lanIp'])
    deviceSerialNumber = (data[loopCount]["serial"])
    if ipCheck(candidateIPString) == True:
        print(f"{candidateIPString} is a Valid IP Address for Serial {deviceSerialNumber}")
    else:
        print(f"{candidateIPString} is Not a Valid IP Address for Serial {deviceSerialNumber}")



    loopCount = loopCount + 1









