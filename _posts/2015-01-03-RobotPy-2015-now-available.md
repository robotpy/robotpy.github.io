---
layout: post
title: 2015 RobotPy now available!
---

Now that kickoff is over and the game has been released, we're happy to announce the initial release of RobotPy for 2015. There's a lot of moving pieces in various stages of completion, but here's where we are now:

* [WPILib](https://github.com/robotpy/robotpy-wpilib) is available and should be fully functional. Check out our [getting started guide](http://robotpy.readthedocs.org/en/latest/getting_started.html) to install WPILib and the Python interpreter on your robot.
* [pynetworktables](https://github.com/robotpy/pynetworktables) is available for robots and clients to connect to the SmartDashboard or from coprocessors, and should be fully functional.
* [pyfrc](https://github.com/robotpy/pyfrc) is mostly there, with the simulator working and some of the unit test functionality working. I'm hoping to finish this up by the end of the weekend.
* We have initial support for the [FRCSim Simulator](https://github.com/robotpy/robotpy-frcsim.git), but the documentation is light and not all devices have been implemented yet. The [python version of the GearsBot example](https://github.com/robotpy/robotpy-wpilib/tree/master/examples/examples/GearsBot) mostly works though. :) 
* The Eclipse plugins aren't anywhere near functional yet (sorry!). Hopefully by next week.
* We've got numpy built for the RoboRIO, and it's easily installable via opkg. Check out [https://github.com/robotpy/roborio-packages](https://github.com/robotpy/roborio-packages) for more information.

Our initial RobotPy release for 2015 is now available for download on our [release page](https://github.com/robotpy/robotpy-wpilib/releases).

The team has put months of effort into this release, and we're really excited about 2015! Special thanks to Christian Balcom (@computer-whisperer, FRC Team 4819), who has done a significant amount of work on the pure python port of WPILib, and various useful tooling.

Go ahead and start using what we have, and report bugs as you find them! We expect that there will be a lot of bugfixes over the next few weeks, but that will probably be true for the other languages too. Please [report any problems on our issue tracker](https://github.com/robotpy/robotpy-wpilib/issues) as you find them!
