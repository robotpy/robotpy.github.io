---
layout: post
title: 2017 RobotPy now available!
---

It's a little late, but we're happy to announce the initial release of RobotPy for the 2017 season. This release contains most new changes for WPILib in 2017. Here's what this package provides you:

* Python 3.6.0 interpreter for RoboRIO
* WPILib/HAL packages for RoboRIO
* [pynetworktables](https://github.com/robotpy/pynetworktables) and [robotpy-wpilib-utilities](https://github.com/robotpy/robotpy-wpilib-utilities)

This release will only work correctly on a RoboRIO that has been reimaged for the 2017 season.

There's a couple of important things to note here:

* Because 3rd party drivers are now being supported separately from WPILib, CANTalon has been removed from this release. We will be releasing support in a separate library hopefully within a few days.
* pynetworktables has been rewritten based on the ntcore library, and it should support all of the new cool things that ntcore supports
* The HAL changes in WPILib this year mean that:
  * CPU usage should be significantly less than it was last year (observed 4-10% idle usage, compared to 20% last year)
  * Tests should run a lot faster (I've seen 50% improvements on basic tests
* CameraServer has been removed for now. We will have a python-compatible version of the new cscore library available in the near future, which should result in a significantly upgraded experience for image processing
* We've improved our test coverage significantly, so there's less chance of things breaking

Additionally, the [documentation site](http://robotpy.readthedocs.io) has been restructured significantly, so that all RobotPy projects essentially share the same set of documentation -- no more need to remember five different sites!

Thanks to everyone who contributed to this release, but particularly @james-ward @auscompgeek @Twinters007 and @ArthurAllshire 

Installation instructions can be found on [our documentation site](http://robotpy.readthedocs.org), and are also included as a README file with this zipfile. We expect there to be some bugs at first as teams start playing with their new toys, so please [report them on our issue tracker](https://github.com/robotpy/robotpy-wpilib/issues) as you find them!