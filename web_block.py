import platform
from pathlib import Path
from tempfile import mkstemp

hosts = {
    "Windows": r"C:\Windows\System32\drivers\etc\hosts",  # Windows (aka NT)
    "Linux":    "/etc/hosts",                             # Linux (any distro)
    "SunOS":    "/etc/hosts",                             # Solaris
    "Darwin":   "a.txt"                                   # macOS
}
localhost = "127.0.0.1"


def block(websites):
    host_file_path = hosts[platform.system()]
    sites_to_block = list(websites.split(" "))

    with open(host_file_path, "r+") as host_file:
        file_content = host_file.read()
        for site in sites_to_block:
            if site not in file_content:
                host_file.write(f"\n# web_block - {site}\n{localhost}\t{site}\n")
                print(f"Blocked {site}.")
            else:
                print(f"{site} has already been blocked.")


'''def unblock(websites):
    sites_to_unblock = list(websites.split(" "))
    filepath = hosts[platform.system()]
    tmp_fd, tmp_path = mkstemp(prefix=".web_block.", text=True)
    tmp_path = Path(tmp_path)
    with open(filepath, "r+") as host_file, open(tmp_fd, "w") as tmp_file:
        for line in host_file:
            if line in sites_to_unblock:
                next(host_file)
                continue
            tmp_file.write(line)
    tmp_path.replace(filepath)'''
