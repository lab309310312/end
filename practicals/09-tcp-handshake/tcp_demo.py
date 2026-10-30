#!/usr/bin/env python3
# Educational simulation of TCP connection setup and teardown.

def main():
    client_isn = 1000
    server_isn = 5000
    print("TCP THREE-WAY HANDSHAKE")
    print("-" * 58)
    print(f"Client -> Server : SYN     seq={client_isn}")
    print(f"Server -> Client : SYN-ACK seq={server_isn}, ack={client_isn + 1}")
    print(f"Client -> Server : ACK     seq={client_isn + 1}, ack={server_isn + 1}")
    print("State: ESTABLISHED\n")

    print("TCP ORDERLY CONNECTION TERMINATION (typical four segments)")
    print("-" * 58)
    print(f"Client -> Server : FIN     seq={client_isn + 1}")
    print(f"Server -> Client : ACK     ack={client_isn + 2}")
    print(f"Server -> Client : FIN     seq={server_isn + 1}")
    print(f"Client -> Server : ACK     ack={server_isn + 2}")
    print("State: CLOSED (after the required TCP state transitions)")
    print("\nSequence numbers are illustrative; FIN consumes one sequence number.")
    print("This is a simulation, not actual network traffic.")

if __name__ == "__main__":
    main()
