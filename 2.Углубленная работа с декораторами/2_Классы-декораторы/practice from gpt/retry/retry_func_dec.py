import functools
import logging
import time
from typing import ParamSpec, TypeVar, Callable, Sequence

log = logging.getLogger(__name__)

P = ParamSpec("P")
R = TypeVar("R")


def retry(
    decorated_func: Callable[P, R] | None = None,
    *,
    max_retry_count: int = 3,
    initial_timeout: int = 2,
    timeout_multiplier: int = 5,
    exceptions: Sequence[Exception] = (Exception,),
):

    if decorated_func is not None:
        return retry(
            max_retry_count=max_retry_count,
            initial_timeout=initial_timeout,
            timeout_multiplier=timeout_multiplier,
            exceptions=exceptions,
        )(decorated_func)

    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        @functools.wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            timeout = initial_timeout
            for attempt in range(1, max_retry_count + 1):
                log.debug("Run %r attempt #%s", func.__name__, attempt)
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == max_retry_count:
                        raise
                    log.warning("Caught exception: %s, will retry in %ss", e, timeout)
                    time.sleep(timeout)
                    timeout *= timeout_multiplier

        return wrapper

    return decorator