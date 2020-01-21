from examples.proto.lib import core_api_pb2 as core_api
from google.protobuf.json_format import MessageToJson


def handle(event, context):
    person = core_api.Person()
    person.id = "foo"
    person.name = "bar"
    return MessageToJson(person)
