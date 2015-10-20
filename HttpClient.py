class HttpClient(object):

    def __new__(self, method, url, content_type="json", **kwargs):
        if api_token == None:
            raise AuthenticationError("An API token is required!")

        if "headers" in kwargs:
            kwargs["headers"]["Authorization"] = "Token token=" + api_token
            if content_type != "multipart":
                kwargs["headers"]["Content-Type"] = "application/json"
        else:
            kwargs.update({"headers": {}})
            kwargs["headers"].update(
                {"Authorization": "Token token=" + api_token}
            )
            if content_type != "multipart":
                kwargs["headers"].update(
                    {"Content-Type": "application/json"}
                )
        req = requests.request(method, api_base + url, **kwargs)
        resp = json.loads(req.text)
        if req.ok == False:
            print(resp)
            raise ApiServerError(resp["error"]["message"])
        return resp