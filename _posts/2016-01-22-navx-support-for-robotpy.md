---
layout: post
title: NavX device support in RobotPy 2016.1.1 released
---

This is a bugfix release of RobotPy, and all RobotPy users are recommended to upgrade, particularly owners of NavX devices or those who want to use the PIDController object.

If you want to see the NavX stuff in action, one of the NavX samples that I ported over shows a [robot rotating to a specific angle based on a button press]("https://github.com/robotpy/robotpy-wpilib-utilities/tree/master/samples/navx_rotate_to_angle"), and it works in simulation (not tested on a real robot). Very cool demo -- you will need to make sure you have the latest version of pyfrc installed as well.

For NavX device python documentation, see our [readthedocs site]("http://robotpy-wpilib-utilities.readthedocs.org/en/latest/robotpy_ext.common_drivers.navx.html").


* Fixed a crash in the PIDController object
* New version of robotpy-wpilib-utilities 2016.2.0 includes support for the NavX MXP


RobotPy releases can be downloaded from our [github releases page]("https://github.com/robotpy/robotpy-wpilib/releases").