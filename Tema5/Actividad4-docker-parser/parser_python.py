import sys
import re

def parse_docker_network(filepath):
    networks_found = []
    subnets_found = []
    
    with open(filepath, 'r') as f:
        for line in f:
            line_str = line.strip()
            if "net_interface_" in line_str:
                networks_found.append(line_str)
            elif line_str.startswith("subnet:"):
                subnets_found.append(line_str.split(":")[1].strip())
                
    return len(networks_found), len(subnets_found)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        parse_docker_network(sys.argv[1])