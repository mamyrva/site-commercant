---
name: Garage Delorme
description: Garage automobile à Gap ; la page est un pont élévateur, rien n'est caché.
colors:
  nuit: "#111418"
  nuit-2: "#1A1F25"
  clair: "#E9ECEF"
  blanc: "#FFFFFF"
  jaune: "#F2C230"
  jaune-vif: "#FFD24D"
  acier: "#5B6573"
  acier-clair: "#A3ACB8"
  texte: "#111418"
  texte-doux: "#4A525D"
  filet: "#C9CED4"
  erreur: "#B3261E"
  erreur-fond: "#FBEAEA"
  erreur-texte: "#5C1410"
typography:
  display:
    fontFamily: "Archivo, Helvetica Neue, Arial, sans-serif"
    fontSize: "clamp(2.1rem, 1.1rem + 3.4vw, 4.25rem)"
    fontWeight: 800
    lineHeight: 0.98
    letterSpacing: "-0.02em"
    fontVariation: "'wdth' 118"
  headline:
    fontFamily: "Archivo, Helvetica Neue, Arial, sans-serif"
    fontSize: "clamp(1.9rem, 1.2rem + 2.8vw, 3.4rem)"
    fontWeight: 800
    lineHeight: 1.02
    letterSpacing: "-0.015em"
    fontVariation: "'wdth' 112"
  title:
    fontFamily: "Archivo, Helvetica Neue, Arial, sans-serif"
    fontSize: "clamp(1.3rem, 1rem + 1.2vw, 1.85rem)"
    fontWeight: 700
    fontVariation: "'wdth' 112"
  logotype:
    fontFamily: "Archivo, Helvetica Neue, Arial, sans-serif"
    fontSize: "1.05rem"
    fontWeight: 800
    letterSpacing: "0.04em"
    fontVariation: "'wdth' 125"
  lead:
    fontFamily: "Archivo, Helvetica Neue, Arial, sans-serif"
    fontSize: "1.0625rem"
    fontWeight: 400
    lineHeight: 1.55
  body:
    fontFamily: "Archivo, Helvetica Neue, Arial, sans-serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.55
  label:
    fontFamily: "Archivo, Helvetica Neue, Arial, sans-serif"
    fontSize: "0.8125rem"
    fontWeight: 700
  pin-label:
    fontFamily: "Archivo, Helvetica Neue, Arial, sans-serif"
    fontSize: "0.875rem"
    fontWeight: 700
    fontVariation: "'wdth' 110"
rounded:
  outil: "3px"
  rond: "50%"
spacing:
  marge: "clamp(1.25rem, 5vw, 5rem)"
  section: "clamp(4.5rem, 9vw, 8rem)"
  entete: "4.25rem"
components:
  button-primary:
    backgroundColor: "{colors.jaune}"
    textColor: "{colors.nuit}"
    rounded: "{rounded.outil}"
    padding: "0.8rem 1.4rem"
    height: "3.25rem"
  button-primary-hover:
    backgroundColor: "{colors.jaune-vif}"
    textColor: "{colors.nuit}"
  button-outline:
    backgroundColor: "transparent"
    textColor: "{colors.clair}"
    rounded: "{rounded.outil}"
    padding: "0.8rem 1.4rem"
    height: "3.25rem"
  input-field:
    backgroundColor: "{colors.blanc}"
    textColor: "{colors.texte}"
    rounded: "{rounded.outil}"
    padding: "0.7rem 0.85rem"
    height: "3rem"
  choice-chip:
    backgroundColor: "{colors.blanc}"
    textColor: "{colors.texte}"
    rounded: "{rounded.outil}"
    padding: "0.5rem 1.1rem"
    height: "2.75rem"
  choice-chip-selected:
    backgroundColor: "{colors.nuit}"
    textColor: "{colors.blanc}"
  tracking-step-active:
    backgroundColor: "{colors.jaune}"
    textColor: "{colors.nuit}"
    rounded: "{rounded.rond}"
    size: "2rem"
  header:
    backgroundColor: "{colors.nuit}"
    textColor: "{colors.clair}"
    padding: "0.75rem clamp(1.25rem, 5vw, 5rem)"
---

# Design System: Garage Delorme

## Overview

**Creative North Star: "Le pont élévateur"**

Le site se comporte comme le pont élévateur de l'atelier : au défilement, la voiture dessinée au trait monte, son dessous apparaît, et les quatre services s'épinglent sur les pièces concernées. Tout le système découle de cette image de transparence technique : un sol d'atelier anthracite et un blanc d'atelier en grandes zones, un jaune sécurité rare, et un dessin acier précis comme une notice.

La densité est faible et l'échelle grande, au niveau de finition d'un site constructeur : titres étendus, peu de texte, actions évidentes. Les sections alternent fond sombre (scène, « En panne », suivi, pied de page) et fond clair (services, formulaire, infos). Les surfaces sont plates, avec des filets d'un pixel ; la profondeur vient du mouvement du pont, pas d'ombres.

Le site refuse la photo d'atelier générique accompagnée de « Votre garage de confiance ». Il n'y a pas d'illustration décorative : chaque trait dessine une pièce réelle.

**Key Characteristics:**
- Deux grands fonds en alternance, anthracite (nuit) et blanc atelier (clair).
- Un seul accent, le jaune sécurité, pour les bras du pont, l'action principale et l'état actif.
- Archivo variable : étendu (110 à 125 %) pour les titres et le logotype, largeur normale pour le texte.
- Dessin technique au trait (acier et clair), pas d'aplats illustratifs.
- Une seule signature animée : la voiture qui monte avec le défilement.

## Colors

Une palette d'atelier presque monochrome et froide, avec un unique jaune de sécurité.

### Primary
- **Jaune sécurité** (jaune) : bras du pont (traits et patins), bouton d'action principale, étape active du suivi, pastilles et tiges des étiquettes épinglées, point « aujourd'hui » des horaires, anneau de focus et sélection de texte. Le numéro de téléphone de l'en-tête est en jaune, car appeler est l'action principale.
- **Jaune vif** (jaune-vif) : survol du bouton principal uniquement.

### Neutral
- **Sol d'atelier** (nuit) : fond de la scène, de l'en-tête (à 94 % d'opacité avec flou), des sections sombres et du pied de page ; fond des cases cochées et des étapes faites.
- **Panneau anthracite** (nuit-2) : emplacements de photo sur fond sombre.
- **Blanc atelier** (clair) : fond des sections claires ; carrosserie et roues dessinées sur la scène ; texte sur fond sombre.
- **Blanc** (blanc) : titres sur fond sombre, fond des champs, des choix et du résultat de suivi.
- **Acier** (acier) : dessin technique (colonnes du pont, sol du logotype), flèche des listes déroulantes, barre de défilement.
- **Acier clair** (acier-clair) : texte secondaire sur fond sombre (chapeau, liens de navigation, sous-titres d'étiquettes, pied de page).
- **Encre** (texte) : texte courant sur fond clair. Même valeur que nuit, nommée par rôle.
- **Encre douce** (texte-doux) : paragraphes secondaires, notes et aides sur fond clair.
- **Filet** (filet) : bordures de champ au repos, séparateurs de liste et du tableau des horaires.

### Status
- **Erreur** (erreur, erreur-fond, erreur-texte) : bordure des champs invalides et message d'erreur du formulaire, rien d'autre.

### Named Rules
**The Yellow Rule.** Le jaune sert seulement aux bras du pont, à l'action principale et à l'état actif (étape en cours, jour en cours, focus, sélection). Les pastilles et tiges des étiquettes en font partie, car elles appartiennent au pont. Sur un écran, une seule action est en jaune par groupe d'actions ; la seconde est en filet. Le jaune n'est jamais une décoration ni une couleur de titre.

**The Two Floors Rule.** Une section est soit sur le sol d'atelier (nuit), soit sur le blanc atelier (clair). Pas de dégradés, pas de troisième fond de section.

## Typography

**Display Font:** Archivo variable (graisses 100 à 900, largeur 62 à 125 %), auto-hébergée, avec Helvetica Neue et Arial en secours.
**Body Font:** la même Archivo, en largeur normale.

**Character:** une seule famille, dont l'axe de largeur porte la hiérarchie : étendue et grasse, elle sonne comme une plaque de constructeur ; normale, elle reste lisible en plein soleil sur téléphone.

### Hierarchy
- **Display** (800, largeur 118 %, de 2,1 à 4,25 rem, interlignage 0,98) : le titre de la scène et le titre de la page de suivi. Équilibré (`text-wrap: balance`).
- **Headline** (800, largeur 112 %, de 1,9 à 3,4 rem, interlignage 1,02) : titres de section et titre des pages légales.
- **Title** (700, largeur 112 %, de 1,3 à 1,85 rem) : noms des services. L'adresse reprend cette voix en 800 (de 1,5 à 2,1 rem, interlignage 1,15).
- **Logotype** (800, largeur 125 %, 1,05 rem, capitales, espacement 0,04 em) : « Garage » en 400 acier clair, « Delorme » en blanc. 0,875 rem et 112 % sur téléphone.
- **Lead** (400, 1,0625 rem, 40 à 46 caractères par ligne) : chapeaux sous les titres.
- **Body** (400, 1 rem, interlignage 1,55, 44 à 68 caractères par ligne).
- **Label** (700, 0,8125 rem, casse normale) : intitulés de champ, légendes de groupe de choix, légende du tableau des horaires.
- **Pin label** (700, largeur 110 %, 0,875 rem) : nom du service sur une étiquette du pont, avec un sous-titre en 0,75 rem acier clair.

### Named Rules
**The Width Carries Rank Rule.** La hiérarchie passe par la largeur et la graisse d'Archivo (110 à 125 % pour les titres et le logotype), jamais par une seconde famille.

**The Tabular Figures Rule.** Les téléphones, horaires, numéros d'étape et codes de suivi sont en chiffres tabulaires.

## Layout

Une colonne pleine largeur avec une marge latérale fluide (marge) et un rythme vertical de section fluide (section). L'en-tête est collant ; sa hauteur réelle est mesurée par le script et écrite dans entete, pour que la scène collante se cale exactement dessous.

- **Points de rupture :** 40 rem (téléphone ou plus large) et 60 rem (bureau).
- **Moins de 40 rem :** le numéro de l'en-tête se réduit à l'icône téléphone ; la voiture déborde à 116 % de la largeur et les quatre étiquettes s'étagent sur quatre lignes sous elle ; les sous-titres d'étiquette sont masqués.
- **60 rem et plus :** navigation visible ; scène en deux colonnes (5fr texte, 7fr pont) ; les sections passent en deux colonnes (services 1fr 1fr, « En panne » 1fr 1fr, formulaire 1fr 2fr, suivi 1fr 1fr, infos 1fr 1fr) avec un écart de 4 à 5 rem ; les étapes du suivi s'alignent en quatre colonnes surmontées d'un filet de 2 px.
- **Largeurs de lecture :** formulaire et étapes limités à 52 rem ; pages légales à 52 rem.
- **Cibles tactiles :** 2,75 rem minimum (choix, bouton de langue), 3 rem pour les champs, 3,25 rem pour les boutons.

## Elevation & Depth

Le système est plat. Aucune ombre portée : la séparation vient de l'alternance des deux fonds et de filets d'un pixel. La seule profondeur est celle du pont : la voiture monte réellement dans la scène. Deux anneaux d'état existent : le halo jaune à 60 % autour d'un champ en focus et le cerne nuit d'un pixel autour du point « aujourd'hui ». L'en-tête est translucide (94 %) avec un flou de 8 px.

### Named Rules
**The Lift Is The Depth Rule.** Aucune carte flottante ni ombre décorative : si quelque chose doit sembler en relief, c'est la voiture sur le pont.

## Shapes

Des angles d'outillage : un rayon de 3 px (outil) sur les boutons, les champs, les choix et le bouton de langue. Le cercle complet (rond) est réservé aux pastilles des étiquettes, aux numéros d'étape et au point « aujourd'hui ». Les sections, panneaux et emplacements photo ont des angles vifs. Bordures d'un pixel pour les séparateurs, 1,5 px pour les contrôles et les numéros d'étape. Le dessin est au trait, extrémités arrondies : 1,4 à 1,7 pour les pièces, 5 pour les bras jaunes.

## Components

### Logotype animé
Deux colonnes de pont en acier clair, un sol en acier et une traverse jaune. Au chargement, la traverse monte (1,6 s, courbe d'entrée-sortie, avec un léger dépassement), puis le nom « Garage Delorme » se dévoile de gauche à droite par découpe (900 ms, 0,9 s de délai). En mouvement réduit et en mode capture : traverse en position haute, nom visible, sans animation.

### Scène du pont (signature)
- **Structure :** section anthracite haute de 230 vh avec un contenu collant sous l'en-tête : titre, chapeau, deux actions, indication « Faites monter la voiture », puis le dessin.
- **Dessin :** colonnes et sol en acier, carrosserie et roues en blanc atelier, bras et patins en jaune, dessous (carter, réservoir, bras de suspension) en gris clair qui apparaît à mesure que la voiture monte.
- **Mouvement :** la position du défilement donne une progression de 0 à 1 ; la voiture monte de 34 % de la hauteur du dessin. L'indication de défilement s'efface dès le premier quart.
- **Étiquettes épinglées :** une pastille jaune sur la pièce, une tige jaune d'un pixel qui descend dans l'espace libéré sous la voiture, puis le nom du service. Chaque étiquette apparaît à son seuil (0,2, 0,4, 0,6, 0,8) : fondu de 450 ms, puis la tige se déroule en 500 ms. Les étiquettes de droite s'alignent à droite de leur point.

### Boutons
- **Shape :** angles d'outil (3 px), hauteur minimale 3,25 rem, graisse 700, icône au trait de 1,15 em possible avant ou après le texte.
- **Primary :** fond jaune, texte nuit, bordure jaune. Un seul par groupe d'actions.
- **Outline :** fond transparent, bordure de 1,5 px dans la couleur du texte (clair sur fond sombre, encre sur fond clair).
- **Hover / Focus :** survol en jaune vif pour le principal, voile gris à 12 % pour le filet ; enfoncement d'un pixel au clic ; transitions de 200 ms ; anneau de focus jaune de 2 px, décalé de 3 px.

### Contrôles de formulaire
- **Champs :** fond blanc, bordure filet de 1,5 px, angles d'outil, hauteur 3 rem, intitulé en Label au-dessus.
- **Focus :** bordure nuit et halo jaune de 3 px à 60 %.
- **Listes déroulantes :** apparence native retirée, chevron acier au trait.
- **Choix (rendez-vous ou devis) :** pastilles rectangulaires blanches à bordure filet ; l'option cochée passe en fond nuit et texte blanc.
- **Erreur :** bordure rouge sur le champ, message en encadré rose pâle avec un filet rouge à gauche.

### Étapes du suivi
Quatre étapes numérotées dans des cercles de 2 rem (Véhicule reçu, Diagnostic, Réparation, Prête à récupérer). Étape faite : cercle nuit avec une coche jaune au trait. Étape active : cercle jaune, chiffre nuit. Étape à venir : acier clair. Sur bureau, chaque étape est surmontée d'un filet de 2 px, jaune pour les étapes faites et active. La même composition sert d'aperçu sur l'accueil (fond sombre) et de résultat sur la page de suivi (fond blanc dans un cadre filet). Le champ de code est en capitales espacées et chiffres tabulaires.

### Tableau des horaires
Lignes séparées par des filets, jour à gauche, heures à droite en chiffres tabulaires, jours fermés en encre douce. La ligne du jour en cours passe en 800 et reçoit un point jaune cerné de nuit. Au-dessus, une phrase d'état (« Ouvert jusqu'à… » ou « Fermé pour le moment… ») calculée à l'heure de Paris.

### En-tête et navigation
En-tête collant anthracite translucide, filet inférieur sombre. Liens de navigation en 500, 0,875 rem, acier clair, blancs au survol, visibles à partir de 60 rem. Le téléphone reste toujours visible (icône seule sur téléphone). Bouton de langue carré de 2,75 rem à bordure fine.

### Pied de page
Fond nuit, texte acier clair en 0,9375 rem, liens en blanc atelier soulignés, mention légale finale en 0,8125 rem.

### Mouvement
- **Une signature :** seule la scène du pont est pilotée par le défilement. Le logotype ne s'anime qu'une fois, au chargement.
- **Apparitions au défilement :** les blocs marqués montent de 18 px en fondu (600 ms d'opacité, 700 ms de déplacement), une seule fois, et seulement si JavaScript est actif.
- **Mouvement réduit :** la scène perd sa hauteur de défilement et s'affiche dans son état final (voiture levée, étiquettes visibles), le logotype est statique, les apparitions sont immédiates, le défilement doux est coupé.
- **Mode capture (?capture) :** mêmes états statiques que le mouvement réduit, avec une scène de hauteur fixe (780 px minimum) pour les captures pleine page.

## Do's and Don'ts

### Do:
- **Do** réserver le jaune (jaune) aux bras du pont, à l'action principale et à l'état actif, selon The Yellow Rule.
- **Do** composer chaque section sur l'un des deux fonds, nuit ou clair.
- **Do** porter la hiérarchie par la largeur d'Archivo : 118 % pour le titre de scène, 112 % pour les titres de section et de service, 125 % pour le logotype.
- **Do** dessiner au trait avec des extrémités arrondies, en acier pour la structure et en blanc atelier pour la voiture.
- **Do** utiliser les chiffres tabulaires pour les téléphones, horaires, étapes et codes.
- **Do** fournir un état final statique pour toute animation, en mouvement réduit comme en mode capture.
- **Do** garder des cibles tactiles d'au moins 2,75 rem.

### Don't:
- **Don't** ajouter une seconde animation pilotée par le défilement : le pont est la seule signature.
- **Don't** utiliser de photo d'atelier générique ni d'illustration décorative ; les emplacements photo restent des panneaux nuit-2 jusqu'à l'arrivée des vraies photos.
- **Don't** ajouter d'ombres portées ni de cartes flottantes.
- **Don't** mettre deux boutons jaunes côte à côte.
- **Don't** introduire une seconde famille de caractères.
- **Don't** reprendre la petite capitale espacée (comme « Exemple de suivi ») comme style de surtitre : c'est un défaut ouvert, pas une règle.

## Known open items

Le site a été livré à la demande du propriétaire alors que la dernière revue concluait encore « à corriger ». Ces points restent ouverts ; ils ne sont pas des règles et ne doivent pas être reproduits.

- Les pièces du dessous (carter, réservoir, bras de suspension) se lisent mal quand la voiture est levée.
- Sur le pont en version bureau, l'étiquette « Dépannage » croise la colonne droite et « Entretien » croise la roue avant.
- Sur téléphone, « Dépannage » va jusqu'au bord droit, et une bande vide d'environ 200 px reste sous la scène.
- L'icône native du sélecteur de date n'est pas mise aux couleurs du site.
- La légende « Exemple de suivi » est en petites capitales espacées, à la manière d'un surtitre.
