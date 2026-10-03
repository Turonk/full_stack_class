export function button({ label, onClick }) {
  const el = document.createElement("button");
  el.className = "kit-btn";
  el.type = "button";
  el.textContent = label;
  if (onClick) el.addEventListener("click", onClick);
  return el;
}

export function badge(text) {
  const el = document.createElement("span");
  el.className = "kit-badge";
  el.textContent = text;
  return el;
}

export function card({ title, body }) {
  const el = document.createElement("article");
  el.className = "kit-card";
  const h = document.createElement("h2");
  h.textContent = title;
  const p = document.createElement("p");
  p.textContent = body;
  el.append(h, p);
  return el;
}

export function nav(links) {
  const el = document.createElement("nav");
  links.forEach((link) => {
    const a = document.createElement("a");
    a.href = link.href;
    a.textContent = link.label;
    el.append(a);
  });
  return el;
}

export function playerBar(title) {
  const el = document.createElement("div");
  el.className = "kit-player";
  el.setAttribute("role", "region");
  el.setAttribute("aria-label", "Плеер");
  const play = button({ label: "Play" });
  play.setAttribute("aria-label", "Играть");
  const name = document.createElement("p");
  name.textContent = title;
  el.append(play, name);
  return el;
}
