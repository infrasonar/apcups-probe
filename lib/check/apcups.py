from asyncsnmplib.mib.mib_index import MIB_INDEX
from libprobe.asset import Asset
from libprobe.exceptions import CheckException
from ..utils import get_data

QUERIES = (
    MIB_INDEX['PowerNet-MIB']['upsAdvBattery'],
    MIB_INDEX['PowerNet-MIB']['upsAdvIdent'],
    MIB_INDEX['PowerNet-MIB']['upsAdvInput'],
    MIB_INDEX['PowerNet-MIB']['upsAdvOutput'],
    MIB_INDEX['PowerNet-MIB']['upsBasicBattery'],
    MIB_INDEX['PowerNet-MIB']['upsBasicIdent'],
    MIB_INDEX['PowerNet-MIB']['upsBasicInput'],
    MIB_INDEX['PowerNet-MIB']['upsBasicOutput'],
)


async def check_apcups(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:
    state = await get_data(asset, asset_config, check_config, QUERIES)

    if not any(state.values()):
        raise CheckException('no data found')

    # we merge everything into single item
    # this is safe because we query only scalar objects
    item = {
        k: v
        for items in state.values()
        for item in items
        for k, v in item.items()
    }
    item['name'] = 'ups'
    return {
        'ups': [item]
    }
