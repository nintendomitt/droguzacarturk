/* Video kapak -> site icinde oynatici.
   YouTube (data-yt): youtube-nocookie iframe'i ayni kartin icinde acilir.
   Instagram reels (data-ig): sayfanin ustunde bir pencerede Instagram'in resmi
   gomme oynaticisi acilir; siteden cikilmaz. Tiklanana kadar ne YouTube'a ne
   Instagram'a istek gider (kapaklar i.ytimg.com / sitenin kendi /assets/reels).
   Kayan seritteyse (.vd-track) video oynarken serit durur. */
(function () {
  var css = ".vd-ig{position:absolute;top:8px;right:8px;width:22px;height:22px;border-radius:6px;" +
    "background:linear-gradient(45deg,#f9a825,#e1306c 55%,#833ab4);box-shadow:0 2px 6px rgba(0,0,0,.3)}" +
    ".vd-ig::after{content:'';position:absolute;inset:5px;border:2px solid #fff;border-radius:50%}" +
    ".ig-lb{position:fixed;inset:0;z-index:9999;background:rgba(6,15,34,.86);display:flex;align-items:center;" +
    "justify-content:center;padding:16px}.ig-lb .ig-box{position:relative;width:min(420px,94vw);height:min(760px,88vh);" +
    "background:#fff;border-radius:14px;box-shadow:0 20px 60px rgba(0,0,0,.45)}" +
    ".ig-lb iframe{width:100%;height:100%;border:0;display:block;border-radius:14px}.ig-lb .ig-x{position:absolute;top:-14px;right:-14px;" +
    "width:38px;height:38px;border-radius:50%;border:0;background:#fff;color:#0B1A38;font-size:24px;line-height:38px;" +
    "cursor:pointer;box-shadow:0 4px 14px rgba(0,0,0,.35)}@media(max-width:480px){.ig-lb .ig-x{top:6px;right:6px}}";
  var st = document.createElement("style"); st.textContent = css; document.head.appendChild(st);

  var lb = null, lastCard = null;
  function closeIg() {
    if (!lb) return;
    lb.remove(); lb = null;
    document.querySelectorAll(".vd-track.is-playing").forEach(function (t) { t.classList.remove("is-playing"); });
    if (lastCard) { lastCard.focus({ preventScroll: true }); lastCard = null; }
  }
  function openIg(c) {
    var id = c.getAttribute("data-ig");
    var title = (c.querySelector(".vd-t") || {}).textContent || "Video";
    closeIg(); lastCard = c;
    lb = document.createElement("div");
    lb.className = "ig-lb"; lb.setAttribute("role", "dialog"); lb.setAttribute("aria-modal", "true");
    lb.setAttribute("aria-label", title);
    lb.innerHTML = '<div class="ig-box"><iframe src="https://www.instagram.com/reel/' + id +
      '/embed/" title="' + title.replace(/"/g, "&quot;") +
      '" allow="autoplay; encrypted-media; picture-in-picture; fullscreen" allowfullscreen loading="eager"></iframe>' +
      '<button type="button" class="ig-x" aria-label="Kapat">&times;</button></div>';
    document.body.appendChild(lb);
    lb.querySelector(".ig-x").focus();
    var t = c.closest(".vd-track");
    if (t) t.classList.add("is-playing");
    if (window.gtag) gtag("event", "video_play", { video_id: id, video_provider: "instagram", page_location: location.pathname });
  }

  function stop(c) {
    if (!c || !c.classList.contains("on")) return;
    c.innerHTML = c.getAttribute("data-html") || "";
    c.classList.remove("on");
    var t = c.closest(".vd-track");
    if (t && !t.querySelector(".vd-card.on")) t.classList.remove("is-playing");
  }
  function play(c) {
    if (c.getAttribute("data-ig")) { document.querySelectorAll(".vd-card.on").forEach(stop); openIg(c); return; }
    document.querySelectorAll(".vd-card.on").forEach(stop);
    var id = c.getAttribute("data-yt");
    if (!id) return;
    var title = (c.querySelector(".vd-t") || {}).textContent || "Video";
    c.setAttribute("data-html", c.innerHTML);
    c.classList.add("on");
    c.innerHTML =
      '<iframe src="https://www.youtube-nocookie.com/embed/' + id +
      '?autoplay=1&rel=0&modestbranding=1&playsinline=1" title="' +
      title.replace(/"/g, "&quot;") +
      '" allow="autoplay; encrypted-media; picture-in-picture; fullscreen" allowfullscreen></iframe>' +
      '<button type="button" class="vd-x" aria-label="Kapat">&times;</button>';
    var t = c.closest(".vd-track");
    if (t) t.classList.add("is-playing");
    if (window.gtag) gtag("event", "video_play", { video_id: id, video_provider: "youtube", page_location: location.pathname });
  }
  document.addEventListener("click", function (e) {
    if (lb && (e.target === lb || (e.target.closest && e.target.closest(".ig-x")))) { e.preventDefault(); closeIg(); return; }
    var x = e.target.closest && e.target.closest(".vd-x");
    if (x) { e.preventDefault(); stop(x.closest(".vd-card")); return; }
    var c = e.target.closest && e.target.closest(".vd-card");
    if (c && !c.classList.contains("on")) { e.preventDefault(); play(c); }
  });
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && lb) { closeIg(); return; }
    if (e.key !== "Enter" && e.key !== " ") return;
    var c = e.target.closest && e.target.closest(".vd-card");
    if (c && !c.classList.contains("on") && e.target === c) { e.preventDefault(); play(c); }
  });
})();
