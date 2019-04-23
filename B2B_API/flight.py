from flask import request
import requests, json, calendar, time, urllib.parse

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

def addOrder():
    TOKEN = request.headers['TOKEN']
    data = request.data
    dataOrder = json.loads(data)

    flight_id = dataOrder['flight_id']
    ret_flight_id = dataOrder['ret_flight_id']
    lion_captcha = dataOrder['lion_captcha']
    lion_session_id = dataOrder['lion_session_id']
    adult = dataOrder['adult']
    child = dataOrder['child']
    infant = dataOrder['infant']
    con_salutation = dataOrder['con_salutation']
    con_first_name = dataOrder['con_first_name']
    con_last_name = dataOrder['con_last_name']
    con_phone = dataOrder['con_phone']
    con_other_phone = dataOrder['con_other_phone']
    con_email_address = dataOrder['con_email_address']

    qString = ''
    if flight_id:
        qString += 'flight_id=' + flight_id + '&'

    if ret_flight_id:
        qString += 'ret_flight_id=' + ret_flight_id + '&'

    if lion_captcha:
        qString += 'lioncaptcha=' + lion_captcha + '&'

    if lion_session_id:
        qString += 'lionsessionid=' + lion_session_id + '&'

    if con_salutation:
        qString += 'conSalutation=' + con_salutation + '&'

    if con_first_name:
        qString += 'conFirstName=' + con_first_name + '&'

    if con_last_name:
        qString += 'conLastName=' + con_last_name + '&'

    if con_phone:
        qString += 'conPhone=' + urllib.parse.quote_plus(con_phone) + '&'

    if con_other_phone:
        qString += 'conOtherPhone=' + urllib.parse.quote_plus(con_other_phone) + '&'

    if con_email_address:
        qString += 'conEmailAddress=' + con_email_address + '&'

    #set passenger
    if adult:
        qString += 'adult=' + str(adult) + '&'

        i_adult = 1
        for adultPasenger in dataOrder['adult_passenger']:
            qString += 'ida'+ str(i_adult) + '=' + adultPasenger['id'] + '&'
            qString += 'titlea'+ str(i_adult) + '=' + adultPasenger['title'] + '&'
            qString += 'firstnamea'+ str(i_adult) + '=' + adultPasenger['firstname'] + '&'
            qString += 'lastnamea'+ str(i_adult) + '=' + adultPasenger['lastname'] + '&'
            qString += 'birthdatea'+ str(i_adult) + '=' + adultPasenger['birthdate'] + '&'

            i_adult += 1

    if child:
        qString += 'child=' + str(child) + '&'

        i_child = 1
        for childPasenger in dataOrder['child_passenger']:
            qString += 'idc'+ str(i_child) + '=' + childPasenger['id'] + '&'
            qString += 'titlec'+ str(i_child) + '=' + childPasenger['title'] + '&'
            qString += 'firstnamec'+ str(i_child) + '=' + childPasenger['firstname'] + '&'
            qString += 'lastnamec'+ str(i_child) + '=' + childPasenger['lastname'] + '&'
            qString += 'birthdatec'+ str(i_child) + '=' + childPasenger['birthdate'] + '&'

            i_child += 1

    if infant:
        qString += 'infant=' + str(infant) + '&'

        i_infant = 1
        for infantPasenger in dataOrder['infant_passenger']:
            qString += 'idc' + str(i_infant) + '=' + infantPasenger['id'] + '&'
            qString += 'titlei'+ str(i_infant) + '=' + infantPasenger['title'] + '&'
            qString += 'firstnamei'+ str(i_infant) + '=' + infantPasenger['firstname'] + '&'
            qString += 'lastnamei'+ str(i_infant) + '=' + infantPasenger['lastname'] + '&'
            qString += 'birthdatei'+ str(i_infant) + '=' + infantPasenger['birthdate'] + '&'
            qString += 'parenti'+ str(i_infant) + '=' + str(infantPasenger['parent']) + '&'

            i_infant += 1


    qString += 'token=' + TOKEN + '&output=json&'

    url = ENDPOINT_URI + '/order/add/flight?' + qString[:-1]

    response = getAPI(url)

    #confirm this order
    if response["status"] == 200:
        qString2 = 'token=' + TOKEN + '&output=json&'

        url = ENDPOINT_URI + '/order?' + qString2[:-1]

        response = getAPI(url)

    return response

def deleteOrder(order_id):
    TOKEN = request.headers['TOKEN']
    orderId = order_id

    qString = ''
    if orderId:
        qString += 'order_detail_id=' + orderId + '&'

    qString += 'token=' + TOKEN + '&output=json&'

    url = ENDPOINT_URI + '/order/delete_order?' + qString[:-1]

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

