const stateEl = document.querySelector("#state");
const listEl = document.querySelector("#list");
const detailEl = document.querySelector("#detail");
const qEl = document.querySelector("#q");

let status = "loading";
let tracks = [];

function setStatus(value) {
  status = value;
  stateEl.textContent = value;
}

async function load() {
  setStatus("loading");
  try {
    const res = await fetch("tracks.json");
    if (!res.ok) throw new Error("network");
    tracks = await res.json();
    setStatus(tracks.length ? "ready" : "empty");
    renderList();
  } catch {
    setStatus("error");
    listEl.textContent = "Сеть молчит. Retry: обнови страницу через Live Server.";
  }
}

function renderList() {
  if (status !== "ready") return;
  const q = qEl.value.trim().toLowerCase();
  const shown = tracks.filter((t) => t.title.toLowerCase().includes(q) || t.artist.toLowerCase().includes(q));
  listEl.replaceChildren();
  if (shown.length === 0) {
    listEl.textContent = "Пусто";
    return;
  }
  shown.forEach((t) => {
    const btn = document.createElement("button");
    btn.type = "button";
    btn.textContent = `${t.title} — ${t.artist}`;
    btn.addEventListener("click", () => showDetail(t.id));
    listEl.append(btn, document.createElement("br"));
  });
}

function showDetail(id) {
  const t = tracks.find((x) => x.id === id);
  if (!t) {
    detailEl.hidden = false;
    detailEl.textContent = "404: трека нет";
    return;
  }
  detailEl.hidden = false;
  detailEl.replaceChildren();
  const h = document.createElement("h2");
  h.textContent = t.title;
  const p = document.createElement("p");
  p.textContent = `${t.artist} · ${t.genre}`;
  const back = document.createElement("button");
  back.type = "button";
  back.textContent = "Назад к списку";
  back.addEventListener("click", () => {
    detailEl.hidden = true;
  });
  detailEl.append(h, p, back);
}

qEl.addEventListener("input", renderList);
load();
