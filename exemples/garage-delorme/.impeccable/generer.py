#!/usr/bin/env python3
"""Génère les pages FR et EN du Garage Delorme à partir d'un seul modèle.
Usage : python3 .impeccable/generer.py (depuis la racine du projet)."""
import json
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent / "site"

T = {
 "fr": {
  "lang": "fr", "prefixe": "", "autre": "en/", "autre_label": "EN", "autre_nom": "English version",
  "title": "Garage Delorme · Garage automobile à Gap",
  "desc": "Garage automobile à Gap (Hautes-Alpes) : entretien et révision, diagnostic électronique, dépannage et remorquage, carrosserie. Rendez-vous, devis et suivi en ligne.",
  "fictif": "Exemple fictif : ce site démontre le skill <em>site-commercant</em>. Ce garage n'existe pas.",
  "nav": [("#services", "Services"), ("#panne", "En panne ?"), ("#demande", "Rendez-vous"), ("suivi.html", "Suivi")],
  "h1": "Votre voiture est entre de bonnes mains.",
  "chapeau": "Garage automobile à Gap. Entretien, diagnostic, dépannage et carrosserie : on vous montre tout ce qu'on fait.",
  "cta1": "Prendre rendez-vous", "cta2": "Appeler",
  "defiler": "Faites monter la voiture",
  "labels": [("Carrosserie", "portes, peinture"), ("Diagnostic", "prise de diagnostic"), ("Entretien", "carter, freins"), ("Dépannage", "anneau de remorquage")],
  "pont_alt": "Dessin d'une voiture sur un pont élévateur, qui monte au défilement pour montrer son dessous.",
  "services_titre": "Ce qu'on fait pour vous",
  "services": [
   ("Entretien et révision", "Vidange, freins, pneus, distribution, climatisation. Votre carnet d'entretien est tenu à jour."),
   ("Diagnostic électronique", "Un voyant s'allume ? On lit ce que dit la voiture avant de toucher à quoi que ce soit."),
   ("Dépannage et remorquage", "Panne sur la route : on vient vous chercher, vous et votre véhicule."),
   ("Carrosserie", "Réparation après sinistre, peinture, pare-brise."),
  ],
  "panne_titre": "En panne sur la route ?",
  "panne_texte": "Votre assistance vous oriente vers nous ? Appelez-nous : on prend le relais, et vous suivez la réparation en ligne avec le code qu'on vous donne.",
  "panne_horaires": "Horaires du dépannage : [À COMPLÉTER : horaires du dépannage]",
  "panne_suivi": "Suivre ma réparation",
  "photo": "Photo de l'atelier à venir", "illus": "Illustration · exemple fictif",
  "photo_alt": "Une voiture grise levée sur un pont élévateur aux bras jaunes ; un mécanicien inspecte le dessous, les montagnes au loin.",
  "diag_alt": "La main d'un mécanicien branche la prise de diagnostic sous le tableau de bord ; une tablette affiche des courbes.",
  "form_titre": "Rendez-vous ou devis",
  "form_intro": "Dites-nous ce dont votre voiture a besoin. On vous rappelle pour confirmer.",
  "type": "Votre demande", "type_rdv": "Un rendez-vous", "type_devis": "Un devis",
  "f_nom": "Nom", "f_tel": "Téléphone", "f_mail": "E-mail (facultatif)", "f_vehicule": "Véhicule",
  "f_vehicule_ph": "marque, modèle, année", "f_immat": "Immatriculation (facultatif)", "f_service": "Prestation",
  "f_service_opts": ["Entretien et révision", "Diagnostic électronique", "Dépannage et remorquage", "Carrosserie", "Autre"],
  "f_date": "Date souhaitée", "f_message": "Votre message", "f_envoyer": "Envoyer ma demande",
  "f_rgpd": "Vos informations servent uniquement à vous répondre.", "conf": "Confidentialité",
  "suivi_titre": "Suivez votre réparation",
  "suivi_texte": "Le garage vous remet un code à la dépose du véhicule. Entrez-le pour voir où en est votre voiture.",
  "suivi_cta": "Suivre ma réparation", "exemple": "Exemple de suivi",
  "infos_titre": "Nous trouver",
  "horaires": "Horaires de l'atelier",
  "jours": [("1", "Lundi", "8 h – 12 h · 14 h – 18 h 30"), ("2", "Mardi", "8 h – 12 h · 14 h – 18 h 30"), ("3", "Mercredi", "8 h – 12 h · 14 h – 18 h 30"), ("4", "Jeudi", "8 h – 12 h · 14 h – 18 h 30"), ("5", "Vendredi", "8 h – 12 h · 14 h – 18 h 30"), ("6", "Samedi", "8 h – 12 h"), ("0", "Dimanche", "Fermé")],
  "conges": "Fermetures annuelles : [À COMPLÉTER : dates de congés]",
  "itineraire": "Itinéraire",
  "ml": "Mentions légales", "cookies": "Ce site ne dépose aucun cookie.", "illus_pied": "Exemple fictif : les photos sont des illustrations générées par IA.",
  # suivi
  "s_title": "Suivi de réparation · Garage Delorme, Gap",
  "s_desc": "Suivez l'avancement de la réparation de votre véhicule au Garage Delorme à Gap, avec le code remis à la dépose.",
  "s_h1": "Où en est ma voiture ?",
  "s_intro": "Entrez le code remis par le garage à la dépose de votre véhicule.",
  "s_code": "Code de suivi", "s_ph": "ex. DEMO-4821", "s_voir": "Voir l'avancement",
  "s_etapes": ["Véhicule reçu", "Diagnostic", "Réparation", "Prête à récupérer"],
  "s_demo": "Pour essayer : code DEMO-4821.",
  "s_aide": "Une question ? Appelez le garage.",
  "s_vie": "Aucune donnée personnelle n'est affichée ici : seulement le code et l'étape.",
  "retour": "Retour à l'accueil",
  "maps": "Garage+Delorme+14+avenue+d%27Embrun+05000+Gap",
 },
 "en": {
  "lang": "en", "prefixe": "../", "autre": "../", "autre_label": "FR", "autre_nom": "Version française",
  "title": "Garage Delorme · Car repair garage in Gap, French Alps",
  "desc": "Car repair garage in Gap (French Alps): servicing, electronic diagnostics, breakdown and towing, bodywork. Book, get a quote and track your repair online.",
  "fictif": "Fictional example: this site demonstrates the <em>site-commercant</em> skill. This garage does not exist.",
  "nav": [("#services", "Services"), ("#panne", "Broken down?"), ("#demande", "Book"), ("suivi.html", "Track")],
  "h1": "Your car is in good hands.",
  "chapeau": "Car repair garage in Gap, French Alps. Servicing, diagnostics, breakdown and bodywork: we show you everything we do.",
  "cta1": "Book a visit", "cta2": "Call us",
  "defiler": "Scroll to lift the car",
  "labels": [("Bodywork", "doors, paint"), ("Diagnostics", "diagnostic port"), ("Servicing", "sump, brakes"), ("Breakdown", "towing eye")],
  "pont_alt": "Drawing of a car on a lift, rising as you scroll to show its underside.",
  "services_titre": "What we do for you",
  "services": [
   ("Servicing", "Oil change, brakes, tyres, timing belt, air conditioning. Your service book is kept up to date."),
   ("Electronic diagnostics", "A warning light is on? We read what the car says before touching anything."),
   ("Breakdown and towing", "Broken down on the road: we come and get you and your vehicle."),
   ("Bodywork", "Accident repair, paint, windscreen."),
  ],
  "panne_titre": "Broken down on the road?",
  "panne_texte": "Has your assistance company sent you to us? Call us: we take it from there, and you follow the repair online with the code we give you.",
  "panne_horaires": "Breakdown service hours: [À COMPLÉTER : horaires du dépannage]",
  "panne_suivi": "Track my repair",
  "photo": "Workshop photo coming soon", "illus": "Illustration · fictional example",
  "photo_alt": "A grey car raised on a lift with yellow arms; a mechanic inspects the underside, mountains in the distance.",
  "diag_alt": "A mechanic's hand plugs the diagnostic connector under the dashboard; a tablet shows graphs.",
  "form_titre": "Book or get a quote",
  "form_intro": "Tell us what your car needs. We will call you back to confirm.",
  "type": "Your request", "type_rdv": "A booking", "type_devis": "A quote",
  "f_nom": "Name", "f_tel": "Phone", "f_mail": "Email (optional)", "f_vehicule": "Vehicle",
  "f_vehicule_ph": "make, model, year", "f_immat": "Registration (optional)", "f_service": "Service",
  "f_service_opts": ["Servicing", "Electronic diagnostics", "Breakdown and towing", "Bodywork", "Other"],
  "f_date": "Preferred date", "f_message": "Your message", "f_envoyer": "Send my request",
  "f_rgpd": "Your details are only used to answer you.", "conf": "Privacy (in French)",
  "suivi_titre": "Track your repair",
  "suivi_texte": "The garage gives you a code when you drop off the car. Enter it to see where your car is.",
  "suivi_cta": "Track my repair", "exemple": "Tracking example",
  "infos_titre": "Find us",
  "horaires": "Workshop hours",
  "jours": [("1", "Monday", "8 am – 12 pm · 2 – 6:30 pm"), ("2", "Tuesday", "8 am – 12 pm · 2 – 6:30 pm"), ("3", "Wednesday", "8 am – 12 pm · 2 – 6:30 pm"), ("4", "Thursday", "8 am – 12 pm · 2 – 6:30 pm"), ("5", "Friday", "8 am – 12 pm · 2 – 6:30 pm"), ("6", "Saturday", "8 am – 12 pm"), ("0", "Sunday", "Closed")],
  "conges": "Annual closures: [À COMPLÉTER : dates de congés]",
  "itineraire": "Directions",
  "ml": "Legal notice (in French)", "cookies": "This site sets no cookies.", "illus_pied": "Fictional example: photos are AI-generated illustrations.",
  "s_title": "Repair tracking · Garage Delorme, Gap",
  "s_desc": "Follow the progress of your vehicle's repair at Garage Delorme in Gap, French Alps, with the code given when you dropped it off.",
  "s_h1": "Where is my car?",
  "s_intro": "Enter the code the garage gave you when you dropped off your vehicle.",
  "s_code": "Tracking code", "s_ph": "e.g. DEMO-4821", "s_voir": "Show progress",
  "s_etapes": ["Vehicle received", "Diagnosis", "Repair", "Ready for pick-up"],
  "s_demo": "To try it: code DEMO-4821.",
  "s_aide": "A question? Call the garage.",
  "s_vie": "No personal data is shown here: only the code and the step.",
  "retour": "Back to home",
  "maps": "Garage+Delorme+14+avenue+d%27Embrun+05000+Gap",
 },
}

SVG_DEFS = """<svg class="defs" aria-hidden="true" focusable="false">
  <symbol id="i-tel" viewBox="0 0 24 24"><path d="M5 3.5h3.2l1.6 4.2-2.1 1.5a11 11 0 0 0 7.1 7.1l1.5-2.1 4.2 1.6V19a1.6 1.6 0 0 1-1.7 1.6A16.6 16.6 0 0 1 3.4 5.2 1.6 1.6 0 0 1 5 3.5Z"/></symbol>
  <symbol id="i-lieu" viewBox="0 0 24 24"><path d="M12 21s-6.5-5.6-6.5-11a6.5 6.5 0 0 1 13 0C18.5 15.4 12 21 12 21Z"/><circle cx="12" cy="10" r="2.4"/></symbol>
  <symbol id="i-fleche" viewBox="0 0 24 24"><path d="M5 12h14m-6-6 6 6-6 6"/></symbol>
</svg>"""

def logo(p):
    return f"""<a class="logo" href="{'index.html' if not p['prefixe'] else 'index.html'}" aria-label="Garage Delorme">
    <svg class="logo-pont" viewBox="0 0 40 32" aria-hidden="true"><path class="lp-col" d="M5 2v28M35 2v28"/><path class="lp-bras" d="M5 22h30"/><path class="lp-sol" d="M1 30.5h38"/></svg>
    <span class="logo-nom"><span>Garage</span> Delorme</span>
  </a>"""

def entete(p, page):
    nav = "".join(f'<a href="{h if (h.startswith("#") and page=="index") else ("index.html"+h if h.startswith("#") else h)}">{l}</a>' for h, l in p["nav"])
    autre = p["autre"] + ({"suivi": "suivi.html", "merci": "merci.html"}.get(page, "index.html"))
    return f"""<header class="entete">
  {logo(p)}
  <nav class="nav" aria-label="Sections">{nav}</nav>
  <div class="entete-actions">
    <a class="entete-tel" href="tel:+33492000000"><svg class="ic" aria-hidden="true"><use href="#i-tel"/></svg><span>04 92 00 00 00</span></a>
    <a class="langue" href="{autre}" hreflang="{'en' if p['lang']=='fr' else 'fr'}" lang="{'en' if p['lang']=='fr' else 'fr'}" aria-label="{p['autre_nom']}">{p['autre_label']}</a>
  </div>
</header>"""

def head(p, title, desc, page):
    pre = p["prefixe"]
    chemin = {"index": "", "suivi": "suivi.html", "merci": "merci.html"}[page]
    fr = f"[À COMPLÉTER : adresse du site]/{chemin}"
    en = f"[À COMPLÉTER : adresse du site]/en/{chemin}"
    jsonld = ""
    if page == "index":
        jsonld = """
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "AutoRepair",
  "name": "Garage Delorme",
  "telephone": "+33492000000",
  "address": { "@type": "PostalAddress", "streetAddress": "14 avenue d'Embrun", "postalCode": "05000", "addressLocality": "Gap", "addressCountry": "FR" },
  "openingHoursSpecification": [
    { "@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"], "opens": "08:00", "closes": "12:00" },
    { "@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"], "opens": "14:00", "closes": "18:30" },
    { "@type": "OpeningHoursSpecification", "dayOfWeek": "Saturday", "opens": "08:00", "closes": "12:00" }
  ]
}
</script>"""
    return f"""<!doctype html>
<html lang="{p['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{fr if p['lang']=='fr' else en}">
<link rel="alternate" hreflang="fr" href="{fr}">
<link rel="alternate" hreflang="en" href="{en}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="[À COMPLÉTER : adresse du site]/images/partage.jpg">
<meta property="og:locale" content="{'fr_FR' if p['lang']=='fr' else 'en_GB'}">
<meta name="theme-color" content="#111418">
<link rel="icon" href="{pre}favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{pre}apple-touch-icon.png">
<link rel="preload" href="{pre}fonts/archivo.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{pre}css/style.css">{jsonld}
</head>"""

def pied(p):
    pre = p["prefixe"]
    return f"""<footer class="pied">
  <div class="pied-marque">{logo(p)}</div>
  <address>14 avenue d'Embrun, 05000 Gap · <a href="tel:+33492000000">04 92 00 00 00</a></address>
  <p class="pied-liens"><a href="{pre}mentions-legales.html">{p['ml']}</a> <a href="{pre}confidentialite.html">{p['conf']}</a> <a href="{p['autre']}index.html" hreflang="{'en' if p['lang']=='fr' else 'fr'}">{p['autre_nom']}</a></p>
  <p class="pied-petit">{p['cookies']} {p['illus_pied']}</p>
</footer>"""

# --- Le pont élévateur : colonnes fixes, charge mobile (voiture + bras + dessous) ---
VOITURE = """<svg class="pont-colonnes" viewBox="0 0 640 300" aria-hidden="true">
  <g class="trait-acier">
    <path d="M22 18h20v262H22zM598 18h20v262h-20z"/>
    <path d="M12 280h40M588 280h40"/>
    <path d="M0 281.5h640"/>
  </g>
  <g class="sol"><path d="M60 290l12-8M110 290l12-8M160 290l12-8M210 290l12-8M260 290l12-8M310 290l12-8M360 290l12-8M410 290l12-8M460 290l12-8M510 290l12-8M560 290l12-8"/></g>
</svg>
<div class="pont-charge">
  <svg class="pont-voiture" viewBox="0 0 640 300" aria-hidden="true">
    <g class="dessous">
      <path d="M470 252h56c6 0 10-4 10-9v-6h-76v6c0 5 4 9 10 9z"/><path d="M478 252v-14M490 252v-14M502 252v-14M514 252v-14"/>
      <path d="M472 236l36 4M544 236l-36 4M200 236l-36 4M128 236l36 4"/>
      <path d="M464 248H350M250 248H232M172 248H120l-24-4"/><rect x="176" y="241" width="56" height="14" rx="7"/><path d="M96 244h-8"/>
      <rect x="250" y="239" width="100" height="16" rx="4"/><path d="M262 247h76"/>
      <path d="M508 240m-24 0a24 24 0 1 0 48 0a24 24 0 1 0-48 0M164 240m-24 0a24 24 0 1 0 48 0a24 24 0 1 0-48 0"/>
      <path d="M526 224a24 24 0 0 1 6 12M182 224a24 24 0 0 1 6 12" stroke-width="3.2"/>
      <path d="M598 214h8"/><circle cx="612" cy="214" r="5"/>
      <path d="M394 194h18v8h-18z"/>
    </g>
    <g class="bras">
      <path d="M42 238h20l70 6h40"/><path d="M598 238h-20l-70 6h-40"/>
      <rect x="20" y="228" width="24" height="18" rx="2"/><rect x="596" y="228" width="24" height="18" rx="2"/>
    </g>
    <g class="carrosserie">
      <path d="M58 236v-26c0-20 12-30 34-34l74-14c32-30 68-50 116-54l136-2c44 2 78 26 104 54l64 12c18 4 26 18 26 38v26z"/>
      <path d="M190 162c24-24 52-40 90-42l58-1v43z"/><path d="M350 119h58c34 2 60 18 80 41l-138 2z"/>
      <path d="M344 114v118"/><path d="M576 176l22 4M60 186h14"/><path d="M402 172h22"/>
    </g>
    <g class="roues">
      <circle class="passage" cx="164" cy="240" r="40"/><circle cx="164" cy="240" r="31"/><circle cx="164" cy="240" r="17"/><circle cx="164" cy="240" r="4"/>
      <circle class="passage" cx="508" cy="240" r="40"/><circle cx="508" cy="240" r="31"/><circle cx="508" cy="240" r="17"/><circle cx="508" cy="240" r="4"/>
    </g>
  </svg>
  <ul class="etiquettes">
    <li style="--x:47%;--y:62%" data-seuil="0.2"><span class="pastille"></span><span class="tige"></span><strong>{l0}</strong><em>{d0}</em></li>
    <li style="--x:63%;--y:66%" data-seuil="0.4"><span class="pastille"></span><span class="tige"></span><strong>{l1}</strong><em>{d1}</em></li>
    <li class="a-gauche" style="--x:79%;--y:82%" data-seuil="0.6"><span class="pastille"></span><span class="tige"></span><strong>{l2}</strong><em>{d2}</em></li>
    <li class="a-gauche" style="--x:95.6%;--y:71.3%" data-seuil="0.8"><span class="pastille"></span><span class="tige"></span><strong>{l3}</strong><em>{d3}</em></li>
  </ul>
</div>"""

def accueil(p):
    pre = p["prefixe"]
    lab = {}
    for i, (l, d) in enumerate(p["labels"]):
        lab[f"l{i}"] = l; lab[f"d{i}"] = d
    services = "".join(f'<li data-apparait><h3>{t}</h3><p>{d}</p></li>' for t, d in p["services"])
    opts = "".join(f"<option>{o}</option>" for o in p["f_service_opts"])
    FERME = ' class="ferme"'
    ACTIVE = ' class="active"'
    jours = "".join('<tr data-jour="%s"%s><th scope="row">%s</th><td>%s</td></tr>' % (j, FERME if j == "0" else "", n, h) for j, n, h in p["jours"])
    promo = "".join('<li%s><span>%s</span></li>' % (ACTIVE if i == 2 else "", e) for i, e in enumerate(p["s_etapes"]))
    return f"""{head(p, p['title'], p['desc'], 'index')}
<body>
{SVG_DEFS}
<p class="fictif">{p['fictif']}</p>
{entete(p, 'index')}
<main>
  <section class="scene" aria-labelledby="t-titre">
    <div class="scene-collante">
      <div class="scene-texte">
        <h1 id="t-titre" class="titre">{p['h1']}</h1>
        <p class="chapeau">{p['chapeau']}</p>
        <div class="actions">
          <a class="bouton bouton--jaune" href="#demande">{p['cta1']}</a>
          <a class="bouton" href="tel:+33492000000"><svg class="ic" aria-hidden="true"><use href="#i-tel"/></svg>{p['cta2']}</a>
        </div>
      </div>
      <p class="defiler" aria-hidden="true"><span></span>{p['defiler']}</p>
      <figure class="pont" role="img" aria-label="{p['pont_alt']}">
        {VOITURE.format(**lab)}
      </figure>
    </div>
  </section>

  <section class="services" id="services" aria-labelledby="t-services">
    <div class="services-tete">
      <h2 id="t-services" class="titre-section">{p['services_titre']}</h2>
      <figure class="photo photo--diag" data-apparait><img src="{pre}images/diagnostic.jpg" width="1500" height="1000" loading="lazy" alt="{p['diag_alt']}"><figcaption>{p['illus']}</figcaption></figure>
    </div>
    <ul class="liste-services">{services}</ul>
  </section>

  <section class="panne" id="panne" aria-labelledby="t-panne">
    <div class="panne-texte" data-apparait>
      <h2 id="t-panne" class="titre-section">{p['panne_titre']}</h2>
      <p>{p['panne_texte']}</p>
      <div class="actions">
        <a class="bouton bouton--jaune" href="tel:+33492000000"><svg class="ic" aria-hidden="true"><use href="#i-tel"/></svg>04 92 00 00 00</a>
        <a class="bouton bouton--clair" href="suivi.html">{p['panne_suivi']}<svg class="ic" aria-hidden="true"><use href="#i-fleche"/></svg></a>
      </div>
      <p class="note">{p['panne_horaires']}</p>
    </div>
    <figure class="photo"><img src="{pre}images/atelier.jpg" width="1500" height="1125" loading="lazy" alt="{p['photo_alt']}"><figcaption>{p['illus']}</figcaption></figure>
  </section>

  <section class="demande" id="demande" aria-labelledby="t-demande">
    <div class="demande-intro">
      <h2 id="t-demande" class="titre-section">{p['form_titre']}</h2>
      <p>{p['form_intro']}</p>
    </div>
    <form class="formulaire" name="demande" method="POST" action="{'merci.html' if p['lang']=='fr' else 'merci.html'}" data-netlify="true" netlify-honeypot="adresse-web" data-formulaire>
      <input type="hidden" name="form-name" value="demande">
      <input type="hidden" name="langue" value="{p['lang']}">
      <p class="piege"><label>Ne pas remplir <input name="adresse-web" tabindex="-1" autocomplete="off"></label></p>
      <fieldset class="choix">
        <legend>{p['type']}</legend>
        <label><input type="radio" name="type" value="rendez-vous" checked> <span>{p['type_rdv']}</span></label>
        <label><input type="radio" name="type" value="devis"> <span>{p['type_devis']}</span></label>
      </fieldset>
      <div class="champs">
        <label class="champ"><span>{p['f_nom']}</span><input name="nom" autocomplete="name" required></label>
        <label class="champ"><span>{p['f_tel']}</span><input name="telephone" type="tel" autocomplete="tel" required></label>
        <label class="champ"><span>{p['f_mail']}</span><input name="email" type="email" autocomplete="email"></label>
        <label class="champ"><span>{p['f_vehicule']}</span><input name="vehicule" placeholder="{p['f_vehicule_ph']}" required></label>
        <label class="champ"><span>{p['f_immat']}</span><input name="immatriculation" autocomplete="off"></label>
        <label class="champ"><span>{p['f_service']}</span><select name="prestation">{opts}</select></label>
        <label class="champ" data-si="rendez-vous"><span>{p['f_date']}</span><input name="date" type="date"></label>
        <label class="champ champ--large"><span>{p['f_message']}</span><textarea name="message" rows="4"></textarea></label>
      </div>
      <p class="erreur" role="alert" hidden data-erreur></p>
      <button class="bouton bouton--jaune" type="submit">{p['f_envoyer']}</button>
      <p class="aide">{p['f_rgpd']} <a href="{pre}confidentialite.html">{p['conf']}</a></p>
    </form>
  </section>

  <section class="suivi-promo" aria-labelledby="t-suivi">
    <div data-apparait>
      <h2 id="t-suivi" class="titre-section">{p['suivi_titre']}</h2>
      <p>{p['suivi_texte']}</p>
    </div>
    <div class="promo-schema"><p class="exemple">{p['exemple']}</p><ol class="etapes etapes--promo" aria-hidden="true">{promo}</ol></div>
    <a class="bouton bouton--jaune" href="suivi.html">{p['suivi_cta']}<svg class="ic" aria-hidden="true"><use href="#i-fleche"/></svg></a>
  </section>

  <!-- HORAIRES : modifier aussi contenu/infos.json, le JSON-LD en haut et js/main.js -->
  <section class="infos" id="infos" aria-labelledby="t-infos">
    <h2 id="t-infos" class="titre-section">{p['infos_titre']}</h2>
    <div class="infos-grille">
      <div>
        <p class="adresse">14 avenue d'Embrun<br>05000 Gap</p>
        <p class="etat" data-etat></p>
        <p class="annonce" data-annonce hidden></p>
        <div class="actions">
          <a class="bouton bouton--jaune" href="https://www.google.com/maps/search/?api=1&amp;query={p['maps']}"><svg class="ic" aria-hidden="true"><use href="#i-lieu"/></svg>{p['itineraire']}</a>
          <a class="bouton" href="tel:+33492000000"><svg class="ic" aria-hidden="true"><use href="#i-tel"/></svg>04 92 00 00 00</a>
        </div>
      </div>
      <div>
        <table class="horaires"><caption>{p['horaires']}</caption><tbody>{jours}</tbody></table>
        <p class="note" data-conges>{p['conges']}</p>
      </div>
    </div>
  </section>
</main>
{pied(p)}
<script src="{pre}js/main.js" defer></script>
</body>
</html>
"""

def suivi(p):
    pre = p["prefixe"]
    etapes = "".join(f'<li data-etape="{i+1}"><span>{e}</span></li>' for i, e in enumerate(p["s_etapes"]))
    return f"""{head(p, p['s_title'], p['s_desc'], 'suivi')}
<body class="page-suivi">
{SVG_DEFS}
<p class="fictif">{p['fictif']}</p>
{entete(p, 'suivi')}
<main class="suivi">
  <h1 class="titre">{p['s_h1']}</h1>
  <p class="chapeau">{p['s_intro']}</p>
  <form class="suivi-form" data-suivi novalidate>
    <label class="champ"><span>{p['s_code']}</span><input name="code" autocomplete="off" autocapitalize="characters" spellcheck="false" placeholder="{p['s_ph']}" required></label>
    <button class="bouton bouton--jaune" type="submit">{p['s_voir']}</button>
  </form>
  <p class="aide">{p['s_demo']}</p>
  <p class="erreur" role="alert" hidden data-erreur></p>
  <div class="resultat" data-resultat hidden tabindex="-1">
    <ol class="etapes">{etapes}</ol>
    <p class="resultat-note" data-note></p>
    <p class="aide" data-maj></p>
  </div>
  <p class="aide">{p['s_aide']} <a href="tel:+33492000000">04 92 00 00 00</a></p>
  <p class="aide">{p['s_vie']}</p>
  <p><a class="retour" href="index.html">{p['retour']}</a></p>
</main>
{pied(p)}
<script src="{pre}js/main.js" defer></script>
</body>
</html>
"""

for code, p in T.items():
    dossier = RACINE if code == "fr" else RACINE / "en"
    dossier.mkdir(parents=True, exist_ok=True)
    (dossier / "index.html").write_text(accueil(p), encoding="utf-8")
    (dossier / "suivi.html").write_text(suivi(p), encoding="utf-8")
MERCI = {"fr": ("Demande envoyée · Garage Delorme", "Merci, votre demande est bien partie.", "On vous rappelle dès que possible pour confirmer. En cas d'urgence, appelez le 04 92 00 00 00."),
         "en": ("Request sent · Garage Delorme", "Thank you, your request has been sent.", "We will call you back as soon as possible to confirm. If it is urgent, call +33 4 92 00 00 00.")}
for code, p in T.items():
    t, h, txt = MERCI[code]
    dossier = RACINE if code == "fr" else RACINE / "en"
    page = head(p, t, txt, "merci").replace('<link rel="canonical"', '<meta name="robots" content="noindex">\n<link rel="canonical"')
    page += f"""
<body class="page-suivi">
{SVG_DEFS}
<p class="fictif">{p['fictif']}</p>
{entete(p, 'merci')}
<main class="suivi">
  <h1 class="titre">{h}</h1>
  <p class="chapeau">{txt}</p>
  <p><a class="retour" href="index.html">{p['retour']}</a></p>
</main>
{pied(p)}
</body>
</html>
"""
    (dossier / "merci.html").write_text(page, encoding="utf-8")
print("ok")
