import socket

ip_tables = []
routes = []
one_port_entry = '$IPTABLES -A forward_vpn -s $VPNUSERNET -d ADRESIP -p tcp --dport PORTS -j ACCEPT ## HOSTNAME'
multi_port_entry = '$IPTABLES -A forward_vpn -s $VPNUSERNET -d ADRESIP -p tcp -m multiport --dports PORTS -j ACCEPT ## HOSTNAME'
route_entry = 'push "route ADRESIP 255.255.255.255" ## HOSTNAME'


def make_one_port_entry(ipv4, hostname, port):
    ip_table = one_port_entry.replace('ADRESIP', ipv4)
    ip_table = ip_table.replace('PORTS', port)
    ip_table = ip_table.replace('HOSTNAME', hostname)
    ip_tables.append(ip_table)
    route = route_entry.replace('ADRESIP', ipv4)
    route = route.replace('HOSTNAME', hostname)
    routes.append(route)


def make_multi_port_entry(ipv4, hostname, ports):
    ip_table = multi_port_entry.replace('ADRESIP', ipv4)
    ip_table = ip_table.replace('PORTS', port)
    ip_table = ip_table.replace('HOSTNAME', hostname)
    ip_tables.append(ip_table)
    route = route_entry.replace('ADRESIP', ipv4)
    route = route.replace('HOSTNAME', hostname)
    routes.append(route)


def print_ip_tables():
    for x in ip_tables:
        print(x)


def print_routes():
    for x in routes:
        print(x)


def print_results():
    print("\nIP Tables:")
    print_ip_tables()
    print("\nRoutes:")
    print_routes()


print('How many hostnames you have?')
amount_of_hostnames = input()


for x in range(int(amount_of_hostnames)):
    hostname = input('Enter hostname: ')
    ip_adress = socket.gethostbyname(hostname)
    port = input('Enter port or ports eg.80,443: ')
    if ',' in port:
        make_multi_port_entry(ip_adress, hostname, port)
    else:
        make_one_port_entry(ip_adress, hostname, port)
print_results()
