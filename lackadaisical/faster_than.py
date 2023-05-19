from contextlib import contextmanager
from time import perf_counter
from typing import Iterator

from lackadaisical.too_slow import TooSlow


@contextmanager
def assert_faster_than(seconds: float) -> Iterator[None]:
    """
    Tracks the execution time of a block of code and raises `TooSlow` if the
    actual duration is not less than `seconds`.

    Can be used as either a function decorator or a context manager.

    ```python
    @assert_faster_than(30)
    def test() -> None:
        my_slow_function()
    ```

    ```python
    def test() -> None:
        with assert_faster_than(30):
            my_slow_function()
    ```
    """

    start = perf_counter()
    yield
    duration = perf_counter() - start
    if duration >= seconds:
        raise TooSlow(seconds, duration)
