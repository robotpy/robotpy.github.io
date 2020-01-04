---
layout: post
title: RobotPy 2020 availability
---

Maintaining pure python bindings is a significant amount of work, and as WPILib gains more features and as more and more third party vendors join FRC, it becomes harder to provide support for those vendors and their devices. To reduce the amount of work required to maintain RobotPy in the long term, this year we're moving back to a WPILibC wrapper (which is what we were doing pre-2015).

In the long term, there are lots of benefits to this approach:

* I anticipate that python programs on the RoboRIO will have higher performance
* We will be able to support more third party vendors with minimal effort
* RobotPy will be less effort to maintain for our limited development team

Unfortunately in the short term, the wrappers are not ready yet. **My current goal is to have RobotPy 2020 available by the end of the weekend**.

RobotPy is a community project and only exists because FRC community members contribute! If you'd like to help out, join us at https://gitter.im/robotpy/robotpy-wpilib!

In the meantime, you really should be working on strategy for your team right now anyways! If you do need to do some prototyping, RobotPy 2019 still works great in simulation and on hardware (with the 2019 image).
