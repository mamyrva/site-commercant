# Les fonctions dynamiques

Le site reste **hébergé gratuitement en statique** (Netlify ou GitHub Pages). « Dynamique » veut dire ici : des éléments qui réagissent, des contenus que le commerçant peut changer, et des services qui fonctionnent vraiment. Il n'y a pas de serveur à entretenir. Pour chaque fonction, choisis la solution la plus simple qui marche, et dis clairement à la personne ce qu'elle doit créer (un compte, un abonnement éventuel).

**Avant d'installer un service tiers**, vérifie sur sa documentation actuelle (avec une recherche web) les conditions de la formule gratuite. Elles changent souvent.

## Réserver ou prendre rendez-vous

- **Le commerçant utilise déjà un outil** (Planity, TheFork, Zenchef, Treatwell, Calendly…) : un grand bouton « Réserver » qui ouvre sa page de réservation. C'est le plus fiable, et il n'y a aucun cookie sur le site.
- **Il veut le calendrier intégré dans la page** : l'intégration (iframe) de ces outils dépose des cookies. Il faut alors le bandeau de consentement décrit dans `legal-fr.md`, ou un clic « Afficher le calendrier » qui ne charge l'iframe qu'après accord. Préfère cette seconde solution.
- **Il n'a pas d'outil** : propose un formulaire « Demande de réservation » (voir ci-dessous), en précisant que la boutique confirme par téléphone ou par e-mail.

## Formulaire de contact ou de devis

- **Sur Netlify** : un `<form data-netlify="true" name="contact">` classique. Les messages arrivent dans le tableau de bord Netlify et peuvent être transférés par e-mail. Ajoute un champ piège anti-spam (`netlify-honeypot`).
- **Sinon** : Formspree ou Web3Forms (formules gratuites limitées), avec `action="https://…"`.
- **Toujours** :
  - un message de confirmation clair et une page ou un message d'erreur ;
  - seulement les champs utiles ;
  - un lien vers la page de confidentialité sous le bouton ;
  - la page de confidentialité mise à jour (le service utilisé, la durée de conservation).

## Galerie de photos ou de réalisations

- Une grille d'images en `loading="lazy"` qui s'ouvrent en grand dans un `<dialog>` natif, avec flèches, touche Échap et balayage sur téléphone.
- Les images sont redimensionnées : une vignette d'environ 600 px et une grande image de 1600 px au plus.
- Pour ajouter des photos facilement, la liste est dans `contenu/galerie.json` (voir « Contenu modifiable »).

## Actualités, événements, plat du jour

- Un fichier `contenu/actualites.json` (titre, date, texte, image), affiché par un petit script.
- Le HTML contient aussi une version de secours, écrite en dur, pour Google et pour les navigateurs sans JavaScript.
- Les actualités dont la date est passée se masquent toutes seules.

## Carte, menu ou catalogue modifiable

- Le même principe : `contenu/carte.json`, avec sections, plats, descriptions, prix (confirmés), et des étiquettes « végétarien » ou « fait maison » si elles sont confirmées.
- Pour un restaurant, la carte reste en HTML et jamais en PDF seul (voir `metiers.md`).

## Contenu modifiable par le commerçant

Choisis selon la réponse « Qui mettra le site à jour ? » :

1. **Presque jamais** : tout est écrit dans le HTML, avec des commentaires `<!-- MODIFIER ICI -->` aux endroits qui changent.
2. **De temps en temps** : les contenus qui bougent sont dans `site/contenu/*.json`. Explique à la personne comment modifier un fichier et republier : sur Netlify Drop, il suffit de glisser à nouveau le dossier.
3. **Souvent** : une interface d'administration gratuite branchée sur un dépôt GitHub (par exemple Pages CMS ou Decap CMS). Le commerçant se connecte, modifie un formulaire, et le site se met à jour tout seul. Cela demande un compte GitHub et un hébergement relié au dépôt (Netlify ou GitHub Pages). Vérifie la documentation actuelle de l'outil avant de l'installer, et rédige un mini-guide pas à pas dans `GUIDE-MISE-A-JOUR.md`.

## Suivi de réparation, de commande ou de dossier

Testé le 2026-11-07 avec le Garage Delorme (`exemples/garage-delorme/site/suivi.html`).

- Le client saisit un **code tiré au hasard**, remis par le commerçant. La page lit `contenu/suivi.json`, qui contient le code, l'étape (1 à 4) et une note facultative en français et en anglais.
- **Jamais de nom, de plaque, de téléphone ni d'adresse dans ce fichier** : il est public.
- Le commerçant supprime le dossier une fois l'affaire terminée. Ajoute dans le fichier une clé `_aide` qui explique comment le mettre à jour.
- Si les mises à jour sont fréquentes (plusieurs par jour), republier le site devient lourd. Propose alors l'interface d'administration (Pages CMS ou Decap CMS), ou une feuille Google Sheets publiée en CSV. Pour cette seconde solution, vérifie d'abord les implications RGPD : le site enverra une requête à Google.

## Plusieurs langues

- Une page par langue (`/en/index.html`…), traduite proprement, avec un sélecteur de langue visible. Génère les deux langues à partir d'**un seul modèle** (un petit script Python avec un dictionnaire de textes par langue, comme `exemples/garage-delorme/.impeccable/generer.py`), pour que les versions ne divergent jamais.
- Ajoute des balises `<link rel="alternate" hreflang="…">` sur chaque page et `lang` sur `<html>`.
- Fais relire la traduction par la personne ou par quelqu'un qui parle la langue ; ne l'affiche jamais comme « officielle » sans relecture.

## Avis clients

- Un lien « Voir nos avis Google » vers la fiche du commerce.
- Tu peux citer quelques avis réels, recopiés avec l'accord du commerçant, avec leur source et leur date.
- Pas de widget d'avis tiers sans consentement, et jamais d'avis inventés.

## Commander ou acheter en ligne

Une vraie boutique en ligne (paiement, stocks, livraisons, conditions générales de vente, droit de rétractation, médiateur de la consommation) dépasse ce skill. Propose :

- un lien vers un service existant (Uber Eats, Deliveroo, Click and Collect, boutique Shopify, Etsy…) ;
- ou des liens de paiement simples (Stripe Payment Links, SumUp) pour quelques produits, en signalant que les conditions générales de vente deviennent alors obligatoires.

## Les animations

Le niveau choisi pendant l'entretien est transmis à impeccable, qui les dessine. Règles techniques :

- **Sobre** : un seul moment animé, par exemple l'apparition du haut de page.
- **Animé** : apparitions au défilement (IntersectionObserver), réactions au survol, transitions entre les pages (View Transitions API).
- **Spectaculaire** : un effet interactif en haut de page qui raconte le métier (par exemple un réseau de points qui réagit à la souris pour une agence, la vapeur d'un four, des épis qui bougent au passage), en `<canvas>` léger, arrêté hors de l'écran et désactivé en mouvement réduit ;
   animations liées au défilement (`animation-timeline: scroll()`, avec une solution de repli), canvas ou SVG animé, vidéo en motion design.
- **Toujours** :
  - le contenu reste visible sans animation ;
  - `prefers-reduced-motion` désactive tout mouvement non essentiel ;
  - le site reste rapide sur un vieux téléphone ;
  - il n'y a jamais de bibliothèque chargée depuis un CDN externe : si une bibliothèque est nécessaire, elle est copiée dans `site/js/`.
