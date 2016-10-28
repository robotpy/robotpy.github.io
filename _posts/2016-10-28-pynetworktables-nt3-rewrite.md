---
layout: post
title: pynetworktables NT3 rewrite now available for testing!
---

pynetworktables has been rewritten in the style of ntcore, and now fully
supports all of the NT3 features that are available in ntcore. For the most
part.... it should all work. There are a few breaking changes I can think of:

* Connection listeners are different. Sorry.
* The special array types are gone (yay) and so is the networktables2 package
* It's easier to make client connections (though the old way still works)
* ... and that's about it

I haven't had the opportunity to try this on a real robot yet, BUT the unit
tests have 75% coverage and it works on my machine, so it's probably good to go
if you're using this on a driver station or coprocessor. Try it out, let me know
how it works!

Installation is super easy if you already have python and pip installed:

    pip install --pre pynetworktables

Also, if you're using pynetworktables2js, there's an alpha release of that
available too, which accommodates some of the NT3 changes. However, more work
needs to be done to fully support all of the NT3 features in pynetworktables2js.
