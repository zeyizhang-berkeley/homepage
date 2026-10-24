"use strict";
const root = document.documentElement;
const themeButton = document.querySelector(".theme-toggle");
function updateThemeButton() {
  const dark = root.dataset.theme === "dark";
  themeButton.setAttribute("aria-pressed", String(dark));
  themeButton.setAttribute("aria-label", `Switch to ${dark ? "light" : "dark"} theme`);
  themeButton.querySelector("span").textContent = dark ? "Light theme" : "Dark theme";
  document.querySelector('meta[name="theme-color"]').content = dark ? "#0f1114" : "#fafaf8";
}
if (themeButton) {
  themeButton.hidden = false;
  updateThemeButton();
  themeButton.addEventListener("click", () => {
    root.dataset.theme = root.dataset.theme === "dark" ? "light" : "dark";
    try { localStorage.setItem("zeyi-theme", root.dataset.theme); } catch (_) {}
    updateThemeButton();
  });
}
const navLinks = Array.from(document.querySelectorAll('.toc a[href^="#"]'));
const sections = navLinks.map(a => document.getElementById(a.hash.slice(1))).filter(Boolean);
let scheduled = false;
function updateActiveSection() {
  scheduled = false;
  const offset = Math.min(window.innerHeight * 0.28, 220);
  let current = sections[0];
  for (const section of sections) {
    if (section.getBoundingClientRect().top <= offset) current = section;
  }
  if (window.innerHeight + window.scrollY >= document.documentElement.scrollHeight - 4) current = sections[sections.length - 1];
  navLinks.forEach(a => {
    const active = a.hash === `#${current.id}`;
    a.classList.toggle("is-active", active);
    if (active) a.setAttribute("aria-current", "location");
    else a.removeAttribute("aria-current");
  });
}
function scheduleUpdate() {
  if (!scheduled) { scheduled = true; requestAnimationFrame(updateActiveSection); }
}
if (sections.length) {
  window.addEventListener("scroll", scheduleUpdate, { passive: true });
  window.addEventListener("resize", scheduleUpdate, { passive: true });
  window.addEventListener("hashchange", scheduleUpdate);
  window.addEventListener("load", updateActiveSection);
  updateActiveSection();
}
