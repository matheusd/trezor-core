# Automatically generated by pb2py
# fmt: off
import protobuf as p
if __debug__:
    try:
        from typing import List
    except ImportError:
        List = None  # type: ignore
from .TxInputType import TxInputType
from .TxOutputBinType import TxOutputBinType
from .TxOutputType import TxOutputType


class TransactionType(p.MessageType):
    FIELDS = {
        1: ('version', p.UVarintType, 0),
        2: ('inputs', TxInputType, p.FLAG_REPEATED),
        3: ('bin_outputs', TxOutputBinType, p.FLAG_REPEATED),
        4: ('lock_time', p.UVarintType, 0),
        5: ('outputs', TxOutputType, p.FLAG_REPEATED),
        6: ('inputs_cnt', p.UVarintType, 0),
        7: ('outputs_cnt', p.UVarintType, 0),
        8: ('extra_data', p.BytesType, 0),
        9: ('extra_data_len', p.UVarintType, 0),
        10: ('expiry', p.UVarintType, 0),
        11: ('overwintered', p.BoolType, 0),
    }

    def __init__(
        self,
        version: int = None,
        inputs: List[TxInputType] = None,
        bin_outputs: List[TxOutputBinType] = None,
        lock_time: int = None,
        outputs: List[TxOutputType] = None,
        inputs_cnt: int = None,
        outputs_cnt: int = None,
        extra_data: bytes = None,
        extra_data_len: int = None,
        expiry: int = None,
        overwintered: bool = None,
    ) -> None:
        self.version = version
        self.inputs = inputs if inputs is not None else []
        self.bin_outputs = bin_outputs if bin_outputs is not None else []
        self.lock_time = lock_time
        self.outputs = outputs if outputs is not None else []
        self.inputs_cnt = inputs_cnt
        self.outputs_cnt = outputs_cnt
        self.extra_data = extra_data
        self.extra_data_len = extra_data_len
        self.expiry = expiry
        self.overwintered = overwintered
