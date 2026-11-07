---
name: Au Pain Doré
description: Le carnet de commandes d'une boulangerie de quartier, imprimé en deux encres.
colors:
  couverture: "#2F3A9E"
  couverture-sombre: "#232C7E"
  jaune-autocopiant: "#F4D23C"
  rose-autocopiant: "#F5C3CF"
  carbone: "#1E2156"
  carbone-doux: "#3C3F78"
  rouge-numerotation: "#A8150F"
  ticket: "#FFFDF2"
  creme-couverture: "#F7F1D2"
typography:
  display:
    fontFamily: "Bricolage, Avenir Next Condensed, Arial Narrow, sans-serif"
    fontSize: "clamp(2.6rem, 1.6rem + 6vw, 4.75rem)"
    fontWeight: 800
    lineHeight: 0.92
    fontVariation: "'wdth' 75"
  headline:
    fontFamily: "Bricolage, Avenir Next Condensed, Arial Narrow, sans-serif"
    fontSize: "clamp(1.75rem, 1.3rem + 2.2vw, 2.6rem)"
    fontWeight: 800
    lineHeight: 1
    letterSpacing: "-0.015em"
    fontVariation: "'wdth' 78"
  body:
    fontFamily: "Bricolage, Avenir Next Condensed, Arial Narrow, sans-serif"
    fontSize: "1.0625rem"
    fontWeight: 400
    lineHeight: 1.5
  label:
    fontFamily: "Bricolage, Avenir Next Condensed, Arial Narrow, sans-serif"
    fontSize: "0.75rem"
    fontWeight: 700
    letterSpacing: "0.08em"
    fontVariation: "'wdth' 80"
  manuscrit:
    fontFamily: "Caveat, Bradley Hand, cursive"
    fontSize: "1.55rem"
    fontWeight: 600
    lineHeight: 1.2
rounded:
  feuillet: "3px"
  tampon: "0.4rem"
  tampon-titre: "0.6rem"
spacing:
  pas: "clamp(1rem, 0.8rem + 1vw, 1.5rem)"
  entre-bons: "1.75rem"
  souche: "2.75rem"
  souche-large: "3.5rem"
components:
  bouton-plein:
    backgroundColor: "{colors.carbone}"
    textColor: "{colors.jaune-autocopiant}"
    rounded: "{rounded.tampon}"
    padding: "0.7rem 1.25rem"
    height: "3rem"
  bouton-plein-hover:
    backgroundColor: "#2B2F72"
  bouton-contour:
    textColor: "{colors.carbone}"
    rounded: "{rounded.tampon}"
    padding: "0.7rem 1.25rem"
    height: "3rem"
  bon-jaune:
    backgroundColor: "{colors.jaune-autocopiant}"
    textColor: "{colors.carbone}"
    rounded: "{rounded.feuillet}"
  bon-rose:
    backgroundColor: "{colors.rose-autocopiant}"
    textColor: "{colors.carbone}"
    rounded: "{rounded.feuillet}"
  ticket:
    backgroundColor: "{colors.ticket}"
    textColor: "{colors.carbone}"
    typography: "{typography.manuscrit}"
---

# Design System: Au Pain Doré

## Overview

**Creative North Star: « Le carnet de commandes »**

Le site est le carnet à souches de la boutique : une couverture bleu carbone qui tient une liasse de bons autocopiants jaunes et roses. Chaque section est un bon numéroté. On le lit comme un formulaire imprimé, avec des libellés étroits et des filets, les valeurs sont remplies à la main, et le bon de commande se détache vraiment le long de ses perforations.

Tout est dessiné en deux encres : le carbone (bleu-noir) porte le texte, les filets et les tampons, et le rouge de numérotation porte les numéros de série. Les nuances viennent de hachures, jamais de dégradés. L'ambiance est chaleureuse par la couleur du papier et l'écriture, mais pas vieillotte : la typographie est une grotesque étroite et contemporaine, pas une serif d'antan.

**Key Characteristics:**
- Couverture bleue pleine page, bons en papier coloré posés dessus.
- Souche verticale à gauche de chaque bon : numéro de série rouge, colonne de trous qui laisse voir la couverture.
- Libellés imprimés en petites capitales étroites au-dessus de filets, valeurs en écriture manuscrite.
- Tampons encreurs (contours irréguliers par filtre SVG) pour le nom et les boutons.

## Colors

Deux papiers autocopiants, une couverture, deux encres.

### Primary
- **Bleu couverture** (#2F3A9E) : le fond de page, la couverture et le dos du carnet. Les trous de perforation le laissent voir à travers les bons.
- **Bleu couverture sombre** (#232C7E) : bandeau « exemple fictif », piste de la barre de défilement.

### Secondary
- **Jaune autocopiant** (#F4D23C) : le papier des bons principaux (n° 0001, 0003). C'est aussi l'encre des titres sur la couverture.
- **Rose autocopiant** (#F5C3CF) : le second feuillet de la liasse (n° 0002, 0004, confidentialité), en alternance avec le jaune.

### Tertiary
- **Rouge numérotation** (#A8150F) : les numéros de série des souches. Il sert aussi, fonctionnellement, au signal d'erreur et au champ en cours de saisie (filet de focus, curseur).

### Neutral
- **Encre carbone** (#1E2156) : tout le texte sur papier, les filets, les tampons, les boutons pleins.
- **Carbone doux** (#3C3F78) : libellés imprimés, aides, notes.
- **Papier ticket** (#FFFDF2) : les petits tickets épinglés aux produits, l'emplacement photo.
- **Crème couverture** (#F7F1D2) : le texte courant posé sur la couverture bleue.

### Named Rules
**La règle des deux encres.** Sur le papier, on n'imprime qu'en carbone et en rouge. Toute nuance supplémentaire se fait par hachure (lignes de 1 px) ou par transparence du carbone, jamais par une nouvelle couleur ni par un dégradé.

**La règle du rouge de série.** Le rouge est réservé aux numéros de série et aux signaux de saisie ou d'erreur. Il ne sert jamais à mettre un mot en valeur : l'emphase passe par la graisse et le soulignement carbone.

## Typography

**Display Font:** Bricolage Grotesque (auto-hébergée, variable : graisse, largeur, taille optique), avec repli Avenir Next Condensed / Arial Narrow
**Manuscrit:** Caveat (auto-hébergée), avec repli Bradley Hand

**Character:** une grotesque étroite et franche pour l'imprimé du formulaire, et une écriture rapide pour ce que la boutique « remplit ». Le contraste entre ces deux voix fait tout le carnet.

### Hierarchy
- **Display** (800, largeur 75 %, clamp(2.6rem → 4.75rem), interlignage 0.92, capitales) : uniquement le nom au tampon sur la couverture.
- **Headline** (800, largeur 78 %, clamp(1.75rem → 2.6rem), interlignage 1) : le titre de chaque bon.
- **Title** (700, largeur 85 %, 1.1 → 1.35rem) : les désignations de produits.
- **Body** (400, 1.0625rem, interlignage 1.5, 60–68ch au maximum) : chapeaux et pages légales.
- **Label** (700, largeur 80 %, 0.75rem, approche 0.08em, capitales) : libellés de champs, légendes de tableaux.
- **Manuscrit** (Caveat 600, 1.2–2.2rem) : valeurs remplies (adresse, téléphone, état ouvert/fermé, saisie du formulaire, tickets).

### Named Rules
**La règle du formulaire rempli.** L'écriture manuscrite n'apparaît que pour une valeur écrite dans un champ ou sur un ticket, jamais pour un titre ou un paragraphe.

## Layout

La page suit une seule colonne centrée, `min(100% - 1.5rem, 46rem)` sur téléphone et `min(100% - 4rem, 60rem)` à partir de 52rem. Les bons sont empilés et séparés de 1.75rem. Chaque bon est une grille à deux colonnes : la souche (2.75rem, 3.5rem en grand écran), puis le feuillet, avec une marge intérieure fluide (`--pas`).

Sur grand écran, le bon n° 0001 passe en deux colonnes (infos et actions à gauche, horaires à droite), et le n° 0002 aussi (produits à gauche, photo agrafée à droite). Sur téléphone, les boutons Itinéraire et Appeler remontent juste après l'adresse, pour tenir dans le premier écran. Le tableau des produits s'empile (nom, puis ticket) sous 32rem.

## Elevation & Depth

Le carnet est plat : la profondeur est celle de papiers posés sur une couverture.

### Shadow Vocabulary
- **Feuillet posé** (`box-shadow: 0 1px 1px rgb(0 0 0 / 0.22), 0 14px 28px -14px rgb(0 0 0 / 0.5)`) : chaque bon sur la couverture.
- **Feuillet arraché** (`0 1px 1px rgb(0 0 0 / 0.22), 0 18px 32px -14px rgb(0 0 0 / 0.55)`) : le bon détaché, un peu plus haut.
- **Ticket** (`0 1px 2px rgb(30 33 86 / 0.25)`) : les petits papiers épinglés.

### Named Rules
**La règle de l'ombre noire.** Les ombres sont neutres (noir transparent), décalées vers le bas et floues. Jamais de halo coloré sur le fond bleu.

## Shapes

Des coins presque droits pour le papier (3px), des coins doux pour les tampons (0.4–0.6rem), et des cercles tracés à la main (rayons asymétriques, légère rotation) pour entourer le jour courant. Les perforations sont de vrais trous (rayon de 3.5px, pas de 14px), dessinés avec la couleur de la couverture sur la souche et découpés par un masque sur le bord du bon arraché.

## Components

### Buttons (tampons encreurs)
- **Shape:** double filet, une bordure de 2px et un contour décalé de 1.5px, sur un pseudo-élément passé au filtre d'encre `#encre`. Le libellé reste net (rayon 0.4rem).
- **Primary (plein) :** fond carbone, texte de la couleur du papier (jaune ou rose), Bricolage 800, largeur 75 %, capitales, approche 0.07em, hauteur minimale 3rem.
- **Contour :** même cadre sans fond, texte carbone.
- **Hover / Active / Focus :** au survol, le fond du cadre se teinte (carbone à 10 %, ou #2B2F72 pour le plein). À l'appui, le bouton descend de 1px avec une rotation de -0.4°. Le focus est un contour carbone en tirets, décalé de 4px.

### Bons (cartes)
- **Corner Style:** 3px.
- **Background:** jaune ou rose autocopiant, en alternance.
- **Structure:** souche à gauche (numéro de série vertical rouge, colonne de trous), feuillet à droite.

### Inputs / Fields
- **Style:** pas de cadre, seulement un filet carbone de 1.5px en dessous. La saisie est en Caveat 1.6rem, le libellé imprimé au-dessus.
- **Focus:** le filet devient rouge, 3px.
- **Error:** le filet passe au rouge, avec un message encadré de rouge (2px) et rédigé en carbone.

### Navigation
- Liens en jaune sur la couverture, Bricolage 600 largeur 80 %. Le soulignement n'apparaît qu'au survol.

### Ticket
- Petit papier `#FFFDF2` tourné de ±1.5°, avec un pointillé à gauche. Ligne 1 : l'heure de sortie du four, en libellé imprimé. Ligne 2 : la note du fournil, à la main.

### Bon de commande détachable (signature)
- À l'envoi du formulaire, la souche reste au carnet. Le feuillet est découpé en demi-trous sur son bord gauche, prend sa propre ombre et s'arrache (800ms, `cubic-bezier(.3,.7,.2,1)`, translation de 8 à 18px et rotation de 1.5°). Le récapitulatif apparaît, tamponné « Votre bon est prêt ». Avec réduction des animations, l'état final s'affiche sans mouvement.

## Do's and Don'ts

### Do:
- **Do** poser chaque nouvelle section comme un bon numéroté (souche + feuillet), en alternant jaune et rose.
- **Do** écrire les libellés en petites capitales étroites (0.75rem, 0.08em) au-dessus d'un filet, et les valeurs à la main.
- **Do** ombrer par hachures de 1px (`repeating-linear-gradient` à 45°) quand une case est vide ou fermée.
- **Do** thémer les surfaces du navigateur : sélection carbone sur jaune, curseur rouge, barre de défilement jaune sur bleu sombre.

### Don't:
- **Don't** ajouter une troisième encre ni un dégradé de couleur sur le papier.
- **Don't** utiliser le rouge pour mettre un mot en valeur.
- **Don't** employer l'écriture manuscrite pour un titre ou un paragraphe.
- **Don't** utiliser de photo de banque d'images présentée comme celle de la boutique : l'emplacement photo agrafé attend les vraies photos.
