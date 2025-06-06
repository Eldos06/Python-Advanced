import functools
import logging
import time
from typing import ParamSpec, TypeVar, Callable, Sequence

log = logging.getLogger(__name__)

P = ParamSpec("P")
R = TypeVar("R")


class Retry:
    def __init__(
        self,
        max_retry_count: int = 3,
        initial_timeout: int = 2,
        timeout_multiplier: int = 5,
        exceptions: Sequence[Exception] = (Exception,),
    ) -> None:
        self.max_retry_count = max_retry_count
        self.initial_timeout = initial_timeout
        self.timeout_multiplier = timeout_multiplier
        self.exceptions = exceptions

    def __call__(self, func: Callable[P, R]) -> Callable[P, R]:
        @functools.wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            timeout = self.initial_timeout
            for attempt in range(1, self.max_retry_count + 1):
                log.debug("Run %r attempt #%s", func.__name__, attempt)
                try:
                    return func(*args, **kwargs)
                except self.exceptions as e:
                    if attempt == self.max_retry_count:
                        raise
                    log.warning("Caught exception: %s, will retry in %ss", e, timeout)
                    time.sleep(timeout)
                    timeout *= self.timeout_multiplier

        return wrapper


default_retry = Retry()