# pyquake3 - Python Quake 3 Library


**pyquake3** is a Python library to query and execute RCON commands on a Quake 3 server.

The module is a complete rewrite of an earlier [pyquake3](http://misc.slowchop.com/misc/wiki/pyquake3) module that [Gerald Kaszuba](http://geraldkaszuba.com/) wrote.

This pyquake3 module was developed for and tested with Urban Terror 4.1 / 4.2 running on dedicated server.


# Features
- Send RCON commands
- Access server variables
- Collect player information (e.g. name, ping, frags and IP address)


# Example

    from pyquake3 import PyQuake3
    QUAKE = PyQuake3(server='localhost:27960', rcon_password='secret')

    QUAKE.update()
    print "The server name of '%s' is %s, running map %s with %s player(s)." % (QUAKE.get_address(), QUAKE.values['sv_hostname'], QUAKE.values['mapname'], len(QUAKE.players))

    for gamer in QUAKE.players:
        print "%s with %s frags and a %s ms ping" % (gamer.name, gamer.frags, gamer.ping)

    QUAKE.rcon_update()
    for gamer in QUAKE.players:
        print "%s (%s) has IP address of %s" % (gamer.name, gamer.num, gamer.address)

    QUAKE.rcon('bigtext "pyquake3 is great"')

