let tasks = [];       // {id, text, prio, done}
let filter = "all";
const list = document.getElementById("list");
const stats = document.getElementById("stats");
const empty = document.getElementById("empty");

function save() { try { localStorage.setItem("tasks", JSON.stringify(tasks)); } catch (e) {} }
function load() { try { tasks = JSON.parse(localStorage.getItem("tasks")) || []; } catch (e) { tasks = []; } }

function render() {
  list.innerHTML = "";
  const shown = tasks.filter(t => filter === "all" || (filter === "done" ? t.done : !t.done));
  shown.forEach(t => {
    const li = document.createElement("li");
    li.className = t.prio + (t.done ? " done" : "");
    const cb = document.createElement("input");
    cb.type = "checkbox"; cb.checked = t.done;
    cb.addEventListener("change", () => { t.done = cb.checked; save(); render(); });
    const sp = document.createElement("span");
    sp.textContent = t.text;
    const del = document.createElement("button");
    del.className = "del"; del.textContent = "\u00d7"; del.setAttribute("aria-label", "Delete task");
    del.addEventListener("click", () => { tasks = tasks.filter(x => x.id !== t.id); save(); render(); });
    li.append(cb, sp, del);
    list.appendChild(li);
  });
  const left = tasks.filter(t => !t.done).length;
  stats.textContent = left + " of " + tasks.length + " left";
  empty.hidden = shown.length > 0;
}

document.getElementById("addForm").addEventListener("submit", e => {
  e.preventDefault();
  const input = document.getElementById("taskInput");
  const text = input.value.trim();
  if (!text) return;
  tasks.unshift({ id: Date.now(), text, prio: document.getElementById("prio").value, done: false });
  input.value = "";
  save(); render();
});

document.querySelectorAll(".f").forEach(b => b.addEventListener("click", () => {
  document.querySelector(".f.active").classList.remove("active");
  b.classList.add("active");
  filter = b.dataset.f;
  render();
}));

document.getElementById("clearDone").addEventListener("click", () => {
  tasks = tasks.filter(t => !t.done); save(); render();
});

load(); render();
