# Questionnaire du commerçant

Ne pose que les questions dont la réponse manque. Regroupe-les par trois au maximum dans l'outil de questions structurées, et propose des choix quand c'est possible (le commerçant clique plus volontiers qu'il n'écrit).

## Indispensable (avant de commencer)

| Information | Exemple de question | Choix proposés |
|---|---|---|
| Métier | « Quel est votre activité ? » | Boulangerie-pâtisserie · Restaurant/café · Coiffure/beauté · Artisan du bâtiment · Boutique · Autre |
| Nom et ville | « Comment s'appelle votre commerce, et dans quelle ville ? » | texte libre |
| Clientèle | « Qui sont vos clients principaux ? » | Familles du quartier · Actifs pressés · Touristes · Clientèle haut de gamme · Professionnels |
| Action principale | « Qu'est-ce qu'un visiteur doit faire en priorité ? » | Appeler · Venir en boutique · Réserver · Commander · Demander un devis |
| Style | « Quelle ambiance voulez-vous ? (2 ou 3 mots, ou un site que vous aimez) » | Chaleureux et artisanal · Moderne et épuré · Élégant et haut de gamme · Coloré et joyeux · Brut et authentique |

## Utile (un deuxième tour, ou des `[À COMPLÉTER]`)

- Adresse complète, téléphone, e-mail.
- Horaires d'ouverture, jours de fermeture, fermetures annuelles.
- Les produits ou services phares (3 à 6), avec les prix seulement si le commerçant veut les afficher.
- Ce qui rend le commerce différent : savoir-faire, histoire, labels réels, origine des produits.
- Photos et logo : demande le chemin du dossier. Pas de photos ? Le site doit rester beau sans elles (voir `structure-site.md`).
- Réseaux sociaux (Instagram, Facebook), lien de réservation ou de commande en ligne (TheFork, Planity, Uber Eats…).
- Lien Google Maps ou nom exact de la fiche Google.

## Pour les mentions légales (peut attendre la fin)

- Forme juridique : micro-entreprise / EI, EURL, SARL, SAS, SASU…
- Nom du responsable légal, numéro SIRET (ou SIREN + RCS/RM), capital social pour une société.
- Numéro de TVA intracommunautaire s'il en a un.
- Hébergeur choisi (souvent Netlify ou GitHub Pages : voir `deploiement.md`).

<a id="product-md"></a>
## Modèle de PRODUCT.md

Remplis-le avec les réponses confirmées uniquement. Une information manquante se note « non communiqué ». Ne la remplis pas au hasard.

```markdown
# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack
static HTML/CSS (site vitrine sans framework, hébergement statique gratuit)

## Users
[Clientèle principale et leur situation. Ex. : familles du quartier de la Croix-Rousse qui passent le matin avant l'école ; elles cherchent surtout les horaires et ce qu'il y a aujourd'hui.]

## Product Purpose
Site vitrine de [nom], [métier] à [ville]. Il doit amener le visiteur à [action principale], et rassurer sur [ce qui compte pour cette clientèle].

## Positioning
[Ce qui distingue vraiment ce commerce, d'après le commerçant. Jamais d'invention.]

## Operating Context
Les visiteurs arrivent surtout depuis Google Maps, une recherche « [métier] [ville] » ou Instagram, sur téléphone. Ils veulent en quelques secondes : horaires, adresse, téléphone, offre.

## Capabilities and Constraints
- Pages : [liste issue de metiers.md].
- Action principale : [appel / itinéraire / réservation via X / devis].
- Doit respecter les obligations françaises : mentions légales, confidentialité, pas de cookies non essentiels sans consentement.
- Aucune information non confirmée : les manques sont marqués [À COMPLÉTER].

## Brand Commitments
- Nom : [nom exact, avec sa graphie].
- Style demandé par le commerçant : « [ses mots, tels quels] ».
- Logo / couleurs existants : [chemin ou « aucun »].

## Evidence on Hand
- Photos : [chemin du dossier, ou « aucune : ne pas utiliser de photos de banque d'images présentées comme celles du commerce »].
- Avis clients : [réels, avec la source, ou « aucun : n'en afficher aucun »].

## Product Principles
1. Le visiteur sur téléphone trouve horaires, adresse et contact en moins de 5 secondes.
2. Le site donne envie de venir : il montre le savoir-faire, il ne liste pas des généralités.
3. Tout ce qui est affiché est vrai et vérifiable.

## Accessibility & Inclusion
Contrastes WCAG AA, texte lisible sans zoom sur téléphone, site utilisable au clavier, images décrites.
```
