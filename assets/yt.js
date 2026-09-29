/* YouTube kapak -> yerinde oynatici.
   Tiklanana kadar YouTube'a istek gitmez (yalnizca i.ytimg.com kapak gorseli).
   Tiklaninca youtube-nocookie iframe'i ayni kartin icinde acilir; siteden cikilmaz.
   Kayan seritteyse (.vd-track) video oynarken serit durur. */
(function () {
  function stop(c) {
    if (!c || !c.classList.contains("on")) return;
    c.innerHTML = c.getAttribute("data-html") || "";
    c.classList.remove("on");
    var t = c.closest(".vd-track");
    if (t && !t.querySelector(".vd-card.on")) t.classList.remove("is-playing");
  }
  function play(c) {
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
    if (window.gtag) gtag("event", "video_play", { video_id: id, page_location: location.pathname });
  }
  document.addEventListener("click", function (e) {
    var x = e.target.closest && e.target.closest(".vd-x");
    if (x) { e.preventDefault(); stop(x.closest(".vd-card")); return; }
    var c = e.target.closest && e.target.closest(".vd-card");
    if (c && !c.classList.contains("on")) { e.preventDefault(); play(c); }
  });
  document.addEventListener("keydown", function (e) {
    if (e.key !== "Enter" && e.key !== " ") return;
    var c = e.target.closest && e.target.closest(".vd-card");
    if (c && !c.classList.contains("on") && e.target === c) { e.preventDefault(); play(c); }
  });
})();
