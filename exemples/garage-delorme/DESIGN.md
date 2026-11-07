---
name: Garage Delorme
description: Le terminal de diagnostic de l'atelier, bleu nuit avec un seul voyant cyan.
colors:
  nuit: "#17202E"
  carte: "#202A3E"
  signal: "#6AE4FF"
  blanc: "#FFFFFF"
  brume: "#CDD0D6"
  filet: "#000000"
  trait: "#34405A"
  positif-depart: "#34EDB3"
  positif-arrivee: "#00D1FF"
typography:
  display:
    fontFamily: "Archivo, Helvetica Neue, Arial, sans-serif"
    fontSize: "clamp(2.6rem, 1.2rem + 5.6vw, 6.25rem)"
    fontWeight: 700
    lineHeight: 1.02
    letterSpacing: "-0.036em"
  chiffre:
    fontFamily: "Archivo, Helvetica Neue, Arial, sans-serif"
    fontSize: "clamp(2.6rem, 1.6rem + 4vw, 5.5rem)"
    fontWeight: 700
    lineHeight: 1
    letterSpacing: "-0.036em"
    fontFeature: "tnum"
  headline:
    fontFamily: "Archivo, Helvetica Neue, Arial, sans-serif"
    fontSize: "clamp(2rem, 1.3rem + 2.6vw, 3.5rem)"
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: "-0.036em"
  title:
    fontFamily: "Archivo, Helvetica Neue, Arial, sans-serif"
    fontSize: "clamp(1.6rem, 1.2rem + 1.6vw, 2.25rem)"
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: "-0.036em"
  title-sm:
    fontFamily: "Archivo, Helvetica Neue, Arial, sans-serif"
    fontSize: "1.375rem"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "-0.02em"
  lead:
    fontFamily: "Archivo, Helvetica Neue, Arial, sans-serif"
    fontSize: "clamp(1.05rem, 1rem + 0.3vw, 1.2rem)"
    fontWeight: 400
    lineHeight: 1.5
  body:
    fontFamily: "Archivo, Helvetica Neue, Arial, sans-serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.5
  label:
    fontFamily: "Archivo, Helvetica Neue, Arial, sans-serif"
    fontSize: "0.875rem"
    fontWeight: 600
    lineHeight: 1.5
  small:
    fontFamily: "Archivo, Helvetica Neue, Arial, sans-serif"
    fontSize: "0.8125rem"
    fontWeight: 400
    lineHeight: 1.5
rounded:
  champ: "4px"
  alerte: "8px"
  carte: "15px"
  panneau: "24px"
  pilule: "80px"
spacing:
  xs: "0.4rem"
  sm: "0.75rem"
  md: "1rem"
  lg: "1.5rem"
  xl: "2rem"
  colonne: "4rem"
  section: "5rem"
  marge: "clamp(1.25rem, 5vw, 4rem)"
  large: "75rem"
components:
  pilule-pleine:
    backgroundColor: "{colors.blanc}"
    textColor: "{colors.filet}"
    typography: "{typography.label}"
    rounded: "{rounded.pilule}"
    padding: "0.75rem 1.4rem"
    height: "3rem"
  pilule-pleine-hover:
    backgroundColor: "#E6F9FF"
    textColor: "{colors.filet}"
  lien-fantome:
    backgroundColor: "transparent"
    textColor: "{colors.signal}"
    rounded: "{rounded.pilule}"
    padding: "0.7rem 1.1rem"
    height: "3rem"
  puce:
    backgroundColor: "transparent"
    textColor: "{colors.signal}"
    rounded: "{rounded.pilule}"
    padding: "0.35rem 0.9rem"
  onglet:
    backgroundColor: "transparent"
    textColor: "{colors.brume}"
    rounded: "{rounded.pilule}"
    padding: "0.6rem 1.2rem"
    height: "2.75rem"
  onglet-actif:
    backgroundColor: "{colors.blanc}"
    textColor: "{colors.filet}"
    rounded: "{rounded.pilule}"
  carte:
    backgroundColor: "{colors.carte}"
    rounded: "{rounded.carte}"
    padding: "1.5rem"
  panneau:
    backgroundColor: "{colors.carte}"
    rounded: "{rounded.panneau}"
    padding: "clamp(1.5rem, 4vw, 2.5rem)"
  champ:
    backgroundColor: "{colors.nuit}"
    textColor: "{colors.blanc}"
    rounded: "{rounded.champ}"
    padding: "0.7rem 0.9rem"
    height: "3rem"
  releve-item:
    backgroundColor: "transparent"
    textColor: "{colors.blanc}"
    rounded: "{rounded.carte}"
    padding: "0.7rem 0.9rem"
---

# Design System: Garage Delorme

## Overview

**Creative North Star: "Le terminal de diagnostic de l'atelier"**

Le site se lit comme l'écran de diagnostic d'un garage moderne : un fond bleu nuit uniforme, un seul voyant cyan qui s'allume là où il se passe quelque chose, et du blanc pour lire et pour agir. Le système est la traduction, imposée par l'utilisateur, d'une référence de style de terminal financier (« Idle Finance ») : le cyan devient le voyant du diagnostic, le halo bleu radial devient la lumière des phares derrière le haut de page.

La densité est faible et la hiérarchie brutale : titres très gras et serrés (Archivo 700, interlettrage -0,036 em), un mot du titre en cyan, de grands chiffres vrais, des pilules pour tout ce qui se touche, des cartes plates à filet noir. Aucune ombre portée : la profondeur vient du seul écart entre le fond nuit et les cartes.

La signature est le pont élévateur, en vraie séquence filmée : 60 images WebP d'une voiture que le pont soulève, dessinées sur un canvas et pilotées par le défilement, avec un relevé de quatre services qui s'allume en cyan à mesure qu'elle monte. Rien n'est caché, on voit le dessous.

**Key Characteristics:**
- Fond bleu nuit unique sur toutes les pages, cartes un cran plus claires.
- Un seul accent, le cyan voyant, réservé aux signaux et aux contours d'action.
- Action principale en pilule blanche pleine, action secondaire en contour cyan.
- Archivo 700 très serré pour les titres, chiffres en chasse fixe.
- Plat : filet noir de 1 px, aucune ombre portée.
- Le pont élévateur filmé comme pièce maîtresse, avec repli en image fixe.

## Colors

Une nuit bleue presque monochrome, un voyant cyan, du blanc pour lire.

### Primary
- **Cyan voyant** (signal) : le seul accent. Mot final du titre, contours du téléphone et des liens fantômes, puces d'état, icônes au trait, pastilles du relevé, anneau de focus, sélection de texte, curseur des champs, flèche des listes déroulantes, jour courant des horaires. Il sert aussi d'état d'erreur des champs (bordure 2 px) : le système n'a pas de rouge.

### Neutral
- **Bleu nuit d'atelier** (nuit) : fond de toutes les pages, fond des champs et des choix non cochés. Aussi la `theme-color`.
- **Ardoise de carte** (carte) : cartes, panneau des services, pastille de langue, résultat du suivi.
- **Blanc de lecture** (blanc) : texte principal, pilule pleine, onglet et choix actifs.
- **Brume** (brume) : texte secondaire, descriptions, libellés de chiffres, état fermé.
- **Filet noir** (filet) : bordure 1 px des cartes, panneaux, champs et image du pont ; aussi le texte posé sur blanc.
- **Trait discret** (trait) : sol du logotype, éléments éteints du relevé, rail de l'indicateur de défilement.

### Tertiary
- **Dégradé positif** (positif-depart vers positif-arrivee, `linear-gradient(73.6deg, …)`) : uniquement le rond des étapes faites du suivi de réparation.

### Named Rules
**La règle du voyant unique.** Le cyan est le seul accent. Il marque un signal, un état ou un contour d'action ; il ne remplit jamais une grande surface ni un bouton plein.

**La règle des phares.** Le halo radial bleu (`radial-gradient(ellipse 60% 55% at 50% 0%, …)`) vit seulement derrière l'ouverture du haut de page. Ailleurs, le fond est nuit uni.

**La règle du positif réservé.** Le dégradé turquoise-cyan ne sert qu'à l'avancement réel du suivi. Pas de dégradé décoratif.

## Typography

**Display Font:** Archivo, fonte variable auto-hébergée (`fonts/archivo.woff2`, graisses 100 à 900, chasse 62 à 125 %), avec Helvetica Neue puis Arial.
**Body Font:** Archivo, même fichier.

**Character:** Une seule famille, poussée aux extrêmes : 700 très serré pour affirmer, 400 aéré pour expliquer. Le ton est celui d'un instrument précis, pas d'une affiche.

### Hierarchy
- **Display** (700, clamp jusqu'à 6,25 rem, 1,02) : titre d'ouverture, 16 ch max, centré, équilibré (`text-wrap: balance`), un mot en cyan.
- **Chiffre** (700, clamp jusqu'à 5,5 rem, 1, chiffres tabulaires) : les quatre grands chiffres vrais.
- **Headline** (700, clamp 2 à 3,5 rem, 1,1) : titres de section.
- **Title** (700, clamp 1,6 à 2,25 rem, 1,15) : titre du panneau de service, adresse.
- **Title-sm** (700, 1,375 rem, 1,2) : titres des trois colonnes « Vous êtes… ».
- **Lead** (400, 1,05 à 1,2 rem) : chapeau d'ouverture, 44 ch max.
- **Body** (400, 1 rem, 1,5) : texte courant, souvent en brume, 44 à 52 ch.
- **Label** (600, 0,875 rem) : libellés de champs, légendes, téléphone de l'en-tête.
- **Small** (400, 0,8125 rem) : bandeau « exemple fictif », pied, puces.

### Named Rules
**La règle du titre serré.** Tout titre de 1,6 rem et plus est en 700 à -0,036 em. Pas de titre maigre, pas de titre espacé.

**La règle des chiffres alignés.** Téléphones, horaires, chiffres et codes de suivi passent en chiffres tabulaires.

## Layout

Une colonne centrée de 75 rem maximum (`large`) avec une marge latérale fluide (`clamp(1.25rem, 5vw, 4rem)`) et 5 rem de respiration verticale entre sections. L'ouverture est centrée sous le halo ; le reste est aligné à gauche. L'en-tête est collant (4,5 rem), sur fond nuit à 86 % avec flou.

À partir de 60 rem : navigation visible, trois colonnes pour les publics, formulaire et suivi en deux colonnes avec 4 rem de gouttière, panneau de service avec l'icône à gauche. À partir de 40 rem : chiffres sur quatre colonnes (deux en dessous). Sous 40 rem, les onglets défilent horizontalement de bord à bord et le relevé passe sur deux colonnes.

La scène du pont fait 260 vh ; son contenu reste collé sous l'en-tête, l'image au format 16/9 (5/4 sur téléphone) dimensionnée pour tenir avec le relevé dans la hauteur visible.

Pages courtes (suivi, mentions) : colonne de 52 rem.

## Elevation & Depth

Système entièrement plat. Aucune ombre portée nulle part : la profondeur vient du contraste tonal entre le fond nuit et l'ardoise des cartes, renforcé par un filet noir de 1 px. Seul relief lumineux : le halo des phares derrière l'ouverture. L'étape active du suivi porte un anneau intérieur de 1 px en cyan (`box-shadow: inset 0 0 0 1px`), qui double un contour et ne crée aucune élévation.

### Named Rules
**La règle du filet noir.** Une surface se détache par sa teinte et son filet noir de 1 px, jamais par une ombre.

## Shapes

Trois familles de rayons. Pilule (80 px) pour tout ce qui se touche ou s'étiquette : boutons, liens fantômes, onglets, choix, puces, pastille de langue, numéros d'étapes. Carte (15 px) pour les cartes et les éléments du relevé ; panneau (24 px) pour le grand panneau de service et l'image du pont (15 px sur téléphone). Les champs de saisie restent presque droits (4 px) et les encadrés d'alerte à 8 px. Les icônes sont au trait (1,6 à 1,8), bouts et angles arrondis, jamais pleines.

## Components

### Buttons
Francs et lisibles au soleil.
- **Shape:** pilule (80 px), hauteur minimale 3 rem.
- **Primary (pilule pleine):** fond blanc, texte noir, 600 à 0,9375 rem. Survol : fond bleu glacier très pâle et montée de 1 px (200 ms, `cubic-bezier(.16,1,.3,1)`).
- **Lien fantôme (secondaire):** contour cyan 1 px, texte cyan, transparent ; survol : voile cyan à 8 % et flèche qui avance de 3 px.
- **Téléphone d'en-tête:** même contour cyan, hauteur 2,75 rem, numéro masqué sous 40 rem (icône seule).
- **Focus:** contour cyan 2 px décalé de 3 px, partout.

### Chips
- **Puce d'état:** contour cyan, texte cyan 600 à 0,8125 rem, point cyan devant ; en brume quand l'atelier est fermé.
- **Choix (radio):** pilule nuit, texte brume ; cochée, blanc plein et texte noir.

### Cards / Containers
- **Corner Style:** 15 px (carte), 24 px (panneau).
- **Background:** ardoise de carte.
- **Shadow Strategy:** aucune (voir Elevation & Depth).
- **Border:** filet noir 1 px.
- **Internal Padding:** 1,5 rem (carte), 1,5 à 2,5 rem (panneau).

### Inputs / Fields
- **Style:** fond nuit, filet noir 1 px, rayon 4 px, hauteur 3 rem, texte blanc 1 rem ; libellé au-dessus en 600 à 0,875 rem.
- **Focus:** la bordure passe au cyan, sans halo.
- **Error:** bordure cyan 2 px et message dans un encadré à contour cyan (8 px).

### Navigation
- **En-tête:** logotype à gauche, liens 0,875 rem blancs au centre (cyan au survol), téléphone en contour cyan et pastille « EN » à droite. Sous 60 rem, les liens disparaissent.
- **Onglets des services:** pilules transparentes en brume ; l'onglet actif est blanc plein, texte noir 600. Un seul panneau visible, qui entre en glissant de 8 px (450 ms). Sans JS, tous les panneaux s'affichent.

### Logotype animé
Un pont à deux colonnes en brume, un sol en trait discret et un bras cyan qui monte au chargement (1,6 s, léger dépassement puis retour), suivi de « Garage » en 400 brume et « Delorme » en 700 blanc.

### Le pont élévateur (signature)
Séquence filmée de 60 images WebP (`img/pont/`), caméra fixe, dessinée sur un canvas dans un cadre 16/9 à rayon 24 px et filet noir, sur fond `#0B1220`. La position suit le défilement avec un lissage (lerp de 0,12 par image) pour démarrer et s'arrêter comme un vrai pont hydraulique. Sous l'image, le relevé : quatre éléments à rayon 15 px, éteints (opacité 0,35, trait discret), qui s'allument tour à tour en cyan (bordure et pastille qui se remplit) aux seuils 0,15 / 0,35 / 0,55 / 0,75. Un indicateur « Faites monter la voiture » s'efface dès les premiers pas. Mention « Illustration générée par IA » en bas à droite. En mouvement réduit, sans JS ou en mode `?capture`, on affiche l'image fixe `fin.webp` (voiture levée) avec le relevé entièrement allumé.

### Suivi de réparation
Liste d'étapes numérotées dans des ronds pilule : à venir en contour gris, faites en dégradé positif plein, active en contour et chiffre cyan.

## Do's and Don'ts

### Do:
- **Do** garder le fond bleu nuit sur toutes les pages et poser les blocs sur l'ardoise de carte avec un filet noir de 1 px.
- **Do** réserver le cyan aux signaux : un mot du titre, contours d'action, icônes, états, focus.
- **Do** utiliser la pilule blanche pleine pour l'action principale et le contour cyan pour l'action secondaire, côte à côte.
- **Do** composer les titres en Archivo 700 à -0,036 em et les chiffres en tabulaires.
- **Do** donner à toute animation un état final statique en mouvement réduit et en `?capture`.
- **Do** n'afficher que des chiffres vrais dans les grands chiffres.

### Don't:
- **Don't** ajouter d'ombre portée : la profondeur vient de la teinte et du filet.
- **Don't** introduire un second accent (le jaune de la version précédente est retiré) ni un rouge d'erreur.
- **Don't** remplir un bouton ou une grande surface en cyan.
- **Don't** étendre le halo des phares au-delà de l'ouverture, ni le dégradé positif au-delà du suivi.
- **Don't** utiliser d'icônes pleines ni de caractères en guise d'icônes : trait arrondi uniquement.
- **Don't** reprendre l'identité, les logos ou les noms de constructeurs automobiles.
