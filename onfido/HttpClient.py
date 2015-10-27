from .errors import AuthenticationError, ApiServerError
import requests
import onfido
import json

class HttpClient(object):

    def __new__(self, method, url, content_type="json", **kwargs):
        if onfido.api_token == None:
            raise AuthenticationError("An API token is required!")

        if "headers" in kwargs:
            kwargs["headers"]["Authorization"] = "Token token=" + onfido.api_token
            if content_type != "multipart":
                kwargs["headers"]["Content-Type"] = "application/json"
        else:
            kwargs.update({"headers": {}})
            kwargs["headers"].update(
                {"Authorization": "Token token=" + onfido.api_token}
            )
            if content_type != "multipart":
                kwargs["headers"].update(
                    {"Content-Type": "application/json"}
                )
        req = requests.request(method, onfido.api_base + url, **kwargs)
        resp = json.loads(req.text)
        if req.ok == False:
            print(resp)
            raise ApiServerError(resp["error"]["message"])
        return resp
