const items = [
  { id: 1, name: "Masala Chai",  cat: "tea",   price: 30, color: "#f2c48d", icon: "\u2615", note: "Ginger, cardamom" },
  { id: 2, name: "Green Tea",    cat: "tea",   price: 40, color: "#cfe3b0", icon: "\ud83c\udf43", note: "Light and fresh" },
  { id: 3, name: "Iced Lemon Tea", cat: "tea", price: 50, color: "#f7e6a0", icon: "\ud83c\udf4b", note: "Served cold" },
  { id: 4, name: "Samosa",       cat: "snack", price: 20, color: "#e8b98a", icon: "\ud83e\udd5f", note: "Potato and peas" },
  { id: 5, name: "Vada Pav",     cat: "snack", price: 25, color: "#f0c9a0", icon: "\ud83c\udf54", note: "Mumbai classic" },
  { id: 6, name: "Cheese Sandwich", cat: "snack", price: 60, color: "#f6dfa6", icon: "\ud83e\udd6a", note: "Grilled" },
  { id: 7, name: "Gulab Jamun",  cat: "sweet", price: 35, color: "#e0a07a", icon: "\ud83c\udf6e", note: "Warm, two pieces" },
  { id: 8, name: "Jalebi",       cat: "sweet", price: 40, color: "#f5b94f", icon: "\ud83c\udf6f", note: "Crisp and syrupy" }
];

let cat = "all", query = "", cart = {};
const cards = document.getElementById("cards");

function renderCards() {
  cards.innerHTML = "";
  const shown = items.filter(i =>
    (cat === "all" || i.cat === cat) && i.name.toLowerCase().includes(query));
  shown.forEach(i => {
    const d = document.createElement("article");
    d.className = "card";
    d.innerHTML =
      '<div class="swatch" style="background:' + i.color + '">' + i.icon + '</div>' +
      '<div class="info"><h3>' + i.name + '</h3><small>' + i.note + '</small>' +
      '<div class="row"><strong>\u20b9' + i.price + '</strong>' +
      '<button class="add" data-id="' + i.id + '">Add</button></div></div>';
    cards.appendChild(d);
  });
  document.getElementById("none").hidden = shown.length > 0;
}

function renderCart() {
  const list = document.getElementById("cartList");
  list.innerHTML = "";
  let total = 0, count = 0;
  Object.keys(cart).forEach(id => {
    const it = items.find(x => x.id == id), q = cart[id];
    total += it.price * q; count += q;
    const li = document.createElement("li");
    li.innerHTML = "<span>" + it.name + " x" + q + "</span><span>\u20b9" + it.price * q +
      ' <button class="rm" data-id="' + id + '" aria-label="Remove">\u00d7</button></span>';
    list.appendChild(li);
  });
  document.getElementById("total").textContent = "\u20b9" + total;
  document.getElementById("cartCount").textContent = count;
}

document.getElementById("tabs").addEventListener("click", e => {
  if (!e.target.classList.contains("tab")) return;
  document.querySelector(".tab.active").classList.remove("active");
  e.target.classList.add("active");
  cat = e.target.dataset.cat; renderCards();
});
document.getElementById("search").addEventListener("input", e => {
  query = e.target.value.toLowerCase().trim(); renderCards();
});
cards.addEventListener("click", e => {
  if (e.target.classList.contains("add")) {
    const id = e.target.dataset.id;
    cart[id] = (cart[id] || 0) + 1; renderCart();
  }
});
document.getElementById("cartList").addEventListener("click", e => {
  if (e.target.classList.contains("rm")) {
    const id = e.target.dataset.id;
    if (--cart[id] <= 0) delete cart[id];
    renderCart();
  }
});
document.getElementById("cartBtn").addEventListener("click", () => {
  document.getElementById("cart").hidden = false;
});
document.getElementById("close").addEventListener("click", () => {
  document.getElementById("cart").hidden = true;
});

renderCards(); renderCart();
