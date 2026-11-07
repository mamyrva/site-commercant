# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack
Site statique HTML/CSS/JS, sans framework, hébergé gratuitement (Netlify). Les formulaires passent par Netlify Forms. Le contenu modifiable est dans `site/contenu/*.json`. Le site est publiable depuis `site/`.

## Users
- Les automobilistes de la région de Gap qui viennent pour un entretien, un diagnostic ou de la carrosserie. Ce sont des habitués ou de futurs habitués.
- Les touristes en panne sur la route des vacances, orientés vers le garage par leur assurance ou leur assistance. Ils sont stressés, sur téléphone, souvent loin de chez eux, parfois étrangers (d'où la version anglaise). Ils veulent savoir qu'on s'occupe d'eux et où en est leur voiture.

## Product Purpose
Site du Garage Delorme, garage automobile à Gap. Il présente clairement les services et rassure : on est entre de bonnes mains, avec un garage moderne et pointu. Il permet de prendre rendez-vous, de demander un devis et de suivre l'état de sa voiture.

## Positioning
Transparence et technique : rien n'est caché. Le client sait ce qu'on fait sur sa voiture et où en est la réparation.

## Operating Context
Situations de stress (panne, vacances interrompues) ou de routine (entretien). Visite surtout sur téléphone, parfois depuis le bord de la route ou l'hôtel. L'action se conclut par un appel, un rendez-vous, un devis ou le suivi du véhicule.

## Capabilities and Constraints
- **Pages :**
  - `index.html` : accueil avec les services ;
  - `suivi.html` : suivi de réparation par code ;
  - la version anglaise dans `en/` (accueil et suivi) ;
  - `mentions-legales.html` et `confidentialite.html`.
- **Services, tous confirmés :** entretien et révision, diagnostic électronique, dépannage et remorquage, carrosserie.
- **Fonctions :**
  - **Prise de rendez-vous :** un formulaire de demande. Le garage confirme ensuite par téléphone ; aucun outil de réservation n'est communiqué.
  - **Demande de devis :** un formulaire avec le véhicule, l'immatriculation facultative et le besoin.
  - **Suivi de réparation :** le client saisit le code remis au garage. L'état vient de `contenu/suivi.json`, qui contient uniquement des codes anonymes, sans nom ni plaque. Le garage met ce fichier à jour.
  - **Version anglaise.**
- **Mises à jour :** de temps en temps, par le garagiste. Les horaires, les congés et une annonce sont dans `contenu/infos.json`, et le suivi dans `contenu/suivi.json`.
- **Animation :** niveau « animé » (apparitions au défilement, réactions au survol), avec un logo animé en SVG/CSS. `prefers-reduced-motion` est respecté.
- **Horaires de l'atelier :** du lundi au vendredi, 8 h–12 h et 14 h–18 h 30 ; le samedi, 8 h–12 h ; fermé le dimanche. Les horaires du dépannage ne sont pas communiqués : [À COMPLÉTER].
- **Coordonnées :** 14 avenue d'Embrun, 05000 Gap. Téléphone : 04 92 00 00 00.
- **Rien d'inventé :**
  - pas d'agrément d'assureur ni de marque ;
  - pas de « 24 h/24 » ;
  - pas de délais ni de prix ;
  - pas d'années d'expérience ni d'avis.
- **Exemple fictif :** un bandeau doit l'indiquer.

## Brand Commitments
- **Style de référence imposé par l'utilisateur (2026-11-07)** : la fiche « Idle Finance » (styles.refero.design), traduite en terminal de diagnostic d'atelier : bleu nuit, un seul cyan (le voyant du diagnostic), halo bleu des phares, titres très gras avec un mot en cyan, pilules, cartes à filet noir, aucune ombre, services en onglets, grands chiffres vrais. Le pont élévateur reste la signature (au trait cyan). Le jaune et les photos de la version précédente sont retirés (version archivée).
- Nom : « Garage Delorme ».
- Ressenti voulu : « je suis entre de bonnes mains » et « c'est moderne et pointu ».
- Niveau de finition de référence : les sites des constructeurs automobiles (grandes images, peu de texte, précision). On ne copie jamais leur identité, leurs logos ni leurs noms.
- Idée unique : le pont élévateur. La voiture monte, on voit tout, rien n'est caché : c'est la transparence et la technique.
- Logo : aucun, un logotype animé est à créer.

## Evidence on Hand
- Photos : aucune. Le commerçant les fournira plus tard ; des emplacements élégants sont à prévoir.
- Avis : aucun.

## Product Principles
1. Rassurer d'abord : un visiteur en panne trouve en quelques secondes le téléphone, l'adresse et « on s'occupe de vous ».
2. Montrer plutôt qu'affirmer : la transparence se voit, notamment grâce au suivi de réparation.
3. Tout ce qui est affiché est vrai.

## Accessibility & Inclusion
WCAG AA. Le site doit rester lisible en plein soleil sur un téléphone (fort contraste), utilisable d'une main et en situation de stress. Il existe en anglais.
