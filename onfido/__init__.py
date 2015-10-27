import json
import os
import mimetypes

api_token = None
api_base = "https://api.onfido.com/v1"

def set():
	api_token = "blah123"

from .HttpClient import HttpClient
from .OnfidoObjectBase import OnfidoObjectBase
from .Applicant import Applicant
from .Applicants import Applicants