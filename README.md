# web_block

A simple Python module to block websites. \
It configures the hosts file (`/etc/hosts` on macOS or Linux and `C:\Windows\System32\drivers\etc\hosts` on Windows) to redirect a website passed in as an argument to localhost (`127.0.0.1`), essentially blocking it.

PyPI here: https://pypi.org/project/web-block

## Usage:
### Blocking websites
```py
import web_block
web_block.block("example.com example.org") # Use spaces to separate websites.
```
It's as simple as that.
### Unblocking websites
```py
import web_block
web_block.unblock("example.com example.org") # You can also use `https://www.example.com/abcd.html` and it will automatically get the domain for you.
```
