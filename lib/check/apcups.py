import logging
from icmplib import async_apcups
from libprobe.asset import Asset
from libprobe.exceptions import CheckException, NoCountException


async def check_apcups(
        asset: Asset,
        asset_config: dict,
        config: dict) -> dict:
    address = config.get('address')
    if not address:
        address = asset.name

    ...
