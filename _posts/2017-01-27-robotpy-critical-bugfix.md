---
layout: post
title: RobotPy 2017.0.5 critical bugfix release
---
This is a critical bugfix release for all RobotPy teams. `hal.initialize()` was being called twice, which can lead to unpredictable and unspecified behaviors. 

This also includes some minor updates:

* Upgrade to HAL 2017.2.1
* Will log versions of third party libraries at startup if they support a new robotpy extension point
* Fix SendableChooser to match WPILib Java behavior

All RobotPy teams are strongly urged to upgrade.