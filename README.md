
# Port-Banner-Grabber

Python3 program which detects open ports and give banner output on the socket connection.





## Usage:


```bash
  python3 PortBannerGrabber.py [host] [start-port] [end-port] [maximum-characters]
```
## Example:
```bash
  python3 PortBannerGrabber.py test.com 0 22 1024
```
```
  Host : test.com
  Scanning from 0 to 22
  --
  Port 21 is open. Info: 220 FTP Server ready.

```
