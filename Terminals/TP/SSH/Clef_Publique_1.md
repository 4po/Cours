====================================
+                                  +
+      Compte rendus : Adrien      +
+                                  +
====================================

1) On essaye dee ce connecter par ssh à la machine 10.254.0.9 :

$ssh 10.254.0.9
capteur@10.254.0.9's password:
Permission denied, please try again.
Malheureusement il nous faut un mot de passe.

On nous donne le noms et le mot de passe de la machine :

ssh pi@10.254.0.9
pi@10.254.0.9's password:
Linux Rjardin21 5.4.72+ #1356 Thu Oct 22 13:56:00 BST 2020 armv6l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Thu Nov 19 23:17:53 2020

pi@Rjardin21:~ $

Et voilà on est connecter !


**2) On vas essayer de faire en sorte de ce connecter sans mot de passe :**

```
capteur@l-2-319-04:~$ ssh-copy-id -i .ssh/id_rsa.pub pi@10.254.0.9
/usr/bin/ssh-copy-id: INFO: Source of key(s) to be installed: ".ssh/id_rsa.pub"
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
pi@10.254.0.9's password:

Number of key(s) added: 1

Now try logging into the machine, with:   "ssh 'pi@10.254.0.9'"
and check to make sure that only the key(s) you wanted were added.```
