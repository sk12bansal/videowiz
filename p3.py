import json
import base64
from Plugins.categories import IHelloWorld
from Plugins import PLUGIN_CAT
class HelloWorld(IHelloWorld):
	_req_msg = dict()
	_job_id = None
