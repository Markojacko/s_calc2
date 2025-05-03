import ipaddress

def summarize_network(ip, mask):
    cidr = f"{ip}/{mask}"
    network = ipaddress.ip_network(cidr, strict=False)

    total_hosts = network.num_addresses
    usable_hosts = total_hosts - 2 if network.version == 4 and total_hosts > 2 else total_hosts

    if usable_hosts > 0:
        first_ip = network.network_address + 1 if network.version == 4 else network.network_address
        last_ip = network.broadcast_address - 1 if network.version == 4 else network.network_address + (usable_hosts - 1)
    else:
        first_ip = 'N/A'
        last_ip = 'N/A'

    result = {
        'Version': f"IPv{network.version}",
        'Network Address': str(network.network_address),
        'Broadcast Address': str(network.broadcast_address) if network.version == 4 else 'N/A',
        'Subnet Mask': str(network.netmask),
        'Wildcard Mask': str(network.hostmask) if network.version == 4 else 'N/A',
        'Number of Hosts': usable_hosts,
        'First Usable IP': str(first_ip) if usable_hosts > 0 else 'N/A',
        'Last Usable IP': str(last_ip) if usable_hosts > 0 else 'N/A',
        'CIDR': str(network.with_prefixlen),
        'total_hosts': total_hosts,
        'usable_hosts': usable_hosts,
    }

    # Cloud compatibility warnings
    warnings = []
    if network.version == 4:
        if total_hosts < 8:
            warnings.append("⚠️ Azure: Subnet may be too small. Azure reserves 5 IPs.")
        if total_hosts < 6:
            warnings.append("⚠️ AWS: Subnet may be too small. AWS reserves 5 IPs.")
        if total_hosts < 10:
            warnings.append("⚠️ GCP: Subnet may be too small. GCP reserves several IPs.")
    if not warnings:
        warnings.append("✅ Compatible with major clouds.")

    return {'network': network, 'result': result, 'cloud_warnings': warnings}

def split_network(network, new_prefix):
    return list(network.subnets(new_prefix=new_prefix))
