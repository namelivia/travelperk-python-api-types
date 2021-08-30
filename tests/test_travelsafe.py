from travelperk_python_api_types.travelsafe.summary.summary import Summary
from travelperk_python_api_types.travelsafe.summary.risk_level import RiskLevel
from travelperk_python_api_types.travelsafe.summary.guideline import Guideline
from travelperk_python_api_types.travelsafe.location import Location
from travelperk_python_api_types.travelsafe.info_source import InfoSource
from travelperk_python_api_types.travelsafe.category import Category
from travelperk_python_api_types.travelsafe.airline_measures.airline_measure import (
    AirlineMeasure,
)
from travelperk_python_api_types.travelsafe.airline_measures.airline import Airline
from travelperk_python_api_types.travelsafe.airline_measures.safety_measure import (
    SafetyMeasure,
)
from travelperk_python_api_types.travelsafe.restrictions.restriction import Restriction
from travelperk_python_api_types.travelsafe.restrictions.requirement import Requirement
from travelperk_python_api_types.travelsafe.restrictions.document import Document


class TestTravelsafe:
    def test_travelsafe_entities_are_buildable(self):
        summary = Summary(
            **{
                "summary": "While traveling in Spain you will be required to follow the guidelines introduced by the local government. These regulations are based on risk levels and aimed at improving your safety.",
                "details": "",
                "risk_level": {
                    "id": "high",
                    "name": "High",
                    "details": "Covid cases are multiplying",
                },
                "location": {"name": "Spain", "type": "country", "country_code": "ES"},
                "updated_at": "2020-10-19T10:08:53.777Z",
                "guidelines": [
                    {
                        "category": {"id": "use_of_mask", "name": "Use of masks"},
                        "sub_category": {"id": "required", "name": "Required"},
                        "summary": "Use of masks is required",
                        "details": "Use of masks in all the public areas is required, including open spaces. You might face fines up to €3000 if stopped by the police without mask.",
                        "severity": "1/3",
                    }
                ],
                "info_source": {
                    "name": "Spain Travel Health",
                    "url": "https://www.spth.gob.es/",
                },
            }
        )
        assert type(summary) is Summary
        assert type(summary.risk_level) is RiskLevel
        assert type(summary.location) is Location
        assert type(summary.guidelines[0]) is Guideline
        assert type(summary.guidelines[0].category) is Category
        assert type(summary.guidelines[0].sub_category) is Category
        assert type(summary.info_source) is InfoSource

    def test_airline_entities_are_buildable(self):
        measure = AirlineMeasure(
            **{
                "airline": {"name": "Lufthansa", "iata_code": "LH"},
                "safety_measures": [
                    {
                        "category": {
                            "id": "boarding_or_dissembarking_measurements",
                            "name": "New boarding and disembarking measures",
                        },
                        "sub_category": {"id": "true", "name": "true"},
                        "details": "Travelers should wait until their boarding group is called before using the automatic gates to board the aircraft. Disinfectant wipes will also be provided to passengers for the purpose of cleaning the surfaces in and around their seats.",
                        "summary": "To help passengers can keep a safe distance from one another.",
                    }
                ],
                "info_source": {
                    "name": "Lufthansa' info source",
                    "url": "https://www.lufthansa.com/de/en/protection-measures",
                },
                "updated_at": "2020-10-19T12:14:42.041298+00:00",
            }
        )
        assert type(measure) is AirlineMeasure
        assert type(measure.info_source) is InfoSource
        assert type(measure.airline) is Airline
        assert type(measure.safety_measures[0]) is SafetyMeasure
        assert type(measure.safety_measures[0].category) is Category
        assert type(measure.safety_measures[0].sub_category) is Category

    def test_restrictions_entities_are_buildable(self):
        restriction = Restriction(
            **{
                "id": "e7975c43-b098-4530-ad3e-59615b8572ac",
                "origin": {"name": "France", "type": "country", "country_code": "FR"},
                "destination": {
                    "name": "Spain",
                    "type": "country",
                    "country_code": "ES",
                },
                "authorization_status": "restricted",
                "summary": "Travelling from France to Spain is restricted",
                "details": "Only business related travel is allowed.",
                "start_date": "2020-10-16",
                "end_date": "2020-10-18",
                "updated_at": "2020-09-16T14:54:59.944581+00:00",
                "requirements": [
                    {
                        "category": {"id": "quarantine", "name": "Quarantine"},
                        "sub_category": {
                            "id": "quarantine_required",
                            "name": "Quarantine required",
                        },
                        "summary": "Travelers are required to quarantine for 14 days prior or after entering this destination",
                        "details": "Travelers arriving into Spain are required to go into quarantine",
                        "start_date": "2020-10-02",
                        "end_date": "2020-10-18",
                        "documents": [
                            {
                                "name": "FCS form",
                                "document_url": "https://www.spth.gob.es/create",
                                "download_url": "https://www.spth.gob.es/download.pdf",
                            }
                        ],
                    }
                ],
                "info_source": {
                    "name": "Spain Travel Health",
                    "url": "https://www.spth.gob.es/",
                },
            }
        )
        assert type(restriction) is Restriction
        assert type(restriction.info_source) is InfoSource
        assert type(restriction.origin) is Location
        assert type(restriction.destination) is Location
        assert type(restriction.requirements[0]) is Requirement
        assert type(restriction.requirements[0].category) is Category
        assert type(restriction.requirements[0].sub_category) is Category
        assert type(restriction.requirements[0].documents[0]) is Document
