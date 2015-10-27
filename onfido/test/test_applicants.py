import httpretty
from hamcrest import assert_that, equal_to
import onfido
import os

def load_fixture_string(fixture_name):
    fixture_path = os.path.join(os.path.dirname(__file__), "test_api_responses", fixture_name)
    with open(fixture_path) as infile:
        return infile.read()

class TestApplicants:

	@classmethod
	def setup_class(cls):
		onfido.api_token = "gjh5k3l4jhlk31jh4fl34"

	@httpretty.activate
	def test_load_all_applicants(self):
		httpretty.register_uri(httpretty.GET, "https://api.onfido.com/v1/applicants",
							   body=load_fixture_string("applicants.json"),
							   content_type="application/json")
		response = onfido.Applicants.all()
		print(response)
