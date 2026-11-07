---
name: Au Pain Doré
description: L'affiche de boulangerie, or de croûte sur brun de four.
colors:
  four: "#78300F"
  croute: "#FAAE33"
  miel: "#ECAE68"
  mie-brune: "#402011"
  charbon: "#281006"
  seigle: "#6B2E12"
  framboise: "#D1255C"
  texte: "#F7DDB0"
typography:
  display:
    fontFamily: "Antonio, Arial Narrow, Impact, sans-serif"
    fontSize: "clamp(4.6rem, 18vw, 14rem)"
    fontWeight: 700
    lineHeight: 1.16
    letterSpacing: "-0.02em"
  display-geant:
    fontFamily: "Antonio, Arial Narrow, Impact, sans-serif"
    fontSize: "clamp(7rem, 34vw, 26rem)"
    fontWeight: 700
    lineHeight: 0.78
    letterSpacing: "-0.02em"
  headline:
    fontFamily: "Antonio, Arial Narrow, Impact, sans-serif"
    fontSize: "clamp(3.4rem, 11vw, 9rem)"
    fontWeight: 700
    lineHeight: 0.95
    letterSpacing: "-0.015em"
  title:
    fontFamily: "Antonio, Arial Narrow, Impact, sans-serif"
    fontSize: "clamp(1.8rem, 1.2rem + 2.4vw, 2.8rem)"
    fontWeight: 700
    lineHeight: 0.95
    letterSpacing: "-0.005em"
  body:
    fontFamily: "Hanken Grotesk, Helvetica Neue, Arial, sans-serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.5
  body-small:
    fontFamily: "Hanken Grotesk, Helvetica Neue, Arial, sans-serif"
    fontSize: "0.8125rem"
    fontWeight: 400
    lineHeight: 1.5
  label:
    fontFamily: "Antonio, Arial Narrow, Impact, sans-serif"
    fontSize: "0.875rem"
    fontWeight: 500
    lineHeight: 1
    letterSpacing: "0.04em"
  label-badge:
    fontFamily: "Antonio, Arial Narrow, Impact, sans-serif"
    fontSize: "0.75rem"
    fontWeight: 500
    lineHeight: 1.1
    letterSpacing: "0.06em"
rounded:
  pilule: "9999px"
  carte: "6px"
spacing:
  marge: "clamp(1rem, 4vw, 3.5rem)"
  section: "clamp(4.5rem, 9vw, 7.5rem)"
components:
  pilule-pleine:
    backgroundColor: "{colors.croute}"
    textColor: "{colors.charbon}"
    typography: "{typography.label}"
    rounded: "{rounded.pilule}"
    padding: "0.55rem 1.15rem"
    height: "2.75rem"
  pilule-pleine-hover:
    backgroundColor: "#FFC35A"
  pilule-fantome:
    backgroundColor: "transparent"
    textColor: "{colors.croute}"
    typography: "{typography.label}"
    rounded: "{rounded.pilule}"
    padding: "0.55rem 1.15rem"
    height: "2.75rem"
  pilule-fantome-hover:
    backgroundColor: "{colors.mie-brune}"
  badge-plein:
    backgroundColor: "{colors.croute}"
    textColor: "{colors.charbon}"
    typography: "{typography.label-badge}"
    rounded: "{rounded.pilule}"
    padding: "0.3rem 0.8rem"
  badge-creux:
    backgroundColor: "{colors.mie-brune}"
    textColor: "{colors.croute}"
    typography: "{typography.label-badge}"
    rounded: "{rounded.pilule}"
    padding: "0.3rem 0.8rem"
  badge-etat-ferme:
    backgroundColor: "{colors.framboise}"
    textColor: "#FFF4E6"
    typography: "{typography.label-badge}"
    rounded: "{rounded.pilule}"
    padding: "0.3rem 0.8rem"
  carte:
    backgroundColor: "{colors.mie-brune}"
    textColor: "{colors.texte}"
    rounded: "{rounded.carte}"
    padding: "1.5rem"
  champ:
    backgroundColor: "{colors.charbon}"
    textColor: "{colors.texte}"
    typography: "{typography.body}"
    rounded: "{rounded.pilule}"
    padding: "0.7rem 1.1rem"
    height: "3rem"
---

# Design System: Au Pain Doré

## Overview

**Creative North Star: "L'affiche de marché"**

La boulangerie se lit comme une affiche collée au mur du marché : le nom en capitales étroites énormes, un seul or « croûte » sur un brun « four » qui couvre toutes les pages, et le pain posé directement sur ce fond, sans cadre ni table. La page est faite d'environ 90 % de typographie et 10 % de produit ; le produit n'a de place que parce qu'il est détouré et repose sur la même couleur que la page.

Le système est traduit d'une fiche de style de référence imposée par l'utilisateur (une affiche d'épicerie, or sur brun-rouille), puis adapté au pain : Antonio et Hanken Grotesk remplacent les polices propriétaires, les épis de blé remplacent le feuillage en filigrane, la framboise devient la couleur de l'état « fermé ». Le nom, les textes et la police de la marque de référence ne sont pas repris. Un écart est assumé : le texte courant garde un interlignage de 1,5 (la référence plafonnait à 1,4) pour rester lisible.

Tout est plat : pas d'ombre, pas de halo, pas de bande de couleur pour séparer les sections. La hiérarchie vient de la taille des titres, de l'or, des pilules et des filets en pointillés.

**Key Characteristics:**
- Un fond unique brun de four sur toutes les pages, avec un filigrane d'épis de blé.
- Un seul accent, l'or de croûte, pour les titres, les boutons, les filets et les chiffres.
- Des titres d'affiche en Antonio capitales, de 2,8 rem à 26 rem.
- Des pilules partout (boutons, badges, champs, ligne du jour), des cartes à 6 px.
- Des produits en vrais détourages alpha, posés à même le fond.
- Aucune ombre ; profondeur par superposition des titres et du pain.

## Colors

Un monochrome chaud de bruns de four, porté par un seul or, avec une framboise gardée en réserve pour l'état fermé.

### Primary
- **Or de croûte** (`croute`) : le seul accent. Titres d'affiche et de section, pilule pleine, contour et texte des pilules fantômes, badges pleins, filets en pointillés entre sections, ligne du jour dans les horaires, sélection de texte, contour de focus, curseur des champs. Le texte posé sur l'or est toujours en charbon.

### Secondary
- **Framboise** (`framboise`) : réservée à l'état « fermé ». Elle n'apparaît que sur le badge d'état quand la boutique est fermée, avec un texte crème (#FFF4E6). Nulle part ailleurs.

### Neutral
- **Brun de four** (`four`) : le fond de toutes les pages, accordé au fond d'origine des photos. Aussi la couleur de thème du navigateur.
- **Mie brune** (`mie-brune`) : cartes, badges creux, survol des pilules fantômes.
- **Charbon** (`charbon`) : le plus sombre. Texte sur l'or, fond des champs, message d'erreur, bandeau « exemple fictif ».
- **Seigle** (`seigle`) : bordures discrètes (contour des champs au repos, pointillés entre les lignes de liste et d'horaires).
- **Mie claire** (`texte`) : le texte courant. Jamais de blanc pur.
- **Miel** (`miel`) : or atténué pour les textes secondaires (aides, mentions, jour fermé dans le tableau), choisi pour garder le contraste AA sur le fond et sur les cartes.

### Named Rules
**The One Gold Rule.** L'or de croûte est le seul accent. Pas de deuxième couleur vive, pas de couleur froide ; un nouvel élément qui veut attirer l'œil prend l'or ou grossit.

**The Raspberry Reserve Rule.** La framboise ne signale qu'une chose : « fermé », sur la pilule d'état. Elle ne sert ni à la décoration, ni aux erreurs, ni aux promotions.

**The No Band Rule.** Le brun de four couvre la page d'un bout à l'autre. Aucune section ne reçoit un fond de couleur unie pleine largeur ; les sections se séparent par un filet en pointillés or. Le mince bandeau « exemple fictif » en haut est une obligation du produit, pas un motif à réutiliser.

## Typography

**Display Font:** Antonio (avec Arial Narrow, Impact, sans-serif)
**Body Font:** Hanken Grotesk (avec Helvetica Neue, Arial, sans-serif)

**Character:** Une capitale étroite d'affiche, très grasse et serrée, contre une grotesque sobre pour tout ce qui se lit en phrase. Antonio parle fort et court ; Hanken explique.

### Hierarchy
- **Affiche** (700, clamp(4,6 rem, 18 vw, 14 rem), interlignage 1,16, -0,02 em, capitales) : le nom de la boutique dans la première vue, sur deux lignes. L'interlignage plus ouvert laisse la place à chaque ligne de monter dans sa propre fenêtre.
- **Titre géant** (700, clamp(7 rem, 34 vw, 26 rem), 0,78, -0,02 em, capitales) : un chiffre ou un mot unique décoratif, masqué aux lecteurs d'écran (« 48 h » au-dessus du gâteau, « OUVERT / FERMÉ » dans les horaires).
- **Titre XL** (700, clamp(3,4 rem, 11 vw, 9 rem), 0,95, -0,015 em, capitales) : titres de section (« Ce qui sort du four », l'adresse).
- **Titre M** (700, clamp(1,8 rem, …, 2,8 rem), 0,95, capitales) : sous-titres, titre de carte. Grossi jusqu'à 5,5 rem pour le nom de chaque produit.
- **Liste et horaires** (Antonio 500, 1,05–1,35 rem, capitales, +0,02 à +0,03 em) : lignes de produits et tableau des horaires, chiffres tabulaires.
- **Body** (Hanken 400, 1 rem, 1,5) : texte courant ; l'intro monte à 1,0625 rem et se limite à 40 ch, les pages légales à 68 ch. Jamais au-dessus de 1,125 rem.
- **Small** (Hanken, 0,8125 rem, 1,5, miel) : aides et mentions.
- **Label** (Antonio 500, 0,875 rem, +0,04 em, capitales) : pilules. Badges à 0,75 rem et +0,06 em ; étiquettes de champ à 0,75 rem et +0,08 em, en or.

### Named Rules
**The One Poster Face Rule.** Antonio est la seule police d'affiche. Pas de deuxième police de titre, pas de police système pour l'affichage.

**The Small Text Rule.** Hanken reste petite et posée : 0,8125 à 1,125 rem, interlignage 1,5. Tout ce qui doit frapper passe en Antonio capitales, pas en Hanken grossie.

## Layout

Une seule colonne pleine largeur sur téléphone, avec une marge latérale fluide (`marge`) et un rythme vertical fluide entre sections (`section`). Les sections ne sont pas des blocs colorés : ce sont des zones de texte séparées par un filet en pointillés or inset de la même marge.

Au-dessus de 52 rem : la barre passe en grille trois colonnes (pilules de navigation à gauche, nom au centre, état et Appeler à droite) ; les produits alternent texte et image sur deux colonnes ; la section gâteaux met le titre géant et le gâteau à gauche, la carte à droite ; les horaires passent en 1fr / 1,3fr.

La première vue superpose deux couches dans la même cellule de grille : le titre d'affiche au-dessus (z 2) et la boule de pain alignée en bas à droite, légèrement débordante (z 1). Les titres géants et les produits se chevauchent de la même façon : le gâteau remonte sous les chiffres « 48 h » sans les cacher.

## Elevation & Depth

Aucune ombre, nulle part. La profondeur vient de la superposition (le pain glissé sous le titre, le gâteau sous les chiffres géants) et de trois paliers tonaux : brun de four, puis mie brune pour les cartes, puis charbon pour les champs.

### Named Rules
**The Flat Oven Rule.** Pas de `box-shadow`, pas de `text-shadow`, pas de halo ni de flou. Un élément qui doit se détacher change de palier tonal ou passe à l'or.

## Shapes

Deux formes seulement : la pilule (9999 px) pour tout ce qui se touche ou s'étiquette (boutons, badges, champs, message d'erreur, ligne du jour des horaires), et la carte à coins légèrement adoucis (6 px) pour le seul conteneur, le formulaire de commande. Les bordures font 1 px : or plein sur les pilules fantômes, seigle sur les champs au repos. Les séparateurs sont des pointillés de 1 px : or entre les sections et en haut du pied de page, seigle entre les lignes de liste et d'horaires.

Les produits n'ont pas de forme : ce sont des détourages, leur silhouette est celle du pain.

## Components

### Buttons
Des pilules d'affiche, en capitales Antonio, toutes à 44 px de haut minimum.
- **Shape:** pilule complète (9999 px), bordure or de 1 px.
- **Pilule pleine :** fond or, texte charbon. Une seule action principale par groupe (Itinéraire, Préparer ma demande, Appeler pour confirmer).
- **Pilule fantôme :** fond transparent, contour et texte or. Navigation, téléphone, Instagram, actions secondaires.
- **Hover / Focus :** la pleine s'éclaircit (#FFC35A), la fantôme prend le fond mie brune, en 200 ms. À l'appui, réduction à 0,97. Focus clavier : contour or de 2 px décalé de 3 px.
- **Icônes :** traits SVG de 1,5 px en couleur courante, à gauche du libellé (téléphone, lieu, Instagram).

### Chips (badges)
- **Style :** pilules plus petites, sans bordure, Antonio capitales à 0,75 rem.
- **Plein :** fond or, texte charbon. Les faits du savoir-faire (Levain maison, Fait sur place, Pur beurre).
- **Creux :** fond mie brune, texte or. Les précisions et conditions (Sur commande, 48 h ; Demandez au comptoir).
- **État :** rempli par le script selon l'heure de Paris. Ouvert : badge plein or (« Ouvert jusqu'à 19 h 30 »). Fermé : framboise (« Fermé · demain 7 h »). Dans la barre sur grand écran, sous le titre sur téléphone.

### Cards / Containers
- **Corner Style :** 6 px.
- **Background :** mie brune.
- **Shadow Strategy :** aucune (voir Elevation & Depth).
- **Border :** aucune.
- **Internal Padding :** 1,5 rem, 2 rem au-dessus de 52 rem.

### Inputs / Fields
- **Style :** pilules de 48 px de haut, fond charbon, contour seigle de 1 px, texte mie claire en Hanken 1 rem ; placeholder brun doré. Le sélecteur porte un chevron or. Étiquette au-dessus, en Antonio capitales or.
- **Focus :** le contour passe à l'or.
- **Error :** contour or de 2 px sur le champ fautif ; message dans une pilule charbon, texte or gras, annoncé aux lecteurs d'écran. Pas de rouge : la framboise reste réservée à « fermé ».

### Navigation
Barre sans fond posée sur le brun : pilules fantômes de section à gauche (masquées sur téléphone), logotype « Au Pain Doré » en Antonio or au centre, badge d'état et pilule Appeler à droite. Le pied de page reprend le logotype, avec un filet en pointillés or au-dessus et les liens légaux en or.

### Filet en pointillés
Un trait de 1 px en pointillés or (opacité 0,8) entre chaque section, inset de la marge. Les lignes de liste et du tableau des horaires utilisent la même ligne en seigle.

### Filigrane d'épis
Un motif SVG d'épis de blé en trait or (1,2 px, opacité 0,09), répété en tuiles de 220 × 260 px sur tout le fond du corps. Il donne une texture au brun sans en changer la couleur.

### Produits détourés
Chaque produit est une image WebP à couche alpha réelle, détourée, posée directement sur le brun de four, sans cadre, fond, coin arrondi ni ombre. Le fond d'origine des photos est accordé au brun de four pour que les bords se fondent. Au survol d'une ligne produit, l'image grossit à 1,04 et tourne de -2° (900 ms).

### Typographie géante
Trois tailles d'affiche font la page : l'affiche (le nom), le titre géant (un seul chiffre ou mot, décoratif) et le titre XL (titres de section). Toujours en or, capitales, interlettrage négatif.

### Ligne du jour (horaires)
Le jour courant du tableau devient une pilule or pleine largeur, texte charbon, posée par le script.

### Mouvement
Une seule courbe pour tout ce qui arrive : cubic-bezier(.16, 1, .3, 1).
- **Entrée de l'affiche :** les deux lignes du titre montent depuis le bas de leur fenêtre (1100 ms, la seconde avec 120 ms de retard) ; la boule de pain se pose en apparaissant, depuis 40 px plus bas et à 94 % de sa taille (1300 ms, après 250 ms).
- **Défilement :** sur la première hauteur d'écran, la boule remonte jusqu'à 60 px et tourne jusqu'à 8°, à chaque image d'animation.
- **Apparitions :** les blocs marqués montent de 24 px en apparaissant (opacité 700 ms, déplacement 900 ms) quand ils entrent dans l'écran, une seule fois.
- **Reçu de commande :** se pose comme la boule (600 ms).
- **Mouvement réduit :** défilement doux coupé, aucune animation d'entrée, la boule reste immobile, pas d'effet de survol sur les produits, tout le contenu visible d'emblée. Sans script, tout est visible aussi.

## Do's and Don'ts

### Do:
- **Do** garder le brun de four (`four`) comme fond unique de chaque page, avec le filigrane d'épis.
- **Do** réserver l'or de croûte (`croute`) à l'accent et poser le texte en charbon sur l'or.
- **Do** utiliser la pilule (9999 px) pour boutons, badges et champs, et la carte à 6 px pour le seul conteneur.
- **Do** séparer les sections par un filet en pointillés or de 1 px, jamais par un fond.
- **Do** montrer les produits en vrais détourages alpha, posés à même le fond, et accorder le fond des photos au brun de four avant détourage.
- **Do** faire frapper les titres par la taille : Antonio 700 capitales, interlettrage négatif.
- **Do** prévoir le chemin de mouvement réduit pour toute nouvelle animation : contenu visible, rien qui bouge.

### Don't:
- **Don't** ajouter d'ombre, de halo ou de flou, ni sur les boutons, ni sur les cartes, ni sur les produits.
- **Don't** utiliser la framboise ailleurs que sur l'état « fermé ».
- **Don't** introduire une deuxième couleur d'accent, une couleur froide ou du blanc pur.
- **Don't** poser une section sur une bande de couleur unie pleine largeur.
- **Don't** simuler un détourage avec un masque CSS, un mode de fusion (`mix-blend-mode`) ou une image à fond rectangulaire : le produit doit être une vraie image à transparence.
- **Don't** ajouter une deuxième police d'affiche, ni passer le texte courant au-dessus de 1,125 rem.
