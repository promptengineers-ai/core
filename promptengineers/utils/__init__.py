import logging
import json
from bson import ObjectId

logger = logging.getLogger("uvicorn.error")

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)
