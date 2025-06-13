import socket
import argparse


def scan_tcp_port(host: str, port: int) -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(0.3)
        if sock.connect_ex((host, port)) == 0:
            print(f"port {port}|tcp opened")
        else:
            print(f"port {port}|tcp closed")


def scan_udp_port(host: str, port: int) -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.settimeout(0.3)
        try:
            sock.sendto(b'req\r\n\r\n', (host, port))
            sock.recv(1024)
            print(f"port {port}|udp opened")
        except socket.timeout:
            pass
        except socket.error:
            print(f"port {port}|udp closed")


def scan_ports(host: str, ports: list[int]) -> None:
    print("Scanning ports...")
    for port in ports:
        scan_tcp_port(host, port)
        scan_udp_port(host, port)


def main() -> None:
    parser = argparse.ArgumentParser(description="Scan open ports on a given host")
    parser.add_argument("host", type=str, help="Target host (localhost or IP address)")
    parser.add_argument("ports", type=str, help="Ports")

    args = parser.parse_args()

    ranges = [x.split('-') for x in args.ports.split(',')]
    ports = [x for y in ranges for x in range(int(y[0]), int(y[-1]) + 1)]

    scan_ports(args.host, ports)


if __name__ == "__main__":
    main()
