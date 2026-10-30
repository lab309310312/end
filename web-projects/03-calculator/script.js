let current = "0", previous = null, operator = null, justEvaluated = false;
const display = document.getElementById("display");
const history = document.getElementById("history");

function show() { display.textContent = current; }

function compute(a, b, op) {
  a = parseFloat(a); b = parseFloat(b);
  let r;
  if (op === "+") r = a + b;
  else if (op === "-") r = a - b;
  else if (op === "*") r = a * b;
  else if (op === "/") { if (b === 0) return "Error"; r = a / b; }
  return String(parseFloat(r.toPrecision(12)));
}

function inputNum(n) {
  if (justEvaluated) { current = "0"; justEvaluated = false; }
  current = current === "0" ? n : current + n;
  show();
}

function chooseOp(op) {
  if (operator && !justEvaluated) { current = compute(previous, current, operator); }
  previous = current; operator = op; justEvaluated = false;
  history.textContent = previous + " " + symbol(op);
  current = "0"; show();
}

function symbol(op) { return { "+": "+", "-": "\u2212", "*": "\u00d7", "/": "\u00f7" }[op]; }

function equals() {
  if (!operator) return;
  const expr = previous + " " + symbol(operator) + " " + current;
  current = compute(previous, current, operator);
  history.textContent = expr + " =";
  operator = null; previous = null; justEvaluated = true; show();
}

document.querySelector(".keys").addEventListener("click", e => {
  const b = e.target.closest("button");
  if (!b) return;
  if (b.dataset.num) inputNum(b.dataset.num);
  else if (b.dataset.op) chooseOp(b.dataset.op);
  else {
    const a = b.dataset.act;
    if (a === "clear") { current = "0"; previous = operator = null; history.textContent = ""; }
    if (a === "back") current = current.length > 1 ? current.slice(0, -1) : "0";
    if (a === "dot" && !current.includes(".")) current += ".";
    if (a === "percent") current = String(parseFloat(current) / 100);
    if (a === "equals") return equals();
    show();
  }
});

// Keyboard support
document.addEventListener("keydown", e => {
  if (/^[0-9]$/.test(e.key)) inputNum(e.key);
  else if ("+-*/".includes(e.key)) chooseOp(e.key);
  else if (e.key === "Enter" || e.key === "=") equals();
  else if (e.key === "Backspace") { current = current.length > 1 ? current.slice(0, -1) : "0"; show(); }
  else if (e.key === "Escape") { current = "0"; previous = operator = null; history.textContent = ""; show(); }
  else if (e.key === "." && !current.includes(".")) { current += "."; show(); }
});
