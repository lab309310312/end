# Network & Web Technology (NWT) Practical Lab

A complete, structured laboratory repository containing Cisco Packet Tracer network simulation designs, curriculum practicals, and interactive web applications.

---

## Repository Directory Structure

```text
.
├── cisco-packet-tracer/               # Cisco Packet Tracer (.pkt) simulation models
│   ├── README.md                      # Network topologies & simulation guide
│   ├── bus-topology.pkt               # Bus topology simulation
│   ├── star-topology.pkt              # Star topology simulation
│   ├── ring-topology.pkt              # Ring topology simulation
│   ├── mesh-topology.pkt              # Mesh topology simulation
│   ├── hybrid-topology.pkt            # Hybrid topology simulation
│   ├── lan-configuration.pkt          # Local Area Network setup & ICMP testing
│   └── vlan-configuration.pkt         # VLAN segmentation & 802.1Q trunking
│
├── practicals/                        # Academic lab experiments & implementations
│   ├── README.md                      # Detailed practical instructions & run commands
│   ├── 06-jsp-servlet-session/        # Practical 6: HttpSession, URL rewriting, hidden fields
│   ├── 07-html5-css3/                 # Practical 7: Semantic HTML5 & responsive CSS3 styling
│   ├── 08-javascript-integration/     # Practical 8: DOM manipulation & form validation
│   ├── 09-tcp-handshake/              # Practical 9: TCP 3-way handshake & teardown simulation
│   └── 10-ruby-on-rails/              # Practical 10: Rails MVC task board with database
│
└── web-projects/                      # Standalone interactive frontend web applications
    ├── README.md                      # Overview of web applications
    ├── 01-portfolio/                  # Student portfolio website with typing effect
    ├── 02-task-board/                 # Task tracker with priority filtering & localStorage
    ├── 03-calculator/                 # Arithmetic calculator with history display
    ├── 04-chai-and-co-menu/           # Cafe menu with live search & cart drawer
    └── 05-networking-quiz/            # Timed networking quiz with dynamic scoring
```

---

## 1. Cisco Packet Tracer Topologies (`cisco-packet-tracer/`)

Network simulation files built for **Cisco Packet Tracer (v8.0+)**:

| File | Topology / Scenario | Core Concepts |
|---|---|---|
| [`bus-topology.pkt`](cisco-packet-tracer/bus-topology.pkt) | Bus Topology | Single shared coaxial trunk, BNC connectors, terminators, collision domain |
| [`star-topology.pkt`](cisco-packet-tracer/star-topology.pkt) | Star Topology | Central switch/hub architecture, dedicated host links, fault isolation |
| [`ring-topology.pkt`](cisco-packet-tracer/ring-topology.pkt) | Ring Topology | Closed-loop sequential data circulation, token passing mechanism |
| [`mesh-topology.pkt`](cisco-packet-tracer/mesh-topology.pkt) | Mesh Topology | Redundant multi-point links, high availability, fault tolerance |
| [`hybrid-topology.pkt`](cisco-packet-tracer/hybrid-topology.pkt) | Hybrid Topology | Hierarchical combination of star and bus topologies |
| [`lan-configuration.pkt`](cisco-packet-tracer/lan-configuration.pkt) | LAN Configuration | Switch port assignment, IPv4 host addressing, ICMP echo testing |
| [`vlan-configuration.pkt`](cisco-packet-tracer/vlan-configuration.pkt) | VLAN & Trunking | 802.1Q trunk links, broadcast domain reduction, router-on-a-stick |

---

## 2. Academic Lab Practicals (`practicals/`)

Curriculum practicals with step-by-step code and documentation:

| Lab | Name | Stack | Description |
|---|---|---|---|
| [`06`](practicals/06-jsp-servlet-session/) | JSP / Servlet Session Handling | Java 17+, Jakarta EE, Tomcat 10.1, Maven | Demonstrates `HttpSession`, URL rewriting (`encodeURL`), and hidden form inputs. |
| [`07`](practicals/07-html5-css3/) | HTML5 & CSS3 Responsive UI | HTML5, CSS3 Flexbox/Grid | Semantic structure (`<header>`, `<nav>`, `<main>`, `<article>`) and responsive media queries. |
| [`08`](practicals/08-javascript-integration/) | Interactive Form Validation | HTML5, CSS3, JavaScript | Event handling, input validation, error messages, and safe DOM manipulation. |
| [`09`](practicals/09-tcp-handshake/) | TCP Three-Way Handshake Simulation | Python 3 | Terminal simulation of TCP 3-way handshake (`SYN`, `SYN-ACK`, `ACK`) and 4-way teardown (`FIN`/`ACK`). |
| [`10`](practicals/10-ruby-on-rails/) | Rails Task Board Application | Ruby 3, Rails 7.1+, SQLite3 | MVC architecture, RESTful routing, ActiveRecord models, database migrations, and CRUD operations. |

---

## 3. Interactive Web Projects (`web-projects/`)

Client-side interactive web applications built with modern HTML5, CSS3, and ES6 JavaScript:

| Project | Name | Description | Key Tech / Features |
|---|---|---|---|
| [`01`](web-projects/01-portfolio/) | Developer Portfolio | Personal portfolio showcase | Typewriter effect, mobile hamburger menu, progress bars, contact validation |
| [`02`](web-projects/02-task-board/) | Task Board App | Productivity task tracker | Priority filtering (Low/Med/High), status views, `localStorage` persistence |
| [`03`](web-projects/03-calculator/) | Web Calculator | Arithmetic calculator | Standard operations, decimals, percentage, backspace (`DEL`), calculation history |
| [`04`](web-projects/04-chai-and-co-menu/) | Chai & Co. Menu | Food ordering system | Category filter tabs, real-time live search, interactive cart drawer with live subtotal |
| [`05`](web-projects/05-networking-quiz/) | Networking Quiz | Timed quiz challenge | 5 networking questions, 15s countdown timer bar, instant validation, score recap |

---

## Getting Started

### Prerequisites
- **Git** for version control.
- **Modern Web Browser** (Chrome, Firefox, Edge, Safari) for web projects and practicals 07 & 08.
- **Python 3.x** for practical 09.
- **Java 17+ & Maven** with **Apache Tomcat 10.1** for practical 06.
- **Ruby 3+ & Rails 7.1+** for practical 10.
- **Cisco Packet Tracer (v8.0+)** for network topology simulations.

### Clone the Repository
```bash
git clone https://github.com/lab309310312/end.git
cd end
```

### Running Practicals & Projects

#### Running Web Projects & Web Practicals
Open any `index.html` file in a browser, or run a local HTTP server from the root directory:
```bash
python -m http.server 8000
```
Navigate to:
- Practical 7: `http://localhost:8000/practicals/07-html5-css3/index.html`
- Practical 8: `http://localhost:8000/practicals/08-javascript-integration/index.html`
- Web Projects: `http://localhost:8000/web-projects/<project-name>/`

#### Running TCP Handshake Simulation (Practical 9)
```bash
cd practicals/09-tcp-handshake
python tcp_demo.py
```

#### Building Servlet Session Demo (Practical 6)
```bash
cd practicals/06-jsp-servlet-session
mvn clean package
```
Deploy the generated `target/session-demo.war` to Tomcat's `webapps/` folder.
