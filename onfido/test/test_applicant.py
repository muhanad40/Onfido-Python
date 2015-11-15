import httpretty
from hamcrest import assert_that, equal_to, has_key, contains_inanyorder, instance_of
import onfido
from .test_utils import load_fixture_string

class TestApplicants:

	def setup_class(self):
		onfido.api_token = "gjh5k3l4jhlk31jh4fl34"

	@httpretty.activate
	def test_retrieve_an_applicant(self):
		applicant_id = "9g734m0hg73bf06"
		httpretty.register_uri(httpretty.GET, "https://api.onfido.com/v1/applicants/{0}".format(applicant_id),
							   body=load_fixture_string("applicant.json"),
							   content_type="application/json")
		response = onfido.Applicant.retrieve(applicant_id)
		assert_that(response, instance_of(onfido.Applicant))
		assert_that(response.id, equal_to("1030303-123123-123123"))
		assert_that(response.created_at, equal_to("2014-05-23T13:50:33Z"))
		assert_that(response.href, equal_to("/v1/applicants/1030303-123123-123123"))
		assert_that(response.title, equal_to("Mr"))
		assert_that(response.first_name, equal_to("John"))
		assert_that(response.middle_name, equal_to(None))
		assert_that(response.last_name, equal_to("Smith"))
		assert_that(response.gender, equal_to("male"))
		assert_that(response.dob, equal_to("2013-02-17"))
		assert_that(response.telephone, equal_to("02088909293"))
		assert_that(response.mobile, equal_to(None))
		assert_that(response.country, equal_to("GBR"))
		assert_that(response.id_numbers, contains_inanyorder(
			{
				"type": "ssn",
				"value": "433-54-3937"
			},
			{
				"type": "driving_license",
				"value": "I1234562",
				"state": "CA"
			}
		))
		assert_that(response.addresses, contains_inanyorder(
			{
				"flat_number": None,
				"building_name": None,
				"building_number": "100",
				"street": "Main Street",
				"sub_street": None,
				"state": None,
				"town": "London",
				"postcode": "SW4 6EH",
				"country": "GBR",
				"start_date": "2013-01-01",
				"end_date": None
			},
			{
				"flat_number": "Apt 2A",
				"building_name": None,
				"building_number": "1017",
				"street": "Oakland Ave",
				"sub_street": None,
				"town": "Piedmont",
				"state": "CA",
				"postcode": "94611",
				"country": "USA",
				"start_date": "2006-03-07",
				"end_date": "2012-12-31"
			}
		))

	@httpretty.activate
	def test_create_an_applicant(self):
		applicant_id = "9g734m0hg73bf06"
		httpretty.register_uri(httpretty.POST, "https://api.onfido.com/v1/applicants",
							   body=load_fixture_string("new_applicant.json"),
							   content_type="application/json")
		new_applicant_data = {
			"title": "Mr",
			"first_name": "John",
			"middle_name": None,
			"last_name": "Smith",
			"gender": "male",
			"dob": "1987-02-17",
			"telephone": "0892337217",
			"mobile": None,
			"country": "GBR",
			"addresses": [
				{
					"flat_number": 1,
					"building_name": None,
					"building_number": None,
					"street": "Some street",
					"sub_street": None,
					"state": None,
					"town": "London",
					"postcode": "NW3 5HF",
					"country": "GBR",
					"start_date": "2013-01-01",
					"end_date": None
				}
			]
		}
		new_applicant = onfido.Applicant.create(new_applicant_data)
		assert_that(new_applicant.title, equal_to("Mr"))
		assert_that(new_applicant.first_name, equal_to("John"))
		assert_that(new_applicant.middle_name, equal_to(None))
		assert_that(new_applicant.last_name, equal_to("Smith"))
		assert_that(new_applicant.gender, equal_to("male"))
		assert_that(new_applicant.dob, equal_to("1987-02-17"))
		assert_that(new_applicant.telephone, equal_to("0892337217"))
		assert_that(new_applicant.mobile, equal_to(None))
		assert_that(new_applicant.country, equal_to("GBR"))
		assert_that(new_applicant.addresses, contains_inanyorder({
			"flat_number": 1,
			"building_name": None,
			"building_number": None,
			"street": "Some street",
			"sub_street": None,
			"state": None,
			"town": "London",
			"postcode": "NW3 5HF",
			"country": "GBR",
			"start_date": "2013-01-01",
			"end_date": None
		}))