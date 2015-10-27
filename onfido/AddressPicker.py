class AddressPicker(OnfidoObjectBase):

    @classmethod
    def query(cls, options):
        result = HttpClient("GET", "/applicants/addresses/pick", data=options)
        return result