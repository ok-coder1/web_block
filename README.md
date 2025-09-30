# web_block

A simple Python module to block websites. \
It configures the hosts file (`/etc/hosts` on macOS or Linux and `C:\Windows\System32\drivers\etc\hosts` on Windows) to redirect a website passed in as an argument to localhost (`127.0.0.1`), essentially blocking it.

## Usage:
### Blocking websites
```py
import web_block
web_block.block("example.com example.org")
```
It's as simple as that.
#### Also you do need to add the file to your directory till this is published to PyPI.