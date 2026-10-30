// Typing effect
const words = ["HTML5", "CSS3", "JavaScript", "Java Servlets"];
let w = 0, c = 0, del = false;
const typed = document.getElementById("typed");
function type() {
  const word = words[w];
  typed.textContent = word.slice(0, c);
  if (!del && c < word.length) c++;
  else if (!del) { del = true; return setTimeout(type, 1200); }
  else if (c > 0) c--;
  else { del = false; w = (w + 1) % words.length; }
  setTimeout(type, del ? 60 : 110);
}
type();

// Mobile menu
const nav = document.getElementById("nav");
document.getElementById("menuBtn").addEventListener("click", () => nav.classList.toggle("open"));
nav.addEventListener("click", () => nav.classList.remove("open"));

// Skill bars animate when scrolled into view
const obs = new IntersectionObserver(entries => {
  entries.forEach(en => {
    if (en.isIntersecting) {
      en.target.style.width = en.target.dataset.w + "%";
      obs.unobserve(en.target);
    }
  });
}, { threshold: 0.4 });
document.querySelectorAll(".fill").forEach(f => obs.observe(f));

// Form validation
document.getElementById("contactForm").addEventListener("submit", e => {
  e.preventDefault();
  let ok = true;
  e.target.querySelectorAll("[required]").forEach(f => {
    const bad = !f.value.trim() || (f.type === "email" && !/^\S+@\S+\.\S+$/.test(f.value));
    f.classList.toggle("bad", bad);
    if (bad) ok = false;
  });
  const msg = document.getElementById("msg");
  msg.textContent = ok ? "Message sent. I will reply soon." : "Please fill all fields correctly.";
  if (ok) e.target.reset();
});
