---
layout: post
title: RobotPy 2021 now available
---

We’re happy to announce the release of RobotPy for 2021. We’ve continued cleaning up the mess we started last year, and things should hopefully be much smoother.

* WPILib 2021.2.1 libraries included
* All packages now ship with type hints which enable autocomplete in vscode when using the Python or pylance extensions
* Upgraded pybind11 support no longer crashes when you forget to call `super().__init__`
* New meta package – `pip install robotpy` will now bring in all robotpy packages, and there are various ‘extra’ specifiers that allow installation of other packages also. See [robotpy-meta](https://github.com/robotpy/robotpy-meta) for details

The documentation and examples have not been updated yet. Soon?

The roborio installation process has been a huge pain as robotpy has grown, and this year’s installer is significantly better than what we’ve had in the past. Better error handling, single cache, we’ve gotten rid of the opkg stuff, and everything uses pip now.

First install python:

```
robotpy-installer download-python
robotpy-installer install-python
```

Then use ‘download’ and ‘install’ to download python packages from pypi and the RobotPy server and install them on the roborio. The package names are exactly the same names that you would install locally on your computer with pip. In particular, you can use the new meta package to download everything:

```
robotpy-installer download robotpy[all]
...
robotpy-installer install robotpy[all]
```

Unfortunately, there are some issues with the RoboRIO installer at the moment when using the ‘robotpy’ meta package. Hopefully will be able to address that tomorrow.

Thanks so much to @auscompgeek and @TheTripleV for their help getting this season’s release out.