from libprobe.probe import Probe
from lib.check.apcups import check_apcups
from lib.version import __version__ as version


if __name__ == '__main__':
    checks = {
        'apcups': check_apcups
    }

    probe = Probe("apcups", version, checks)

    probe.start()
