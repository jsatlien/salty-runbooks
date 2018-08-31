## A Simple Postfix Relay

If SSL is clownshoes awful, email is a flaming tire fire of evil.

Self-hosting email is too much of a PITA to even be worth it.
If I had any decency, I'd just pay protonmail and set up a custom domain following their wizard.

However, I'm cheap and don't want to think about switching mail providers or monitoring _more_
accounts at the moment so I've set up a simple postfix relay to forward my messages to my
gmail account. I know, young me that cared about being spied on would be furious.

Of course, for gmail to send _outbound_ messages from this domain, we need the domain to
go whole hog with a LetsEncrypt cert, SASL authentication for the email, and a bunch of
additional postfix configuration. This guide has been cobbled together from several sources.
Let me just say I'm sorry it's like this.

* https://seasonofcode.com/posts/custom-domain-e-mails-with-postfix-and-gmail-the-missing-tutorial.html
* https://wiki.debian.org/PostfixAndSASL#Using_auxprop_with_sasldb
