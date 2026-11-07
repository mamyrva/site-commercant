# Structure technique du site

## Arborescence

```
nom-du-commerce/
├── PRODUCT.md              ← fiche produit pour impeccable (pas publiée en ligne : voir deploiement.md)
├── DESIGN.md               ← système visuel écrit par impeccable
└── site/                   ← le seul dossier mis en ligne
    ├── index.html
    ├── mentions-legales.html
    ├── confidentialite.html
    ├── [carte|tarifs|realisations].html   ← seulement si utile
    ├── css/style.css
    ├── js/main.js          ← interactions, animations, fonctions
    ├── contenu/            ← facultatif : actualites.json, carte.json, galerie.json (contenu modifiable)
    ├── videos/             ← facultatif : vidéo motion design (MP4 + WebM + poster) et LISEZ-MOI.txt
    ├── fonts/              ← polices en .woff2, hébergées ici
    ├── images/
    ├── favicon.svg
    ├── apple-touch-icon.png
    ├── robots.txt
    └── sitemap.xml
```

Séparer `site/` du reste évite de publier les fichiers de travail.

## Règles techniques

- **HTML et CSS statiques**, sans framework, sans étape de compilation. Le commerçant ou un proche doit pouvoir corriger un horaire dans `index.html` avec un simple éditeur de texte. Ajoute un commentaire HTML `<!-- HORAIRES : modifier ici -->` aux endroits qui changent souvent.
- **Une seule feuille de style.** Les variables CSS (`:root`) portent couleurs, polices et espacements, comme défini dans DESIGN.md.
- **JavaScript au service du site** : menu mobile, « ouvert maintenant », animations, galerie, contenus chargés depuis `contenu/*.json`, formulaires. Le site doit rester lisible et utilisable sans JavaScript : les informations essentielles (horaires, adresse, téléphone, offre) sont toujours écrites dans le HTML.
- **Aucune ressource externe obligatoire** : polices, icônes et scripts sont tous dans le dossier (raisons : vitesse, cookies, RGPD). Les seules exceptions sont des liens sortants (Maps, réseaux sociaux, réservation).
- **Images** : en WebP ou AVIF quand c'est possible, en JPEG sinon ; 1600 px de large au maximum ; `width`/`height` renseignés ; `loading="lazy"` sauf pour l'image du haut de page. Sur macOS, `sips -Z 1600 photo.jpg` les redimensionne.
- **Poids cible** : moins de 1 Mo pour la page d'accueil, images comprises, sans compter la vidéo (3 Mo au plus, voir `motion.md`).
- **Contenus en JSON** : un navigateur refuse de charger `contenu/*.json` quand le site est ouvert par double-clic (`file://`). Le HTML garde donc une version de secours écrite en dur. Pour tester en local, lance `python3 -m http.server` depuis `site/`.
- **Liens** : chemins relatifs (`css/style.css`, pas `/css/style.css`) pour que le site s'ouvre aussi par double-clic.
- **Téléphone** : `<a href="tel:+33XXXXXXXXX">` ; **e-mail** : `<a href="mailto:…">`.
- **Formulaire de contact** (si demandé) : sur Netlify, ajouter l'attribut `data-netlify="true"`. Sinon, Formspree (formule gratuite). Sans formulaire, un lien e-mail et le téléphone suffisent souvent, et c'est encore plus simple.

## Design (si impeccable n'est pas disponible)

- Respecte les mots du commerçant sur le style. Traduis-les en choix précis : 2 polices au maximum, une palette de 3 à 5 couleurs avec un contraste AA, des espacements réguliers.
- Évite le « site généré » : pas de dégradé violet par défaut, pas de grilles de trois cartes identiques avec une icône, pas de « Bienvenue sur notre site ».
- Le haut de page dit, sur un téléphone et sans défiler : qui, quoi, où, et l'action principale.
- **Sans photos** : un site typographique soigné, avec des couleurs, des textures CSS et éventuellement des illustrations SVG simples, vaut mieux que des photos de banque d'images. Prévois des emplacements `[À COMPLÉTER : photo de la vitrine]` bien cadrés, que le commerçant remplira.
