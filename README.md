# supybot-meetbot

This is a fork of http://wiki.debian.org/MeetBot with minimal changes to get it ported to Python 3.

Check out the original [README](supybot_fedora/README.txt) and [the original manual](supybot_fedora/doc/Manual.txt) for detailed infomation, installation, and usage instructions.

**Before using this fork, be sure to check out the [hcoop-meetbot](https://github.com/pronovic/hcoop-meetbot) first.**

In addition to the porting changes this supybot-meetbot also:

* Forces a meeting to be given a name -- "#startmeeting" will return a message telling the user to provide a meeting name
* Returns a message to the meeting when doing an "#undo" so it is known what was undid.




