# Vidéos en motion design

Une courte vidéo animée donne au site une vraie personnalité : le logo qui se dessine, les produits qui apparaissent, l'ambiance du lieu. Ce fichier explique quand en faire une, avec quel outil, et comment l'intégrer sans alourdir le site.

## Avec quel outil

**Un logo animé destiné au site** se fait directement en SVG et en CSS dans la page, même si HyperFrames est installé. Le résultat est net à toutes les tailles, pèse quelques octets, et l'animation est rejouée à chaque visite. Un fichier vidéo pour un logo serait plus lourd et plus flou. Testé le 2026-11-07 avec le Garage Delorme : le bras du pont monte, puis le nom apparaît. HyperFrames sert pour les **fichiers vidéo** : présentation, ambiance, réseaux sociaux.

1. **Si les skills HyperFrames sont installés** (le skill `hyperframes` apparaît dans la liste des skills) : charge `hyperframes`. C'est le point d'entrée obligatoire. Il oriente vers le bon flux de travail :
   - un **logo animé** ou une animation typographique courte (moins de 10 s, sans voix) : `motion-graphics` ;
   - une **vidéo de présentation** du commerce ou de ses produits : `product-launch-video`, ou `general-video` pour un format libre ;
   - une **vidéo pour les réseaux** (format vertical 9:16) : demande-la en plus. Elle sert sur Instagram et TikTok, pas sur le site.
   Transmets-lui le `DESIGN.md` du site (couleurs, polices), pour que la vidéo appartienne au même univers.
2. **Sinon** : dis-le en une phrase, puis réalise l'animation directement dans la page (SVG et CSS animés : logo qui se trace, mots qui apparaissent). C'est plus léger, et souvent suffisant.

## Ce que la vidéo peut montrer

- Uniquement de la typographie, des formes, des couleurs et des illustrations, ou **les vraies photos et vidéos du commerçant**.
- Jamais de fausses images présentées comme celles du commerce, ni de chiffres ou de récompenses inventés.
- Si le commerçant n'a pas encore d'images, la vidéo reste graphique : le nom, le métier, le geste dessiné, l'adresse.

## Intégration dans le site

- **Formats** : MP4 (H.264) et WebM, avec une image d'attente (`poster`) en JPEG ou WebP.
- **Poids** :
  - moins de **3 Mo** pour une vidéo en boucle en haut de page, de 6 à 12 secondes ;
  - une version 720p pour les téléphones, chargée avec `<source media="(max-width: 700px)">` ou un petit script.
- **Balise** : `<video autoplay muted loop playsinline preload="metadata" poster="…">`. Une vidéo sans son est obligatoire pour que la lecture automatique fonctionne.
- **Accessibilité** :
  - un bouton visible « Mettre en pause » dès que la vidéo dure plus de 5 secondes (règle WCAG 2.2.2) ;
  - avec `prefers-reduced-motion`, la vidéo ne se lance pas et seule l'image d'attente s'affiche ;
  - le texte important n'est jamais seulement dans la vidéo : il est aussi écrit dans la page.
- **Hébergement** : les fichiers vidéo sont dans `site/videos/`, pas sur YouTube ni Vimeo, dont l'intégration dépose des cookies.
- **Origine** : note dans `site/videos/LISEZ-MOI.txt` comment chaque vidéo a été faite (outil, date, sources des images).

## À la livraison

Donne au commerçant :

- le fichier vidéo du site ;
- la version pour les réseaux, si elle a été faite ;
- une phrase pour expliquer comment remplacer la vidéo plus tard : même nom de fichier, même durée conseillée.
