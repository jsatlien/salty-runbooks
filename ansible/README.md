To deploy to a new linode:

1. Create a linode with the latest debian release (stretch at the time of writing).
2. Add a deploy user with SSH login and paste your public key into `authorized_keys`.
  ```
  useradd deploy && mkdir -p ~deploy/.ssh && chmod 700 ~deploy/.ssh &&
  vi ~deploy/.ssh/authorized_keys && chmod 400 ~deploy/.ssh/authorized_keys &&
  chown -R deploy:deploy ~deploy && echo 'deploy ALL=(ALL) NOPASSWD: ALL' > /etc/sudoers.d/deploy
  ```
3. Make sure the settings in `vars/cons.yml` and `vars/private.yml` are to your liking.
  * If you've just cloned this repo, private.yml may not exist. See SECRETS.md for a var list.
4. Set DNS records before deploy to ensure LetsEncrypt works as intended.
5. Run the playbook: `ansible-playbook -i ./hosts cons.yml`
  * Or just run a subsection: `ansible-playbook -i ./hosts --tags=foo cons.yml`
  * Or just run updates: `ansible-playbook -i ./hosts --tags=updates cons.yml`

## cons

Toplevel tags are roles while nested tags are includes.

* common
  * security
* web
* blog
  * git
  * lisp
  * quicklisp
  * coleslaw
* mail
  * postgres
  * postfix
  * dovecot
  * opendkim
  * dspam
* bookmarks
* irc
* radio
  * nodejs
  * s3fs
  * groovebasin
* media
  * media_basics
  * mediagoblin
  * media_db
  * media_config
* redlinernotes

## metaobject

* thinkpad
  * ssh_keys
  * basics
  * shell
  * apps
* developer
  * emacs
  * ruby
    * rbenv
    * mri
  * lisp
    * clozure
    * quicklisp
  * ocaml
  * latex
