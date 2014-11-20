salty-runbooks
==============

Ansible Playbooks and Salt States

So named for the Melee/FGC concept of a salty runback where after
losing a game, you demand a rematch on the same stage.

## Ansible

You'll need to describe your servers in a [hosts file][inventory].

[inventory]: http://docs.ansible.com/intro_inventory.html

The playbook expects a `deploy` user present with pubkey login and
passwordless sudo privs. You'll need to edit vars/cons.yml to
customize things appropriately for your needs.

Run with `ansible-playbook -vv -i ./hosts cons.yml` optionally adding
`--tags TAG` for the following tags:

Toplevel tags are roles while nested tags are includes.

* common
  * firewall
* web
* blog
  * git
  * lisp
  * quicklisp
* mail
  * postgres
  * postfix
* irc
