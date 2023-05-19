from lackadaisical import TooSlow


def test_actual() -> None:
    assert TooSlow(3, 7).actual == 7


def test_expected() -> None:
    assert TooSlow(3, 7).expected == 3
