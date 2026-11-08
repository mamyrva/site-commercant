# Journal des versions · Changelog

Le projet évolue à chaque nouveau site testé. · The project evolves with every site it is tested on.

## 0.5.1 · 2026-11-08

- **Guide des finitions** (`finitions.md`) : quand animer et combien de temps, les courbes à utiliser, le bouton qui s'enfonce sous le doigt, ce qu'on peut animer sans ralentir un vieux téléphone, les dix défauts qui trahissent un site web sur un téléphone, et le « pire cas réaliste » des données d'un commerce (nom long, e-mail sans coupure, horaires coupés, prix à quatre chiffres, version anglaise plus longue). Inspiré des principes publiés par Emil Kowalski, réécrit avec nos mots. · Finishing guide: motion timing, mobile tells, worst-case shop data.

## 0.5.0 · 2026-11-07

- **Mouvement naturel : filmer plutôt que dessiner.** Pour un objet réel qui bouge, le skill produit une vraie séquence filmée (image de départ, courte vidéo caméra fixe, 60 images WebP) que le défilement fait avancer sur un `<canvas>`, avec un lissage qui fait démarrer et s'arrêter le mouvement en douceur. Il prévoit une image fixe en mouvement réduit. Ajouté à `excellence.md` et `motion.md`. · Natural motion: film it, don't draw it (scroll-scrubbed image sequence with smoothing).
- **Le garage d'exemple refait** à partir d'une fiche de style « fintech nocturne », traduite en terminal de diagnostic bleu nuit et cyan : une vraie voiture monte sur le pont au défilement, et un relevé des quatre services s'allume.
- **La bijouterie d'exemple refaite** à partir d'une fiche de style « projection privée », traduite en « l'écrin après la fermeture » : noir pur, une seule lampe, titres très fins avec un mot en italique, un court film (« Regarder le film ») et des photos qui s'allument au défilement.

## 0.4.0 · 2026-11-07

- **Partir d'une référence de style** (`reference-style.md`) : trouver le `DESIGN.md` d'un site que le commerçant aime (par exemple sur styles.refero.design), puis le traduire dans l'univers du commerce sans jamais le cloner. Méthode tirée de la vidéo « Site Web à +10 000 € avec Claude Code » (Web Marketing Tuto). · Start from a reference style sheet.
- **La boulangerie d'exemple refaite** à partir d'une fiche de style « affiche d'épicerie », traduite en « or de croûte sur brun de four » : titres géants, produits posés à même le fond, état « OUVERT / FERMÉ » en très grand.
- Option « spectaculaire » : un effet interactif en haut de page qui raconte le métier.
- Mise en ligne faite par Claude avec Netlify en ligne de commande.

## 0.3.0 · 2026-11-07

- **Guide « site exceptionnel »** (`excellence.md`) : le test de l'image fixe, les images comme premier levier, un mouvement mis en scène, la performance, et une liste de contrôle avant livraison. Il s'appuie sur les critères des jurys Awwwards et sur les tendances 2026. · "Exceptional site" guide.
- L'entretien demande désormais au commerçant quelles photos il a, et le skill propose une séance photo au téléphone, un photographe ou des illustrations générées par IA, signalées comme telles.
- **Démos en ligne** sur GitHub Pages, avec une page de présentation en FR et en EN. · Live demos.
- Les trois exemples ont maintenant de vraies images : des illustrations générées par IA, signalées comme telles. Maison Vauclair a une photo plein écran en ouverture, Au Pain Doré un tirage du fournil sur la couverture du carnet.

## 0.2.0 · 2026-11-07

- **Entretien complet** avec le commerçant : la vision du site, les sites aimés, le niveau d'animation, la vidéo, l'idée unique, les fonctions et les questions fréquentes (`entretien.md`). · Full owner interview.
- **Sites dynamiques** : réservation, devis, galerie, actualités, contenu modifiable, suivi de commande ou de réparation, plusieurs langues (`fonctionnalites.md`). · Dynamic features.
- **Motion design** : un logo animé en SVG, et des vidéos avec HyperFrames (`motion.md`).
- **Référencement Google mis à jour pour 2026** : les critères officiels du classement local, la fiche Google Business Profile, les Core Web Vitals, les réponses générées par IA, le bloc questions fréquentes, et une checklist après la mise en ligne. · Google SEO refresh.
- Nouveau métier : bijouterie, joaillerie, horlogerie. Leçon tirée du test : pour le luxe, proposer d'abord la voie classique.
- Le vérificateur contrôle aussi les vidéos, les formulaires, les iframes et les pages en plusieurs langues.
- Trois exemples fictifs : boulangerie, bijouterie, garage.

## 0.1.0 · 2026-11-07

- Première version : questionnaire, pages par métier, obligations légales françaises, référencement local, déploiement gratuit et script de vérification. · First release.
