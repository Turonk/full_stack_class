async function loadHits() {
  const box = document.querySelector("#api-hits");
  if (!box) return;
  try {
    const res = await fetch("/api/hits");
    if (!res.ok) throw new Error("bad status");
    const hits = await res.json();
    box.replaceChildren();
    hits.forEach((hit) => {
      const card = document.createElement("article");
      card.className = "card";
      const h = document.createElement("h3");
      h.textContent = hit.title;
      const p = document.createElement("p");
      p.className = "muted";
      p.textContent = `${hit.artist} · ${hit.length}`;
      card.append(h, p);
      box.append(card);
    });
  } catch {
    box.textContent = "API молчит. Сервер запущен?";
  }
}

loadHits();
