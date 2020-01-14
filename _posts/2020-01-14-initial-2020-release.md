---
layout: post
title: Initial RobotPy 2020 pieces available
---

Initial RobotPy for RoboRIO is out! Same features as yesterday, but they all work now. pyfrc and the robotpy-installer have been updated (thanks to Nick of team 5654 for that!). Still no OSX support, someone needs to step up and make that work.

I've pushed pyfrc as a beta release, so you have to pass the `--pre` flag to pip.

```
py -m pip install --pre pyfrc
```

Additionally, the RobotPy RoboRIO installer is no longer a standalone download, but it is installed as part of pyfrc.

Using it is mostly the same as before:

```
py -m robotpy-installer download-robotpy
py -m robotpy-installer install-robotpy
```

There's still work to be done, join us on gitter to help finish it up!