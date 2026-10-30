<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<!doctype html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Session Handling Practical</title>
<style>
body{font-family:Arial,sans-serif;max-width:680px;margin:50px auto;padding:24px;background:#f4f7fb;color:#172033}
main{background:white;padding:28px;border-radius:14px;box-shadow:0 8px 28px #18294a18}
input,button{font:inherit;padding:12px;border-radius:8px}input{width:95%;border:1px solid #aab4c5}
button{margin-top:14px;background:#174ea6;color:white;border:0;cursor:pointer}.error{color:#b42318}
</style></head><body><main>
<h1>JSP/Servlet Session Demo</h1><p>Enter your name to start a server-side HTTP session.</p>
<% if ("1".equals(request.getParameter("error"))) { %><p class="error">Please enter a name.</p><% } %>
<form action="${pageContext.request.contextPath}/start-session" method="post">
<label for="name">Student name</label><br><br><input id="name" name="name" required maxlength="80" autocomplete="name">
<br><button type="submit">Start Session</button></form>
</main></body></html>
