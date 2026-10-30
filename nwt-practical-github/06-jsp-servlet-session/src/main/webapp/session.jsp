<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<% String studentName = (String) session.getAttribute("studentName");
if (studentName == null) { response.sendRedirect(request.getContextPath() + "/index.jsp"); return; }
String safeName = studentName.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;").replace("\"","&quot;").replace("'","&#39;");
String safeHidden = studentName.replace("&","&amp;").replace("\"","&quot;").replace("<","&lt;").replace(">","&gt;"); %>
<!doctype html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Session Details</title>
<style>body{font-family:Arial,sans-serif;max-width:760px;margin:40px auto;padding:20px;background:#f4f7fb;color:#172033}
section{background:#fff;padding:24px;margin:16px 0;border-radius:12px}code{overflow-wrap:anywhere;background:#eef2f8;padding:3px 6px;border-radius:5px}
button,a{display:inline-block;padding:10px 14px;background:#174ea6;color:white;border:0;border-radius:7px;text-decoration:none}</style></head><body>
<h1>Session Handling Results</h1><section><h2>1. HttpSession</h2><p>Welcome, <strong><%= safeName %></strong>.</p>
<p>The name was stored on the server using <code>session.setAttribute("studentName", ...)</code>.</p></section>
<section><h2>2. URL rewriting</h2><p><code>response.encodeURL(...)</code> allows the container to append a session ID when URL-based tracking is needed.</p>
<a href="<%= response.encodeURL(request.getContextPath() + "/session.jsp") %>">Open encoded URL</a>
<p>The session ID may not visibly appear when cookies are supported.</p></section>
<section><h2>3. Hidden form field</h2><p>Hidden inputs are submitted with a form, but users can inspect or change them.</p>
<form action="<%= request.getContextPath() %>/hidden-result.jsp" method="post"><input type="hidden" name="studentName" value="<%= safeHidden %>"><button type="submit">Submit Hidden Field</button></form></section>
<p><a href="<%= request.getContextPath() %>/logout.jsp">End session</a></p></body></html>
