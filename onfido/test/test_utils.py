import os

def load_fixture_string(fixture_name):
	fixture_path = os.path.join(os.path.dirname(__file__), "test_api_responses", fixture_name)
	with open(fixture_path) as infile:
		return infile.read()