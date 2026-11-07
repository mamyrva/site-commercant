# Référencement local

> Mis à jour le 2026-11-07. Le référencement change souvent : avant une livraison, vérifie les points marqués « à revérifier » sur la documentation officielle de Google (developers.google.com/search et support.google.com/business).

Le but : apparaître quand quelqu'un tape « [métier] [ville] » ou « [métier] près de moi », et donner une bonne image quand le lien est partagé.

## Ce que Google regarde vraiment (2026)

- **Les trois critères officiels du classement local** : la **pertinence** (le commerce correspond-il à la recherche ?), la **distance** et la **notoriété** (avis, mentions, liens, présence sur le web). On ne change pas la distance : tout le travail porte sur la pertinence et la notoriété.
- **La fiche Google Business Profile compte plus que le site.** C'est le levier le plus fort pour apparaître dans le « pack local » (la carte avec 3 commerces). Les experts placent la **catégorie principale** de la fiche en tête des facteurs. Le site sert à confirmer et à compléter la fiche : mêmes nom, adresse, téléphone et horaires, au caractère près.
- **Les avis réels** (nombre, fraîcheur, réponses du commerçant) et les **mentions par d'autres sites locaux** (mairie, office de tourisme, presse locale, associations, fournisseurs) pèsent sur la notoriété.
- **La vitesse et la stabilité** (Core Web Vitals, mesurés sur de vrais visiteurs) : affichage du contenu principal (LCP) en 2,5 s au plus, réaction aux clics (INP) en 200 ms au plus, pas de saut de mise en page (CLS ≤ 0,1). Un site statique léger, comme ceux de ce skill, les passe facilement, à condition de garder les images et les vidéos légères. Seuils inchangés depuis 2024, à revérifier.
- **Les réponses générées par IA** (AI Overviews, mode IA de Google) prennent une grande place dans les recherches locales, et beaucoup de visiteurs ne cliquent plus. Pour y être cité :
  - une fiche Google complète et cohérente avec le site ;
  - des textes qui **répondent directement** aux vraies questions des clients, en une ou deux phrases claires (« Êtes-vous ouverts le dimanche ? », « Faites-vous les gâteaux sans gluten ? ») ;
  - des photos réelles, sur le site et sur la fiche ;
  - des avis et des mentions par d'autres sites.

## Bloc « Questions fréquentes »

Ajoute une courte section de 4 à 6 questions que les clients posent vraiment au commerçant (demande-les-lui pendant l'entretien), avec des réponses courtes et exactes. Elle aide les visiteurs et les réponses générées par IA. N'attends pas d'affichage spécial dans Google : le résultat enrichi « FAQ » est réservé depuis 2023 à certains sites officiels. Le balisage `FAQPage` reste facultatif. Si tu l'utilises, il doit reprendre exactement le texte visible.

## Dans chaque page (`<head>`)

```html
<html lang="fr">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>[Nom] · [Métier] à [Ville]</title>  <!-- 50 à 60 caractères, unique par page -->
<meta name="description" content="[Phrase concrète : ce qu'on y trouve, où, l'action principale]. ">  <!-- 140 à 160 caractères -->
<link rel="canonical" href="https://[domaine]/[page]">
<meta property="og:type" content="website">
<meta property="og:title" content="[Nom] · [Métier] à [Ville]">
<meta property="og:description" content="[même idée que la description]">
<meta property="og:image" content="https://[domaine]/images/partage.jpg">  <!-- 1200×630 -->
<meta property="og:locale" content="fr_FR">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">  <!-- 180×180 -->
<meta name="theme-color" content="[couleur principale]">
```

Le domaine est inconnu avant la mise en ligne : mets `[À COMPLÉTER : adresse du site]` dans `canonical`, `og:image` et le sitemap, puis remplace-le après le déploiement (voir `deploiement.md`).

## Données structurées (page d'accueil)

Utilise le type schema.org le plus précis possible : `Bakery`, `Restaurant`, `CafeOrCoffeeShop`, `HairSalon`, `BeautySalon`, `NailSalon`, `Plumber`, `Electrician`, `HousePainter`, `GeneralContractor`, `ClothingStore`, `Florist`, `BookStore`, `ExerciseGym`, `SportsActivityLocation`… Sinon, `LocalBusiness`.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Bakery",
  "name": "[Nom]",
  "url": "https://[domaine]/",
  "image": "https://[domaine]/images/partage.jpg",
  "telephone": "+33[numéro sans le 0]",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "[rue]",
    "postalCode": "[CP]",
    "addressLocality": "[Ville]",
    "addressCountry": "FR"
  },
  "openingHoursSpecification": [
    { "@type": "OpeningHoursSpecification", "dayOfWeek": ["Tuesday","Wednesday","Thursday","Friday","Saturday"], "opens": "07:00", "closes": "19:30" }
  ],
  "sameAs": ["[Instagram]", "[Facebook]"]
}
</script>
```

Règles :
- **Les données structurées doivent correspondre au contenu visible de la page.** Un balisage qui affirme ce que la page ne montre pas (horaires différents, avis absents) peut être sanctionné. Elles rendent la page éligible à un affichage enrichi, sans le garantir.
- **Le JSON doit être valide** : le script de vérification le contrôle.
- Ne mets que des champs confirmés. Un champ inconnu est **retiré** du JSON, sans repère `[À COMPLÉTER]` (Google ignorerait la donnée ou signalerait une erreur). Signale-le plutôt dans la liste de livraison.
- Pas de `aggregateRating` ni de `review` inventés. Google pénalise les avis autoproclamés sur sa propre page.
- Pour un restaurant : `servesCuisine`, `priceRange` (ex. `"€€"`), `menu` (URL de `carte.html`), `acceptsReservations`.
- Pour un artisan : `areaServed` avec la liste des villes.

## Contenu

- Un seul `<h1>` par page, qui dit le métier et la ville avec des mots naturels : « Boulangerie artisanale à Villeurbanne », pas « Bienvenue ».
- Le nom, l'adresse et le téléphone (le « NAP ») doivent être **écrits exactement comme sur la fiche Google** du commerce.
- Des textes concrets : les vrais produits, les quartiers desservis, les spécialités. Google et les clients récompensent le spécifique.
- Chaque image porte un `alt` qui la décrit vraiment (« Baguettes tradition sur une grille de refroidissement »), ou `alt=""` si elle est purement décorative.
- Un lien d'itinéraire : `https://www.google.com/maps/search/?api=1&query=[Nom+adresse+encodés]`.

## Fichiers à la racine

`robots.txt` :
```
User-agent: *
Allow: /
Sitemap: https://[domaine]/sitemap.xml
```

`sitemap.xml` : liste toutes les pages, mentions légales et confidentialité comprises.

## Après la mise en ligne : la checklist Google

1. **Google Business Profile** (business.google.com) : créer ou réclamer la fiche ; choisir la catégorie principale la plus précise ; remplir horaires, horaires exceptionnels, services, description, attributs et photos ; mettre le lien du site.
2. **Google Search Console** (search.google.com/search-console) : ajouter le site, valider la propriété (fichier HTML ou balise `<meta>`), puis envoyer `sitemap.xml`. Surveiller les rapports « Pages » et « Signaux Web essentiels ».
3. **Cohérence** : nom, adresse et téléphone identiques sur le site, la fiche Google, Pages Jaunes, Apple Plans, Bing Places, les réseaux sociaux et les annuaires du métier.
4. **Avis** : demander régulièrement à de vrais clients (un QR code en caisse vers la fiche), et répondre à tous les avis, y compris les négatifs.
5. **Mentions locales** : demander un lien depuis le site de la mairie, de l'office de tourisme, de l'association des commerçants, des fournisseurs, de la presse locale.
6. **Faire vivre** : publier des posts sur la fiche Google (nouveautés, événements) et mettre à jour les horaires exceptionnels (fêtes, congés).

Sources consultées le 2026-11-07, à revérifier : aide Google Business Profile (« Améliorer votre classement local »), documentation Google Search Central (données structurées LocalBusiness, Core Web Vitals), synthèses 2026 d'experts du référencement local (Whitespark Local Search Ranking Factors).
