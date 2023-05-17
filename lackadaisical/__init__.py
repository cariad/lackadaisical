"""
# Support

Please submit all your questions, feature requests and bug reports at
[github.com/cariad/lackadaisical/issues](https://github.com/cariad/lackadaisical/issues).
Thank you!

# Licence

Lackadaisical is [open-source](https://github.com/cariad/lackadaisical) and
released under the
[MIT License](https://github.com/cariad/lackadaisical/blob/main/LICENSE).

You don't have to give attribution in your project, but -- as a freelance
developer with rent to pay -- I appreciate it!

# Author

Hello! 👋 I'm **Cariad Eccleston**, and I'm a freelance Amazon Web Services
architect, DevOps evangelist, CI/CD pipeline engineer and backend developer.

You can find me at [cariad.earth](https://www.cariad.earth),
[github/cariad](https://github.com/cariad),
[linkedin/cariad](https://linkedin.com/in/cariad) and on Mastodon at
[@cariad@tech.lgbt](https://tech.lgbt/@cariad).
"""

from importlib.resources import open_text

with open_text(__package__, "VERSION") as t:
    __version__ = t.readline().strip()
