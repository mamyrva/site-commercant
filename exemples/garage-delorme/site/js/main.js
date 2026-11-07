/* Garage Delorme : pont élévateur au défilement, apparitions, formulaire, horaires, suivi.
   HORAIRES : modifier ici (jours 0 = dimanche … 6 = samedi, minutes depuis minuit),
   et aussi dans contenu/infos.json, le JSON-LD et le tableau des pages. */
(function () {
  "use strict";
  document.documentElement.classList.add("js");

  var EN = document.documentElement.lang === "en";
  var BASE = EN ? "../" : "";
  var NBSP = " ";
  /* ?capture : mise en page statique pour les captures d'écran pleine page (comme le mouvement réduit) */
  var capture = /[?&]capture\b/.test(location.search);
  if (capture) document.documentElement.classList.add("capture");
  var calme = capture || (window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches);
  var TXT = EN ? {
    ouvert: "<strong>Open</strong> until ", ferme: "<strong>Closed</strong> now. Opens again ",
    demain: "tomorrow at ", a: "at ", jours: ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
    requis: "Please fill in: ", envoi: "Sending…", echec: "The request could not be sent. Please call us on +33 4 92 00 00 00.",
    code: "Please enter your tracking code.", inconnu: "We can't find this code. Check it, or call the garage.",
    hs: "Tracking is not available right now. Please call the garage.", maj: "Last updated: "
  } : {
    ouvert: "<strong>Ouvert</strong> jusqu'à ", ferme: "<strong>Fermé</strong> pour le moment. Réouverture ",
    demain: "demain à ", a: "à ", jours: ["dimanche", "lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi"],
    requis: "Merci de remplir : ", envoi: "Envoi…", echec: "La demande n'a pas pu partir. Appelez-nous au 04 92 00 00 00.",
    code: "Entrez votre code de suivi.", inconnu: "Ce code est introuvable. Vérifiez-le, ou appelez le garage.",
    hs: "Le suivi est indisponible pour le moment. Appelez le garage.", maj: "Dernière mise à jour : "
  };

  /* Hauteur réelle de l'en-tête : la scène collante se cale dessous */
  var entete = document.querySelector(".entete");
  var mesurer = function () { if (entete) document.documentElement.style.setProperty("--entete", entete.offsetHeight + "px"); };
  mesurer(); window.addEventListener("resize", mesurer);

  /* ---------- Horaires et « ouvert maintenant » ---------- */
  var HORAIRES = {
    0: [], 6: [[480, 720]],
    1: [[480, 720], [840, 1110]], 2: [[480, 720], [840, 1110]], 3: [[480, 720], [840, 1110]],
    4: [[480, 720], [840, 1110]], 5: [[480, 720], [840, 1110]]
  };
  function heure(m) {
    var h = Math.floor(m / 60), mn = m % 60;
    if (EN) { var s = (h % 12 || 12) + (mn ? ":" + (mn < 10 ? "0" : "") + mn : "") + (h < 12 ? NBSP + "am" : NBSP + "pm"); return s; }
    return h + NBSP + "h" + (mn ? NBSP + (mn < 10 ? "0" : "") + mn : "");
  }
  function maintenant() {
    try {
      var o = {};
      new Intl.DateTimeFormat("en-GB", { timeZone: "Europe/Paris", weekday: "short", hour: "2-digit", minute: "2-digit", hourCycle: "h23" })
        .formatToParts(new Date()).forEach(function (x) { o[x.type] = x.value; });
      return { jour: { Sun: 0, Mon: 1, Tue: 2, Wed: 3, Thu: 4, Fri: 5, Sat: 6 }[o.weekday], min: +o.hour * 60 + +o.minute };
    } catch (e) { var d = new Date(); return { jour: d.getDay(), min: d.getHours() * 60 + d.getMinutes() }; }
  }
  var t = maintenant();
  var etat = document.querySelector("[data-etat]");
  if (etat) {
    var ouvert = null;
    HORAIRES[t.jour].forEach(function (p) { if (t.min >= p[0] && t.min < p[1]) ouvert = p; });
    if (ouvert) etat.innerHTML = TXT.ouvert + heure(ouvert[1]) + ".";
    else {
      var txt = "";
      for (var i = 0; i < 8 && !txt; i++) {
        var j = (t.jour + i) % 7;
        HORAIRES[j].some(function (p) {
          if (i > 0 || p[0] > t.min) { txt = (i === 0 ? TXT.a : i === 1 ? TXT.demain : TXT.jours[j] + " " + TXT.a) + heure(p[0]); return true; }
          return false;
        });
      }
      etat.innerHTML = TXT.ferme + txt + ".";
    }
  }
  var ligne = document.querySelector('.horaires tr[data-jour="' + t.jour + '"]');
  if (ligne) ligne.classList.add("aujourdhui");

  /* ---------- Contenu modifiable : contenu/infos.json ---------- */
  if (document.querySelector("[data-annonce]") && window.fetch && location.protocol !== "file:") {
    fetch(BASE + "contenu/infos.json", { cache: "no-store" }).then(function (r) { return r.ok ? r.json() : null; }).then(function (d) {
      if (!d) return;
      var lng = EN ? "en" : "fr";
      var a = document.querySelector("[data-annonce]");
      if (d.annonce && d.annonce[lng]) { a.textContent = d.annonce[lng]; a.hidden = false; }
      var c = document.querySelector("[data-conges]");
      if (c && d.conges && d.conges[lng]) c.textContent = d.conges[lng];
    }).catch(function () {});
  }

  /* ---------- Le pont élévateur : la voiture monte avec le défilement ---------- */
  var scene = document.querySelector(".scene");
  if (scene) {
    var etiquettes = Array.prototype.slice.call(scene.querySelectorAll(".etiquettes li"));
    var prevu = false;
    var regler = function (p) {
      scene.style.setProperty("--p", p.toFixed(3));
      etiquettes.forEach(function (li) { li.classList.toggle("visible", p >= parseFloat(li.dataset.seuil)); });
    };
    if (calme) regler(1);
    else {
      var calcul = function () {
        prevu = false;
        var r = scene.getBoundingClientRect();
        var course = r.height - window.innerHeight;
        regler(Math.max(0, Math.min(1, course > 0 ? -r.top / course : 1)));
      };
      var demander = function () { if (!prevu) { prevu = true; requestAnimationFrame(calcul); } };
      window.addEventListener("scroll", demander, { passive: true });
      window.addEventListener("resize", demander);
      calcul();
    }
  }

  /* ---------- Apparitions au défilement ---------- */
  var aVoir = document.querySelectorAll("[data-apparait]");
  if ("IntersectionObserver" in window && !calme) {
    var obs = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("vu"); obs.unobserve(e.target); } });
    }, { rootMargin: "0px 0px -10% 0px" });
    aVoir.forEach(function (el) { obs.observe(el); });
  } else aVoir.forEach(function (el) { el.classList.add("vu"); });

  /* ---------- Formulaire rendez-vous / devis (Netlify Forms) ---------- */
  var form = document.querySelector("[data-formulaire]");
  if (form) {
    var dateChamp = form.querySelector('[data-si="rendez-vous"]');
    var erreur = form.querySelector("[data-erreur]");
    var majType = function () { dateChamp.hidden = form.elements.type.value !== "rendez-vous"; };
    form.addEventListener("change", function (e) { if (e.target.name === "type") majType(); });
    majType();
    form.addEventListener("input", function (e) { e.target.removeAttribute("aria-invalid"); erreur.hidden = true; });
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var manquants = Array.prototype.filter.call(form.querySelectorAll("[required]"), function (c) { return !c.value.trim(); });
      if (manquants.length) {
        manquants.forEach(function (c) { c.setAttribute("aria-invalid", "true"); });
        erreur.textContent = TXT.requis + manquants.map(function (c) { return c.closest("label").querySelector("span").textContent.toLowerCase(); }).join(", ") + ".";
        erreur.hidden = false;
        manquants[0].focus();
        return;
      }
      var bouton = form.querySelector('[type="submit"]');
      var libelle = bouton.textContent;
      bouton.disabled = true; bouton.textContent = TXT.envoi;
      fetch("/", { method: "POST", headers: { "Content-Type": "application/x-www-form-urlencoded" }, body: new URLSearchParams(new FormData(form)).toString() })
        .then(function (r) { if (!r.ok) throw new Error(r.status); location.href = form.getAttribute("action"); })
        .catch(function () { erreur.textContent = TXT.echec; erreur.hidden = false; bouton.disabled = false; bouton.textContent = libelle; });
    });
  }

  /* ---------- Suivi de réparation : contenu/suivi.json ---------- */
  var suivi = document.querySelector("[data-suivi]");
  if (suivi) {
    var err = document.querySelector("[data-erreur]");
    var res = document.querySelector("[data-resultat]");
    suivi.addEventListener("submit", function (e) {
      e.preventDefault();
      var code = suivi.elements.code.value.trim().toUpperCase();
      err.hidden = true; res.hidden = true;
      if (!code) { err.textContent = TXT.code; err.hidden = false; suivi.elements.code.focus(); return; }
      fetch(BASE + "contenu/suivi.json", { cache: "no-store" }).then(function (r) { if (!r.ok) throw 0; return r.json(); }).then(function (d) {
        var dossier = (d.dossiers || []).filter(function (x) { return String(x.code).toUpperCase() === code; })[0];
        if (!dossier) { err.textContent = TXT.inconnu; err.hidden = false; return; }
        res.querySelectorAll("[data-etape]").forEach(function (li) {
          var n = +li.dataset.etape;
          li.classList.toggle("faite", n < dossier.etape);
          li.classList.toggle("active", n === dossier.etape);
          if (n === dossier.etape) li.setAttribute("aria-current", "step"); else li.removeAttribute("aria-current");
        });
        var note = dossier.note && (dossier.note[EN ? "en" : "fr"] || dossier.note.fr);
        res.querySelector("[data-note]").textContent = note || "";
        res.querySelector("[data-maj]").textContent = d.mis_a_jour ? TXT.maj + new Date(d.mis_a_jour + "T12:00:00").toLocaleDateString(EN ? "en-GB" : "fr-FR", { day: "numeric", month: "long", year: "numeric" }) : "";
        res.hidden = false; res.focus();
      }).catch(function () { err.textContent = TXT.hs; err.hidden = false; });
    });
  }
})();
