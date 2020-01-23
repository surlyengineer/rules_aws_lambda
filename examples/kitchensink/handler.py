import redis
import silly

from google.protobuf.json_format import MessageToJson

from examples.kitchensink.lib import core_api_pb2 as core_api
from examples.kitchensink.lib.id import new_id

def handle(event, context):
    person = core_api.Person()
    person.id = new_id()
    person.name = silly.name()
    return MessageToJson(person)
