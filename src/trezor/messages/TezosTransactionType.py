# Automatically generated by pb2py
# fmt: off
import protobuf as p

from .TezosContractID import TezosContractID


class TezosTransactionType(p.MessageType):
    FIELDS = {
        1: ('amount', p.UVarintType, 0),
        2: ('destination', TezosContractID, 0),
        3: ('parameters', p.BytesType, 0),
    }

    def __init__(
        self,
        amount: int = None,
        destination: TezosContractID = None,
        parameters: bytes = None,
    ) -> None:
        self.amount = amount
        self.destination = destination
        self.parameters = parameters
