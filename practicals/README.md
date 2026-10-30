# Academic Lab Practicals

Structured lab experiments and implementations for the **Network and Web Technology (NWT)** course.

## Practicals Directory

| Folder | Practical Title | Key Concepts & Stack |
|---|---|---|
| [`06-jsp-servlet-session/`](06-jsp-servlet-session/) | Practical 6 — JSP/Servlet Session Handling | `HttpSession`, cookies, URL rewriting, hidden form fields (Java 17+, Maven, Tomcat 10.1) |
| [`07-html5-css3/`](07-html5-css3/) | Practical 7 — HTML5 & CSS3 Responsive Page | Semantic HTML5 tags (`<header>`, `<nav>`, `<main>`, `<section>`), CSS Flexbox/Grid, media queries |
| [`08-javascript-integration/`](08-javascript-integration/) | Practical 8 — JavaScript Form Validation | Client-side DOM manipulation, event listeners, `preventDefault()`, sanitization |
| [`09-tcp-handshake/`](09-tcp-handshake/) | Practical 9 — TCP Handshake Simulation | TCP 3-way handshake (`SYN`, `SYN-ACK`, `ACK`) and 4-way orderly teardown (`FIN`/`ACK`) (Python 3) |
| [`10-ruby-on-rails/`](10-ruby-on-rails/) | Practical 10 — Ruby on Rails Task Board | MVC architecture, RESTful routing, ActiveRecord models, migrations, CRUD (Ruby 3, Rails 7.1+, SQLite3) |

## Quick Execution Reference

### Practical 6 (Java / Jakarta EE)
```bash
cd practicals/06-jsp-servlet-session
mvn clean package
```
Deploy `target/session-demo.war` to Apache Tomcat 10.1 `webapps/` folder and visit `http://localhost:8080/session-demo/`.

### Practical 7 (HTML5 & CSS3)
Open `practicals/07-html5-css3/index.html` directly in any web browser.

### Practical 8 (JavaScript Integration)
Open `practicals/08-javascript-integration/index.html` directly in any web browser.

### Practical 9 (TCP Simulation)
```bash
cd practicals/09-tcp-handshake
python tcp_demo.py
```

### Practical 10 (Ruby on Rails)
Generate a base Rails shell, integrate the provided MVC files, run migrations, and start the local Puma server:
```bash
rails new task_board -d sqlite3
cd task_board
# Copy practicals/10-ruby-on-rails files into this app
bundle install
bin/rails db:migrate
bin/rails server
```
Visit `http://localhost:3000`.
