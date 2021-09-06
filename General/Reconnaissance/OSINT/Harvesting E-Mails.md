# Grabbing E-Mails from Google using goog-mail.py
`goog-mail.py` is a useful script used for getting E-Mail addresses from Google search results. Its author is unknown, but the script is available in many different places online.
1. You will need to download the script from https://github.com/leebaird/discover/blob/master/mods/goog-mail.py (or any other place you found it)
```bash
wget https://raw.githubusercontent.com/leebaird/discover/master/mods/goog-mail.py
```

```bash
┌──(backslash0㉿kali)-[~/MHN/Reconnaissance/OSINT]
└─$ wget https://raw.githubusercontent.com/leebaird/discover/master/mods/goog-mail.py                                                                                                                                                    1 ⨯
--2021-09-06 10:05:18--  https://raw.githubusercontent.com/leebaird/discover/master/mods/goog-mail.py
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.110.133, 185.199.108.133, 185.199.111.133, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.110.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 2103 (2.1K) [text/plain]
Saving to: ‘goog-mail.py’

goog-mail.py.1                                              100%[========================================================================================================================================>]   2.05K  --.-KB/s    in 0s      

2021-09-06 10:05:18 (41.9 MB/s) - ‘goog-mail.py’ saved [2103/2103]
```

2. Run the script providing a `domain_name`
```bash
python2 goog-mail.py [domain_name]
```

```bash
┌──(backslash0㉿kali)-[~/MHN/Reconnaissance/OSINT]
└─$ python2 goog-mail.py uk.ibm.com
ukclubom@uk.ibm.com
martyn.spink@uk.ibm.com
gfhelp@uk.ibm.com
iand_ferguson@uk.ibm.com
graham.butler@uk.ibm.com
laurence.carpanini@uk.ibm.com
Pensions@uk.ibm.com
Bennett@uk.ibm.com
ibm_crc@uk.ibm.com
brian.mcglone@uk.ibm.com
wakefim@uk.ibm.com
```

3. Make sure the E-Mails look valid
