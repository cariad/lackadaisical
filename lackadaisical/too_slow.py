class TooSlow(Exception):
    def __init__(self, expected: float, actual: float) -> None:
        self.expected_seconds = expected
        self.actual_seconds = actual

        actual_plural = "" if actual == 1 else "s"

        super().__init__(
            f"Operation took {actual:.1f} second{actual_plural} (expected "
            f"{expected} at most)"
        )
