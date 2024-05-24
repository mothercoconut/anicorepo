# Network Security Scanner

The Network Security Scanner is a Python-based tool that provides various network scanning functionalities, including network device discovery, OS fingerprinting, port scanning, and vulnerability scanning.

## Requirements
- Python 3.x
- Nmap library (`python-nmap`)

## Installation
1. Clone the repository or download the source code files.
2. Install the required dependencies by running the following command:
        pip install -r requirements.txt
You will most likely also need to set the environment variables, and if so, run the setvariables.bat script and it will automatically configure ONLY the installed and needed packages (if they're installed in the default locations!). If you'd prefer not to run that, I understand, and I can instead provide an example or demonstration!


## Usage
To run it, I prefer just pressing run, having it hand me the python.exe path as well as the .py file and then just adding my args onto the end of that!
To run the Network Security Scanner, use the following command:
        python network_scanner.py <target> [options]

- `<target>`: The target host or network range to scan.

Available options:
- `-p` or `--ports`: Port range to scan (default: 1-450).
- `-o` or `--output`: Output file to save the results in JSON format.
- `-d` or `--discover`: Perform network device discovery.
- `-f` or `--fingerprint`: Perform OS fingerprinting on discovered devices. !!MUST USE -d ARG FOR -f TO WORK!!
- `-v` or `--vulnerabilities`: Perform vulnerability scanning.
- `-s` or `--subdomains`: Perform subdomain scanning.
- `--dos`: Perform DoS attack with the specified number of requests.

Example usage: python network_scanner.py 192.168.0.0/24 -p 1 1000 -d -f -v

^This will scan the network, identified as 192.169.0.0/24, from port 1 to port 1000 (-p 1 1000), will identify devices (-d), fingerprint them (-f), and also perform a vulnerability scan on all scanned ports (-v).

## Architecture
The Network Security Scanner consists of the following main components:
1. `scan_ports`: Performs port scanning on the specified target using Nmap.
2. `discover_devices`: Performs network device discovery using Nmap's `-sn` option.
3. `fingerprint_os`: Performs OS fingerprinting on discovered devices using Nmap's `-O` option.
4. `scan_vulnerabilities`: Performs vulnerability scanning using Nmap's `vulners` script.
5. `scan_subdomains`: Performs subdomain scanning using a list of common subdomains.
6. `perform_dos`: Performs a DoS attack on the specified target with the given number of requests.

The tool utilizes the `python-nmap` library to interact with Nmap and perform the scanning operations. The results are stored in a dictionary and can be optionally saved to a JSON file.