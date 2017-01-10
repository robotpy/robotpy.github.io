---
layout: post
title: RobotPy 2017.0.1 critical bugfix release now available
---

This fixes two major bugs in the original RobotPy release:

* [#246](https://github.com/robotpy/robotpy-wpilib/issues/246) The installer did not work properly on systems without an ssh configuration file, or on Windows
* [#243](https://github.com/robotpy/robotpy-wpilib/issues/243) Robot code would fail at system start due to a bug in the python 3.6 random module (thanks to @auscompgeek for finding the fix!)

All RobotPy users should upgrade to this latest version of RobotPy.