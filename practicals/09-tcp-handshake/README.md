# Practical 9 — TCP Connection Establishment and Termination
**Aim:** Demonstrate TCP's three-way handshake and orderly connection termination.

Run with Python 3:
```bash
python tcp_demo.py
```

## Three-way handshake
1. **SYN:** Client requests a connection with initial sequence number `x`.
2. **SYN-ACK:** Server acknowledges `x + 1` and sends its sequence number `y`.
3. **ACK:** Client acknowledges `y + 1`; the connection is established.

## Typical four-segment termination
1. Client sends **FIN**.
2. Server sends **ACK**.
3. Server sends **FIN** when ready.
4. Client sends **ACK**.

TCP is full duplex, so each direction closes independently. Captures can differ due to timing or combined ACK/FIN segments. This program is a simulation, not a live packet capture.
