from onfido import HttpClient, Applicant

class Applicants(object):

    @classmethod
    def retrieve(cls):
        result = HttpClient("GET", "/applicants")
        applicants = result['applicants']
        return [Applicant(applicant) for applicant in applicants]