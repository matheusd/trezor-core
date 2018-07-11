# Automatically generated by pb2py
# fmt: off
import protobuf as p
if __debug__:
    try:
        from typing import List
    except ImportError:
        List = None  # type: ignore
from .MoneroExportedKeyImage import MoneroExportedKeyImage


class MoneroKeyImageSyncStepResp(p.MessageType):
    MESSAGE_WIRE_TYPE = 521
    FIELDS = {
        1: ('kis', MoneroExportedKeyImage, p.FLAG_REPEATED),
    }

    def __init__(
        self,
        kis: List[MoneroExportedKeyImage] = None,
    ) -> None:
        self.kis = kis if kis is not None else []
