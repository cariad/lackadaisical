# Lackadaisical

[![codecov](https://codecov.io/gh/cariad/lackadaisical/branch/main/graph/badge.svg?token=DXirnPrRzJ)](https://codecov.io/gh/cariad/lackadaisical)

_adjective: lacking spirit or liveliness._

**Lackadaisical** is a Python package for keeping an eye on slow code.

## Usage

To assert that a block of code should execute and return within a number of seconds, use `lackadaisical.assert_faster_than` as either a decorator or a context manager.

For example, `assert_faster_than` will raise `lackadaisical.TooSlow` if this test doesn't finish within 30 seconds of starting:

```python
from lackadaisical import assert_faster_than

@assert_faster_than(30)
def test_my_slow_function() -> None:
    my_slow_function()
```

In this example, the test's setup is free to take as long as it needs and only the slow function is monitored:

```python
from lackadaisical import assert_faster_than

def test_my_slow_function() -> None:
    data = my_slow_preparation()

    with assert_faster_than(30):
        my_slow_function(data)
```

`assert_faster_than` will not interrupt your code's execution after its time has elapsed, but `lackadaisical.TooSlow` will report the difference between the actual and expected execution times to help you diagnose the problem.

```text
Operation took 2.6 seconds (expected 2.0 at most)
```

## Installation

Lackadaisical requires Python 3.9 or later and can be installed from [PyPI](https://pypi.org/project/lackadaisical/).

```shell
pip install lackadaisical
```

## Support

Please submit all your questions, feature requests and bug reports at [github.com/cariad/lackadaisical/issues](https://github.com/cariad/lackadaisical/issues). Thank you!

## Licence

Lackadaisical is [open-source](https://github.com/cariad/lackadaisical) and released under the [MIT License](https://github.com/cariad/lackadaisical/blob/main/LICENSE).

You don't have to give attribution in your project, but -- as a freelance developer with rent to pay -- I appreciate it!

## Author

Hello! 👋 I'm **Cariad Eccleston**, and I'm a freelance Amazon Web Services architect, DevOps evangelist, CI/CD pipeline engineer and backend developer.

You can find me at [cariad.earth](https://www.cariad.earth), [github/cariad](https://github.com/cariad), [linkedin/cariad](https://linkedin.com/in/cariad) and on Mastodon at [@cariad@tech.lgbt](https://tech.lgbt/@cariad).
