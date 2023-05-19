class TooSlow(Exception):
    """
    Raised if a block of code takes too long to execute.
    """

    def __init__(self, expected: float, actual: float) -> None:
        self._expected = expected
        self._actual = actual

        plural = "" if actual == 1 else "s"

        super().__init__(
            f"Operation took {actual:.1f} second{plural} (expected {expected} "
            "at most)"
        )

    @property
    def actual(self) -> float:
        """
        Actual execution time in seconds.
        """

        return self._actual

    @property
    def expected(self) -> float:
        """
        Expected execution time in seconds.
        """

        return self._expected
