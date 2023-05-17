from contextlib import contextmanager
from time import perf_counter
from typing import Iterator

from lackadaisical.too_slow import TooSlow


@contextmanager
def assert_faster_than(seconds: float) -> Iterator[None]:
    start = perf_counter()
    yield
    duration = perf_counter() - start
    if duration > seconds:
        raise TooSlow(seconds, duration)
