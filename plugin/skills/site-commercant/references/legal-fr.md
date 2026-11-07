# Obligations légales en France (site vitrine)

Ce n'est pas un conseil juridique : c'est le socle commun que tout site professionnel français doit respecter (loi pour la confiance dans l'économie numérique, dite LCEN, art. 6 ; RGPD ; directive ePrivacy et lignes directrices de la CNIL). En cas de doute (activité réglementée, données sensibles), conseille au commerçant de demander l'avis de sa CCI, de sa CMA ou de son comptable.

## 1. Mentions légales : `mentions-legales.html`

Elles sont obligatoires, et le lien doit apparaître dans le pied de page de **toutes** les pages.

**Éditeur du site**
- Entreprise individuelle ou micro-entreprise : nom et prénom de l'exploitant, nom commercial, adresse, téléphone, e-mail, numéro SIRET.
- Société : dénomination sociale, forme juridique (SARL, SAS…), capital social, adresse du siège, téléphone, e-mail, RCS + ville (ou numéro RM pour un artisan), SIRET.
- Numéro de TVA intracommunautaire, s'il y en a un.
- Activité réglementée : ordre professionnel, titre, règles applicables.
- **Directeur de la publication** : en général le gérant ou l'exploitant.

**Hébergeur** : nom, adresse, téléphone. Les coordonnées des hébergeurs courants sont dans `deploiement.md`.

**Propriété intellectuelle** : une phrase indiquant que les textes et photos appartiennent à l'entreprise, sauf mention contraire, avec les crédits photo éventuels.

Toute information manquante devient un `[À COMPLÉTER : numéro SIRET]`. **Jamais** de numéro fictif.

## 2. Confidentialité : `confidentialite.html`

Même un site vitrine traite des données personnelles dès qu'il a un formulaire, un lien e-mail ou des statistiques. La page indique, en langage simple :
- qui est responsable (l'entreprise, avec ses coordonnées) ;
- quelles données sont collectées et pourquoi (ex. : nom, e-mail et message du formulaire, pour répondre à la demande) ;
- la base légale (consentement, ou intérêt légitime pour répondre à une demande) ;
- combien de temps elles sont gardées (ex. : 3 ans après le dernier contact pour un prospect) ;
- qui y a accès (l'entreprise, le service de formulaire comme Netlify Forms ou Formspree, s'il y en a un) ;
- les droits de la personne (accès, rectification, effacement, opposition), comment les exercer, et la possibilité de saisir la CNIL (cnil.fr).

## 3. Cookies : rester simple

**Choix par défaut : aucun cookie non essentiel → aucun bandeau nécessaire.** C'est le choix le plus simple, le plus rapide et le plus respectueux. Concrètement :
- pas de Google Analytics, pas de pixel Facebook ou Meta, pas de vidéos YouTube intégrées directement ;
- pour Google Maps, préférer **un lien** « Voir sur Google Maps » (ou une image de carte statique enregistrée sur le site) plutôt qu'une carte intégrée en iframe, qui dépose des cookies ;
- les polices sont hébergées sur le site, pas chargées depuis Google Fonts (le transfert de l'adresse IP vers Google a été sanctionné en Europe) ;
- statistiques si le commerçant en veut : une solution exemptée de consentement selon la CNIL, correctement configurée (ex. : Plausible, Matomo en mode exempté, ou les statistiques de l'hébergeur).

Si le commerçant tient à un outil qui dépose des cookies (YouTube, carte intégrée, Analytics) : il faut un bandeau de consentement **avant** le dépôt, avec « Tout refuser » aussi visible que « Tout accepter ». Signale-le-lui, et la charge que ça ajoute, avant de l'installer.

Sur la page de confidentialité, indique clairement : « Ce site ne dépose aucun cookie de suivi. »

## 4. Autres points

- **Formulaire de contact** : demande seulement les champs nécessaires (nom, moyen de contact, message). Ajoute une phrase sous le bouton avec un lien vers la page de confidentialité. Pas de case précochée.
- **Prix affichés** : en euros TTC. Pour un restaurant, préciser « service compris » s'il est inclus.
- **Avis clients** : uniquement de vrais avis, avec leur source (ex. : « Avis Google »). Inventer ou sélectionner trompeusement des avis est une pratique commerciale trompeuse.
- **Photos** : uniquement des photos du commerçant ou sous licence libre, créditées si la licence l'exige. Une photo de banque d'images ne doit pas laisser croire qu'elle montre le commerce ou ses produits.
- **Médiateur de la consommation** : il n'est obligatoire pour le site que si le commerçant vend en ligne. Si c'est le cas, ajoute un `[À COMPLÉTER : médiateur de la consommation]` dans les mentions légales.
