---
layout: post
title: robotpy-build is now semiwrap
---

robotpy-build was created in 2020 to automate large portions of the work
required to maintain and build the wrappers that RobotPy creates over the WPILib
C++ libraries. semiwrap is a rewrite of that project, incorporating five years
of lessons learned while maintaining over a dozen different projects wrapping
hundreds of C++ classes and functions.

This rewrite is intended to be used more broadly for autogenerating pybind11
wrappers around C++ code, not just for RobotPy. It is built around hatchling and
the meson build system, I encourage you to take a look!

* Github: [https://github.com/robotpy/semiwrap](https://github.com/robotpy/semiwrap)
* Documentation: [https://semiwrap.readthedocs.io](https://semiwrap.readthedocs.io)
