from platform import system
from python_hosts import Hosts, HostsEntry
from pyuac import isUserAdmin, runAsAdmin
from tldextract import extract

hosts = {
    "Darwin":   "/etc/hosts",                             # macOS
    "Linux":    "/etc/hosts",                             # Linux (any distro)
    "SunOS":    "/etc/hosts",                             # Solaris
    "Windows": r"C:\Windows\System32\drivers\etc\hosts"   # Windows (aka NT)
}
hosts_file = Hosts(path = hosts[system()])
localhost = "127.0.0.1"


def block(websites):
    sites_to_block = list(websites.split(" "))
    for site in sites_to_block:
        site = extract(site) # To remove any trailing slash and https://
        domain = site.domain + "." + site.suffix # To remove any trailing slash and https://
        if hosts_file.exists(names = [domain]):
            print(f"{domain} has already been blocked.")
        else:
            domain_wildcard = "*." + site.domain + "." + site.suffix
            hosts_entry = HostsEntry(entry_type = "ipv4", address = localhost, names = [domain, domain_wildcard], comment = "web_block")
            hosts_entry_wildcard = HostsEntry(entry_type = "ipv4", address = localhost, names =
            hosts_file.add([hosts_entry])
            if isUserAdmin():
                hosts_file.write()
                print(f"Blocked {domain}.")
            else:
                if system() == "Windows":
                    runAsAdmin()
                else:
                    print("Insufficient permissions. Try running using `sudo`.")


def unblock(websites):
    sites_to_unblock = list(websites.split(" "))
    for site in sites_to_unblock:
        site = extract(site)
        domain = site.domain + "." + site.suffix
        if hosts_file.exists(names = [domain]):
            hosts_file.remove_all_matching(name = domain)
            if isUserAdmin():
                hosts_file.write()
                print(f"Unblocked {domain}.")
            else:
                if system() == "Windows":
                    runAsAdmin()
                else:
                    print("Insufficient permissions. Try running using `sudo`.")
        else:
            print(f"{domain} has already been unblocked.")
