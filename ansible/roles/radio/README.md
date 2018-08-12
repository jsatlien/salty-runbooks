## Groovebasin

Currently, this is not publicly exposed via Nginx or started as a service.

I shell in as the local user, fire up `screen`, cd to the `groovebasin` directory,
and run `sudo -u {{ groovebasin_user }} node lib/server.js`.

Then proxy over SSH with `ssh -L 16242:127.0.0.1:16242 {{ default_user }}@domain` and rock and roll. 🤘
It would be good to have a supervisor script or other method for keeping this running later.
