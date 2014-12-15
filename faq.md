---
layout: page
title: Frequently Asked Questions
---

Here you can find answers to some of the most frequently asked questions about RobotPy.

<p class="message">Please note that we're still getting stuff ready for 2015, so this documentation is somewhat out of date!</p>

## Installing and Running RobotPy


### What version of Python is RobotPy based on?

RobotPy 2014.2 is based on Python 3.2.5.  This means you should reference the [Python 3.x documentation](http://docs.python.org/py3k/) instead of the Python 2.x documentation.

RobotPy 2015 will use Python 3.4.

### What happens when my code crashes?

An exception will be printed out to the console. It is highly recommended that you enable NetConsole for your robot, so you can see these messages.

### Is WPILib available?

Of course!  Just "import wpilib".  Class and function names are identical to the Java version.

Prior to 2015, the API matched the C++ version of WPILib.

### Is Command-based programming available?

Of course! Check out the wpilib.commands package. There is also a python sample available at TODO

### Is there an easy way to test my code outside of the robot?

Glad you asked! Check out the [pyfrc](http://github.com/robotpy/pyfrc) project, which allows your robot code to run on your computer along with easy pytest integration and a lightweight robot simulator.

### Is RobotPy compatible with the 2015+ FRCSim/Gazebo Robot Simulator

Absolultely! Documentation can be found at... 

# Competition

## Is RobotPy competition-legal?

As RobotPy was not written by anyone involved with the GDC, we can't provide a guaranteed answer (particularly not for future years).  However, we see no reason that RobotPy would not be legal: to the cRIO/RoboRIO, it looks just like any other C++ WPILib-using program that reads text files.  RobotPy itself should be considered COTS software as it is freely available to all teams. Teams have been using RobotPy since 2010 without any problems from FIRST, and we expect that to continue.

Caveat emptor: while RobotPy is almost certainly legal to use, your team should carefully consider the risk of using such a large piece of unofficial software; unless RobotPy is used by many teams, if you run into trouble at a competition, there may not be anyone else there to help! However, we've found that most problems teams run into are problems with WPILib itself, and not RobotPy.

Also, be sure to keep in mind the fact that Python is a dynamic language and is NOT compiled.  This means that typos can easily go undetected until your robot runs that particular line of code, resulting in an exception and 5 second restart.  Make sure to test your code thoroughly ([pyfrc](http://github.com/robotpy/pyfrc) can help you out with that). 

## Is RobotPy stable?

Yes! While it is not an officially supported language, teams have been using RobotPy since 2010. Most of the time when bugs are found, they are found in the underlying WPILib, instead of RobotPy itself.

# Performance

## Is RobotPy fast?

TODO for 2015.

We've not yet benchmarked it, but it's almost certainly just as fast as Java for typical WPILib-using robot code.  RobotPy uses the native C++ WPILib, and thus the only interpreted portions are your specific robot actions.  If you have particularly performance sensitive code, you can write it in C++ and add SWIG wrappers to interface to it from Python (note, however, that this takes a fair amount of coding expertise).

# RobotPy Development

## Who created RobotPy?

RobotPy was created by Peter Johnson, programming mentor for FRC Team 294, [Beach Cities Robotics](http://www.bcrobotics.org/).  He was inspired by the [Lua port for the cRIO](http://redmine.zombiezen.com/projects/greyhoundlua/) created by Ross Light, FRC Team 973.

Since 2011, RobotPy updates are also maintained by Dustin Spicuzza, programming mentor for FRC Team 2423 and 1418.

# How can I help?

RobotPy is an open project that all members of the FIRST community can easily and quickly contribute to. If you find a bug, or have an idea that you think others can use:

* Test and report any issues you find.
* Port and test a useful library.
* Write a Python module and share it with others (and contribute it to the [robotpy-wpilib-utilities](https://github.com/robotpy/robotpy-wpilib-utilities) package!)
