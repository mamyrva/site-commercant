---
name: Maison Vauclair
description: Joaillier et horloger à Bordeaux. Une maison moderne sur fond blanc, une seule couleur signature, le vert jade.
colors:
  fond: "#FFFFFF"
  fond-doux: "#F5F5F3"
  encre: "#141414"
  encre-douce: "#55524C"
  filet: "#E3E2DE"
  photo: "#EFEEEB"
  jade: "#134E46"
typography:
  display:
    fontFamily: "Italiana, Didot, Bodoni 72, serif"
    fontSize: "clamp(2.3rem, 1.4rem + 4.2vw, 5.25rem)"
    fontWeight: 400
    lineHeight: 1.04
    letterSpacing: "0.005em"
  headline:
    fontFamily: "Italiana, Didot, Bodoni 72, serif"
    fontSize: "clamp(2.2rem, 1.4rem + 3.4vw, 4.25rem)"
    fontWeight: 400
    lineHeight: 1.06
  title:
    fontFamily: "Italiana, Didot, Bodoni 72, serif"
    fontSize: "clamp(1.75rem, 1.3rem + 1.6vw, 2.5rem)"
    fontWeight: 400
    lineHeight: 1.2
  logotype:
    fontFamily: "Italiana, Didot, Bodoni 72, serif"
    fontSize: "clamp(1.5rem, 1.1rem + 1.6vw, 2.25rem)"
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: "0.32em"
  body:
    fontFamily: "Jost, Futura, Avenir Next, sans-serif"
    fontSize: "1.0625rem"
    fontWeight: 300
    lineHeight: 1.65
  body-small:
    fontFamily: "Jost, Futura, Avenir Next, sans-serif"
    fontSize: "0.9375rem"
    fontWeight: 300
    lineHeight: 1.65
  label:
    fontFamily: "Jost, Futura, Avenir Next, sans-serif"
    fontSize: "0.75rem"
    fontWeight: 500
    lineHeight: 1.65
    letterSpacing: "0.18em"
rounded:
  none: "0px"
spacing:
  marge: "clamp(1.25rem, 5vw, 5rem)"
  section: "clamp(5rem, 10vw, 9rem)"
components:
  button-primary:
    backgroundColor: "{colors.jade}"
    textColor: "{colors.fond}"
    typography: "{typography.label}"
    rounded: "{rounded.none}"
    padding: "0.8rem 1.75rem"
    height: "3.25rem"
  button-primary-hover:
    backgroundColor: "#0C3832"
    textColor: "{colors.fond}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.encre}"
    typography: "{typography.label}"
    rounded: "{rounded.none}"
    padding: "0.8rem 1.75rem"
    height: "3.25rem"
  button-secondary-hover:
    backgroundColor: "{colors.encre}"
    textColor: "{colors.fond}"
  photo-placeholder:
    backgroundColor: "{colors.photo}"
    textColor: "#5F594F"
    rounded: "{rounded.none}"
  photo-placeholder-sombre:
    backgroundColor: "#0F3F39"
    textColor: "#C4D6D1"
    rounded: "{rounded.none}"
  tile:
    backgroundColor: "{colors.fond}"
    textColor: "{colors.encre}"
    rounded: "{rounded.none}"
  tile-hover:
    backgroundColor: "#E6EEEB"
    textColor: "{colors.jade}"
  jade-band:
    backgroundColor: "{colors.jade}"
    textColor: "{colors.fond}"
    padding: "{spacing.section} {spacing.marge}"
  header:
    backgroundColor: "{colors.fond}"
    textColor: "{colors.encre}"
    padding: "1.5rem {spacing.marge} 0"
  footer:
    backgroundColor: "{colors.fond}"
    textColor: "{colors.encre-douce}"
    padding: "4rem {spacing.marge} 3rem"
  hours-table:
    backgroundColor: "{colors.fond-doux}"
    textColor: "{colors.encre}"
    typography: "{typography.body-small}"
---

# Design System: Maison Vauclair

## Overview

**Creative North Star: "La vitrine claire"**

Maison Vauclair joue franchement la catégorie de la grande joaillerie moderne : beaucoup de blanc, de la lumière, une typographie très fine, et une seule couleur signature, le vert jade. Rien n'est ironique ni décalé : le visiteur doit reconnaître en une seconde une maison sérieuse, puis trouver l'adresse et les horaires. Le niveau de finition vise celui des grandes maisons (Tiffany, Messika servent de référence de finition seulement : on ne reprend ni leurs couleurs, ni leurs noms, ni leur identité).

La page respire. Les sections sont séparées par de grands espaces verticaux et par des filets d'un pixel, jamais par des ombres ou des cadres arrondis. Les titres sont en Italiana, une capitale de vitrine très déliée ; tout le reste (texte, boutons, menus, libellés) est en Jost, avec des libellés en petites capitales très espacées. Le jade apparaît en aplat pleine largeur une fois (la bande de l'atelier) et sur l'action principale ; ailleurs il ne sert qu'aux états (survol, jour du jour, « Ouvert »).

Tant que le commerçant n'a pas fourni ses photos, chaque emplacement photo est un aplat gris clair avec un dessin d'atelier au trait et la mention « Photo à venir ». Ces dessins sont provisoires par nature : ils tiennent la place de la photo, ils ne la remplacent pas.

**Key Characteristics:**
- Fond blanc pur, encre presque noire, filets fins couleur pierre claire.
- Une seule couleur signature, le vert jade, en aplat et sur l'action principale.
- Titres Italiana fins ; texte et libellés Jost, petites capitales espacées.
- Angles droits partout, aucune ombre, profondeur par aplats et filets.
- Emplacements photo dessinés au trait, prêts à recevoir les vraies photos.
- Un seul mouvement : le grand visuel du haut se dévoile au chargement.

## Colors

Une palette de papier blanc et d'encre, réchauffée par des gris pierre, avec une seule couleur vive : le vert jade.

### Primary
- **Vert jade** (jade) : la couleur signature. Fond de la bande « L'atelier », fond du bouton principal (« Venir à la Maison », « Itinéraire »), soulignement et couleur des liens au survol, jour courant dans le tableau des horaires, mot « Ouvert »/« Fermé », sélection de texte et barre de défilement. Au survol, le bouton plein fonce en jade profond (#0C3832).

### Neutral
- **Blanc vitrine** (fond) : fond de page, de l'en-tête et du pied de page ; texte sur le jade.
- **Blanc cassé** (fond-doux) : fond de la seule section « Venir à la Maison », pour la poser comme un comptoir à part.
- **Encre** (encre) : titres, texte principal, contour du bouton secondaire, contour du focus clavier.
- **Encre douce** (encre-douce) : texte courant secondaire (chapeaux, descriptions des tuiles, adresse dans l'en-tête, pied de page).
- **Filet** (filet) : tous les traits d'un pixel qui séparent (bas de l'en-tête, haut du pied de page, haut de la section visite, haut du tableau des horaires).
- **Gris photo** (photo) : fond des emplacements photo en attente.

### Named Rules
**La règle de la voix unique.** Le jade est la seule couleur vive du site. Une seule bande pleine largeur en jade par page ; sinon il se limite à l'action principale et aux états. On n'ajoute jamais une deuxième couleur d'accent.

**La règle des teintes dérivées.** Les quelques tons hors palette (jade profond #0C3832 au survol, fond sombre des photos sur jade #0F3F39, textes clairs sur jade #E3ECE9 et #D6E4E0) sont des déclinaisons du jade ou de la pierre. Toute nouvelle teinte doit en être une aussi.

## Typography

**Display Font:** Italiana (avec Didot, Bodoni 72, serif)
**Body Font:** Jost (avec Futura, Avenir Next, sans-serif)

**Character:** Italiana donne la voix de vitrine, fine et haute, comme une enseigne gravée ; Jost, géométrique et calme, porte tout ce qui doit se lire vite. Les deux polices sont hébergées avec le site (aucune ressource externe).

### Hierarchy
- **Display** (Italiana 400, de 2,3 à 5,25 rem, interligne 1,04) : le seul grand titre d'accueil, « Joaillier et horloger à Bordeaux », centré, équilibré.
- **Headline** (Italiana 400, de 2,2 à 4,25 rem, interligne 1,06) : titres de section (« Nos créations », « L'atelier est dans la boutique », « Montres », « Venir à la Maison ») et titre des pages légales.
- **Promesse** (Italiana 400, de 1,9 à 3,4 rem, interligne 1,12) : une phrase citée en grand dans la bande jade, une seule par page.
- **Title** (Italiana 400, de 1,75 à 2,5 rem, interligne 1,2) : l'adresse en grand dans la section visite.
- **Logotype** (Italiana 400, capitales, espacement 0,32 em) : « MAISON VAUCLAIR », centré dans l'en-tête, plus petit (1,5 rem) dans le pied de page. Il n'y a pas de logo dessiné : le logotype typographique en tient lieu.
- **Body** (Jost 300, 1,0625 rem, interligne 1,65) : chapeaux et paragraphes, 36 à 42 caractères de large au plus dans les blocs de section, 68 caractères sur les pages légales.
- **Body small** (Jost 300, 0,9375 rem) : descriptions des tuiles, services, horaires.
- **Label** (Jost 500, 0,75 rem, espacement 0,18 em, capitales) : menu, boutons (0,2 em), titres des tuiles et des services (0,8125 rem, 0,16 em), légende du tableau des horaires, liens du pied de page.

### Named Rules
**La règle des deux voix.** Italiana pour ce qui se regarde (titres, logotype, promesse), Jost pour ce qui se lit ou se clique. Jamais Italiana dans un bouton, un menu ou un paragraphe ; jamais Jost en grand titre.

**La règle du poids léger.** Le texte courant est en Jost 300 ; le 500 est réservé aux libellés en capitales et au jour courant. Pas de gras dans les titres : Italiana n'existe qu'en 400.

## Layout

Deux mesures pilotent tout l'espace : la **marge** (marge latérale de toutes les sections, de 1,25 rem sur téléphone à 5 rem sur grand écran) et la **section** (espace vertical entre sections, de 5 à 9 rem). Pas de conteneur centré à largeur fixe : les sections vont d'un bord à l'autre, le texte est tenu par sa longueur de ligne.

Ordre de la page d'accueil : en-tête, grand visuel pleine largeur (16/7 sur grand écran, 4/3 sur téléphone, limité à environ un tiers de la hauteur d'écran) puis titre, chapeau et deux boutons centrés dessous ; grille des créations ; bande jade de l'atelier ; montres ; venir à la Maison ; pied de page.

- **Grille des créations** : deux colonnes sur téléphone, quatre au-delà de 56 rem.
- **Sections en deux colonnes** (atelier, montres, visite) : empilées sur téléphone ; côte à côte au-delà de 56 rem, avec un écart de 3 à 8 rem et des proportions inégales (1,4/1 pour les montres, 1,2/1 pour la visite, moitié-moitié pour l'atelier).
- **Points de rupture** : 56 rem (passage en grand écran) et 26 rem (très petits téléphones : menu et titres des tuiles se resserrent, titres des tuiles en bas de casse).

## Elevation & Depth

Le système est entièrement plat : aucune ombre portée, aucun flou. La profondeur vient des aplats (blanc, blanc cassé, gris photo, jade) et des filets d'un pixel. Le seul relief est temporel : le grand visuel du haut se dévoile de haut en bas au chargement (1,6 s, découpe progressive), puis tout reste immobile. Ce dévoilement est supprimé quand le visiteur a demandé moins d'animations.

### Named Rules
**La règle du papier à plat.** Aucune ombre, nulle part. Pour séparer, on change d'aplat ou on trace un filet.

**La règle du mouvement unique.** Un seul moment animé par page, le dévoilement du visuel d'ouverture. Les survols sont de simples fondus (300 à 400 ms) ; rien ne bouge au défilement.

## Shapes

Angles droits partout (0 px) : boutons, emplacements photo, tuiles, bandes. Les seules formes rondes sont celles des dessins et des petites icônes au trait. Les traits sont fins et réguliers : filets d'un pixel, contour de bouton d'un pixel, focus clavier d'un pixel décalé de 4 px, icônes tracées à 1,4, dessins à 1,1.

Les emplacements photo ont des proportions fixes, pour que la photo du commerçant tombe juste : carré pour les tuiles, portrait 4/5 pour l'atelier, paysage 3/2 pour les montres, 16/7 (4/3 sur téléphone) pour l'ouverture.

## Components

### Buttons
Rectangles nets, sobres, comme une étiquette de vitrine.
- **Shape :** angles droits (0 px), hauteur minimale 3,25 rem, largeur minimale 13 rem (10,5 rem dans l'ouverture), libellé Jost 500 en capitales très espacées (0,2 em).
- **Primary (plein) :** aplat jade, texte blanc. Réservé à l'action principale : venir en boutique, itinéraire. Un seul par groupe d'actions.
- **Secondary (filet) :** fond transparent, contour encre d'un pixel, texte encre. Pour l'action secondaire : appeler.
- **Hover / Focus :** le bouton plein fonce en jade profond ; le bouton filet se remplit d'encre et son texte passe en blanc ; fondu de 300 ms. Focus clavier : contour d'un pixel décalé de 4 px.
- **Icône :** facultative, au trait, à gauche du libellé (itinéraire, téléphone).

### Navigation (en-tête)
- **Style :** fond blanc, filet en bas. Sur grand écran, trois colonnes : adresse à gauche, logotype centré, état ouvert/fermé et lien « Itinéraire » à droite ; le menu centré dessous. Sur téléphone, logotype puis menu, l'état passe en dessous et l'adresse est masquée.
- **Menu :** libellés Jost 500, 0,75 rem, capitales espacées ; au survol, texte et soulignement d'un pixel en jade.
- **Pages légales :** même en-tête, réduit au logotype et à un lien « Accueil ».

### Tuiles (créations)
- **Structure :** un emplacement photo carré, un titre en libellé capitales sous la photo, une phrase courte en encre douce. Toute la tuile est un lien.
- **Signature :** un court trait jade (1,5 rem) sous le titre, qui s'allonge à 3,5 rem au survol ; la photo se teinte légèrement de jade (#E6EEEB) et le titre passe en jade.

### Emplacements photo (dessins au trait)
Le composant qui permet au site d'être élégant sans photos.
- **Fond :** gris photo ; sur la bande jade, version sombre (#0F3F39) avec un trait vert clair (#8DB3AB) et une mention claire (#C4D6D1).
- **Dessin :** un dessin d'atelier au trait (bague solitaire, bague, alliances, collier et boucles, montre, établi avec triboulet et loupe), sans remplissage, trait #857E71 de 1,1, bouts arrondis, centré.
- **Mention :** « Photo à venir » (ou « Photo de l'atelier à venir ») en libellé 0,6875 rem, capitales, espacement 0,2 em, centrée en bas. Les tuiles de la grille n'ont pas de mention.
- **Accessibilité :** chaque emplacement est décrit comme « Emplacement photo : … » pour les lecteurs d'écran.
- **Remplacement :** quand le commerçant fournit ses photos, la photo prend tout l'emplacement aux mêmes proportions ; le dessin et la mention disparaissent. On ne remplace jamais un dessin par une photo de banque d'images.

### Bande jade (atelier)
- **Style :** aplat jade pleine largeur, espacement de section, texte blanc ; paragraphes en vert très clair (#E3ECE9), descriptions en #D6E4E0.
- **Contenu :** titre de section, phrase d'introduction, promesse en Italiana, liste de services séparés par des filets blancs à 25 % d'opacité (libellé en capitales + description), et un emplacement photo sombre en portrait.
- **Focus :** le contour du focus clavier passe en blanc sur le jade.

### Tableau des horaires
- **Style :** pleine largeur de sa colonne, sans fond propre (il repose sur le blanc cassé de la section visite), chiffres à chasse fixe, jours à gauche, heures alignées à droite, une ligne par jour séparée par un filet. (Le site livré trace les lignes intérieures en #CFDAD6, un gris-vert isolé, et la première en filet : c'est un écart, la règle reste le filet.)
- **Légende :** « Horaires » en libellé capitales encre douce, au-dessus.
- **États :** jours fermés en gris pierre (#5F594F) ; le jour courant passe en Jost 500 jade (ajouté par le script). Au-dessus du tableau, une ligne d'état indique « Ouvert aujourd'hui jusqu'à … » ou « Fermé … Réouverture … », le mot clé en jade.

### Pied de page
- **Style :** fond blanc, filet en haut, tout centré : logotype réduit, adresse et téléphone, liens en capitales espacées (Instagram avec son icône au trait, mentions légales, confidentialité), puis une petite ligne en encre douce.

## Do's and Don'ts

### Do:
- **Do** garder le fond blanc pur (fond) et réserver le blanc cassé (fond-doux) à la section visite.
- **Do** utiliser le jade pour une seule bande pleine largeur, l'action principale et les états, rien d'autre.
- **Do** composer les titres en Italiana 400 et tout le reste en Jost, texte courant en 300.
- **Do** séparer par des filets d'un pixel (filet) et par l'espace de section, jamais par une ombre.
- **Do** garder les angles droits (0 px) sur les boutons, photos et tuiles.
- **Do** respecter les proportions des emplacements photo (carré, 4/5, 3/2, 16/7) quand on y place les photos du commerçant.
- **Do** décrire chaque emplacement photo et chaque photo pour les lecteurs d'écran.

### Don't:
- **Don't** ajouter une deuxième couleur vive ni un dégradé.
- **Don't** utiliser d'ombre portée, d'arrondi ou d'effet de verre.
- **Don't** écrire un titre en Jost gras ou un bouton en Italiana.
- **Don't** animer autre chose que le dévoilement du visuel d'ouverture.
- **Don't** remplacer un dessin au trait par une photo de banque d'images ou un visuel de marque : seule une vraie photo de la maison prend sa place.
- **Don't** reprendre les couleurs, les noms ou l'identité de Tiffany ou de Messika : elles servent de référence de finition, pas de modèle.
