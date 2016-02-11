---
layout: post
title: RobotPy 2016.2.0, PyFRC 2016.2.3 released
---

RobotPy WPILib 2016.2.0 now has full CANTalon support including enhanced sensor support in simulation, the new motion profiling stuff that was introduced for 2016, and a bunch of new setter functions and other random status things. The simulation hal_data structures have been updated as well, which may break your tests. However, the new API should be easier to use and more consistent.

Additionally, PyFRC 2016.2.3 has been released, with a useful new feature that allows you to select autonomous mode via NetworkTables if you're using the [AutonomousModeSelector](http://robotpy-wpilib-utilities.readthedocs.org/en/latest/robotpy_ext.autonomous.html) object to select autonomous modes (used in the [Magicbot framework](http://robotpy-wpilib-utilities.readthedocs.org/en/latest/magicbot.html) too). Check out this screenshot:

![PyFRC Screenshot](/assets/pyfrc_autonomous_ss.png)

RobotPy releases can be downloaded from our [github releases page]("https://github.com/robotpy/robotpy-wpilib/releases"), and pyfrc can be upgraded using Pip.