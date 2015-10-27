class Check(OnfidoObjectBase):

    @classmethod
    def create(cls, applicant_id, type, reports):
        options = {
            "type": type,
            "reports": reports
        }
        options = json.dumps(options)
        check = HttpClient("POST", "/applicants/{0}/checks".format(applicant_id), data=options)
        return Check(check)
    
    @classmethod
    def all(cls, applicant_id):
        result = HttpClient("GET", "/applicants/{0}/checks".format(applicant_id))
        checks = result["checks"]
        return [Check(check) for check in checks]