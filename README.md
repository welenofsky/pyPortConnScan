pyPortConnScan
=======

A python TCP "connect scan" port scanner ported to Python 3. pyPortConnScan is a command line utility that sends TCP command to a specified port and returns the response. pyPortConnScan can scan multiple ports at a time but only one server at a time. An example is below. 


python3 portscan.py -H 127.0.0.1 -p 20,22,80

pyPortConnScan can be useful for people interested in seeing if a specific service is running on a specified ip:port. Most of the code/ideas was from a book called Violent Python and I just ported it to python 3.