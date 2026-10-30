package com.example;

import java.io.IOException;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.servlet.http.HttpSession;

@WebServlet("/start-session")
public class SessionServlet extends HttpServlet {
    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        request.setCharacterEncoding("UTF-8");
        String name = request.getParameter("name");
        if (name == null || name.isBlank()) {
            response.sendRedirect(request.getContextPath() + "/index.jsp?error=1");
            return;
        }
        HttpSession session = request.getSession(true);
        session.setAttribute("studentName", name.trim());
        response.sendRedirect(response.encodeRedirectURL(request.getContextPath() + "/session.jsp"));
    }
}
