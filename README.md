salty-runbooks
==============

Ansible Playbooks and Salt States

So named for the Melee/FGC concept of a salty runback where after
losing a game, you demand a rematch on the same stage.

## Ansible

You'll need to describe your servers in a [hosts file][inventory].

[inventory]: http://docs.ansible.com/intro_inventory.html

The primary playbook `cons.yml` was designed with Debian Wheezy
servers in mind and will require tweaking to run elsewhere.

The playbook expects a `deploy` user present with pubkey login and
passwordless sudo privs. You'll need to edit vars/cons.yml to
customize things appropriately for your needs or even keep sensitive
data in an uncommitted/gitignored vars/private.yml file.

Run with `ansible-playbook -vv -i ./hosts cons.yml` optionally adding
`--tags TAG` for the following tags:

Toplevel tags are roles while nested tags are includes.

* common
  * security
* web
* blog
  * git
  * lisp
  * quicklisp
* mail
  * postgres
  * postfix
  * dovecot
  * opendkim
  * dspam
* bookmarks
* irc
* radio
  * backports
  * libgroove
