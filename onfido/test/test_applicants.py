import httpretty
from hamcrest import assert_that, equal_to, contains_inanyorder, instance_of
import onfido
from .test_utils import load_fixture_string

class TestApplicants:

	def setup_class(self):
		onfido.api_token = "gjh5k3l4jhlk31jh4fl34"

	@httpretty.activate
	def test_retrieve_all_applicants(self):
		httpretty.register_uri(httpretty.GET, "https://api.onfido.com/v1/applicants",
							   body=load_fixture_string("applicants.json"),
							   content_type="application/json")
		all_applicants = onfido.Applicants.retrieve()
		assert_that(len(all_applicants), equal_to(1))
		assert_that(all_applicants[0], instance_of(onfido.Applicant))
