# Metasploit Shodan Scan
This is a very simple metasploit module that Me and The Chandler Police Department Intern team made.
It uses the Metasploit python module aswell as the Shodan API. 
It takes the input IP and returns all of the open ports as well as the programs running on the ports.
I havent made it work with the msfconsole as metasploit dosent natively support python 
modules, and I'm worried about breaking the code if I try.

- --fhost : Use this modifier to set the IP address that you want to scan with Shodan.
- --apikey : Use this to set the Shodan apikey to run the scan.
  
If you are going to try this out, remember to add
'export PYTHONPATH=/usr/share/metasploit-framework/lib/msf/core/modules/external/python:$PYTHONPATH'
to your .bashrc or .zshrc to make sure the metasploit module is usable.
