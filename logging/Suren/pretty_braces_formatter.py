from ast import arg
import logging
from pathlib import Path
from common import configure_logging
from utils import User


class BraceMessage:
    def __init__(self, ftm, args):
        self.ftm = ftm
        self.args = args

    def __str__(self):
        if len(self.args) == 1 and isinstance((kwargs := self.args[0]), dict):
            return self.ftm.format(**kwargs)
        return self.ftm.format(*self.args)
    
class BraceStyleAdapter(logging.LoggerAdapter):
    def log(self, level, msg, /, *args, stacklevel=1, **kwargs):
        if self.isEnabledFor(level):
            msg, kwargs = self.process(msg, kwargs)
            self.logger.log(
                level,
                BraceMessage(msg, args),
                **kwargs,
                stacklevel = stacklevel + 1
            )

logger = BraceStyleAdapter(logging.getLogger(__name__))
        
def main():
    logger.warning("Hello! Starting main")
    logger.debug("Hello, {!r}", Path(__file__).name)
    user = User()
    logger.info("User {user}, repr: {user!r}", {"user": user})
    logger.info("User {user}, repr: {user}", {"user":user})
    logger.warning("Done doing something")

if __name__ == "__main__":
    configure_logging(level=logging.DEBUG)
    main()















































