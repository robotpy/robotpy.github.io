---
layout: post
title: Critical pyfrc bugfix release 2015.1.0
---

If you used pyfrc 2015.0.x and uploaded code to your robot there was a critical bug that may prevent your robot from running robot programs (affects python and Java). To fix this, please upgrade pyfrc to the latest version, and run the following command:

    Windows:    py -m pyfrc.robotpy.fixbug

    Linux/OSX:  python3 -m pyfrc.robotpy.fixbug

Additionally, if you upgrade pyfrc, any future code deploys will check for this bug and repair it if found.

If you want to fix this manually, you can ssh in as admin, and execute ```rm /var/local/natinst/log/FRC_UserProgram.log```.

We apologize for any inconvenience. More information can be found at [https://github.com/robotpy/pyfrc/issues/14](https://github.com/robotpy/pyfrc/issues/14).