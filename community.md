---
layout: page
title: RobotPy Community

# Feel free to add your team to this list!
teamlist:
    2015:
        - ["865", ""]
        - ["1418", ""]
        - ["2423", ""]
        - ["4480", ""]
        - ["4819", ""]
    2014:
        - ["294", ""]
        - ["865", "https://github.com/Team865/frc2014.5"]
        - ["1243", ""]
        - ["1418", "https://github.com/frc1418/2014"]
        - ["2423", "https://github.com/team2423/2014"]
        - ["3966", "https://github.com/LN-STEMpunks/Shrimp"]
        - ["4038", "https://bitbucket.org/ariovistus/frc2014"]
        - ["4604", ""]
    2013:
        - ["294", "https://github.com/team294/FRC2013"]
        - ["2423", "https://github.com/team2423/2013"]
        - ["4038", ""]
        - ["4561", "https://github.com/RTHS-TerrorBytes/Robot-Code-2013"]
    2012:
        - ["294", ""]
        - ["2423", "https://github.com/team2423/2008-2012/tree/master/Kwarqs2012"]
    2011:
        - ["294", ""]
        - ["2423", "https://github.com/team2423/2008-2012/tree/master/Kwarqs2011/trunk"]

---

The RobotPy project was started in 2010, and since then the community surrounding RobotPy has continued to grow!

If you need support, you can find it in the following locations

* [RobotPy mailing list](https://groups.google.com/forum/#!forum/robotpy)
* [ChiefDelphi Python Forums](http://www.chiefdelphi.com/forums/forumdisplay.php?f=187)


IRC
---

During the FRC Build Season, some RobotPy developers may be able to be reached on **#robotpy** channel on [Freenode](http://freenode.net/irc_servers.shtml). _Note: the channel is not very active, but if you stick around long enough someone will probably answer your question -- think in terms of email response time_


Teams that use RobotPy
----------------------

Here is a list of teams that are known to have used RobotPy over the years, and that have publicly released their source code for others to learn from.

{% for year in page.teamlist %}
### {{ year[0] }}

{% for teaminfo in year[1] %}
* [{{ teaminfo[0] }}](http://www.thebluealliance.com/team/{{ teaminfo[0] }}){% if teaminfo[1] != "" %} - [code]({{ teaminfo[1] }}){% endif %}{% endfor %}

{% endfor %}
