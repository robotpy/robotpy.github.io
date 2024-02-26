---
layout: post
title: RobotPy 2024 is now available
---

This is the first year that Python has been an officially supported language! Lots of changes this year.

* The biggest change is instead of `python robot.py XXX`, you run `python -m robotpy XXX`
* The installation process will be much smoother! Just run `python -m robotpy sync` and `python -m robotpy deploy` in a directory with your robot code and everything will get downloaded and installed on the rio.
* `commands2` is not available yet, but hopefully soon

I am still working on updating the robotpy documentation site, but lots of documentation has been done on frc-docs! See https://github.com/wpilibsuite/frc-docs/pull/2501 for new documentation on defining requirements, deploy, and more.

---

Note that there is a 2024-compatible version of robotpy-commands-v2 available, it's just marked as a beta release at this time because it's incomplete and I'm not comfortable saying that it's good to go. If you want to use it, you can set up the following `pyproject.toml` next to your `robot.py`:

```toml
#
# Use this configuration file to control what RobotPy packages are installed
# on your RoboRIO
#

[tool.robotpy]

# Version of robotpy this project depends on
robotpy_version = "2024.1.1.1"

# Which extra RobotPy components should be installed
# -> equivalent to `pip install robotpy[extra1, ...]
robotpy_extras = [
    # "all"
    # "apriltag"
    # "commands2"
    # "cscore"
    # "navx"
    # "pathplannerlib"
    # "phoenix5"
    # "phoenix6"
    # "playingwithfusion"
    # "rev"
    # "romi"
    # "sim"
]

# Other pip packages to install
requires = [
    "robotpy-commands-v2==2024.0.0b4"
]
```

After that, run `python -m robotpy sync` and it should download/install commands v2 + the kickoff release.