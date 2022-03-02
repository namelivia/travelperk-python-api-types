from travelperk_python_api_types.greenperk.greenperk.emissions import Emissions
from travelperk_python_api_types.greenperk.greenperk.emission_value import EmissionValue


class TestGreenPerk:
    def test_entities_are_buildable(self):
        emissions = Emissions(**{"emissions": {"CO2e_kg": 21}, "distance_km": 200})
        assert type(emissions) is Emissions
        assert type(emissions.emissions) is EmissionValue
