/* Maison Vauclair : « ouvert maintenant ? », la lampe qui s'allume, le film.
   HORAIRES : modifier ici. Jours : 0 = dimanche … 6 = samedi. Heures en minutes depuis minuit. */
(function () {
  "use strict";

  /* ?capture : état final statique, pour les captures d'écran */
  var capture = /[?&]capture\b/.test(location.search);
  var calme = capture || (window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches);
  if (capture) document.documentElement.classList.add("capture");
  else document.documentElement.classList.add("js");

  var HORAIRES = {
    0: [], 1: [],
    2: [[600, 1140]], 3: [[600, 1140]], 4: [[600, 1140]], 5: [[600, 1140]], 6: [[600, 1140]]
  };
  var JOURS = ["dimanche", "lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi"];
  var NBSP = " ";

  function heure(m) {
    var h = Math.floor(m / 60), min = m % 60;
    return h + NBSP + "h" + (min ? NBSP + (min < 10 ? "0" : "") + min : "");
  }

  function maintenant() {
    try {
      var o = {};
      new Intl.DateTimeFormat("en-GB", {
        timeZone: "Europe/Paris", weekday: "short", hour: "2-digit", minute: "2-digit", hourCycle: "h23"
      }).formatToParts(new Date()).forEach(function (x) { o[x.type] = x.value; });
      return {
        jour: { Sun: 0, Mon: 1, Tue: 2, Wed: 3, Thu: 4, Fri: 5, Sat: 6 }[o.weekday],
        minutes: parseInt(o.hour, 10) * 60 + parseInt(o.minute, 10)
      };
    } catch (e) {
      var d = new Date();
      return { jour: d.getDay(), minutes: d.getHours() * 60 + d.getMinutes() };
    }
  }

  function prochaineOuverture(jour, minutes) {
    for (var i = 0; i < 8; i++) {
      var j = (jour + i) % 7, p = HORAIRES[j];
      for (var k = 0; k < p.length; k++) {
        if (i > 0 || p[k][0] > minutes) {
          return (i === 0 ? "aujourd'hui à" : i === 1 ? "demain à" : JOURS[j] + " à") + NBSP + heure(p[k][0]);
        }
      }
    }
    return "";
  }

  var t = maintenant(), ouvert = null;
  HORAIRES[t.jour].forEach(function (p) { if (t.minutes >= p[0] && t.minutes < p[1]) ouvert = p; });

  var etat = document.querySelector("[data-etat]");
  if (etat) {
    etat.innerHTML = ouvert
      ? "<strong>Ouvert</strong> aujourd'hui jusqu'à" + NBSP + heure(ouvert[1]) + "."
      : "<strong>Fermé</strong> pour le moment. Réouverture " + prochaineOuverture(t.jour, t.minutes) + ".";
  }
  var court = document.querySelector("[data-etat-court]");
  if (court) {
    court.textContent = ouvert
      ? "Ouvert jusqu'à" + NBSP + heure(ouvert[1])
      : "Fermé · réouverture " + prochaineOuverture(t.jour, t.minutes);
  }
  var ligne = document.querySelector('.horaires tr[data-jour="' + t.jour + '"]');
  if (ligne) ligne.classList.add("aujourdhui");

  /* La lampe s'allume : chaque photo sort de l'ombre quand elle arrive à l'écran */
  var photos = document.querySelectorAll("[data-lampe]");
  if (!calme && "IntersectionObserver" in window) {
    var obs = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("allume"); obs.unobserve(e.target); } });
    }, { rootMargin: "0px 0px -18% 0px", threshold: 0.15 });
    photos.forEach(function (p) { obs.observe(p); });
  } else photos.forEach(function (p) { p.classList.add("allume"); });

  /* Le film : s'ouvre dans une fenêtre, se lit sans son, s'arrête à la fermeture */
  var film = document.querySelector("dialog.film");
  var ouvrir = document.querySelector("[data-film]");
  if (film && ouvrir) {
    var video = film.querySelector("video");
    if (typeof film.showModal !== "function") { ouvrir.hidden = true; }
    else {
      ouvrir.addEventListener("click", function () {
        film.showModal();
        video.preload = "auto";
        if (!calme) { var lecture = video.play(); if (lecture && lecture.catch) lecture.catch(function () {}); }
        video.controls = calme;
      });
      film.querySelector("[data-film-fermer]").addEventListener("click", function () { film.close(); });
      film.addEventListener("click", function (e) { if (e.target === film) film.close(); });
      film.addEventListener("close", function () { video.pause(); ouvrir.focus(); });
    }
  }
})();
