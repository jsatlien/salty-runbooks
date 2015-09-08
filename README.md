salty-runbooks
==============

Ansible Playbooks and Salt States

So named for the Melee/FGC concept of a salty runback where after
losing a game, you demand a rematch on the same stage.

## Ansible

You'll need to describe your servers in a [hosts file][inventory].

[inventory]: http://docs.ansible.com/intro_inventory.html

The primary playbook `cons.yml` was designed with Debian Jessie
servers in mind and will require tweaking to run elsewhere.

The secondary playbook `metaobject.yml` is designed to build a Debian Jessie
based development setup specific to the whims of yours truly.

Both playbooks expect a `deploy` user present with pubkey login and
passwordless sudo privs. You can create such a user on a new machine
by running the following commands as root:

```bash
useradd deploy && passwd deploy && mkdir -p ~deploy/.ssh
chmod 700 ~deploy/.ssh && touch ~deploy/.ssh/authorized_keys
chmod 400 ~deploy/.ssh/authorized_keys && chown deploy:deploy -R ~deploy
echo 'deploy ALL=(ALL) NOPASSWD: ALL' > /etc/sudoers.d/deploy
```

Finally, add your SSH public key to the deploy user's authorized_keys file.

You'll need to edit vars/cons.yml or vars/metaobject.yml to
customize things appropriately for your needs or even keep sensitive
data in an uncommitted/gitignored vars/private.yml file.

Run with `ansible-playbook -vv -i ./hosts foo.yml` optionally adding
`--tags TAG`. The tags for each playbook are described in READMEs in
their respective directories.

## SaltStack
