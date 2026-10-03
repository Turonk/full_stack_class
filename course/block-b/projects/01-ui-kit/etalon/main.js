import { badge, button, card, nav, playerBar } from "./ui.js";

const navHost = document.querySelector("#nav");
navHost.replaceWith(
  nav([
    { href: "#gallery", label: "Галерея" },
    { href: "../03-pulse-api/etalon/README.md", label: "API" },
  ]),
);

const gallery = document.querySelector("#gallery");
gallery.append(
  badge("v2"),
  button({
    label: "Ripple",
    onClick: (event) => {
      event.currentTarget.animate(
        [{ transform: "scale(1)" }, { transform: "scale(1.06)" }, { transform: "scale(1)" }],
        { duration: 280 },
      );
    },
  }),
  card({ title: "Карточка", body: "Компонент без фреймворка: функция вернула DOM." }),
  playerBar("Night Circuit"),
);
