const questions = [
  { q: "Which cable is used to connect a PC to a switch?", o: ["Crossover", "Straight-through", "Rollover", "Coaxial"], a: 1 },
  { q: "Which layer of the OSI model does a router work at?", o: ["Layer 1", "Layer 2", "Layer 3", "Layer 4"], a: 2 },
  { q: "Which command shows the path packets take to a host?", o: ["ping", "tracert", "arp -a", "hostname"], a: 1 },
  { q: "What does a VLAN do?", o: ["Increases cable length", "Splits a switch into separate broadcast domains", "Encrypts traffic", "Assigns DNS names"], a: 1 },
  { q: "Which routing protocol is a link-state protocol?", o: ["RIP", "OSPF", "Static", "ARP"], a: 1 }
];
const TIME = 15;
let idx = 0, score = 0, left = TIME, timer = null, locked = false;

const $ = id => document.getElementById(id);
function show(id) { ["start", "game", "result"].forEach(s => $(s).hidden = s !== id); }

function load() {
  locked = false;
  const q = questions[idx];
  $("progress").textContent = "Question " + (idx + 1) + " of " + questions.length;
  $("bar").style.width = (idx / questions.length * 100) + "%";
  $("question").textContent = q.q;
  $("feedback").textContent = "";
  $("next").hidden = true;
  $("options").innerHTML = "";
  q.o.forEach((text, i) => {
    const b = document.createElement("button");
    b.className = "opt"; b.textContent = text;
    b.addEventListener("click", () => answer(i));
    $("options").appendChild(b);
  });
  startTimer();
}

function startTimer() {
  clearInterval(timer);
  left = TIME; updateTimer();
  timer = setInterval(() => {
    left--; updateTimer();
    if (left <= 0) { clearInterval(timer); answer(-1); }
  }, 1000);
}
function updateTimer() {
  $("timer").textContent = left;
  $("timer").classList.toggle("low", left <= 5);
}

function answer(choice) {
  if (locked) return;
  locked = true; clearInterval(timer);
  const correct = questions[idx].a;
  const btns = document.querySelectorAll(".opt");
  btns.forEach((b, i) => {
    b.disabled = true;
    if (i === correct) b.classList.add("correct");
    else if (i === choice) b.classList.add("wrong");
  });
  if (choice === correct) { score++; $("feedback").textContent = "Correct."; }
  else $("feedback").textContent = choice === -1 ? "Time is up." : "Not quite. The right answer is highlighted.";
  $("next").textContent = idx === questions.length - 1 ? "See score" : "Next question";
  $("next").hidden = false;
}

$("next").addEventListener("click", () => {
  idx++;
  if (idx < questions.length) load(); else finish();
});

function finish() {
  show("result");
  $("score").textContent = score + " / " + questions.length;
  const pct = score / questions.length;
  $("grade").textContent = pct === 1 ? "Perfect score." : pct >= 0.6 ? "Good work." : "Review the labs and try again.";
}

$("startBtn").addEventListener("click", () => { idx = 0; score = 0; show("game"); load(); });
$("again").addEventListener("click", () => { idx = 0; score = 0; show("game"); load(); });
