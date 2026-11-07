#!/usr/bin/env python3
"""Vérifie un site vitrine de commerçant : bases techniques, SEO local, obligations légales.

Usage : python3 verifier.py <dossier-du-commerce | dossier-site>
Sortie : liste ERREUR / ATTENTION / À COMPLÉTER, code de retour 1 s'il reste des erreurs.
Uniquement la bibliothèque standard (Python 3.8+).
"""
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

PLACEHOLDER = re.compile(r"\[À COMPLÉTER[^\]]*\]")
LOREM = re.compile(r"lorem ipsum|dolor sit amet", re.I)
TRACKERS = re.compile(
    r"googletagmanager|google-analytics|gtag\(|connect\.facebook\.net|fbq\(|hotjar|"
    r"fonts\.googleapis|fonts\.gstatic|youtube\.com/embed|google\.com/maps/embed",
    re.I,
)
SIRET = re.compile(r"\b\d{3}\s?\d{3}\s?\d{3}\s?\d{5}\b")


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.lang = None
        self.title = ""
        self._in_title = False
        self.meta = {}
        self.links = []
        self.imgs = []
        self.videos = []
        self.iframes = []
        self.forms = []
        self.h1 = 0
        self.jsonld = []
        self._in_jsonld = False
        self._buf = ""
        self.text = []
        self._skip = 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "html":
            self.lang = a.get("lang")
        elif tag == "title":
            self._in_title = True
        elif tag == "meta":
            key = a.get("name") or a.get("property")
            if key:
                self.meta[key.lower()] = a.get("content", "")
            if "charset" in a:
                self.meta["charset"] = a["charset"]
        elif tag == "a" and a.get("href"):
            self.links.append(a["href"])
        elif tag == "link" and a.get("rel"):
            self.links.append(("rel:" + a["rel"], a.get("href", "")))
        elif tag == "img":
            self.imgs.append(a)
        elif tag == "video":
            self.videos.append(a)
        elif tag == "iframe":
            self.iframes.append(a)
        elif tag == "form":
            self.forms.append(a)
        elif tag == "h1":
            self.h1 += 1
        elif tag == "script" and a.get("type") == "application/ld+json":
            self._in_jsonld = True
            self._buf = ""
        if tag in ("script", "style"):
            self._skip += 1

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
        elif tag == "script" and self._in_jsonld:
            self._in_jsonld = False
            self.jsonld.append(self._buf)
        if tag in ("script", "style") and self._skip:
            self._skip -= 1

    def handle_data(self, data):
        if self._in_title:
            self.title += data
        if self._in_jsonld:
            self._buf += data
        elif not self._skip:
            self.text.append(data)


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    root = Path(sys.argv[1]).expanduser().resolve()
    site = root / "site" if (root / "site").is_dir() else root
    if not site.is_dir():
        print(f"ERREUR : dossier introuvable : {site}")
        return 2

    errors, warns, todo = [], [], []

    def err(page, msg):
        errors.append(f"{page} : {msg}")

    def warn(page, msg):
        warns.append(f"{page} : {msg}")

    pages = sorted(site.rglob("*.html"))
    names = {p.relative_to(site).as_posix() for p in pages}
    if "index.html" not in names:
        err("site", "pas de index.html à la racine du dossier publié")
    for req in ("mentions-legales.html", "confidentialite.html"):
        if req not in names:
            err("site", f"page obligatoire manquante : {req}")
    for req in ("robots.txt", "sitemap.xml"):
        if not (site / req).exists():
            warn("site", f"{req} manquant")
    if not any((site / f).exists() for f in ("favicon.svg", "favicon.ico", "favicon.png")):
        warn("site", "pas de favicon")
    for f in ("PRODUCT.md", "DESIGN.md"):
        if (site / f).exists():
            warn("site", f"{f} est dans le dossier publié : il serait mis en ligne")

    titles = {}
    has_jsonld_business = False
    for p in pages:
        rel = p.relative_to(site).as_posix()
        raw = p.read_text(encoding="utf-8", errors="replace")
        pg = Page()
        pg.feed(raw)
        text = " ".join(pg.text)

        if not pg.lang:
            err(rel, "attribut lang manquant sur <html> (fr, en…)")
        elif "/" not in rel and not pg.lang.lower().startswith("fr"):
            warn(rel, f'page principale en lang="{pg.lang}" : le site français devrait être en lang="fr"')
        if "charset" not in pg.meta:
            err(rel, "<meta charset> manquant")
        if "width=device-width" not in pg.meta.get("viewport", ""):
            err(rel, "meta viewport manquante : le site s'affichera mal sur téléphone")
        t = pg.title.strip()
        if not t:
            err(rel, "<title> vide")
        else:
            titles.setdefault(t, []).append(rel)
            if len(t) > 65:
                warn(rel, f"title long ({len(t)} caractères, viser 50–60)")
        d = pg.meta.get("description", "").strip()
        if not d:
            err(rel, "meta description manquante")
        elif not PLACEHOLDER.search(d) and not 70 <= len(d) <= 170:
            warn(rel, f"meta description de {len(d)} caractères (viser 140–160)")
        if pg.h1 != 1:
            err(rel, f"{pg.h1} balise(s) <h1> (il en faut exactement une)")
        for img in pg.imgs:
            if "alt" not in img:
                err(rel, f"image sans attribut alt : {img.get('src', '?')}")
            src = img.get("src", "")
            if src and not src.startswith(("http", "data:")):
                if not (p.parent / src).resolve().exists():
                    err(rel, f"image introuvable : {src}")
        for link in pg.links:
            href = link[1] if isinstance(link, tuple) else link
            if href.startswith("/") and not href.startswith("//"):
                warn(rel, f"lien absolu {href} : ne marchera pas en double-clic ni sur GitHub Pages en sous-dossier")
            elif href and not re.match(r"^(https?:|mailto:|tel:|#|//|data:|\[)", href):
                target = (p.parent / href.split("#")[0].split("?")[0]).resolve()
                if href.split("#")[0] and not target.exists():
                    err(rel, f"lien cassé : {href}")
        hrefs = [l for l in pg.links if isinstance(l, str)]
        if "mentions-legales.html" not in " ".join(hrefs) and rel != "mentions-legales.html":
            err(rel, "pas de lien vers les mentions légales (pied de page)")
        if rel == "index.html" and not any(h.startswith("tel:") for h in hrefs):
            warn(rel, "pas de numéro de téléphone cliquable (tel:)")
        for v in pg.videos:
            if "autoplay" in v:
                if "muted" not in v:
                    err(rel, "vidéo en lecture automatique sans « muted » : elle ne démarrera pas sur téléphone")
                if "playsinline" not in v:
                    warn(rel, "vidéo en lecture automatique sans « playsinline » (iPhone)")
                if "data-pause" not in raw and "pause" not in raw.lower():
                    warn(rel, "vidéo en lecture automatique sans bouton pause visible (WCAG 2.2.2)")
            if "poster" not in v:
                warn(rel, "vidéo sans image d'attente (poster)")
        for fr in pg.iframes:
            src = fr.get("src", "") or fr.get("data-src", "")
            if src.startswith("http") and "maps/embed" not in src:
                warn(rel, f"iframe externe ({src[:60]}) : dépose souvent des cookies, à charger après consentement (voir legal-fr.md)")
        if pg.forms and "confidentialite.html" not in raw:
            err(rel, "formulaire sans lien vers la page de confidentialité")
        if TRACKERS.search(raw):
            err(rel, "ressource tierce qui dépose des cookies ou transfère l'IP (Analytics, Google Fonts, iframe YouTube/Maps…) : voir legal-fr.md")
        if LOREM.search(raw):
            err(rel, "texte « lorem ipsum » oublié")
        for block in pg.jsonld:
            try:
                data = json.loads(block)
            except json.JSONDecodeError as e:
                err(rel, f"JSON-LD invalide : {e}")
                continue
            items = data if isinstance(data, list) else [data]
            for it in items:
                if not isinstance(it, dict):
                    continue
                if it.get("@type") and it.get("address"):
                    has_jsonld_business = True
                if "aggregateRating" in it or "review" in it:
                    warn(rel, "aggregateRating/review dans le JSON-LD : seulement si ce sont de vrais avis vérifiables")
                if PLACEHOLDER.search(json.dumps(it, ensure_ascii=False)):
                    warn(rel, "repère [À COMPLÉTER] dans le JSON-LD : retirer le champ tant qu'il est inconnu")
        if rel == "mentions-legales.html":
            low = text.lower()
            if not (SIRET.search(text) or "siret" in low and PLACEHOLDER.search(text)):
                err(rel, "ni numéro SIRET ni repère [À COMPLÉTER] pour le SIRET")
            for word in ("hébergeur", "directeur de la publication"):
                if word not in low and word.replace("é", "e") not in low:
                    err(rel, f"rubrique manquante : {word}")
        for m in PLACEHOLDER.findall(raw):
            todo.append(f"{rel} : {m}")

    for extra in ("robots.txt", "sitemap.xml"):
        f = site / extra
        if f.exists():
            for m in PLACEHOLDER.findall(f.read_text(encoding="utf-8", errors="replace")):
                todo.append(f"{extra} : {m}")

    todo = list(dict.fromkeys(todo))
    if pages and not has_jsonld_business:
        warn("index.html", "pas de données structurées LocalBusiness (avec address)")
    for t, ps in titles.items():
        if len(ps) > 1:
            warn(", ".join(ps), f"même <title> sur plusieurs pages : « {t} »")

    # Poids
    total = sum(f.stat().st_size for f in site.rglob("*") if f.is_file())
    for f in site.rglob("*"):
        if f.suffix.lower() in (".jpg", ".jpeg", ".png", ".webp", ".avif") and f.stat().st_size > 400_000:
            warn(f.relative_to(site).as_posix(), f"image lourde ({f.stat().st_size // 1024} Ko) : compresser ou redimensionner")

    print(f"Site vérifié : {site}  ({len(pages)} pages, {total // 1024} Ko au total)\n")
    for label, items in (("ERREUR", errors), ("ATTENTION", warns)):
        for i in items:
            print(f"{label:10} {i}")
    if todo:
        print(f"\nÀ COMPLÉTER ({len(todo)}) :")
        for i in todo:
            print(f"  - {i}")
    print(f"\nBilan : {len(errors)} erreur(s), {len(warns)} avertissement(s), {len(todo)} information(s) à compléter.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
