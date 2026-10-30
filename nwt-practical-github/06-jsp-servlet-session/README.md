# Practical 6 — JSP/Servlet Session Handling

**Aim:** Demonstrate server-side `HttpSession`, URL rewriting, and hidden form fields.

## Requirements
- JDK 17+, Maven, Apache Tomcat 10.1
- Uses `jakarta.servlet.*`; Tomcat 9 requires `javax.servlet.*` imports instead.

## Run
```bash
mvn clean package
```
Copy `target/session-demo.war` to Tomcat's `webapps/`, start Tomcat, then open `http://localhost:8080/session-demo/`.

## Demonstration
1. Enter a name on the home page.
2. The servlet stores it in an `HttpSession`.
3. Show the URL-encoded link using `response.encodeURL(...)`.
4. Submit the hidden-field form and inspect the received value.
5. Explain that hidden fields and URL parameters are client-visible and tamperable; do not store secrets in them.
