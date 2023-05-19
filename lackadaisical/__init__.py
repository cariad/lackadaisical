from importlib.resources import open_text

from lackadaisical.faster_than import assert_faster_than
from lackadaisical.too_slow import TooSlow

with open_text(__package__, "VERSION") as t:
    __version__ = t.readline().strip()

__all__ = [
    "TooSlow",
    "assert_faster_than",
]
