import socket
import argparse

def scan_ports(host, start_port, end_port):
    print("Scanning ports...")
    for port in range(start_port, end_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.1)
            if sock.connect_ex((host, port)) == 0:
                print(f"port {port} opened")

def main():
    parser = argparse.ArgumentParser(description="Scan open ports on a given host")
    parser.add_argument("host", type=str, help="Target host (localhost or IP address)")
    parser.add_argument("start", type=int, help="Start port")
    parser.add_argument("end", type=int, help="End port")

    args = parser.parse_args()

    if not (1 <= args.start <= 65535):
        print("Error: start port must be in the range 1-65535")
        return
    if not (1 <= args.end <= 65535):
        print("Error: end port must be in the range 1-65535")
        return
    if args.start > args.end:
        print("Error: start port there can't be more end port")
        return

    scan_ports(args.host, args.start, args.end)

if __name__ == "__main__":
    main()