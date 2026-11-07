---
name: Maison Vauclair
description: L'écrin après la fermeture. Boutique noire, une seule lampe allumée sur l'établi.
colors:
  lampe: "#F5F5F0"
  vide: "#000000"
  blanc: "#FFFFFF"
  texte-doux: "rgba(255, 255, 255, 0.86)"
  fumee: "#A3A3A3"
  charbon: "#202020"
  graphite: "#333333"
typography:
  display:
    fontFamily: "Jost, Helvetica Neue, Arial, sans-serif"
    fontSize: "clamp(2.75rem, 1.4rem + 5.6vw, 6.5rem)"
    fontWeight: 300
    lineHeight: 1
    letterSpacing: "-0.05em"
  headline:
    fontFamily: "Jost, Helvetica Neue, Arial, sans-serif"
    fontSize: "clamp(2rem, 1.3rem + 2.6vw, 3.5rem)"
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: "-0.035em"
  accent:
    fontFamily: "Instrument Serif, Iowan Old Style, Georgia, serif"
    fontWeight: 400
    letterSpacing: "-0.02em"
  title:
    fontFamily: "Jost, Helvetica Neue, Arial, sans-serif"
    fontSize: "1.3125rem"
    fontWeight: 400
    letterSpacing: "-0.01em"
  lead:
    fontFamily: "Jost, Helvetica Neue, Arial, sans-serif"
    fontSize: "1.125rem"
    fontWeight: 400
    lineHeight: 1.5
  body:
    fontFamily: "Jost, Helvetica Neue, Arial, sans-serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.5
    fontFeature: "\"ss01\" on"
  label:
    fontFamily: "Jost, Helvetica Neue, Arial, sans-serif"
    fontSize: "0.75rem"
    fontWeight: 500
    letterSpacing: "0.08em"
  badge:
    fontFamily: "Jost, Helvetica Neue, Arial, sans-serif"
    fontSize: "0.6875rem"
    fontWeight: 500
    letterSpacing: "0.05em"
  logotype:
    fontFamily: "Jost, Helvetica Neue, Arial, sans-serif"
    fontSize: "0.875rem"
    fontWeight: 500
    letterSpacing: "0.22em"
  closing:
    fontFamily: "Jost, Helvetica Neue, Arial, sans-serif"
    fontSize: "clamp(2.75rem, 1.2rem + 6vw, 7rem)"
    fontWeight: 300
    lineHeight: 1
    letterSpacing: "-0.05em"
  legal-title:
    fontFamily: "Jost, Helvetica Neue, Arial, sans-serif"
    fontSize: "clamp(2.25rem, 1.6rem + 2vw, 3.25rem)"
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: "-0.035em"
  address:
    fontFamily: "Jost, Helvetica Neue, Arial, sans-serif"
    fontSize: "clamp(1.75rem, 1.4rem + 1.2vw, 2.25rem)"
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: "-0.025em"
  nav:
    fontFamily: "Jost, Helvetica Neue, Arial, sans-serif"
    fontSize: "0.9375rem"
    fontWeight: 500
  small:
    fontFamily: "Jost, Helvetica Neue, Arial, sans-serif"
    fontSize: "0.8125rem"
    fontWeight: 400
    letterSpacing: "0.03em"
rounded:
  focus: "4px"
  carte: "10px"
  pilule: "9999px"
  rond: "50%"
spacing:
  marge-mobile: "1.25rem"
  marge: "2.5rem"
  section-mobile: "6rem"
  section: "7.5rem"
  entete: "4.5rem"
  large: "75rem"
  gouttiere-mobile: "1rem"
  gouttiere: "1.5rem"
components:
  pilule-lampe:
    backgroundColor: "{colors.lampe}"
    textColor: "{colors.vide}"
    rounded: "{rounded.pilule}"
    padding: "0 1.5rem"
    height: "3rem"
  pilule-lampe-hover:
    backgroundColor: "{colors.blanc}"
    textColor: "{colors.vide}"
  pilule-fantome:
    backgroundColor: "transparent"
    textColor: "{colors.blanc}"
    rounded: "{rounded.pilule}"
    padding: "0 1.25rem"
    height: "3rem"
  pilule-petite:
    rounded: "{rounded.pilule}"
    padding: "0 1.1rem"
    height: "2.5rem"
  verre:
    backgroundColor: "rgba(200, 200, 200, 0.1)"
    textColor: "{colors.blanc}"
    typography: "{typography.badge}"
    rounded: "{rounded.pilule}"
    padding: "0.5rem 1rem"
  carte-media:
    backgroundColor: "{colors.charbon}"
    textColor: "{colors.blanc}"
    rounded: "{rounded.carte}"
  carte-charbon:
    backgroundColor: "{colors.charbon}"
    textColor: "{colors.blanc}"
    rounded: "{rounded.carte}"
    padding: "2rem 1.5rem"
  film-rond:
    backgroundColor: "rgba(255, 255, 255, 0.08)"
    textColor: "{colors.blanc}"
    rounded: "{rounded.rond}"
    size: "3.5rem"
---

# Design System: Maison Vauclair

## Overview

**Creative North Star: "L'écrin après la fermeture"**

La boutique est fermée, la rue est noire, une seule lampe reste allumée sur l'établi de l'atelier. Tout le système découle de cette image : un fond noir pur partout, du texte blanc, une seule chaleur (le crème de la lampe) réservée au bouton principal, et des photographies cinématographiques où les bijoux sortent de l'ombre sous la lumière de l'établi. C'est la traduction joaillière de la référence « Sequel » imposée par l'utilisateur (voir PRODUCT.md, Brand Commitments) : on en garde la grammaire (noir, pilules, cartes charbon, verre dépoli, bouton rond du film, grand titre de clôture), jamais le nom, le logo, les textes ni les polices propriétaires.

La densité est faible et la page respire : de grandes photos à bords doucement arrondis, des titres très fins à interlettrage serré, un seul mot en italique sérif par grand titre pour porter l'émotion (« ici », « choisir », « boutique »). Le mouvement appartient au monde : les photos « s'allument » quand on y arrive, comme si la lampe se rallumait au-dessus de chaque pièce. Le premier écran est une photo plein cadre de la bague sous la lampe, avec un bouton rond « Regarder le film » qui ouvre un court film.

Toutes les photographies et le film sont des illustrations générées par IA, signalées comme telles dans le pied de page et sous le film. Ce système remplace la version « canon » (blanc et jade, Italiana), archivée dans `.impeccable/archive-canon/`.

**Key Characteristics:**
- Noir pur (#000) comme seul fond, blanc pour le texte, charbon pour les cartes.
- Une seule chaleur : le crème de la lampe, uniquement sur la pilule pleine principale (et le point du jour courant dans les horaires).
- Jost en 300 aux grandes tailles, interlettrage négatif ; un mot en Instrument Serif italique par grand titre.
- Pilules entièrement arrondies, cartes à 10 px, pastilles en verre dépoli.
- Photos à la lampe, qui passent de l'ombre à la lumière au défilement.
- Presque aucune ombre : la profondeur vient du noir, du charbon et des voiles dégradés.

## Colors

Une palette de nuit : noir absolu, blanc, deux gris de profondeur et une seule lueur chaude.

### Primary
- **Crème de la lampe** (lampe) : l'unique couleur chaude du site. Fond de la pilule principale « Venir à la Maison » / « Itinéraire », contour de focus clavier, et petit point devant le jour courant dans le tableau des horaires. Au survol, la pilule passe au blanc pur.

### Neutral
- **Le vide** (vide) : le fond de toute la page, de l'en-tête collant, du film et de son lecteur. C'est la boutique après la fermeture.
- **Blanc** (blanc) : titres, texte principal, liens, contour des pilules fantômes.
- **Blanc voilé** (texte-doux) : paragraphes d'introduction et textes courants longs (chapeau, textes de l'atelier et des montres, état d'ouverture, pages légales).
- **Fumée** (fumee) : textes secondaires, libellés en capitales, jours fermés, adresse du pied, mentions. Éclaircie par rapport à la référence pour tenir le contraste AA sur le noir et sur le charbon.
- **Charbon** (charbon) : une marche au-dessus du vide. Cartes (atelier, horaires), fond des cartes photo avant chargement, bandeau « Exemple fictif ».
- **Graphite** (graphite) : filets de 1 px (lignes des services, lignes des horaires, filet sous le grand titre de clôture).

### Named Rules
**The Une Seule Lampe Rule.** Le crème n'apparaît que sur la pilule pleine principale, le focus clavier et le repère du jour courant. Jamais en fond de section, jamais en texte, jamais sur un deuxième bouton plein dans le même bloc.

**The Noir Absolu Rule.** Le fond est #000, sans dégradé ni teinte. La profondeur se lit par paliers : vide, puis charbon, puis photo.

## Typography

**Display Font:** Jost, variable 100 à 900 (avec Helvetica Neue, Arial)
**Accent Font:** Instrument Serif italique (avec Iowan Old Style, Georgia)
**Body Font:** Jost (même famille, alternates `ss01` actives)

**Character:** Un sans géométrique très fin, presque chuchoté aux grandes tailles, interrompu par un seul mot en italique sérif qui porte la chaleur humaine de la phrase. L'exception « italique sérif en titre » est voulue et consignée dans `.impeccable/config.json`.

### Hierarchy
- **Display** (display) : le titre d'ouverture « Vos bijoux naissent *ici*. ». Le grand titre de clôture du pied reprend le même registre un cran plus grand (jusqu'à 7rem, même graisse, même interlettrage), souligné d'un filet graphite.
- **Headline** (headline) : un titre par section, une phrase complète terminée par un point, avec son mot en italique. Sur les pages légales, le titre principal reprend ce registre sans italique.
- **Accent** (accent) : le mot en italique sérif à l'intérieur d'un display ou d'un headline, et seulement là.
- **Title** (title) : nom de la pièce sur les cartes photo (« Bagues de fiançailles », « Montres »). L'adresse de la page Visite monte en 300 entre 1.75 et 2.25rem.
- **Lead** (lead) : chapeau d'ouverture et paragraphes de section, limités à 32–36rem de large, en blanc voilé.
- **Body** (body) : texte courant, horaires (chiffres tabulaires), adresse.
- **Label** (label) : capitales espacées en fumée pour les libellés (légende « Horaires », intitulés des services en blanc, intertitres des pages légales, mention sous le film).
- **Badge** (badge) : capitales des pastilles en verre.
- **Logotype** (logotype) : « MAISON VAUCLAIR » en capitales très espacées, dans l'en-tête et le pied. Aucun logo dessiné.

### Named Rules
**The Un Seul Mot Rule.** Chaque grand titre contient exactement un mot en Instrument Serif italique, le mot qui porte l'émotion. Jamais deux, jamais une phrase entière, jamais dans le texte courant ni dans les libellés (l'italique du bandeau fictif et des mentions reste en Jost).

**The Murmure Rule.** Au-dessus de 2rem, Jost est en 300 avec un interlettrage négatif (-0.035em à -0.05em). Le gras n'existe pas dans les titres ; l'insistance passe par la taille et l'italique.

## Layout

Une colonne centrée de 75rem maximum (large), avec des marges latérales de 1.25rem sur téléphone et 2.5rem dès 48rem. Les sections sont séparées par un grand vide vertical (6rem, puis 7.5rem dès 48rem), sans filets ni fonds alternés : c'est le noir qui sépare.

L'ouverture échappe à la colonne : la photo occupe toute la largeur et presque toute la hauteur de l'écran (100svh moins l'en-tête), avec le texte en bas à gauche dans la colonne et le bouton rond du film en bas à droite. Sur téléphone, une photo en portrait dédiée remplace la photo paysage et le cadrage glisse pour garder la bague visible.

Les grilles s'ouvrent progressivement : cartes photo sur une colonne puis deux dès 48rem (gouttière 1rem puis 1.5rem) ; carte de l'atelier empilée puis photo et texte côte à côte dès 60rem (1.15fr / 1fr) ; montres en grande photo 16:9 avec texte dessous sur deux colonnes dès 60rem ; visite en deux colonnes (adresse, carte des horaires) dès 56rem. Un titre de section est suivi de 3rem avant son contenu. L'en-tête mesure 4.5rem et reste collé en haut, sur fond noir.

## Elevation & Depth

Le système est plat. La profondeur vient de trois paliers tonals (vide, charbon, photo) et des voiles dégradés noirs posés sur les photos pour garantir la lecture du texte. Il n'existe que deux ombres, toutes deux héritées de la référence : celle de la pilule crème et celle des pastilles en verre. Sur fond noir, l'ombre de la pilule est quasi imperceptible ; elle ne doit pas servir de modèle pour en ajouter ailleurs.

### Shadow Vocabulary
- **Pilule lampe** (`box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15)`) : uniquement sur la pilule crème.
- **Verre dépoli** (`box-shadow: 0 10px 30px rgba(0, 0, 0, 0.35), inset 0 1px 0 rgba(255, 255, 255, 0.08)`) : uniquement sur les pastilles en verre, avec `backdrop-filter: blur(20px) saturate(1.4)`.

### Voiles
- **Voile d'ouverture** : dégradé du bas vers le haut, noir à 75 %, 45 % à 30 % de hauteur, transparent à 55 %.
- **Voile de carte** : noir à 60 % en bas, transparent à 45 %.

### Named Rules
**The Cartes Sans Ombre Rule.** Les cartes charbon et les cartes photo ne portent jamais d'ombre ni de bordure ; elles se détachent du noir par leur seule valeur.

## Shapes

Deux formes seulement, plus le cercle. Tout ce qui se clique est une pilule entièrement arrondie (9999px) ou un cercle (bouton du film, bouton de fermeture). Tout ce qui contient (cartes photo, carte de l'atelier, carte des horaires, photo des montres, lecteur du film) a des coins doucement arrondis à 10px, avec `overflow: hidden` pour que la photo épouse l'arrondi. Les filets sont de 1px en graphite. Les icônes sont des traits fins (1.5px, extrémités rondes) en SVG, à 1.05rem, en couleur du texte ; seule l'icône lecture est pleine.

## Components

### Buttons
Des pilules calmes et sûres, comme une porte qu'on pousse.
- **Shape :** pilule (rounded.pilule), hauteur minimale 3rem, Jost 500 à 1rem, icône éventuelle à gauche.
- **Primary (pilule lampe) :** fond crème, texte noir. Une seule par groupe d'actions, toujours l'action « venir » (Venir à la Maison, Itinéraire).
- **Hover / Focus :** le fond passe au blanc pur en 250ms ; le focus clavier est un contour crème de 1px décalé de 4px.
- **Ghost (pilule fantôme) :** transparente, contour blanc à 70 %, texte blanc ; au survol, contour blanc plein et fond blanc à 6 %. Réservée à l'action secondaire « Appeler ».
- **Petite :** variante d'en-tête, 2.5rem de haut, texte 0.875rem.

### Chips (pastilles en verre)
- **Style :** verre dépoli gris clair à 10 %, flou 20px, capitales badge en blanc, pilule.
- **Usage :** catégorie d'une carte photo (en haut à droite : « Fiançailles », « Mariage », « Horlogerie »…) et état d'ouverture en direct au-dessus du titre d'ouverture. Elles portent une information réelle, jamais un slogan.

### Cards / Containers
- **Carte photo (carte-media) :** photo plein cadre au ratio 1000/860, coins 10px, voile noir en bas, nom et description en bas à gauche, pastille en verre en haut à droite. Toute la carte est un lien ; au survol, la photo grossit de 3 % en 1200ms.
- **Carte charbon :** fond charbon, coins 10px, padding 2rem 1.5rem (3.5rem sur grand écran pour l'atelier, 2rem pour les horaires). Contient des listes à filets graphite.
- **Shadow Strategy :** aucune (voir Elevation & Depth).

### Navigation
En-tête collant de 4.5rem sur fond noir : logotype à gauche, trois liens centrés (Jost 500, 0.9375rem, blanc à 80 % d'opacité, 100 % au survol), petite pilule lampe à droite. Sous 56rem les liens disparaissent ; restent le logotype et la pilule. Le pied reprend le logotype, l'adresse en fumée, et des liens à 85 % d'opacité soulignés au survol.

### Le bouton du film (signature)
Un cercle de 3.5rem en verre (blanc à 8 %, flou 12px, contour blanc à 85 %) avec l'icône lecture pleine, suivi du libellé « Regarder le film », posé en bas à droite de la photo d'ouverture. Au survol, le cercle s'éclaircit et grossit de 6 % (400ms, sortie douce). Sous 48rem, le libellé devient invisible à l'écran mais reste lu par les lecteurs d'écran. Il ouvre une fenêtre modale : film de 5 s sans son en boucle, coins 10px, fond derrière noir à 88 %, mention « Film généré par IA · sans son », bouton rond de fermeture en haut à droite. La vidéo s'arrête à la fermeture et le focus revient au bouton.

### La lampe s'allume (signature de mouvement)
Chaque photo de section part dans l'ombre (luminosité 0.3, saturation 0.6, légère mise à l'échelle 1.04) et s'allume en 1600ms, courbe `cubic-bezier(.16,1,.3,1)`, quand elle entre à l'écran (IntersectionObserver, une seule fois). Avec `?capture` ou `prefers-reduced-motion`, les photos sont directement allumées, sans transition, et le film s'ouvre avec ses contrôles sans lecture automatique.

## Do's and Don'ts

### Do:
- **Do** garder le fond en noir pur et poser chaque contenant en charbon à coins de 10px, sans ombre.
- **Do** réserver le crème de la lampe à une seule pilule pleine par groupe d'actions, toujours l'action « venir en boutique ».
- **Do** écrire chaque grand titre en Jost 300 à interlettrage négatif avec exactement un mot en Instrument Serif italique.
- **Do** éclairer les photos comme sous une seule lampe d'établi, dans le noir, et les faire « s'allumer » au défilement, avec l'état final immédiat en mouvement réduit et en `?capture`.
- **Do** signaler toute photo ou vidéo générée par IA, dans le pied de page et sous le film.
- **Do** placer le texte sur photo uniquement au-dessus d'un voile noir dégradé.

### Don't:
- **Don't** ajouter une deuxième couleur chaude, un fond crème ou un texte crème.
- **Don't** ajouter d'ombre en dehors de la pilule crème et des pastilles en verre.
- **Don't** mettre plus d'un mot en italique sérif par titre, ni d'italique sérif dans le texte courant.
- **Don't** utiliser de gras dans les titres ni de capitales dans les titres ; les capitales sont pour les libellés, les pastilles et le logotype.
- **Don't** reprendre le nom, le logo, les textes ou les polices propriétaires de la référence « Sequel ».
- **Don't** utiliser une pastille en verre comme accroche décorative au-dessus d'un titre : elle porte une catégorie ou l'état d'ouverture réel.
