from asyncsnmplib.mib.mib_index import MIB_INDEX
from libprobe.asset import Asset
from libprobe.check import Check
from libprobe.exceptions import CheckException
from ..snmpclient import get_snmp_client
from ..snmpquery import snmpquery

QUERIES = (
    (MIB_INDEX['PowerNet-MIB']['upsAdvBattery'], False),
    (MIB_INDEX['PowerNet-MIB']['upsAdvIdent'], False),
    (MIB_INDEX['PowerNet-MIB']['upsAdvInput'], False),
    (MIB_INDEX['PowerNet-MIB']['upsAdvOutput'], False),
    (MIB_INDEX['PowerNet-MIB']['upsBasicBattery'], False),
    (MIB_INDEX['PowerNet-MIB']['upsBasicIdent'], False),
    (MIB_INDEX['PowerNet-MIB']['upsBasicInput'], False),
    (MIB_INDEX['PowerNet-MIB']['upsBasicOutput'], False),
)


class CheckApcUps(Check):
    key = 'apcups'
    unchanged_eol = 0

    @staticmethod
    async def run(asset: Asset, local_config: dict, config: dict) -> dict:

        snmp = get_snmp_client(asset, local_config, config)
        state = await snmpquery(snmp, QUERIES)

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
