/* Au Pain Doré : ouvert maintenant, entrée de l'affiche, apparitions, demande de gâteau.
   HORAIRES : modifier ici. Jours : 0 = dimanche … 6 = samedi. Heures en minutes depuis minuit. */
(function () {
  "use strict";
  document.documentElement.classList.add("js");
  var calme = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var NBSP = " ";
  var HORAIRES = {
    0: [[420, 780]], 1: [],
    2: [[420, 1170]], 3: [[420, 1170]], 4: [[420, 1170]], 5: [[420, 1170]],
    6: [[420, 780], [900, 1140]]
  };
  var JOURS = ["dimanche", "lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi"];
  function heure(m) { var h = Math.floor(m / 60), mn = m % 60; return h + NBSP + "h" + (mn ? NBSP + (mn < 10 ? "0" : "") + mn : ""); }
  function maintenant() {
    try {
      var o = {};
      new Intl.DateTimeFormat("en-GB", { timeZone: "Europe/Paris", weekday: "short", hour: "2-digit", minute: "2-digit", hourCycle: "h23" })
        .formatToParts(new Date()).forEach(function (x) { o[x.type] = x.value; });
      return { jour: { Sun: 0, Mon: 1, Tue: 2, Wed: 3, Thu: 4, Fri: 5, Sat: 6 }[o.weekday], min: +o.hour * 60 + +o.minute };
    } catch (e) { var d = new Date(); return { jour: d.getDay(), min: d.getHours() * 60 + d.getMinutes() }; }
  }

  /* ---------- Ouvert maintenant ---------- */
  var t = maintenant(), ouvert = null, prochaine = null;
  HORAIRES[t.jour].forEach(function (p) { if (t.min >= p[0] && t.min < p[1]) ouvert = p; });
  if (!ouvert) {
    for (var i = 0; i < 8 && !prochaine; i++) {
      var j = (t.jour + i) % 7;
      HORAIRES[j].some(function (p) {
        if (i > 0 || p[0] > t.min) { prochaine = { quand: i === 0 ? "aujourd'hui" : i === 1 ? "demain" : JOURS[j], h: p[0] }; return true; }
        return false;
      });
    }
  }
  var courts = Array.prototype.slice.call(document.querySelectorAll("[data-etat-court]"));
  var geant = document.querySelector("[data-etat-geant]");
  var phrase = document.querySelector("[data-etat]");
  if (ouvert) {
    courts.forEach(function (c) { c.textContent = "Ouvert jusqu'à " + heure(ouvert[1]); c.hidden = false; });
    if (geant) geant.textContent = "Ouvert";
    if (phrase) phrase.innerHTML = "C'est <strong>ouvert</strong> jusqu'à" + NBSP + heure(ouvert[1]) + ".";
  } else if (prochaine) {
    courts.forEach(function (c) { c.textContent = "Fermé · " + prochaine.quand + " " + heure(prochaine.h); c.classList.add("ferme"); c.hidden = false; });
    if (geant) geant.textContent = "Fermé";
    if (phrase) phrase.innerHTML = "C'est <strong>fermé</strong> pour l'instant. On rouvre " + prochaine.quand + " à" + NBSP + heure(prochaine.h) + ".";
  }
  var ligne = document.querySelector('.table-horaires tr[data-jour="' + t.jour + '"]');
  if (ligne) ligne.classList.add("aujourdhui");

  /* ---------- La boule de pain bouge légèrement au défilement ---------- */
  var pain = document.querySelector(".affiche-pain");
  if (pain && !calme) {
    var prevu = false;
    var bouger = function () {
      prevu = false;
      var p = Math.max(0, Math.min(1, window.scrollY / (window.innerHeight || 1)));
      pain.style.setProperty("--defile", p.toFixed(3));
    };
    window.addEventListener("scroll", function () { if (!prevu) { prevu = true; requestAnimationFrame(bouger); } }, { passive: true });
  }

  /* ---------- Apparitions ---------- */
  var aVoir = document.querySelectorAll("[data-apparait]");
  if ("IntersectionObserver" in window && !calme) {
    var obs = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("vu"); obs.unobserve(e.target); } }); }, { rootMargin: "0px 0px -8% 0px" });
    aVoir.forEach(function (el) { obs.observe(el); });
  } else aVoir.forEach(function (el) { el.classList.add("vu"); });

  /* ---------- Demande de gâteau ---------- */
  var form = document.querySelector("[data-commande]");
  if (!form) return;
  var recu = document.querySelector("[data-recu]");
  var recuTexte = document.querySelector("[data-recu-texte]");
  var erreur = form.querySelector("[data-erreur]");
  var champJour = form.elements.jour;
  function iso(d) { return d.getFullYear() + "-" + String(d.getMonth() + 1).padStart(2, "0") + "-" + String(d.getDate()).padStart(2, "0"); }
  var auPlusTot = new Date(); auPlusTot.setHours(0, 0, 0, 0); auPlusTot.setDate(auPlusTot.getDate() + 2);
  champJour.min = iso(auPlusTot);
  function signaler(champ, message) { erreur.textContent = message; erreur.hidden = false; champ.setAttribute("aria-invalid", "true"); champ.focus(); }
  form.addEventListener("input", function (e) { e.target.removeAttribute("aria-invalid"); erreur.hidden = true; });
  form.addEventListener("submit", function (e) {
    e.preventDefault();
    if (!champJour.value) return signaler(champJour, "Indiquez le jour où vous voulez le gâteau.");
    var d = new Date(champJour.value + "T12:00:00");
    if (d < auPlusTot) return signaler(champJour, "Il faut 48 h au fournil : à partir du " + auPlusTot.toLocaleDateString("fr-FR", { day: "numeric", month: "long" }) + ".");
    if (d.getDay() === 1) return signaler(champJour, "La boutique est fermée le lundi : choisissez un autre jour.");
    if (!form.elements.parts.value) return signaler(form.elements.parts, "Choisissez le nombre de parts.");
    var envie = form.elements.envie.value.trim(), nom = form.elements.nom.value.trim();
    recuTexte.textContent = "Un gâteau de " + form.elements.parts.value + (envie ? ", " + envie : "") +
      ", pour le " + d.toLocaleDateString("fr-FR", { weekday: "long", day: "numeric", month: "long" }) + (nom ? ", au nom de " + nom : "") + ".";
    form.hidden = true; recu.hidden = false; recu.focus();
  });
  document.querySelector("[data-recommencer]").addEventListener("click", function () { recu.hidden = true; form.hidden = false; champJour.focus(); });
})();
