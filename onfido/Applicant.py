from . import OnfidoObjectBase, HttpClient

class Applicant(OnfidoObjectBase):

    def get():
        print(api_token)

    @classmethod
    def create(cls, options):
        options = json.dumps(options)
        applicant = HttpClient("POST", "/applicants", data=options)
        return cls(applicant)

    def check(self, type, reports):
        return Check.create(self.id, type, reports)

    def all_checks(self):
        return Check.all(self.id)

    def upload_document(self, file, type, side=""):
        file_extension = os.path.splitext(file.name)[1]
        file_mimetype = mimetypes.types_map[file_extension]
        document_upload = HttpClient(
            "POST", "/applicants/{0}/documents".format(self.id),
            files={"file": ("passport", file, file_mimetype)},
            data={"type": type},
            content_type="multipart")
        return Document(document_upload)

    @classmethod
    def retrieve(cls, applicant_id):
        applicant = HttpClient("GET", "/applicants/{0}".format(applicant_id))
        return cls(applicant)