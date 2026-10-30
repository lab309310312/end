<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<% String name=request.getParameter("studentName"); if(name==null) name="(not supplied)";
name=name.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;").replace("\"","&quot;").replace("'","&#39;"); %>
<!doctype html><html lang="en"><head><meta charset="UTF-8"><title>Hidden Field Result</title></head>
<body style="font-family:Arial,sans-serif;max-width:700px;margin:40px auto"><h1>Hidden Field Result</h1>
<p>Value received from hidden field: <strong><%= name %></strong></p><p>Hidden inputs are not confidential or tamper-proof.</p><a href="session.jsp">Back</a></body></html>
