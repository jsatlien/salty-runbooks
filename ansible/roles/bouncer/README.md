## IRC Bouncer (znc)

You'll need to generate a pass and salt in ZNC's format.

I recommend installing znc on the host, then ssh'ing over
and running `znc --makepass` to generate it. Then update
`private.yml` accordingly.

As for connecting, I like using spacemacs and ERC.
The important thing to note is the _username_ prompt
should be answered with `irc_nick` and the password
prompt answered with `znc_nick/irc_network:zncpassword`.
