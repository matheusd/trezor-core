#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Dusan Klinec, ph4r05, 2018

from apps.monero.xmr import common, crypto
from apps.monero.xmr.monero import TsxData
from apps.monero.xmr.serialize import xmrtypes, xmrserialize
from trezor.messages.MoneroTsxData import MoneroTsxData
from trezor.messages.MoneroTxDestinationEntry import MoneroTxDestinationEntry
from trezor.messages.MoneroAccountPublicAddress import MoneroAccountPublicAddress


class TrezorError(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for kw in kwargs:
            setattr(self, kw, kwargs[kw])


class TrezorSecurityError(TrezorError):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class TrezorInvalidStateError(TrezorError):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class TrezorTxPrefixHashNotMatchingError(TrezorError):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


def compute_tx_key(spend_key_private, tx_prefix_hash, salt=None, rand_mult=None):
    """

    :param spend_key_private:
    :param tx_prefix_hash:
    :param salt:
    :param rand_mult:
    :return:
    """
    if not salt:
        salt = crypto.random_bytes(32)

    if not rand_mult:
        rand_mult_num = crypto.random_scalar()
        rand_mult = crypto.encodeint(rand_mult_num)
    else:
        rand_mult_num = crypto.decodeint(rand_mult)

    rand_inp = crypto.sc_add(spend_key_private, rand_mult_num)
    passwd = crypto.keccak_2hash(crypto.encodeint(rand_inp) + tx_prefix_hash)
    tx_key = crypto.pbkdf2(passwd, salt, count=100)
    return tx_key, salt, rand_mult


async def translate_monero_dest_entry(dst_entry: MoneroTxDestinationEntry):
    d = xmrtypes.TxDestinationEntry()
    d.amount = dst_entry.amount
    d.is_subaddress = dst_entry.is_subaddress
    d.addr = xmrtypes.AccountPublicAddress(m_spend_public_key=dst_entry.addr.m_spend_public_key,
                                           m_view_public_key=dst_entry.addr.m_view_public_key)
    return d


async def tsx_data_translate(tsx_data: MoneroTsxData):
    tsxd = TsxData()
    for fld in TsxData.MFIELDS:
        fname = fld[0]
        if hasattr(tsx_data, fname):
            setattr(tsxd, fname, getattr(tsx_data, fname))

    if tsx_data.change_dts:
        tsxd.change_dts = translate_monero_dest_entry(tsx_data.change_dts)

    tsxd.outputs = [translate_monero_dest_entry(x) for x in tsx_data.outputs]
    return tsxd




