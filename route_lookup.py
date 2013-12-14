import json
import urllib2

#test data
import bos_sea_data
import sample_data


appId = '015d2e15'
appKey = 'b98718a9c785fc9ea31ba1ea12af9b47'

depart_ap = 'BOS'
arrival_ap = 'SEA'
year = '2013'
month = '12'
day = '13'

# depart_ap = raw_input('Departure airport: ')
# arrival_ap = raw_input('Arrival airport: ')
# date = raw_input('Depature date (MM/DD/YYYY): ').split('/')

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

# json_data = urllib2.urlopen(url)
# data = json.load(json_data)

data = bos_sea_data.route_lookup_data

# print data

flights = {}

for ele in data['flightStatuses']:
	flights[ele['carrierFsCode'] + ' ' + ele['flightNumber']] = ele['flightId']

list_o_keys = flights.keys()
list_o_keys.sort()

print  str(len(flights.keys())) + ' flights found:'

for index in range(0, len(list_o_keys)):
	print str(index + 1) + '. ' + list_o_keys[index]

flight_select = raw_input('Select flight to look up: ')

flight_id = str(flights[list_o_keys[int(flight_select) - 1]])

url2 = 'https://api.flightstats.com/flex/flightstatus/rest/v2/json/flight/status/' + \
		flight_id + '?appId=015d2e15&appKey=b98718a9c785fc9ea31ba1ea12af9b47'

#json_data2 = urllib2.urlopen(url2)
#data2 = json.load(json_data2)

data2 = bos_sea_data.flight_lookup_data

print data2['flightStatus'].keys()
for x in data2['flightStatus'].keys():
	print x

print data2['flightStatus']['operationalTimes']
for x in data2['flightStatus']['operationalTimes'].keys():
	print x
