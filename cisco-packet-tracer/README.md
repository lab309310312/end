# Cisco Packet Tracer Network Simulations

This directory contains Cisco Packet Tracer (`.pkt`) network topology designs and configuration labs for the **Network and Web Technology (NWT)** curriculum.

## Files Overview

| File | Description | Core Concepts |
|---|---|---|
| [`bus-topology.pkt`](bus-topology.pkt) | Bus Topology Design | Single shared backbone cable, terminators, drop lines, shared collision domain |
| [`star-topology.pkt`](star-topology.pkt) | Star Topology Design | Central network device (switch/hub), point-to-point connections, fault isolation |
| [`ring-topology.pkt`](ring-topology.pkt) | Ring Topology Design | Circular node arrangement, unidirectional/bidirectional transmission |
| [`mesh-topology.pkt`](mesh-topology.pkt) | Mesh Topology Design | Redundant point-to-point links between nodes, high availability, fault tolerance |
| [`hybrid-topology.pkt`](hybrid-topology.pkt) | Hybrid Topology Design | Combination of two or more distinct topologies (e.g., Star-Bus or Star-Ring) |
| [`lan-configuration.pkt`](lan-configuration.pkt) | Local Area Network (LAN) | Switch ports configuration, PC IPv4 addressing, subnet masks, ICMP connectivity tests |
| [`vlan-configuration.pkt`](vlan-configuration.pkt) | Virtual LAN (VLAN) & Trunking | 802.1Q trunk links, VLAN database, broadcast domain segmentation, Router-on-a-Stick (sub-interfaces) |

## Requirements
- **Cisco Packet Tracer** version 8.0 or newer (download from [Cisco Networking Academy / Skills for All](https://www.netacad.com/)).

## How to Open and Simulate
1. Launch **Cisco Packet Tracer**.
2. Go to **File -> Open...** (or press `Ctrl + O`).
3. Select any `.pkt` file from this directory.
4. Switch to **Simulation Mode** (bottom-right icon or `Shift + S`) to inspect ARP, ICMP, and switch frame forwarding in detail.
5. In **Realtime Mode**, click on any PC -> **Desktop** -> **Command Prompt** and test connectivity using:
   ```cmd
   ping <destination-ip>
   ```
