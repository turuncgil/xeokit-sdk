import requests
from requests_ntlm import HttpNtlmAuth
import json
from requests.structures import CaseInsensitiveDict
import ifcopenshell.util

def getTokenByUsernameAndPassword():
    endpoint = 'https://info.nestcollaboration.ch/gateway/v2/user/login'
    data = '{ "username": "akel@nest.local", "password": "n3EsT?!4ever%20?22" }'
    headers = {'Content-Type': 'application/json'}

    # Call API
    result = requests.post(endpoint, headers=headers, data=data)

    loginRes = json.loads(result.content)
    token = loginRes['token']
    return token


def getAllSystemDatas(token):
    endpoint = "https://info.nestcollaboration.ch/db/metadata"

    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Authorization"] = "Bearer " + token

    resp = requests.get(endpoint, headers=headers)

    # returns JSON object as
    # a dictionary
    return json.loads(resp.content)


def getSensorResponseByNumericId(numericId):
    # API base url
    baseUrl = 'https://visualizer.nestcollaboration.ch/Realtime/data/'
    requestUrl = baseUrl + numericId
    df_read = requests.get(requestUrl, auth=HttpNtlmAuth('akel', 'n3EsT?!4ever%20?22'))
    return df_read


def getSensorData(systemDatas):
    sensorData = []

    for data in systemDatas:
        location_buildingDistrict = str(data['location_buildingDistrict'])
        datapoint_Unit = str(data['datapoint_Unit'])
        if location_buildingDistrict == 'Unit UMAR':
            if datapoint_Unit == '°C':
                numericId = str(data['numericid'])

                # Call the API for sensor values
                df_read = getSensorResponseByNumericId(numericId)

                # Room
                roomNumber = str(data['location_roomNr'])

                # Datapoint signal desc
                datapoint_SignalDescription = str(data['datapoint_SignalDescription'])

                abc = [(roomNumber), (datapoint_SignalDescription), df_read.content]
                sensorData.append(abc)
                # print(sensorData)

    return sensorData


def getSpacesByIfc(ifcFile):
    products = ifcFile.by_type("IfcProduct")
    spaces = []
    for i in products:
        if i.is_a("IfcSpace"):
            spaces.append(i)

    print(spaces)
    return spaces

def Average(lst):
    return sum(lst) / len(lst)


def writeSensorDataToIfcFile(ifcFile, ifcFileSpaces, mno):

    owner_history = ifcFile.by_type("IfcOwnerHistory")[0]

    # loop in ifc file spaces
    for space in ifcFileSpaces:

        # space of ifc file contains room number in second index
        ifcSpaceRoomNumber = space[2]

        value_result_list = []

        # loop in API sensor values
        for sensorData in mno:

            # 0. index is room number
            apiRoomNumber = sensorData[0]

            # 2. index is sensor data values(json)
            sensorValue = json.loads(sensorData[2])

            if len(sensorValue) > 0:
                if apiRoomNumber == ifcSpaceRoomNumber:
                    print('Room API ' + apiRoomNumber)
                    print('Room IFC ' + ifcSpaceRoomNumber)
                    val = sensorValue[0]['value']
                    value_result_list.append(val)

        if len(value_result_list) > 0:
            average = Average(value_result_list)
            print(average)

            property_values = [
                ifcFile.createIfcPropertySingleValue("SpaceThermalRequirements", "SpaceTemperature", space,
                                                     ifcFile.create_entity("IfcThermodynamicTemperatureMeasure",
                                                                           average))
            ]
            property_set = ifcFile.createIfcPropertySet(space.GlobalId, owner_history, "SpaceThermalRequirements",
                                                        None, property_values)
            ifcFile.createIfcRelDefinesByProperties(space.GlobalId, owner_history, None, None, [space],
                                                    property_set)

    ifcFile.write('../output/output.ifc')

def buildIFCFile():
    # get token
    token = getTokenByUsernameAndPassword()
    systemDatas = getAllSystemDatas(token)
    sensorData = getSensorData(systemDatas)

    # m is room number
    # n is data signal desc
    # o is all sensor values
    mno = sensorData

    ifcFile = ifcopenshell.open('../input/input.ifc')
    ifcFileSpaces = getSpacesByIfc(ifcFile)
    writeSensorDataToIfcFile(ifcFile, ifcFileSpaces, mno)

if __name__ == '__main__':
    buildIFCFile()
