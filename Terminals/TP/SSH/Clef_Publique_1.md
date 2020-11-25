```
====================================
+                                  +
+      Compte rendus : 0xE         +
+                                  +
====================================
```

**1) On essaye de ce connecter par ssh à la machine 10.254.0.9 :**

```
$ssh 10.254.0.9
capteur@10.254.0.9's password:
Permission denied, please try again.
```

**Malheureusement il nous faut un mot de passe.**

**On nous donne le noms et le mot de passe de la machine :**

```
pi@10.254.0.9's password:
Linux Rjardin21 5.4.72+ #1356 Thu Oct 22 13:56:00 BST 2020 armv6l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Thu Nov 19 23:17:53 2020

pi@Rjardin21:~ $
```

**Et voilà on est connecter !**

**2) On vas essayer de faire en sorte de ce connecter sans mot de passe :**

```markdown
capteur@l-2-319-04:~$ ssh-copy-id -i .ssh/id_rsa.pub pi@10.254.0.9
/usr/bin/ssh-copy-id: INFO: Source of key(s) to be installed: ".ssh/id_rsa.pub"
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
pi@10.254.0.9's password:

Number of key(s) added: 1

Now try logging into the machine, with:   "ssh 'pi@10.254.0.9'"
and check to make sure that only the key(s) you wanted were added.
```

**Nous avons donc ici le masque (255.255.0.0 (Notation CIDR '/8')) et l'adresse Ip (10.254.0.9).**

**On cherche la passerelle :**

```bash
pi@Rjardin21:~ $ netstat -rde
Table de routage IP du noyau
Destination     Passerelle      Genmask         Indic Metric Ref    Use Iface
10.0.0.0        0.0.0.0         255.0.0.0       U     202    0        0 eth0
```

**0.0.0.0 ici on ne connais donc pas la passerelle on passe par un proxy.**

**3) On veut maintenant installer des paquest apt sur la machine on fais donc :**

```bash
capteur@l-2-319-04:~$ scp /etc/apt/apt.conf pi@10.254.0.9:/etc/apt
scp: /etc/apt/apt.conf: Permission denied
```

**Nous n'avons pas les permissions, on fais donc : **

```bash
capteur@l-2-319-04:~$ scp /etc/apt/apt.conf pi@10.254.0.9:/home/pi
apt.conf                                                                                           100%   49    15.5KB/s   00:00                     
```

**Et voilà maintenant connectons-nous à la machine et on vas utilisé mv pour changer le fichié de place.**

```bash
capteur@l-2-319-04:~$ ssh pi@10.254.0.9
Linux Rjardin21 5.4.72+ #1356 Thu Oct 22 13:56:00 BST 2020 armv6l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Fri Nov 20 18:05:06 2020 from 10.23.19.4


pi@Rjardin21:~ $ sudo mv apt.conf /etc/apt/
```

**Enfin, le fichié et a la bonne place on vas donc installer néofetch : **

```bash
pi@Rjardin21:~ $ sudo apt install neofetch 
```

**On vas donc le lancé pour voir la config de la machine :**

```bash
pi@Rjardin21:~ $ neofetch 
  `.::///+:/-.        --///+//-:``    pi@Rjardin21 
 `+oooooooooooo:   `+oooooooooooo:    ------------ 
  /oooo++//ooooo:  ooooo+//+ooooo.    OS: Raspbian GNU/Linux 10 (buster) armv6l 
  `+ooooooo:-:oo-  +o+::/ooooooo:     Host: Raspberry Pi Model B Rev 2 
   `:oooooooo+``    `.oooooooo+-      Kernel: 5.4.72+ 
     `:++ooo/.        :+ooo+/.`       Uptime: 19 hours, 13 mins 
        ...`  `.----.` ``..           Packages: 519 (dpkg) 
     .::::-``:::::::::.`-:::-`        Shell: bash 5.0.3 
    -:::-`   .:::::::-`  `-:::-       Terminal: /dev/pts/0 
   `::.  `.--.`  `` `.---.``.::`      CPU: BCM2835 (1) @ 700MHz 
       .::::::::`  -::::::::` `       Memory: 41MiB / 431MiB 
 .::` .:::::::::- `::::::::::``::.
-:::` ::::::::::.  ::::::::::.`:::-                           
::::  -::::::::.   `-::::::::  ::::
-::-   .-:::-.``....``.-::-.   -::-
 .. ``       .::::::::.     `..`..
   -:::-`   -::::::::::`  .:::::`
   :::::::` -::::::::::` :::::::.
   .:::::::  -::::::::. ::::::::
    `-:::::`   ..--.`   ::::::.
      `...`  `...--..`  `...`
            .::::::::::
             `.-::::-`
```

**Et voilà nous avons nos composant d'affichié.**

**4) On vas utilisé htop pour voir les processus en cours :**

<a href="https://ibb.co/jgCfZXP"><img src="https://i.ibb.co/pJHwrFB/Capture-du-2020-11-25-09-23-20.png" alt="Capture-du-2020-11-25-09-23-20" border="0"></a>

**5) Nous avons déjà fais le apt nous avons donc fini !**

