# Automatically generated by pb2py
# fmt: off
import protobuf as p


class OntologyOntIdAttribute(p.MessageType):
    FIELDS = {
        1: ('key', p.UnicodeType, 0),
        2: ('type', p.UnicodeType, 0),
        3: ('value', p.UnicodeType, 0),
    }

    def __init__(
        self,
        key: str = None,
        type: str = None,
        value: str = None,
    ) -> None:
        self.key = key
        self.type = type
        self.value = value
