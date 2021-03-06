import sys
from detox.proc import Detox


def parse(args):
    from tox.session import prepare
    return prepare(args)


def main(args=None):
    if args is None:
        args = sys.argv[1:]
    config = parse(args)
    # now = py.std.time.time()
    detox_instance = Detox(config)
    detox_instance.startloopreport()
    retcode = detox_instance.runtestsmulti(config.envlist)
    # elapsed = py.std.time.time() - now
    # cumulated = detox.toxsession.report.cumulated_time
    # detox.toxsession.report.line(
    #    "detox speed-up: %.2f (elapsed %.2f, cumulated %.2f)" % (
    #        cumulated / elapsed, elapsed, cumulated), bold=True)
    return retcode
