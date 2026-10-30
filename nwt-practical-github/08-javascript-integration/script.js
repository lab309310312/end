"use strict";
const form = document.querySelector("#studentForm");
const nameInput = document.querySelector("#studentName");
const emailInput = document.querySelector("#email");
const message = document.querySelector("#message");
const result = document.querySelector("#result");

form.addEventListener("submit", (event) => {
  event.preventDefault();
  const name = nameInput.value.trim();
  const email = emailInput.value.trim();

  if (name.length < 2) {
    message.textContent = "Please enter a name with at least 2 characters.";
    message.style.color = "#b42318";
    result.hidden = true;
    nameInput.focus();
    return;
  }
  if (!emailInput.checkValidity()) {
    message.textContent = "Please enter a valid email address.";
    message.style.color = "#b42318";
    result.hidden = true;
    emailInput.focus();
    return;
  }
  document.querySelector("#resultName").textContent = name;
  document.querySelector("#resultEmail").textContent = email;
  message.textContent = "Registration completed successfully.";
  message.style.color = "#167647";
  result.hidden = false;
});
