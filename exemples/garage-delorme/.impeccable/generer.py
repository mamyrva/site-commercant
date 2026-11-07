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
  "h1": "Votre voiture est entre de bonnes mains.", "h1_a": "Votre voiture est entre de bonnes", "h1_b": "mains.",
  "pont_titre": "Le pont élévateur",
  "chiffres_titre": "En bref",
  "chiffres": [("6 j/7", "l'atelier est ouvert du lundi au samedi"), ("4", "métiers sous le même toit"), ("1 code", "pour suivre votre réparation en ligne"), ("0 cookie", "de suivi sur ce site")],
  "publics_titre": "Vous êtes…",
  "publics": [
   ("i-maison", "De la région", "Entretien, révision, pneus ou contrôle avant les vacances : prenez rendez-vous, on vous rappelle pour confirmer.", "#demande", "Prendre rendez-vous", "tel:+33492000000", "Appeler"),
   ("i-route", "En panne sur la route", "On vient vous chercher, vous et votre véhicule. Vous suivez ensuite la réparation en ligne, avec le code qu'on vous donne.", "tel:+33492000000", "Appeler", "suivi.html", "Suivre ma réparation"),
   ("i-bouclier", "Envoyé par votre assistance", "Votre assistance vous oriente vers nous ? Appelez-nous : on prend le relais avec elle.", "tel:+33492000000", "Appeler", "#infos", "Nous trouver"),
  ],
  "chapeau": "Garage automobile au 14 avenue d'Embrun, à Gap. Entretien, diagnostic, dépannage et carrosserie : on vous montre tout ce qu'on fait.",
  "cta1": "Prendre rendez-vous", "cta2": "Appeler",
  "defiler": "Faites monter la voiture",
  "labels": [("Carrosserie", "portes, peinture"), ("Diagnostic", "prise de diagnostic"), ("Entretien", "carter, freins"), ("Dépannage", "anneau de remorquage")],
  "pont_alt": "Une voiture grise posée sur un pont élévateur à deux colonnes, dans un atelier éclairé en bleu. Au défilement, le pont la soulève et montre son dessous.",
  "pont_mention": "Illustration générée par IA",
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
  "ml": "Mentions légales", "cookies": "Ce site ne dépose aucun cookie.", "illus_pied": "Exemple fictif.",
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
  "h1": "Your car is in good hands.", "h1_a": "Your car is in good", "h1_b": "hands.",
  "pont_titre": "The vehicle lift",
  "chiffres_titre": "At a glance",
  "chiffres": [("6 days", "the workshop is open Monday to Saturday"), ("4", "trades under one roof"), ("1 code", "to track your repair online"), ("0 cookies", "no tracking on this site")],
  "publics_titre": "You are…",
  "publics": [
   ("i-maison", "Local", "Servicing, tyres or a check before the holidays: book a visit and we will call you back to confirm.", "#demande", "Book a visit", "tel:+33492000000", "Call us"),
   ("i-route", "Broken down on the road", "We come and get you and your vehicle. Then you follow the repair online with the code we give you.", "tel:+33492000000", "Call us", "suivi.html", "Track my repair"),
   ("i-bouclier", "Sent by your assistance company", "Has your assistance company sent you to us? Call us: we take it from there with them.", "tel:+33492000000", "Call us", "#infos", "Find us"),
  ],
  "chapeau": "Car repair garage at 14 avenue d'Embrun, Gap, French Alps. Servicing, diagnostics, breakdown and bodywork: we show you everything we do.",
  "cta1": "Book a visit", "cta2": "Call us",
  "defiler": "Scroll to lift the car",
  "labels": [("Bodywork", "doors, paint"), ("Diagnostics", "diagnostic port"), ("Servicing", "sump, brakes"), ("Breakdown", "towing eye")],
  "pont_alt": "A grey car on a two-post lift in a blue-lit workshop. As you scroll, the lift raises it to show its underside.",
  "pont_mention": "AI-generated illustration",
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
  "ml": "Legal notice (in French)", "cookies": "This site sets no cookies.", "illus_pied": "Fictional example.",
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
  <symbol id="i-cle" viewBox="0 0 48 48"><path d="M30 6a10 10 0 0 0-9 14L7 34a4 4 0 0 0 6 6l14-14a10 10 0 0 0 14-9l-6 6-6-2-2-6z"/></symbol>
  <symbol id="i-diag" viewBox="0 0 48 48"><rect x="6" y="10" width="26" height="20" rx="3"/><path d="M11 24l5-6 4 4 6-8M32 18h6a4 4 0 0 1 4 4v14M38 36h8M19 30v8M13 38h12"/></symbol>
  <symbol id="i-remorque" viewBox="0 0 48 48"><path d="M4 32V20h14l6 8h8V14l12 10M4 32h40M10 32a4 4 0 1 0 8 0M30 32a4 4 0 1 0 8 0M44 24v8"/></symbol>
  <symbol id="i-carrosserie" viewBox="0 0 48 48"><path d="M6 30l4-10c1-3 3-4 6-4h16c3 0 5 1 6 4l4 10v8H6zM6 30h36M12 38v3M36 38v3"/><circle cx="14" cy="32" r="2"/><circle cx="34" cy="32" r="2"/><path d="M20 10l4-4M28 10l-2-5M24 12V4"/></symbol>
  <symbol id="i-maison" viewBox="0 0 48 48"><path d="M6 22L24 8l18 14M10 20v20h28V20M20 40V28h8v12"/></symbol>
  <symbol id="i-route" viewBox="0 0 48 48"><path d="M16 42L22 6M32 42L26 6M24 12v4M24 22v4M24 32v4"/></symbol>
  <symbol id="i-bouclier" viewBox="0 0 48 48"><path d="M24 4l16 6v12c0 10-7 18-16 22C15 40 8 32 8 22V10z"/><path d="M17 24l5 5 9-10"/></symbol>
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
<meta name="theme-color" content="#17202E">
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

# --- Le pont élévateur : une vraie séquence filmée (images fixes) pilotée par le défilement ---
NB_IMAGES = 60

def accueil(p):
    pre = p["prefixe"]
    icones = ["i-cle", "i-diag", "i-remorque", "i-carrosserie"]
    onglets = "".join(
        '<button class="onglet" role="tab" id="o-%d" aria-controls="p-%d" aria-selected="%s" tabindex="%s" type="button">%s</button>'
        % (i, i, "true" if i == 0 else "false", "0" if i == 0 else "-1", t) for i, (t, d) in enumerate(p["services"]))
    panneaux = "".join(
        '<article class="panneau" role="tabpanel" id="p-%d" aria-labelledby="o-%d"%s><svg class="ic-ligne" aria-hidden="true"><use href="#%s"/></svg><h3>%s</h3><p>%s</p>'
        '<div class="actions"><a class="pilule pilule--pleine" href="#demande">%s</a><a class="lien-fantome" href="tel:+33492000000">%s<svg class="ic" aria-hidden="true"><use href="#i-fleche"/></svg></a></div></article>'
        % (i, i, "" if i == 0 else " data-cache", icones[i], t, d, p["cta1"], p["cta2"]) for i, (t, d) in enumerate(p["services"]))
    releve = "".join('<li data-seuil="%s"><span class="pastille"></span><strong>%s</strong><em>%s</em></li>' % (("0.15","0.35","0.55","0.75")[i], l, d) for i, (l, d) in enumerate(p["labels"]))
    chiffres = "".join('<div class="chiffre"><p class="chiffre-valeur">%s</p><p class="chiffre-libelle">%s</p></div>' % (v, l) for v, l in p["chiffres"])
    publics = "".join(
        '<div class="public" data-apparait><svg class="ic-ligne" aria-hidden="true"><use href="#%s"/></svg><h3>%s</h3><p>%s</p>'
        '<div class="actions"><a class="pilule pilule--pleine" href="%s">%s</a><a class="lien-fantome" href="%s">%s<svg class="ic" aria-hidden="true"><use href="#i-fleche"/></svg></a></div></div>'
        % pub for pub in p["publics"])
    opts = "".join(f"<option>{o}</option>" for o in p["f_service_opts"])
    FERME = ' class="ferme"'
    jours = "".join('<tr data-jour="%s"%s><th scope="row">%s</th><td>%s</td></tr>' % (j, FERME if j == "0" else "", n, h) for j, n, h in p["jours"])
    promo = "".join('<li%s><span>%s</span></li>' % (' class="active"' if i == 2 else (' class="faite"' if i < 2 else ""), e) for i, e in enumerate(p["s_etapes"]))
    return f"""{head(p, p['title'], p['desc'], 'index')}
<body>
{SVG_DEFS}
<p class="fictif">{p['fictif']}</p>
{entete(p, 'index')}
<main>
  <section class="ouverture" aria-labelledby="t-titre">
    <p class="puce puce--etat" data-etat-court hidden></p>
    <h1 id="t-titre" class="titre">{p['h1_a']} <span class="signal">{p['h1_b']}</span></h1>
    <p class="chapeau">{p['chapeau']}</p>
    <div class="actions actions--centre">
      <a class="pilule pilule--pleine" href="#demande">{p['cta1']}</a>
      <a class="lien-fantome" href="tel:+33492000000"><svg class="ic" aria-hidden="true"><use href="#i-tel"/></svg>04 92 00 00 00</a>
    </div>
  </section>

  <section class="scene" aria-label="{p['pont_titre']}">
    <div class="scene-collante">
      <figure class="pont">
        <div class="pont-image">
          <img class="pont-affiche" src="{pre}img/pont/fin.webp" width="1280" height="720" alt="{p['pont_alt']}" decoding="async">
          <canvas class="pont-film" width="1280" height="720" data-images="{NB_IMAGES}" data-dossier="{pre}img/pont/" aria-hidden="true"></canvas>
          <span class="pont-mention">{p['pont_mention']}</span>
        </div>
        <figcaption>
          <ol class="releve">{releve}</ol>
        </figcaption>
      </figure>
      <p class="defiler" aria-hidden="true"><span></span>{p['defiler']}</p>
    </div>
  </section>

  <section class="services" id="services" aria-labelledby="t-services">
    <h2 id="t-services" class="titre-section">{p['services_titre']}</h2>
    <div class="onglets" role="tablist" aria-label="{p['services_titre']}">{onglets}</div>
    <div class="panneaux">{panneaux}</div>
  </section>

  <section class="chiffres" aria-label="{p['chiffres_titre']}">{chiffres}</section>

  <section class="publics" id="panne" aria-labelledby="t-publics">
    <h2 id="t-publics" class="titre-section">{p['publics_titre']}</h2>
    <div class="publics-grille">{publics}</div>
    <p class="note">{p['panne_horaires']}</p>
  </section>

  <section class="demande" id="demande" aria-labelledby="t-demande">
    <div class="demande-intro">
      <h2 id="t-demande" class="titre-section">{p['form_titre']}</h2>
      <p>{p['form_intro']}</p>
    </div>
    <form class="formulaire carte" name="demande" method="POST" action="merci.html" data-netlify="true" netlify-honeypot="adresse-web" data-formulaire>
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
      <button class="pilule pilule--pleine" type="submit">{p['f_envoyer']}</button>
      <p class="aide">{p['f_rgpd']} <a href="{pre}confidentialite.html">{p['conf']}</a></p>
    </form>
  </section>

  <section class="suivi-promo" aria-labelledby="t-suivi">
    <div>
      <h2 id="t-suivi" class="titre-section">{p['suivi_titre']}</h2>
      <p>{p['suivi_texte']}</p>
      <a class="lien-fantome" href="suivi.html">{p['suivi_cta']}<svg class="ic" aria-hidden="true"><use href="#i-fleche"/></svg></a>
    </div>
    <div class="carte">
      <p class="exemple">{p['exemple']}</p>
      <ol class="etapes" aria-hidden="true">{promo}</ol>
    </div>
  </section>

  <!-- HORAIRES : modifier aussi contenu/infos.json, le JSON-LD en haut et js/main.js -->
  <section class="infos" id="infos" aria-labelledby="t-infos">
    <div>
      <h2 id="t-infos" class="titre-section">{p['infos_titre']}</h2>
      <p class="adresse">14 avenue d'Embrun<br>05000 Gap</p>
      <p class="etat" data-etat></p>
      <p class="annonce" data-annonce hidden></p>
      <div class="actions">
        <a class="pilule pilule--pleine" href="https://www.google.com/maps/search/?api=1&amp;query={p['maps']}"><svg class="ic" aria-hidden="true"><use href="#i-lieu"/></svg>{p['itineraire']}</a>
        <a class="lien-fantome" href="tel:+33492000000"><svg class="ic" aria-hidden="true"><use href="#i-tel"/></svg>04 92 00 00 00</a>
      </div>
    </div>
    <div class="carte">
      <table class="horaires"><caption>{p['horaires']}</caption><tbody>{jours}</tbody></table>
      <p class="note" data-conges>{p['conges']}</p>
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
