# Faire un site exceptionnel, pas seulement correct

Un site correct ne donne envie à personne. Le but est qu'un client se dise « waouh » dans les deux premières secondes, puis trouve ce qu'il cherche en dix. Ce guide résume ce qui sépare les sites primés (Awwwards, FWA) des sites ordinaires, appliqué à un petit commerce. Lis-le avant de construire, puis repasse-le en revue avant de livrer.

## Les trois piliers (il faut les trois)

Le critère des jurés : un site exceptionnel réunit **une direction artistique précise**, **un mouvement mis en scène** et **la performance**. S'il en manque un, il plafonne. Les jurys Awwwards notent le design (40 %), l'ergonomie (30 %), la créativité (20 %) et le contenu (10 %), sur de vrais appareils.

### 1. La direction artistique : le test de l'image fixe

- **Le test** : fais une capture du premier écran, animations coupées. Si elle n'est pas déjà belle, voulue et reconnaissable entre mille, aucune animation ne la sauvera.
- **Un seul point de vue** : chaque choix (couleur, police, grille, image) sert la même idée, celle qu'impeccable a fixée dans le contrat de direction.
- **Un titre qui dit l'offre**, en très grand : « Votre voiture est entre de bonnes mains », pas « Bienvenue ». Le très grand amplifie aussi un message flou ; écris-le précis.
- **Deux familles de polices au plus**, de préférence variables. Les tailles s'adaptent à l'écran avec `clamp()`.
- **Casser la grille à des moments choisis**, pas partout.

### 2. Les images : le premier levier pour un commerce

- **De vraies images font plus que n'importe quel effet** : le lieu, les produits, les mains au travail, l'équipe (avec leur accord). Pour un commerce, c'est le levier le plus fort.
- **Mets-les en scène** : grands cadrages, recadrages audacieux, une image forte par écran plutôt que dix vignettes. Le texte peut se poser sur l'image, si le contraste reste lisible.
- **Si le commerçant a des photos** : utilise-les, recadre-les et harmonise-les : même température, même traitement.
- **S'il n'en a pas**, propose-lui dans l'ordre :
  1. une séance de photos au téléphone, avec une liste de 10 plans à faire (la vitrine, le produit phare, les mains au travail, l'intérieur en lumière du jour…) ;
  2. un photographe local, une demi-journée ;
  3. des **illustrations générées par IA**, uniquement pour l'ambiance (une matière, une lumière, un geste générique). Elles doivent porter la mention « illustration » et ne jamais faire croire qu'elles montrent le commerce, ses produits réels ou son équipe. Si un outil de génération est connecté (ElevenLabs, par exemple), annonce le coût avant de lancer. Note l'origine de chaque image dans les métadonnées et dans `site/images/LISEZ-MOI.txt`.
- **Un site de démonstration fictif** (comme les exemples du dépôt) peut utiliser des images générées, avec la mention « Exemple fictif · images générées par IA ».

### 3. Le mouvement mis en scène

- **Un ou deux moments forts**, chorégraphiés, qui racontent quelque chose (la voiture qui monte sur le pont, le bon qui se détache), plutôt que des effets partout.
- **Chaque animation explique un changement d'état.** Une animation purement décorative, c'est du bruit.
- **Les durées** : 0,2 à 0,6 s pour les interactions, une courbe qui démarre vite et ralentit (`cubic-bezier(.16,1,.3,1)`), des apparitions en cascade avec 60 à 100 ms d'écart.
- **N'anime que `transform` et `opacity`** (ainsi que `clip-path` et `filter` s'ils restent fluides).
- **Pas d'écran de chargement**, pas de défilement détourné, pas de contenu caché tant qu'une animation n'a pas tourné.
- **Toujours** prévoir un chemin `prefers-reduced-motion` où tout reste visible et compréhensible.

## Les détails qui font « pro »

- Les états : survol, focus clavier visible, appui, chargement, succès, erreur. Chaque action reçoit une réponse visuelle.
- Les surfaces du navigateur aux couleurs du site : sélection de texte, curseur de saisie, barres de défilement, contour de focus, menus déroulants.
- Des chiffres tabulaires pour les horaires et les prix.
- Les transitions entre les pages (`@view-transition`, dans les navigateurs qui le gèrent).
- Une image de partage soignée (1200 × 630) : c'est la première image que verront les amis du client sur WhatsApp.
- Un favicon et une icône pour l'écran d'accueil du téléphone, aux couleurs du site.

## La performance (le pilier qu'on oublie)

- **Fluide (60 images par seconde) sur un téléphone Android moyen.** Teste avec le ralentissement du processeur ×4 des outils du navigateur.
- **Core Web Vitals** : affichage du contenu principal en 2,5 s au plus, réaction aux clics en 200 ms au plus, pas de saut de mise en page (CLS ≤ 0,1).
- **Images en AVIF ou WebP**, aux bonnes dimensions, chargées en différé (`loading="lazy"`) sous le premier écran, avec `width` et `height` renseignés.
- **De la 3D ou du WebGL seulement pour un moment qui le mérite**, jamais pour toute la page. Pour la profondeur, préfère des couches qui bougent à des vitesses différentes (parallaxe légère).

## Les erreurs qui font un site « juste correct »

1. Des emplacements vides « photo à venir » en vitrine : le site paraît inachevé.
2. Une mise en page vue cent fois : grande image, titre, trois cartes identiques.
3. Des animations partout, et aucune qui compte.
4. Du texte gris sur fond gris, ou sur une image chargée.
5. Un site magnifique sur ordinateur et raté sur téléphone. Or c'est sur téléphone que les clients cherchent.
6. Une mise en page générée par IA livrée telle quelle, sans regard critique.
7. Suivre une tendance qui ne correspond pas au commerce.

## Le contrôle avant livraison

- [ ] Le premier écran, figé, est beau et reconnaissable (sur téléphone **et** sur ordinateur).
- [ ] On comprend en deux secondes ce qu'est le commerce et ce qu'on peut faire.
- [ ] Il y a de vraies images, ou des illustrations clairement signalées, et aucun emplacement vide en vitrine.
- [ ] Un ou deux moments animés racontent quelque chose, et le chemin en mouvement réduit fonctionne.
- [ ] Le site reste fluide avec le processeur ralenti ×4.
- [ ] Les états (survol, focus, erreur, succès) sont tous dessinés.
- [ ] L'image de partage et les icônes sont soignées.

Sources (consultées le 2026-11-07) : critères Awwwards (via webdesignawards.io), analyse d'un juré Awwwards (hontran.dev, « Best award-winning websites 2026 »), tendances 2026 d'Envato, MotionKit et We.Inc. Ces sources sont commerciales : on n'en garde que les points qui se recoupent.
