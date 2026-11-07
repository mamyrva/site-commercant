# Partir d'une référence de style (DESIGN.md)

Un site d'agence se reconnaît à un système de design cohérent : une palette aux rôles précis, une échelle typographique, des composants et des règles « à faire / à ne pas faire ». Le moyen le plus rapide d'atteindre ce niveau, c'est de partir de la **référence de style d'un site que le commerçant aime**, puis de la traduire dans son univers. Testé le 2026-11-07 : la boulangerie d'exemple a été refaite à partir de la fiche de style d'une marque de condiments (« Hungry Tiger »), traduite en « or de croûte sur brun de four ».

## Où trouver une référence

- **styles.refero.design** : une bibliothèque de fichiers `DESIGN.md` tirés de vrais sites (Apple, Stripe, des marques alimentaires, de mode…), écrits pour les agents IA. On y cherche le site cité par le commerçant, ou un site du même esprit.
- Le commerçant peut aussi coller lui-même une fiche de style, comme Maxime l'a fait pour la boulangerie.
- À défaut, décris le site de référence toi-même : palette, polices, composants, règles.

## Comment la traduire (obligatoire)

La référence donne la **grammaire** (rôles des couleurs, échelle des titres, formes, densité, règles) ; le commerce donne **tout le reste**. Ne publie jamais un clone.

1. **Renomme** chaque couleur et chaque élément dans le monde du commerce : « Tiger Gold » devient « or de croûte », les feuillages en filigrane deviennent des épis de blé.
2. **Ajuste** les teintes si le métier le demande, en gardant les rôles : un seul accent, trois niveaux de surface.
3. **Remplace les polices propriétaires** par des polices libres proches, celles que la fiche suggère souvent elle-même (Antonio, Inter…). Elles sont hébergées sur le site.
4. **Ne reprends jamais** le nom, le logo, les textes, les photos ni les illustrations de la marque de référence.
5. **Garde les règles de fond** du skill : contraste AA, rien d'inventé, les informations pratiques en premier sur téléphone, le mouvement réduit.
6. Note dans `PRODUCT.md` (Brand Commitments) : « Style de référence : <nom>, traduit en <univers> ». Transmets la fiche traduite à impeccable comme direction imposée : une direction choisie par l'utilisateur l'emporte sur le tirage.

## Ce que la fiche impose souvent, et comment l'adapter à un commerce

- **Des titres énormes et peu de texte** : parfait pour l'accueil. Les horaires, l'adresse et le téléphone restent lisibles et présents dans le premier écran.
- **« Pas de texte courant au-delà de 18 px »** : à respecter, mais les informations pratiques passent avant le style.
- **Des produits posés à même le fond** : génère ou photographie les produits sur un fond de la couleur du site, puis fonds les bords avec un masque radial (`mask-image`).
