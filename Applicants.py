class Applicants(object):

    @classmethod
    def all(cls):
        result = HttpClient("GET", "/applicants")
        applicants = result['applicants']
        return [Applicant(applicant) for applicant in applicants]