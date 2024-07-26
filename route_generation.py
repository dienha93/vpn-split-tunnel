import subprocess
target_domains = [
    'github.com',
    'api.github.com',
    'avatars.githubusercontent.com',
    'collector.github.com',
    'github.githubassets.com',
]
all_ip_domains = []
local_gateway_ip = '192.168.1.1'
for skype_domain in target_domains:
    result = subprocess.check_output(['dig', '+short',  skype_domain])
    ip_domains = result.decode().strip().split('\n')
    for ip_domain in ip_domains:
        all_ip_domains.append(ip_domain);
for ip_domain in all_ip_domains:
    print(f'sudo route add {ip_domain if not ip_domain.endswith(".") else ip_domain[:-1]}{"" if ip_domain.endswith(".") else "/32"} {local_gateway_ip}')
