from travelperk_python_api_types.trips.trips.trips import Trips
from travelperk_python_api_types.trips.trips.trip import Trip
from travelperk_python_api_types.trips.bookings.bookings import Bookings
from travelperk_python_api_types.trips.bookings.booking import Booking
from travelperk_python_api_types.trips.location import Location
from travelperk_python_api_types.trips.bookings.reference import Reference
from travelperk_python_api_types.trips.bookings.leg import Leg
from travelperk_python_api_types.trips.bookings.segment import Segment
from travelperk_python_api_types.trips.bookings.origin import Origin
from travelperk_python_api_types.trips.bookings.destination import Destination


class TestTrips:
    def test_trips_entities_are_buildable(self):
        trips = Trips(
            **{
                "trips": [
                    {
                        "id": "172",
                        "booker_id": "172",
                        "trip_name": "The Great Voyage",
                        "start": "2020-11-20T00:00:00",
                        "end": "2020-11-25T00:00:00",
                        "status": "booked",
                        "modified": "2020-09-16T07:08:06.290253+00:00",
                    },
                    {
                        "id": "205",
                        "booker_id": "205",
                        "trip_name": "Road trip Barcelona",
                        "start": "2020-09-25T10:00:00+00:00",
                        "end": "2020-09-26T10:00:00+00:00",
                        "status": "booked",
                        "modified": "2020-09-14T12:55:06.720754+00:00",
                    },
                ],
                "limit": 10,
                "offset": 0,
                "total": 2,
            }
        )
        assert type(trips) is Trips
        assert type(trips.trips[0]) is Trip

    def test_bookings_entities_are_buildable(self):
        bookings = Bookings(
            **{
                "bookings": [
                    {
                        "id": "70",
                        "start": "2021-03-06T00: 00: 00+00: 00",
                        "end": "2021-03-07T00: 00: 00+00: 00",
                        "type": "flight",
                        "status": "ticketed",
                        "modified": "2021-01-02T11: 11: 20.714987+00: 00",
                        "trip_id": "51",
                        "references": [{"type": "PNR", "value": "HNTCEBSMPO"}],
                        "location": {
                            "name": "Test location",
                            "address": "",
                            "latitude": "59.5468062",
                            "longitude": "113.9913155",
                            "iata_code": None,
                        },
                        "legs": [
                            {
                                "segments": [
                                    {
                                        "origin": {
                                            "location": {
                                                "name": "",
                                                "address": "",
                                                "latitude": "85.5975436",
                                                "longitude": "18.7959996",
                                                "iata_code": "UYM",
                                            },
                                            "time": "2021-03-06T00: 00: 00+01: 00",
                                        },
                                        "destination": {
                                            "location": {
                                                "name": "",
                                                "address": "",
                                                "latitude": "-54.3854772",
                                                "longitude": "81.6402173",
                                                "iata_code": "EKD",
                                            },
                                            "time": "2021-03-07T12: 00: 00+01: 00",
                                        },
                                        "external_id": "XX1234",
                                    },
                                    {
                                        "origin": {
                                            "location": {
                                                "name": "",
                                                "address": "",
                                                "latitude": "67.1291014",
                                                "longitude": "21.1347543",
                                                "iata_code": "IWP",
                                            },
                                            "time": "2021-03-08T00: 00: 00+01: 00",
                                        },
                                        "destination": {
                                            "location": {
                                                "name": "",
                                                "address": "",
                                                "latitude": "8.6677113",
                                                "longitude": "-13.9691879",
                                                "iata_code": "TMQ",
                                            },
                                            "time": "2021-03-09T12: 00: 00+01: 00",
                                        },
                                        "external_id": "XX1234",
                                    },
                                ]
                            },
                            {
                                "segments": [
                                    {
                                        "origin": {
                                            "location": {
                                                "name": "",
                                                "address": "",
                                                "latitude": "23.5841460",
                                                "longitude": "-141.9148137",
                                                "iata_code": "UJH",
                                            },
                                            "time": "2021-03-10T12: 00: 00+01: 00",
                                        },
                                        "destination": {
                                            "location": {
                                                "name": "",
                                                "address": "",
                                                "latitude": "-6.0933315",
                                                "longitude": "-7.6775088",
                                                "iata_code": "ZVO",
                                            },
                                            "time": "2021-03-11T00: 00: 00+01: 00",
                                        },
                                        "external_id": "XX1234",
                                    },
                                    {
                                        "origin": {
                                            "location": {
                                                "name": "",
                                                "address": "",
                                                "latitude": "78.4132615",
                                                "longitude": "-156.7342795",
                                                "iata_code": "OJR",
                                            },
                                            "time": "2021-03-12T12: 00: 00+01: 00",
                                        },
                                        "destination": {
                                            "location": {
                                                "name": "",
                                                "address": "",
                                                "latitude": "-44.6617225",
                                                "longitude": "163.2773819",
                                                "iata_code": "YNX",
                                            },
                                            "time": "2021-03-13T00: 00: 00+01: 00",
                                        },
                                        "external_id": "XX1234",
                                    },
                                ]
                            },
                        ],
                    },
                ],
                "limit": 10,
                "offset": 0,
                "total": 4,
            }
        )
        assert type(bookings) is Bookings
        assert type(bookings.bookings[0]) is Booking
        assert type(bookings.bookings[0].references[0]) is Reference
        assert type(bookings.bookings[0].location) is Location
        assert type(bookings.bookings[0].legs[0]) is Leg
        assert type(bookings.bookings[0].legs[0].segments[0]) is Segment
        assert type(bookings.bookings[0].legs[0].segments[0].origin) is Origin
        assert type(bookings.bookings[0].legs[0].segments[0].destination) is Destination
