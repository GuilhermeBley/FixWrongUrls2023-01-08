import mysql.connector
import requests
from VehicleRepository import VehicleRepository

host="your_host",
user="your_username",
password="your_password",
database="your_database"

vehicleRepo = VehicleRepository(host, user, password, database)

skip = 0
take = 1000

while (True):
    
    itemsToTryUpdate = vehicleRepo.getWithInvalidPartialKey(skip, take)

    if (itemsToTryUpdate.count() == 0):
        break
    
    for item in itemsToTryUpdate:
        fsId = item[0]
        partialKey = item[1]
        url = item[2]
        fsmdId = item[3]

        correctUrl = url.replace(' ', '')

        response = requests.get(correctUrl)

        if (response.status_code == 404):
            print('Id {fsId} was not found.')
            continue # go next to  try update

        # do update

        correctPartialKey = partialKey.replace(' ', '')

        vehicleRepo.updateFileAndFileMetaData(fsId, fsmdId, correctPartialKey, correctUrl)
