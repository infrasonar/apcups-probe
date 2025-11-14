from libprobe.probe import Probe
from lib.check.apcups import CheckApcUps
from lib.version import __version__ as version


if __name__ == '__main__':
    checks = (
        CheckApcUps,
    )

    probe = Probe("apcups", version, checks)

    probe.start()
