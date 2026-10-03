const KEY = "pulse.cart";
const catalogEl = document.querySelector("#catalog");
const cartEl = document.querySelector("#cart");
const sumEl = document.querySelector("#sum");
const statusEl = document.querySelector("#catalog-status");
const filterEl = document.querySelector("#filter");

let products = [];
let cart = loadCart();

function loadCart() {
  try {
    return JSON.parse(localStorage.getItem(KEY)) ?? [];
  } catch {
    return [];
  }
}

function saveCart() {
  localStorage.setItem(KEY, JSON.stringify(cart));
}

async function loadProducts() {
  try {
    const response = await fetch("products.json");
    if (!response.ok) throw new Error("Сеть");
    products = await response.json();
    statusEl.textContent = "";
    renderCatalog();
  } catch {
    statusEl.textContent = "Не удалось загрузить каталог. Открой магазин через Live Server, не как file://";
  }
}

function renderCatalog() {
  const q = filterEl.value.trim().toLowerCase();
  const list = products.filter((p) => p.title.toLowerCase().includes(q));
  catalogEl.replaceChildren();
  if (list.length === 0) {
    catalogEl.textContent = "Ничего не нашли";
    return;
  }
  list.forEach((p) => {
    const article = document.createElement("article");
    article.className = "card";
    article.innerHTML = "";
    const h = document.createElement("h3");
    h.textContent = p.title;
    const price = document.createElement("p");
    price.textContent = `${p.price} ₽`;
    const btn = document.createElement("button");
    btn.className = "btn";
    btn.type = "button";
    btn.textContent = "В корзину";
    btn.addEventListener("click", () => addToCart(p.id));
    article.append(h, price, btn);
    catalogEl.append(article);
  });
}

function addToCart(id) {
  const product = products.find((p) => p.id === id);
  if (!product) return;
  const line = cart.find((l) => l.id === id);
  if (line) line.qty += 1;
  else cart.push({ id, title: product.title, price: product.price, qty: 1 });
  saveCart();
  renderCart();
}

function removeLine(id) {
  cart = cart.filter((l) => l.id !== id);
  saveCart();
  renderCart();
}

function renderCart() {
  cartEl.replaceChildren();
  if (cart.length === 0) {
    cartEl.textContent = "Корзина пуста";
    sumEl.textContent = "0";
    return;
  }
  cart.forEach((line) => {
    const row = document.createElement("p");
    row.textContent = `${line.title} × ${line.qty}`;
    const del = document.createElement("button");
    del.type = "button";
    del.textContent = "Удалить";
    del.addEventListener("click", () => removeLine(line.id));
    row.append(" ", del);
    cartEl.append(row);
  });
  const sum = cart.reduce((acc, line) => acc + line.price * line.qty, 0);
  sumEl.textContent = String(sum);
}

document.querySelector("#clear").addEventListener("click", () => {
  cart = [];
  saveCart();
  renderCart();
});

filterEl.addEventListener("input", renderCatalog);

document.querySelector("#order").addEventListener("submit", (event) => {
  event.preventDefault();
  const name = document.querySelector("#name").value.trim();
  const email = document.querySelector("#email").value.trim();
  document.querySelector("#name-error").textContent = name ? "" : "Как тебя зовут?";
  document.querySelector("#email-error").textContent = email.includes("@") ? "" : "Нужна почта с @";
  if (!name || !email.includes("@")) return;
  document.querySelector("#order-status").textContent = "Заказ принят (учебный, без оплаты)";
});

loadProducts();
renderCart();
