/* Au Pain Doré : « ouvert maintenant ? » et bon de commande de gâteau.
   HORAIRES : modifier ici. Jours : 0 = dimanche … 6 = samedi. Heures en minutes depuis minuit. */
(function () {
  "use strict";

  var HORAIRES = {
    0: [[7 * 60, 13 * 60]],
    1: [],
    2: [[7 * 60, 19 * 60 + 30]],
    3: [[7 * 60, 19 * 60 + 30]],
    4: [[7 * 60, 19 * 60 + 30]],
    5: [[7 * 60, 19 * 60 + 30]],
    6: [[7 * 60, 13 * 60], [15 * 60, 19 * 60]]
  };
  var JOURS = ["dimanche", "lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi"];

  function heure(m) {
    var h = Math.floor(m / 60), min = m % 60;
    return h + "\u00a0h" + (min ? " " + (min < 10 ? "0" : "") + min : "");
  }

  /* Heure de Lyon, quel que soit le fuseau du téléphone */
  function maintenantLyon() {
    try {
      var p = new Intl.DateTimeFormat("en-GB", {
        timeZone: "Europe/Paris", weekday: "short", hour: "2-digit", minute: "2-digit", hourCycle: "h23"
      }).formatToParts(new Date());
      var o = {};
      p.forEach(function (x) { o[x.type] = x.value; });
      var j = { Sun: 0, Mon: 1, Tue: 2, Wed: 3, Thu: 4, Fri: 5, Sat: 6 }[o.weekday];
      return { jour: j, minutes: parseInt(o.hour, 10) * 60 + parseInt(o.minute, 10) };
    } catch (e) {
      var d = new Date();
      return { jour: d.getDay(), minutes: d.getHours() * 60 + d.getMinutes() };
    }
  }

  function prochaineOuverture(jour, minutes) {
    for (var i = 0; i < 8; i++) {
      var j = (jour + i) % 7;
      var plages = HORAIRES[j];
      for (var k = 0; k < plages.length; k++) {
        if (i > 0 || plages[k][0] > minutes) {
          var quand = i === 0 ? "à " : i === 1 ? "demain à " : JOURS[j] + " à ";
          return quand + heure(plages[k][0]);
        }
      }
    }
    return "";
  }

  var etat = document.querySelector("[data-etat]");
  if (etat) {
    var t = maintenantLyon();
    var ouvert = null;
    HORAIRES[t.jour].forEach(function (p) { if (t.minutes >= p[0] && t.minutes < p[1]) ouvert = p; });
    etat.innerHTML = ouvert
      ? "Oui, c'est <strong>ouvert</strong> jusqu'à\u00a0" + heure(ouvert[1]) + "."
      : "C'est <strong>fermé</strong> pour l'instant. On rouvre " + prochaineOuverture(t.jour, t.minutes) + ".";
    etat.hidden = false;
    var ligne = document.querySelector('.horaires tr[data-jour="' + t.jour + '"]');
    if (ligne) {
      ligne.classList.add("aujourdhui");
      ligne.querySelector("th").setAttribute("aria-label", ligne.querySelector("th").textContent + " (aujourd'hui)");
    }
  }

  /* ---------- Bon de commande ---------- */
  var form = document.querySelector("[data-commande]");
  if (!form) return;
  var bon = form.closest(".bon");
  var recu = bon.querySelector("[data-recu]");
  var recuTexte = bon.querySelector("[data-recu-texte]");
  var erreur = form.querySelector("[data-erreur]");
  var champJour = form.elements.jour;

  function iso(d) {
    return d.getFullYear() + "-" + String(d.getMonth() + 1).padStart(2, "0") + "-" + String(d.getDate()).padStart(2, "0");
  }
  var auPlusTot = new Date();
  auPlusTot.setHours(0, 0, 0, 0);
  auPlusTot.setDate(auPlusTot.getDate() + 2);
  champJour.min = iso(auPlusTot);

  function signaler(champ, message) {
    erreur.textContent = message;
    erreur.hidden = false;
    champ.setAttribute("aria-invalid", "true");
    champ.focus();
  }

  form.addEventListener("input", function (e) {
    e.target.removeAttribute("aria-invalid");
    erreur.hidden = true;
  });

  form.addEventListener("submit", function (e) {
    e.preventDefault();
    var v = champJour.value;
    if (!v) return signaler(champJour, "Indiquez le jour où vous voulez le gâteau.");
    var d = new Date(v + "T12:00:00");
    if (d < auPlusTot) return signaler(champJour, "Il faut 48 h au fournil : choisissez une date à partir du " + auPlusTot.toLocaleDateString("fr-FR", { day: "numeric", month: "long" }) + ".");
    if (d.getDay() === 1) return signaler(champJour, "La boutique est fermée le lundi : choisissez un autre jour.");
    if (!form.elements.parts.value) return signaler(form.elements.parts, "Choisissez le nombre de parts.");

    var envie = form.elements.envie.value.trim();
    var nom = form.elements.nom.value.trim();
    var jourTexte = d.toLocaleDateString("fr-FR", { weekday: "long", day: "numeric", month: "long" });
    recuTexte.textContent =
      "Un gâteau de " + form.elements.parts.value + (envie ? ", " + envie : "") +
      ", pour le " + jourTexte + (nom ? ", au nom de " + nom : "") + ".";

    bon.classList.add("detache");
    form.hidden = true;
    recu.hidden = false;
    recu.focus();
  });

  bon.querySelector("[data-recommencer]").addEventListener("click", function () {
    bon.classList.remove("detache");
    recu.hidden = true;
    form.hidden = false;
    form.reset();
    champJour.focus();
  });
})();
