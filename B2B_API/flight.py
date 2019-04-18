from flask import request
import requests, json, calendar, time

from config import SECRET_KEY, BUSINESS_ID, BUSINESS_NAME, ENDPOINT_URI

def getToken():
    url = ENDPOINT_URI + '/apiv1/payexpress?method=getToken&secretkey=' + SECRET_KEY + '&output=json'
    response = getAPI(url)

    return response

def searchFlight():
    TOKEN = request.headers['TOKEN']
    departure = request.args.get('departure')
    arrival = request.args.get('arrival')
    date = request.args.get('date')
    ret_date = request.args.get('ret_date')
    adult = request.args.get('adult')
    child = request.args.get('child')
    infant = request.args.get('infant')

    qString = ''
    if departure:
        qString += 'd=' + departure + '&'

    if arrival:
        qString += 'a=' + arrival + '&'

    if date:
        qString += 'date=' + date + '&'

    if ret_date:
        qString += 'ret_date=' + ret_date + '&'

    if adult:
        qString += 'adult=' + str(adult) + '&'

    if child:
        qString += 'child=' + str(child) + '&'

    if infant:
        qString += 'infant=' + str(infant) + '&'

    qString += 'token=' + TOKEN + '&output=json&'

    url = ENDPOINT_URI + '/search/flight?' + qString[:-1]

    response = getAPI(url)

    return response

def searchNearestAirport():
    TOKEN = request.headers['TOKEN']
    ip_address = request.args.get('ip')
    longitude = request.args.get('long')
    latitude = request.args.get('lat')

    qString = ''
    if ip_address:
        qString += 'ip=' + ip_address + '&'

    if longitude:
        qString += 'longitude=' + longitude + '&'

    if latitude:
        qString += 'latitude=' + latitude + '&'

    qString += 'token=' + TOKEN + '&output=json&'

    url = ENDPOINT_URI + '/flight_api/getNearestAirport?' + qString[:-1]
    response = getAPI(url)

    return response

def searchPopularAirport():
    TOKEN = request.headers['TOKEN']
    depart = request.args.get('depart')

    qString = ''
    if depart:
        qString += 'depart=' + depart + '&'

    qString += 'token=' + TOKEN + '&output=json&'

    url = ENDPOINT_URI + '/flight_api/getPopularDestination?' + qString[:-1]
    response = getAPI(url)

    return response

def searchAirport():
    TOKEN = request.headers['TOKEN']

    qString = 'token=' + TOKEN + '&output=json&'

    url = ENDPOINT_URI + '/flight_api/all_airport?' + qString[:-1]
    response = getAPI(url)

    return response

def checkFlightUpdated():
    TOKEN = request.headers['TOKEN']
    departure = request.args.get('departure')
    arrival = request.args.get('arrival')
    date = request.args.get('date')
    adult = request.args.get('adult')
    child = request.args.get('child')
    infant = request.args.get('infant')

    #set currnent timestamp
    timestamp = calendar.timegm(time.gmtime())

    qString = ''
    if departure:
        qString += 'd=' + departure + '&'

    if arrival:
        qString += 'a=' + arrival + '&'

    if date:
        qString += 'date=' + date + '&'

    if adult:
        qString += 'adult=' + str(adult) + '&'

    if child:
        qString += 'child=' + str(child) + '&'

    if infant:
        qString += 'infant=' + str(infant) + '&'

    qString += 'time=' + str(timestamp) + '&'
    qString += 'token=' + TOKEN + '&output=json&'

    url = ENDPOINT_URI + '/ajax/mCheckFlightUpdated?' + qString[:-1]

    response = getAPI(url)

    return response

def getLionCaptcha():
    TOKEN = request.headers['TOKEN']

    qString = 'token=' + TOKEN + '&output=json&'

    url = ENDPOINT_URI + '/flight_api/getLionCaptcha?' + qString[:-1]

    response = getAPI(url)

    return response

def getFlightData():
    TOKEN = request.headers['TOKEN']
    flight_id = request.args.get('flight_id')
    date = request.args.get('date')
    ret_flight_id = request.args.get('ret_flight_id')
    ret_date = request.args.get('ret_date')

    qString = ''
    if flight_id:
        qString += 'flight_id=' + flight_id + '&'

    if ret_flight_id:
        qString += 'ret_flight_id=' + ret_flight_id + '&'

    if date:
        qString += 'date=' + date + '&'

    if ret_date:
        qString += 'ret_date=' + ret_date + '&'

    qString += 'token=' + TOKEN + '&output=json&'

    url = ENDPOINT_URI + '/flight_api/get_flight_data?' + qString[:-1]

    response = getAPI(url)

    return response



#private function
def getAPI(URL):
    header = {'twh': BUSINESS_ID + ';' + BUSINESS_NAME + ';' }
    try:
        res = requests.get(URL, headers=header)
        # res = requests.get(URL)
        res.raise_for_status()

        response = {"status": 200, "data": res.json()}
    except Exception as e:
        err = str(e)
        if '400' in err:
            code = 400
            error_message = json.loads(e.response.text)
            message = error_message["error"]["message"]
        else:
            code = 403
            message = err

        response = {"status": code, "message": message}

    return response

