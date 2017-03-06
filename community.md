---
layout: page
title: RobotPy Community

# Feel free to add your team to this list!
teamlist:
    2017:
        - ["247", ""]
        - ["1123", "https://github.com/FRC-1123/frc2017-1123"]
        - ["1418", ""]
        - ["1432", ""]
        - ["1973", ""]
        - ["2186", "https://github.com/DrWateryCat/Robotics2017"]
        - ["2423", ""]
        - ["2539", "https://github.com/FRC2539/pybot/tree/steamworks"]
        - ["2605", "https://github.com/Seamonsters-2605/CompetitionBot2017"]
        - ["3184", "https://github.com/FRC3184/frc2017"]
        - ["4096", ""]
        - ["4480", "https://github.com/bb20basketball/2017-Robot-Code"]
        - ["4774", ""]
        - ["4796", ""]
        - ["5045", ""]
        - ["5929", ""]
        - ["6098", "https://github.com/bIrobot/2017-Caroline"]
        - ["6413", ""]
    2016:
        - ["74", "https://github.com/Team74/FRC_2016_Python_Stronghold"]
        - ["94", "https://github.com/TechnoJays/robot2016"]
        - ["1288", ""]
        - ["1418", "https://github.com/frc1418/2016-robot"]
        - ["1915", ""]
        - ["2036", ""]
        - ["2423", "https://github.com/frc2423/2016"]
        - ["2605", "https://github.com/Seamonsters-2605/"]
        - ["3184", "https://github.com/FRC3184/frc2016"]
        - ["3223", "https://github.com/Retro3223/dashboard2016"]
        - ["4009", "https://github.com/DenfeldRobotics4009/2016_Freckles"]
        - ["4096", "https://github.com/CtrlZ-FRC4096/Robot-2016-Public"]
        - ["4393", ""]
        - ["4480", "https://github.com/bb20basketball/2016-RobotCode"]
        - ["4688", "https://github.com/clxe/frc2016"]
        - ["4774", "https://github.com/thedropbears"]
        - ["4819", "https://github.com/Team4819/2016-Codebase"]
        - ["5045", "https://github.com/Team5045/2016-bot"]
        - ["5929", ""]
    2015:
        - ["94", "https://github.com/TechnoJays/robot2015"]
        - ["865", "https://github.com/Team865/tachyon"]
        - ["1288", "http://www.chiefdelphi.com/forums/showthread.php?t=135688"]
        - ["1418", "https://github.com/frc1418/2015-robot"]
        - ["2423", "https://github.com/frc2423/2015"]
        - ["3145", ""]
        - ["3223", "https://github.com/Retro3223/2015-recycle-rush"]
        - ["3966", ""]
        - ["4009", "https://github.com/DenfeldRobotics4009/2015_Lopez_Jr"]
        - ["4480", "https://github.com/bb20basketball/2015-Team4480-Code"]
        - ["4819", "https://github.com/Team4819/2015-Python-Codebase"]
        - ["5045", ""]
    2014:
        - ["94", "https://github.com/TechnoJays/robot2014"]
        - ["294", ""]
        - ["865", "https://github.com/Team865/frc2014.5"]
        - ["1243", ""]
        - ["1418", "https://github.com/frc1418/2014"]
        - ["2423", "https://github.com/team2423/2014"]
        - ["2928", "https://github.com/VikingRobotics/2014_Base"]
        - ["3966", "https://github.com/LN-STEMpunks/Shrimp"]
        - ["4038", "https://bitbucket.org/ariovistus/frc2014"]
        - ["4604", ""]
        - ["5080", "https://github.com/JohnDickinsonHS/FRC"]
    2013:
        - ["294", "https://github.com/team294/FRC2013"]
        - ["2423", "https://github.com/team2423/2013"]
        - ["4038", ""]
        - ["4561", "https://github.com/RTHS-TerrorBytes/Robot-Code-2013"]
    2012:
        - ["294", ""]
        - ["2423", "https://github.com/team2423/2008-2012/tree/master/Kwarqs2012"]
        - ["2945", "https://github.com/manitourobotics/2012-python"]
    2011:
        - ["294", ""]
        - ["2423", "https://github.com/team2423/2008-2012/tree/master/Kwarqs2011/trunk"]

---

The RobotPy project was started in 2010, and since then the community surrounding RobotPy has continued to grow!

If you need support, you can find it in the following locations

* [RobotPy mailing list](https://groups.google.com/forum/#!forum/robotpy)
* [ChiefDelphi Python Forums](http://www.chiefdelphi.com/forums/forumdisplay.php?f=187)

Release Announcements
---------------------

During the build season, we post release announcements to the
[ChiefDelphi Python forum](http://www.chiefdelphi.com/forums/forumdisplay.php?f=187) and
to the RobotPy mailing list, particularly if critical bugs are fixed.

If you're on a team that uses RobotPy, we highly recommend subscribing to our
[mailing list](https://groups.google.com/forum/#!forum/robotpy).

Chat
----

During the FRC Build Season, some RobotPy developers may be able to be reached on
the [RobotPy Gitter Channel](https://gitter.im/robotpy/robotpy-wpilib).  _Note: the channel is not very active, but if you stick around long enough someone will probably answer your question -- think in terms of email response time_


Teams that use RobotPy
----------------------

Here is a list of teams that are known to have used RobotPy over the years, and that have publicly released their source code for others to learn from. Is your team using RobotPy? Add it to the list by [editing this page on github](https://github.com/robotpy/robotpy.github.io/blob/master/community.md)!

{% for year in page.teamlist %}
### {{ year[0] }}

{% for teaminfo in year[1] %}
* [{{ teaminfo[0] }}](http://www.thebluealliance.com/team/{{ teaminfo[0] }}){% if teaminfo[1] != "" %} - [code]({{ teaminfo[1] }}){% endif %}{% endfor %}

{% endfor %}
