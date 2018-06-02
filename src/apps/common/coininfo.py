class CoinInfo:

    def __init__(
        self,
        coin_name: str,
        coin_shortcut: str,
        address_type: int,
        address_type_p2sh: int,
        maxfee_kb: int,
        signed_message_header: str,
        xpub_magic: int,
        bech32_prefix: str,
        cashaddr_prefix: str,
        segwit: bool,
        fork_id: int,
        force_bip143: bool
    ):
        self.coin_name = coin_name
        self.coin_shortcut = coin_shortcut
        self.address_type = address_type
        self.address_type_p2sh = address_type_p2sh
        self.maxfee_kb = maxfee_kb
        self.signed_message_header = signed_message_header
        self.xpub_magic = xpub_magic
        self.bech32_prefix = bech32_prefix
        self.cashaddr_prefix = cashaddr_prefix
        self.segwit = segwit
        self.fork_id = fork_id
        self.force_bip143 = force_bip143


# the following list is generated using tools/codegen/gen_coins.py
# do not edit manually!
COINS = [
    CoinInfo(
        coin_name='Bitcoin',
        coin_shortcut='BTC',
        address_type=0,
        address_type_p2sh=5,
        maxfee_kb=2000000,
        signed_message_header='Bitcoin Signed Message:\n',
        xpub_magic=0x0488b21e,
        bech32_prefix='bc',
        cashaddr_prefix=None,
        segwit=True,
        fork_id=None,
        force_bip143=False,
    ),
    CoinInfo(
        coin_name='Testnet',
        coin_shortcut='TEST',
        address_type=111,
        address_type_p2sh=196,
        maxfee_kb=10000000,
        signed_message_header='Bitcoin Signed Message:\n',
        xpub_magic=0x043587cf,
        bech32_prefix='tb',
        cashaddr_prefix=None,
        segwit=True,
        fork_id=None,
        force_bip143=False,
    ),
    CoinInfo(
        coin_name='Bcash',
        coin_shortcut='BCH',
        address_type=0,
        address_type_p2sh=5,
        maxfee_kb=500000,
        signed_message_header='Bitcoin Signed Message:\n',
        xpub_magic=0x0488b21e,
        bech32_prefix=None,
        cashaddr_prefix='bitcoincash',
        segwit=False,
        fork_id=0,
        force_bip143=True,
    ),
    CoinInfo(
        coin_name='Bcash Testnet',
        coin_shortcut='TBCH',
        address_type=111,
        address_type_p2sh=196,
        maxfee_kb=10000000,
        signed_message_header='Bitcoin Signed Message:\n',
        xpub_magic=0x043587cf,
        bech32_prefix=None,
        cashaddr_prefix='bchtest',
        segwit=False,
        fork_id=0,
        force_bip143=True,
    ),
    CoinInfo(
        coin_name='Namecoin',
        coin_shortcut='NMC',
        address_type=52,
        address_type_p2sh=5,
        maxfee_kb=10000000,
        signed_message_header='Namecoin Signed Message:\n',
        xpub_magic=0x019da462,
        bech32_prefix=None,
        cashaddr_prefix=None,
        segwit=False,
        fork_id=None,
        force_bip143=False,
    ),
    CoinInfo(
        coin_name='Litecoin',
        coin_shortcut='LTC',
        address_type=48,
        address_type_p2sh=50,
        maxfee_kb=40000000,
        signed_message_header='Litecoin Signed Message:\n',
        xpub_magic=0x019da462,
        bech32_prefix='ltc',
        cashaddr_prefix=None,
        segwit=True,
        fork_id=None,
        force_bip143=False,
    ),
    CoinInfo(
        coin_name='Dogecoin',
        coin_shortcut='DOGE',
        address_type=30,
        address_type_p2sh=22,
        maxfee_kb=1000000000,
        signed_message_header='Dogecoin Signed Message:\n',
        xpub_magic=0x02facafd,
        bech32_prefix=None,
        cashaddr_prefix=None,
        segwit=False,
        fork_id=None,
        force_bip143=False,
    ),
    CoinInfo(
        coin_name='Dash',
        coin_shortcut='DASH',
        address_type=76,
        address_type_p2sh=16,
        maxfee_kb=100000,
        signed_message_header='DarkCoin Signed Message:\n',
        xpub_magic=0x02fe52cc,
        bech32_prefix=None,
        cashaddr_prefix=None,
        segwit=False,
        fork_id=None,
        force_bip143=False,
    ),
    CoinInfo(
        coin_name='Zcash',
        coin_shortcut='ZEC',
        address_type=7352,
        address_type_p2sh=7357,
        maxfee_kb=1000000,
        signed_message_header='Zcash Signed Message:\n',
        xpub_magic=0x0488b21e,
        bech32_prefix=None,
        cashaddr_prefix=None,
        segwit=False,
        fork_id=None,
        force_bip143=False,
    ),
    CoinInfo(
        coin_name='Zcash Testnet',
        coin_shortcut='TAZ',
        address_type=7461,
        address_type_p2sh=7354,
        maxfee_kb=10000000,
        signed_message_header='Zcash Signed Message:\n',
        xpub_magic=0x043587cf,
        bech32_prefix=None,
        cashaddr_prefix=None,
        segwit=False,
        fork_id=None,
        force_bip143=False,
    ),
    CoinInfo(
        coin_name='Bgold',
        coin_shortcut='BTG',
        address_type=38,
        address_type_p2sh=23,
        maxfee_kb=500000,
        signed_message_header='Bitcoin Gold Signed Message:\n',
        xpub_magic=0x0488b21e,
        bech32_prefix='btg',
        cashaddr_prefix=None,
        segwit=True,
        fork_id=79,
        force_bip143=True,
    ),
    CoinInfo(
        coin_name='DigiByte',
        coin_shortcut='DGB',
        address_type=30,
        address_type_p2sh=63,
        maxfee_kb=500000,
        signed_message_header='DigiByte Signed Message:\n',
        xpub_magic=0x0488b21e,
        bech32_prefix='dgb',
        cashaddr_prefix=None,
        segwit=True,
        fork_id=None,
        force_bip143=False,
    ),
    CoinInfo(
        coin_name='Monacoin',
        coin_shortcut='MONA',
        address_type=50,
        address_type_p2sh=55,
        maxfee_kb=5000000,
        signed_message_header='Monacoin Signed Message:\n',
        xpub_magic=0x0488b21e,
        bech32_prefix='mona',
        cashaddr_prefix=None,
        segwit=True,
        fork_id=None,
        force_bip143=False,
    ),
    CoinInfo(
        coin_name='Fujicoin',
        coin_shortcut='FJC',
        address_type=36,
        address_type_p2sh=16,
        maxfee_kb=1000000,
        signed_message_header='FujiCoin Signed Message:\n',
        xpub_magic=0x0488b21e,
        bech32_prefix='fc',
        cashaddr_prefix=None,
        segwit=True,
        fork_id=None,
        force_bip143=False,
    ),
    CoinInfo(
        coin_name='Vertcoin',
        coin_shortcut='VTC',
        address_type=71,
        address_type_p2sh=5,
        maxfee_kb=40000000,
        signed_message_header='Vertcoin Signed Message:\n',
        xpub_magic=0x0488b21e,
        bech32_prefix='vtc',
        cashaddr_prefix=None,
        segwit=True,
        fork_id=None,
        force_bip143=False,
    ),
]