from time import sleep

from pytest import raises

from lackadaisical import TooSlow, assert_faster_than


def test_context__over() -> None:
    with raises(TooSlow) as ex:
        with assert_faster_than(0.5):
            sleep(0.6)

    assert str(ex.value) == "Operation took 0.6 seconds (expected 0.5 at most)"


def test_context__under() -> None:
    with assert_faster_than(0.5):
        sleep(0.4)


def test_decorator__over() -> None:
    @assert_faster_than(0.5)
    def my_slow_function() -> None:
        sleep(0.6)

    with raises(TooSlow) as ex:
        my_slow_function()

    assert str(ex.value) == "Operation took 0.6 seconds (expected 0.5 at most)"


def test_decorator__under() -> None:
    @assert_faster_than(0.5)
    def my_slow_function() -> None:
        sleep(0.4)

    my_slow_function()
