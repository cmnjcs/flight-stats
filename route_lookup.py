import json
import urllib2

# keys
import codes

# test data
import bos_sea_data
import sample_data


appId = codes.appId
appKey = codes.appKey

depart_ap = 'BOS'
arrival_ap = 'SEA'
year = '2013'
month = '12'
day = '13'

depart_ap = raw_input('Departure airport: ')
arrival_ap = raw_input('Arrival airport: ')
(month, day, year) = raw_input('Depature date (MM/DD/YYYY): ').split('/')

codeType = 'IATA'

url = 'https://api.flightstats.com/flex/flightstatus/rest/v2/json/route/status/' + \
		depart_ap + '/' + \
		arrival_ap + '/dep/' + \
		year + '/' + month + '/' + day + '?' + \
		'appId=' + appId + '&appKey=' + appKey + \
		'&hourOfDay=0&utc=false&numHours=24&codeType=IATA&maxFlights=5'

#testUrl = 'https://api.flightstats.com/flex/flightstatus/rest/v2/json/route/status/BOS/SEA/dep/2013/12/13?appId=015d2e15&appKey=b98718a9c785fc9ea31ba1ea12af9b47&hourOfDay=0&utc=false&numHours=24&codeType=IATA&maxFlights=5'

#if not (testUrl == url):
#	for x in range(0, len(testUrl)):
#		print url[x],testUrl[x]
#		if not(url[x] == testUrl[x]):
#			print "!!!!!!!!!!"


## Enable for live data
#j son_data = urllib2.urlopen(url)
# data = json.load(json_data)

## Enable for testing data
data = bos_sea_data.route_lookup_data

# print data

flights = {}

for flight in data['flightStatuses']:
	flights[flight['carrierFsCode'] + ' ' + flight['flightNumber']] = flight['flightId']

list_o_keys = flights.keys()
list_o_keys.sort()

print  str(len(flights.keys())) + ' flights found:'

for index in range(0, len(list_o_keys)):
	print str(index) + '. ' + list_o_keys[index]

while True:
	flight_select = int(raw_input('Select flight to look up: '))
	if not (flight_select > len(list_o_keys) - 1 or flight_select < 0):
		break

flight_id = str(flights[list_o_keys[flight_select]])

url2 = 'https://api.flightstats.com/flex/flightstatus/rest/v2/json/flight/status/' + \
		flight_id + '?appId=015d2e15&appKey=b98718a9c785fc9ea31ba1ea12af9b47'

#json_data2 = urllib2.urlopen(url2)
#data2 = json.load(json_data2)

for flight in data['flightStatuses']:
	#print flight['flightId'], flight_id, type(flight['flightId'])
	if(str(flight['flightId']) == flight_id):
		data2 = {'flightStatus': flight}
		break

#data2 = bos_sea_data.flight_lookup_data

#print data2

#print data2.keys()

#print data2['flightStatus'].keys()
#for x in data2['flightStatus'].keys():
#	print x

#print data2['flightStatus']['airportResources']
#for x in data2['flightStatus']['airportResources'].keys():
#	print x

#print data2['flightStatus']['operationalTimes']
#for x in data2['flightStatus']['operationalTimes'].keys():
#	print x

# date/time processing
sched_depart = ''
est_depart = ''
sched_arr = ''
est_arr = ''
act_depart = ''
act_arrival = ''

if 'scheduledGateDeparture' in data2['flightStatus']['operationalTimes'].keys():
	sched_depart = str(data2['flightStatus']['operationalTimes']['scheduledGateDeparture']['dateLocal'])
	sched_depart = sched_depart[sched_depart.index('T') + 1:]
	(hour, minute, second) = sched_depart.split(':')
	sched_depart = hour + minute
	#print sched_depart

if 'estimatedGateDeparture' in data2['flightStatus']['operationalTimes'].keys():
	est_depart = str(data2['flightStatus']['operationalTimes']['estimatedGateDeparture']['dateLocal'])
	est_depart = est_depart[est_depart.index('T') + 1:]
	(hour, minute, second) = est_depart.split(':')
	est_depart = hour + minute
	#print est_depart

if 'scheduledGateArrival' in data2['flightStatus']['operationalTimes'].keys():
	sched_arr = str(data2['flightStatus']['operationalTimes']['scheduledGateArrival']['dateLocal'])
	sched_arr = sched_arr[sched_arr.index('T') + 1:]
	(hour, minute, second) = sched_arr.split(':')
	sched_arr = hour + minute
	#print sched_arr

if 'estimatedGateArrival' in data2['flightStatus']['operationalTimes'].keys():
	est_arr = str(data2['flightStatus']['operationalTimes']['estimatedGateArrival']['dateLocal'])
	est_arr = est_arr[est_arr.index('T') + 1:]
	(hour, minute, second) = est_arr.split(':')
	est_arr = hour + minute
	#print est_arr

# gate info processing
departureGate = ''
if 'departureTerminal' in data2['flightStatus']['airportResources']:
	if 'departureGate' in data2['flightStatus']['airportResources']:
		departureGate = data2['flightStatus']['airportResources']['departureGate']
	departureGate = data2['flightStatus']['airportResources']['departureTerminal'] + ' ' + departureGate

arrivalGate = ''
if 'arrivalTerminal' in data2['flightStatus']['airportResources']:
	if 'arrivalGate' in data2['flightStatus']['airportResources']:
		arrivalGate = data2['flightStatus']['airportResources']['arrivalGate']
	arrivalGate = data2['flightStatus']['airportResources']['arrivalTerminal'] + ' ' + arrivalGate

codeshares = ''
# codeshare processing
if 'codeshares' in data2['flightStatus'].keys():
	codeshares = 'Also operating as:\n'
	for flight in data2['flightStatus']['codeshares']:
		codeshares += flight['fsCode'] + ' ' + flight['flightNumber'] + "\n"


print "FLIGHT INFO"
print list_o_keys[flight_select]
print "Dep: " + departureGate
print "Arr: " + arrivalGate

print "Sched.	ETD	ATD	Sched.	ETA	ATA"
print sched_depart + '\t' + est_depart + '\t' + act_depart
print '\t\t\t' + sched_arr + '\t' + est_arr + '\t' + act_arrival

print 'EQP: ' + data2['flightStatus']['flightEquipment']['scheduledEquipmentIataCode']
print codeshares
