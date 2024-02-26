---
layout: post
title: RobotPy 2024 Beta 3 is now available
---

Python will be an official FRC language for 2024, and this is our first beta release
for the season. We've done a lot of work on infrastructure related to RobotPy, and
hopefully it will be simpler to maintain in the future.

There is no updated documentation at this time. To install the beta release, you can
do `pip install robotpy==2024.0.0b3`. See our normal documentation for installation,
deployment, etc -- most things haven't changed.

* Development has moved to a monorepo called [mostrobotpy](https://github.com/robotpy/mostrobotpy)
* Most WPILib 2024.0.0 beta 3 features are available
  * NT4 structured binding support is not implemented
  * Python 3.8 and 3.9 support is broken, oops
* The commands implementation is now pure python thanks to @TheTripleV, please try it out and report bugs
  * .. there are a lot of bugs
  * .. there is a lot missing -- see https://github.com/robotpy/robotpy-commands-v2/issues/28
  * Do you love commands and love writing python? It would be great to have more people contribute to this.
* REV and NavX vendors are available
  * CTRE is managing their own releases this year, and I believe it will be available soon
* Our examples repository has a 2024-beta branch
