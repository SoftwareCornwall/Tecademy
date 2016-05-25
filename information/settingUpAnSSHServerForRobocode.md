# How to set up a Robocode SSH server to upload your Robocode robot

## Install an ssh server on your Robocode server

Open a terminal and type ```sudo apt-get install openssh-server```

## Check the server IP address

In the terminal, type ```ifconfig```

Look for the IP address which will probably be 10.x.x.x or 192.168.x.x

## Check your client can connect to the SSH server

On the client (probably a Raspberry Pi) open a terminal and ping the Robocode SSH server to ensure you can reach it.  For example, if the server ip address is 192.168.1.100 then you would type ```ping 192.168.1.100```

Press ```Ctrl+c``` to stop the pings

If you have connectivity to the Robocode server you should see a response like

```64 bytes from 192.168.1.100: icmp_seq=1 ttl=64 time=0.071 ms```

If you cannot connect to the server, you will need to get some help from your network administrator.

## Generate an SSH key pair

To speed things up, you will generate an SSH key pair so that you don't have to provide a password everytime you upload your robot code to the Robocode SSH server.

*Instructions here to generate the key and add the key to the server*

## Upload your Robocode robot

Assuming the Robocode SSH server is 192.168.1.100, use the following command to upload your robot to the server

```ssh 192.168.1.100 - blah blah```


