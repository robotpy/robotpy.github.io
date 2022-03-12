---
layout: post
title: Robot integration testing is back!
---

We're really happy to announce that `py robot.py test` will work once again (after upgrading to pyfrc 2022.1.0 or later)! For those who don’t remember, historically RobotPy would run a quick integration test on your code when you deploy it. It was quite useful for catching typos and other silly things that would be caught by a compiler in other languages.

Currently, we am not enabling tests on deploy by default until the stability of this feature is proven. We’ve tested it on many of our examples, so we're reasonably confident that it isn’t entirely useless.

Please try this out and let me know if it works (or not) for your robot!

## Known Issues

If you use REV robotics motor controllers, the test program may hang after tests complete. I’ve alerted the vendor but they still haven’t released a fix.