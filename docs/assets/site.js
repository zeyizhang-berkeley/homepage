"use strict";
const root = document.documentElement;
const isChinese = root.lang.toLowerCase().startsWith("zh");
const themeButton = document.querySelector(".theme-toggle");
function updateThemeButton() {
  const dark = root.dataset.theme === "dark";
  themeButton.setAttribute("aria-pressed", String(dark));
  themeButton.setAttribute("aria-label", isChinese ? (dark ? "切换为浅色模式" : "切换为深色模式") : `Switch to ${dark ? "light" : "dark"} theme`);
  themeButton.querySelector("span").textContent = isChinese ? (dark ? "浅色模式" : "深色模式") : (dark ? "Light theme" : "Dark theme");
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
const topbar = document.querySelector(".topbar");
const navList = document.querySelector(".toc__list");
const languageSwitch = document.querySelector(".language-switch");
const languageOptions = Array.from(document.querySelectorAll(".language-switch__option"));
const languageDestinations = languageOptions.map(option => new URL(option.dataset.languageTarget, location.href));
function updateLanguageLink(sectionId) {
  languageOptions.forEach((option, index) => {
    const destination = languageDestinations[index];
    destination.hash = sectionId || location.hash;
    option.href = destination.href;
  });
}
updateLanguageLink();
if (languageSwitch) {
  let languageNavigationTimer;
  const currentLanguage = isChinese ? "zh" : "en";
  window.addEventListener("pageshow", () => {
    clearTimeout(languageNavigationTimer);
    languageSwitch.dataset.language = currentLanguage;
  });
  languageOptions.forEach(option => option.addEventListener("click", event => {
    if (event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
    event.preventDefault();
    clearTimeout(languageNavigationTimer);
    languageSwitch.dataset.language = option.dataset.languageOption;
    if (option.dataset.languageOption === currentLanguage) return;
    const delay = matchMedia("(prefers-reduced-motion: reduce)").matches ? 0 : 160;
    languageNavigationTimer = setTimeout(() => location.assign(option.href), delay);
  }));
}
const navLinks = Array.from(document.querySelectorAll('.toc a[href^="#"]'));
const sections = navLinks.map(a => document.getElementById(a.hash.slice(1))).filter(Boolean);
let headerHeight = 0;
let scheduled = false;
let activeSectionId = null;
let navRevealTimer = null;
function revealActiveLink() {
  navRevealTimer = null;
  if (!navList || navList.scrollWidth <= navList.clientWidth + 1 ||
      document.querySelector(".figure-viewer[open]")) return;
  const activeLink = navLinks.find(a => a.hash === `#${activeSectionId}`);
  if (!activeLink) return;
  const viewport = navList.getBoundingClientRect();
  const item = activeLink.getBoundingClientRect();
  if (item.left < viewport.left + 4) {
    navList.scrollBy({ left: item.left - viewport.left - 4, behavior: "instant" });
  } else if (item.right > viewport.right - 4) {
    navList.scrollBy({ left: item.right - viewport.right + 4, behavior: "instant" });
  }
}
function updateHeaderHeight() {
  headerHeight = topbar ? Math.ceil(topbar.getBoundingClientRect().height) : 0;
  root.style.setProperty("--header-height", `${headerHeight}px`);
  activeSectionId = null;
  scheduleUpdate();
}
function updateActiveSection() {
  scheduled = false;
  if (!sections.length || document.querySelector(".figure-viewer[open]")) return;
  const offset = headerHeight + 32;
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
  activeSectionId = current.id;
  updateLanguageLink(current.id);
  // A second scroll container can interrupt Chromium's page smooth scroll.
  // Wait until page scrolling (or a resize) has settled before revealing the tab.
  clearTimeout(navRevealTimer);
  navRevealTimer = setTimeout(revealActiveLink, 150);
}
function scheduleUpdate() {
  if (!scheduled) { scheduled = true; requestAnimationFrame(updateActiveSection); }
}
if (sections.length) {
  window.addEventListener("scroll", scheduleUpdate, { passive: true });
  window.addEventListener("resize", updateHeaderHeight, { passive: true });
  window.addEventListener("hashchange", scheduleUpdate);
  window.addEventListener("load", updateHeaderHeight);
  if (topbar && typeof ResizeObserver !== "undefined") {
    new ResizeObserver(updateHeaderHeight).observe(topbar);
  }
  updateHeaderHeight();
  updateActiveSection();
}

const figureViewer = document.getElementById("figure-lightbox");
if (figureViewer) {
  const enlargedImage = figureViewer.querySelector(".figure-viewer__image");
  const closeButton = figureViewer.querySelector(".figure-viewer__close");
  let openedFrom = null;
  let scrollPosition = null;
  let savedStyles = null;
  let startedOnBackdrop = false;

  document.querySelectorAll(".pub__figure-link").forEach(button => {
    button.addEventListener("click", () => {
      if (figureViewer.open) return;
      const thumbnail = button.querySelector("img");
      openedFrom = button;
      enlargedImage.src = button.dataset.figureSrc || thumbnail.currentSrc || thumbnail.src;
      enlargedImage.alt = thumbnail.alt;
      scrollPosition = { left: window.scrollX, top: window.scrollY };
      const body = document.body;
      const scrollbarWidth = window.innerWidth - root.clientWidth;
      const paddingRight = parseFloat(getComputedStyle(body).paddingRight) || 0;
      savedStyles = {
        position: body.style.position, top: body.style.top,
        left: body.style.left, width: body.style.width,
        paddingRight: body.style.paddingRight,
        overflow: root.style.overflow, scrollBehavior: root.style.scrollBehavior
      };
      root.style.scrollBehavior = "auto";
      root.style.overflow = "hidden";
      body.style.position = "fixed";
      body.style.top = `${-scrollPosition.top}px`;
      body.style.left = `${-scrollPosition.left}px`;
      body.style.width = "100%";
      body.style.paddingRight = `${paddingRight + scrollbarWidth}px`;
      startedOnBackdrop = false;
      figureViewer.showModal();
      closeButton.focus({ preventScroll: true });
    });
  });

  closeButton.addEventListener("click", () => figureViewer.close());
  function isBackdrop(event) {
    const box = figureViewer.getBoundingClientRect();
    return event.target === figureViewer &&
      (event.clientX < box.left || event.clientX > box.right ||
       event.clientY < box.top || event.clientY > box.bottom);
  }
  figureViewer.addEventListener("pointerdown", event => {
    startedOnBackdrop = isBackdrop(event);
  });
  figureViewer.addEventListener("click", event => {
    if (startedOnBackdrop && isBackdrop(event)) figureViewer.close();
    startedOnBackdrop = false;
  });
  // Native dialog handles Escape and keeps keyboard focus inside the viewer.
  figureViewer.addEventListener("close", () => {
    if (!savedStyles) return;
    for (const property of ["position", "top", "left", "width", "paddingRight"]) {
      document.body.style[property] = savedStyles[property];
    }
    root.style.overflow = savedStyles.overflow;
    window.scrollTo({ ...scrollPosition, behavior: "instant" });
    openedFrom.focus({ preventScroll: true });
    root.style.scrollBehavior = savedStyles.scrollBehavior;
    enlargedImage.removeAttribute("src");
    enlargedImage.alt = "";
    savedStyles = null;
    openedFrom = null;
  });
}
