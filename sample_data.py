sample_data = {
 "request": {
  "departureAirport": {
   "requestedCode": "SEA",
   "fsCode": "SEA"
  },
  "arrivalAirport": {
   "requestedCode": "BZN",
   "fsCode": "BZN"
  },
  "date": {
   "year": "2013",
   "month": "12",
   "day": "12",
   "interpreted": "2013-12-12"
  },
  "hourOfDay": {
   "requested": "0",
   "interpreted": 0
  },
  "utc": {
   "requested": "false",
   "interpreted": False
  },
  "numHours": {
   "requested": "24",
   "interpreted": 24
  },
  "codeType": {
   "requested": "IATA",
   "interpreted": "IATA"
  },
  "maxFlights": {
   "requested": "5",
   "interpreted": 5
  },
  "extendedOptions": {},
  "url": "https://api.flightstats.com/flex/flightstatus/rest/v2/json/route/status/SEA/BZN/dep/2013/12/12"
 },
 "appendix": {
  "airlines": [
   {
    "fs": "AS",
    "iata": "AS",
    "icao": "ASA",
    "name": "Alaska Airlines",
    "phoneNumber": "1-800-252-7522",
    "active": True
   },
   {
    "fs": "DL",
    "iata": "DL",
    "icao": "DAL",
    "name": "Delta Air Lines",
    "phoneNumber": "1-800-221-1212",
    "active": True
   },
   {
    "fs": "QX",
    "iata": "QX",
    "icao": "QXE",
    "name": "Horizon Air",
    "active": True
   },
   {
    "fs": "AF",
    "iata": "AF",
    "icao": "AFR",
    "name": "Air France",
    "phoneNumber": "1-800-237-2747",
    "active": True
   },
   {
    "fs": "KE",
    "iata": "KE",
    "icao": "KAL",
    "name": "Korean Air Lines",
    "active": True
   }
  ],
  "airports": [
   {
    "fs": "BZN",
    "iata": "BZN",
    "icao": "KBZN",
    "faa": "BZN",
    "name": "Gallatin Field",
    "street1": "6, Gallatin Field",
    "city": "Bozeman",
    "cityCode": "BZN",
    "stateCode": "MT",
    "postalCode": "59715",
    "countryCode": "US",
    "countryName": "United States",
    "regionName": "North America",
    "timeZoneRegionName": "America/Denver",
    "weatherZone": "MTZ055",
    "localTime": "2013-12-12T20:36:31.043",
    "utcOffsetHours": -7,
    "latitude": 45.777687,
    "longitude": -111.160334,
    "elevationFeet": 4474,
    "classification": 4,
    "active": True,
    "delayIndexUrl": "https://api.flightstats.com/flex/delayindex/rest/v1/json/airports/BZN?codeType=fs",
    "weatherUrl": "https://api.flightstats.com/flex/weather/rest/v1/json/all/BZN?codeType=fs"
   },
   {
    "fs": "SEA",
    "iata": "SEA",
    "icao": "KSEA",
    "faa": "SEA",
    "name": "Seattle-Tacoma International Airport",
    "city": "Seattle",
    "cityCode": "SEA",
    "stateCode": "WA",
    "postalCode": "98158",
    "countryCode": "US",
    "countryName": "United States",
    "regionName": "North America",
    "timeZoneRegionName": "America/Los_Angeles",
    "weatherZone": "WAZ001",
    "localTime": "2013-12-12T19:36:31.043",
    "utcOffsetHours": -8,
    "latitude": 47.443839,
    "longitude": -122.301732,
    "elevationFeet": 429,
    "classification": 1,
    "active": True,
    "delayIndexUrl": "https://api.flightstats.com/flex/delayindex/rest/v1/json/airports/SEA?codeType=fs",
    "weatherUrl": "https://api.flightstats.com/flex/weather/rest/v1/json/all/SEA?codeType=fs"
   }
  ],
  "equipments": [
   {
    "iata": "DH8D",
    "name": "??",
    "turboProp": False,
    "jet": False,
    "widebody": False,
    "regional": False
   },
   {
    "iata": "DH4",
    "name": "De Havilland (Bombardier) DHC-8-400 Dash 8/8Q",
    "turboProp": True,
    "jet": False,
    "widebody": False,
    "regional": True
   }
  ]
 },
 "flightStatuses": [
  {
   "flightId": 318308318,
   "carrierFsCode": "QX",
   "flightNumber": "2460",
   "departureAirportFsCode": "SEA",
   "arrivalAirportFsCode": "BZN",
   "departureDate": {
    "dateLocal": "2013-12-12T12:50:00.000",
    "dateUtc": "2013-12-12T20:50:00.000Z"
   },
   "arrivalDate": {
    "dateLocal": "2013-12-12T15:35:00.000",
    "dateUtc": "2013-12-12T22:35:00.000Z"
   },
   "status": "L",
   "schedule": {
    "flightType": "J",
    "serviceClasses": "Y",
    "restrictions": ""
   },
   "operationalTimes": {
    "publishedDeparture": {
     "dateLocal": "2013-12-12T12:50:00.000",
     "dateUtc": "2013-12-12T20:50:00.000Z"
    },
    "publishedArrival": {
     "dateLocal": "2013-12-12T15:35:00.000",
     "dateUtc": "2013-12-12T22:35:00.000Z"
    },
    "scheduledGateDeparture": {
     "dateLocal": "2013-12-12T12:50:00.000",
     "dateUtc": "2013-12-12T20:50:00.000Z"
    },
    "estimatedGateDeparture": {
     "dateLocal": "2013-12-12T13:08:00.000",
     "dateUtc": "2013-12-12T21:08:00.000Z"
    },
    "actualGateDeparture": {
     "dateLocal": "2013-12-12T13:25:00.000",
     "dateUtc": "2013-12-12T21:25:00.000Z"
    },
    "flightPlanPlannedDeparture": {
     "dateLocal": "2013-12-12T13:33:00.000",
     "dateUtc": "2013-12-12T21:33:00.000Z"
    },
    "estimatedRunwayDeparture": {
     "dateLocal": "2013-12-12T13:33:00.000",
     "dateUtc": "2013-12-12T21:33:00.000Z"
    },
    "actualRunwayDeparture": {
     "dateLocal": "2013-12-12T13:33:00.000",
     "dateUtc": "2013-12-12T21:33:00.000Z"
    },
    "scheduledGateArrival": {
     "dateLocal": "2013-12-12T15:35:00.000",
     "dateUtc": "2013-12-12T22:35:00.000Z"
    },
    "estimatedGateArrival": {
     "dateLocal": "2013-12-12T16:03:00.000",
     "dateUtc": "2013-12-12T23:03:00.000Z"
    },
    "actualGateArrival": {
     "dateLocal": "2013-12-12T15:56:00.000",
     "dateUtc": "2013-12-12T22:56:00.000Z"
    },
    "flightPlanPlannedArrival": {
     "dateLocal": "2013-12-12T15:44:00.000",
     "dateUtc": "2013-12-12T22:44:00.000Z"
    },
    "estimatedRunwayArrival": {
     "dateLocal": "2013-12-12T15:53:00.000",
     "dateUtc": "2013-12-12T22:53:00.000Z"
    },
    "actualRunwayArrival": {
     "dateLocal": "2013-12-12T15:51:00.000",
     "dateUtc": "2013-12-12T22:51:00.000Z"
    }
   },
   "codeshares": [
    {
     "fsCode": "AS",
     "flightNumber": "2460",
     "relationship": "X"
    },
    {
     "fsCode": "DL",
     "flightNumber": "7545",
     "relationship": "Z"
    }
   ],
   "delays": {
    "departureGateDelayMinutes": 35,
    "arrivalGateDelayMinutes": 21,
    "arrivalRunwayDelayMinutes": 7
   },
   "flightDurations": {
    "scheduledBlockMinutes": 105,
    "blockMinutes": 91,
    "scheduledAirMinutes": 71,
    "airMinutes": 78,
    "scheduledTaxiOutMinutes": 43,
    "taxiOutMinutes": 8,
    "taxiInMinutes": 5
   },
   "airportResources": {
    "departureTerminal": "C",
    "departureGate": "16A"
   },
   "flightEquipment": {
    "scheduledEquipmentIataCode": "DH4",
    "actualEquipmentIataCode": "DH8D"
   }
  },
  {
   "flightId": 318308317,
   "carrierFsCode": "QX",
   "flightNumber": "2462",
   "departureAirportFsCode": "SEA",
   "arrivalAirportFsCode": "BZN",
   "departureDate": {
    "dateLocal": "2013-12-12T20:45:00.000",
    "dateUtc": "2013-12-13T04:45:00.000Z"
   },
   "arrivalDate": {
    "dateLocal": "2013-12-12T23:28:00.000",
    "dateUtc": "2013-12-13T06:28:00.000Z"
   },
   "status": "S",
   "schedule": {
    "flightType": "J",
    "serviceClasses": "Y",
    "restrictions": ""
   },
   "operationalTimes": {
    "publishedDeparture": {
     "dateLocal": "2013-12-12T20:45:00.000",
     "dateUtc": "2013-12-13T04:45:00.000Z"
    },
    "publishedArrival": {
     "dateLocal": "2013-12-12T23:28:00.000",
     "dateUtc": "2013-12-13T06:28:00.000Z"
    },
    "scheduledGateDeparture": {
     "dateLocal": "2013-12-12T20:45:00.000",
     "dateUtc": "2013-12-13T04:45:00.000Z"
    },
    "flightPlanPlannedDeparture": {
     "dateLocal": "2013-12-12T20:54:00.000",
     "dateUtc": "2013-12-13T04:54:00.000Z"
    },
    "estimatedRunwayDeparture": {
     "dateLocal": "2013-12-12T20:54:00.000",
     "dateUtc": "2013-12-13T04:54:00.000Z"
    },
    "scheduledGateArrival": {
     "dateLocal": "2013-12-12T23:28:00.000",
     "dateUtc": "2013-12-13T06:28:00.000Z"
    },
    "flightPlanPlannedArrival": {
     "dateLocal": "2013-12-12T23:20:00.000",
     "dateUtc": "2013-12-13T06:20:00.000Z"
    },
    "estimatedRunwayArrival": {
     "dateLocal": "2013-12-12T23:20:00.000",
     "dateUtc": "2013-12-13T06:20:00.000Z"
    }
   },
   "codeshares": [
    {
     "fsCode": "AS",
     "flightNumber": "2462",
     "relationship": "X"
    },
    {
     "fsCode": "KE",
     "flightNumber": "6235",
     "relationship": "Z"
    },
    {
     "fsCode": "AF",
     "flightNumber": "9664",
     "relationship": "Z"
    }
   ],
   "flightDurations": {
    "scheduledBlockMinutes": 103,
    "scheduledAirMinutes": 86,
    "scheduledTaxiOutMinutes": 9,
    "scheduledTaxiInMinutes": 8
   },
   "flightEquipment": {
    "scheduledEquipmentIataCode": "DH4"
   }
  }
 ]
}