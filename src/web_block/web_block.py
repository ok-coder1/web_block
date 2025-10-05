import platform
import tldextract
from python_hosts import Hosts, HostsEntry

hosts = {
    "Windows": r"C:\Windows\System32\drivers\etc\hosts",  # Windows (aka NT)
    "Linux":    "/etc/hosts",                             # Linux (any distro)
    "SunOS":    "/etc/hosts",                             # Solaris
    "Darwin":   "/etc/hosts"                              # macOS
}
hosts_file = Hosts(path = hosts[platform.system()])
localhost = "127.0.0.1"


def block(websites):
    sites_to_block = list(websites.split(" "))
    for site in sites_to_block:
        site = tldextract.extract(site)
        domain = site.domain + "." + site.suffix
        if hosts_file.exists(names = [domain]):
            print(f"{domain} has already been blocked.")
        else:
            hosts_entry = HostsEntry(entry_type = "ipv4", address = localhost, names = [domain], comment = "web_block")
            hosts_file.add([hosts_entry])
            hosts_file.write()
            print(f"Blocked {domain}.")


def unblock(websites):
    sites_to_unblock = list(websites.split(" "))
    for site in sites_to_unblock:
        site = tldextract.extract(site)
        domain = site.domain + "." + site.suffix
        if hosts_file.exists(names = [domain]):
            hosts_file.remove_all_matching(name = domain)
            hosts_file.write()
            print(f"Unblocked {domain}.")
        else:
            print(f"{domain} has already been unblocked.")
