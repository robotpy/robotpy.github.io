---
layout: post
title: Initial RobotPy 2020 pieces available
---


Non-roborio builds of some core robotpy pieces are now available for installation from pypi! If you're on Windows and have Python 3.6-3.8, you can do this to try it out:

```
py -m pip install -U wpilib robotpy-halsim-gui robotpy-wpilib-utilities
```

It's best to do this in a clean virtualenv for now -- you will need to uninstall pyfrc as it will conflict with the new sim. Once you have it installed, you can:

```
py robot.py sim
```

Please give it a try and let us know what breaks. There's still a lot missing, but it's coming soon:

* commands
* SendableChooser
* Shuffleboard
* Some new 2020 features

Tomorrow night I'll push a roborio release, pyfrc/installer updates, and hopefully some 3rd party vendor packages.