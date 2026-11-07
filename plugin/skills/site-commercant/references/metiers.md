# Pages et sections selon le métier

Principe : **une page d'accueil riche plutôt que cinq pages vides.** Le visiteur sur téléphone fait défiler, il ne navigue pas. Ajoute une page séparée seulement quand le contenu est long : une carte de restaurant complète, un portfolio de chantiers, une grille de tarifs détaillée.

Toujours présents, quel que soit le métier :
- `index.html` : l'accueil ;
- `mentions-legales.html` ;
- `confidentialite.html` ;
- un bloc **Infos pratiques**, visible dès le haut de la page sur téléphone (ou à un clic) : horaires, adresse, téléphone cliquable, bouton « Itinéraire » ;
- le pied de page : coordonnées, réseaux sociaux, liens vers les pages légales.

## Boulangerie, pâtisserie, chocolatier, fromager, caviste, primeur (commerce de bouche)
- **Accueil** : accroche + produit signature, savoir-faire (fait maison, farines, origine : seulement si c'est confirmé), produits phares par catégorie, commandes spéciales (gâteaux, événements), infos pratiques.
- **Action principale** : venir en boutique ou appeler pour une commande.
- **Ce que le client cherche** : « ouvert maintenant ? », « dimanche ? », commandes pour les fêtes.

## Restaurant, café, bar, traiteur
- **Accueil** : ambiance (une photo forte), type de cuisine, extrait de la carte, réservation, infos pratiques.
- **`carte.html`** si la carte est longue. Écris-la en HTML, jamais en PDF seul : un PDF se lit mal sur téléphone et Google ne le comprend pas. Les prix viennent exclusivement du commerçant.
- **Action principale** : réserver (lien TheFork/Zenchef s'il existe, sinon le téléphone).
- **Obligation** : l'origine des viandes bovines doit être affichée sur la carte si le restaurant en sert. Ajoute un `[À COMPLÉTER]` si l'information manque.

## Coiffure, barbier, esthétique, onglerie, spa
- **Accueil** : univers du salon, prestations principales, équipe (avec l'accord des personnes), réservation, infos pratiques.
- **`tarifs.html`** si la grille est longue. L'affichage des prix des prestations est une obligation en salon ; sur le site, c'est un plus fort.
- **Action principale** : prendre rendez-vous (lien Planity/Treatwell s'il existe, sinon le téléphone).

## Artisan du bâtiment (plombier, électricien, menuisier, peintre…)
- **Accueil** : métier et zone d'intervention (villes), services, réalisations avec photos de vrais chantiers, gages de confiance réels (assurance décennale, labels RGE ou Qualibat s'ils sont confirmés), demande de devis.
- **`realisations.html`** s'il y a beaucoup de photos de chantiers.
- **Action principale** : appeler ou demander un devis (formulaire simple : voir `structure-site.md`).
- **Obligation** : l'assurance décennale (assureur et zone couverte) doit figurer sur les devis. Sur le site, la mentionner rassure : ne l'affiche que si elle est confirmée.

## Boutique (mode, déco, cadeaux, librairie, fleuriste…)
- **Accueil** : univers de la boutique, sélection ou nouveautés, marques ou créateurs (s'ils sont confirmés), services (emballage cadeau, livraison locale), infos pratiques, Instagram.
- **Action principale** : venir en boutique. Un site e-commerce sort du cadre de ce skill : propose plutôt un lien vers une boutique en ligne existante.

## Bijouterie, joaillerie, horlogerie
- **Accueil** : une pièce ou une création signature en très grand, le savoir-faire de l'atelier (création sur mesure, réparation, entretien de montres), les familles de produits (bagues, alliances, colliers, montres), les marques distribuées, puis la visite en boutique (adresse, horaires, accès, sonnette ou porte sécurisée s'il y en a une).
- **`atelier.html`** si l'atelier de création ou de réparation est un vrai argument : étapes du sur-mesure, services, délais confirmés.
- **Action principale** : venir en boutique. La décision d'achat se prend sur place : le site doit rassurer et donner envie de pousser la porte.
- **Marques** : n'affiche le nom ou le logo d'une marque de montres ou de bijoux, ou les mots « revendeur agréé » ou « officiel », **que si le commerçant le confirme**. Ces marques contrôlent strictement leur réseau de distribution, et leurs logos sont protégés. Sans confirmation : `[À COMPLÉTER : marques dont vous êtes revendeur agréé]`.
- **Garanties et métaux** : ne mentionne les titres (or 750 ‰, argent 925 ‰), les poinçons, les certificats de pierres (GIA, HRD…) ou les garanties qu'avec la confirmation du commerçant.
- **Images** : les visuels officiels des marques sont soumis à leurs conditions d'utilisation. Préfère les photos de l'atelier et des créations maison.
- **Prix** : souvent pas affichés dans le luxe. Si c'est le cas, une formule du type « sur demande en boutique » suffit.
- **Style « luxe »** : un commerçant qui dit « luxe », même « audacieux », veut en général **ressembler à une grande maison** : fond blanc, beaucoup d'espace, typographie très fine, une couleur signature, de grandes photos. Demande-lui 2 ou 3 marques dont il aime le site (pour le niveau de finition, sans jamais copier leur identité), et propose cette voie classique **avant** les directions décalées. Testé le 2026-11-07 : une façade de pierre gravée, pourtant soignée, a été rejetée (« pas comme une vraie marque de luxe ») ; la version sobre façon Tiffany/Messika a été retenue.
- **Sans photos** : remplace chaque photo par un dessin au trait de bijoutier (griffes, facettes, maillons, carrure de montre) avec la mention « Photo à venir ». Le site reste élégant en attendant les vraies photos.

## Sport, bien-être, cours (coach, yoga, danse, auto-école…)
- **Accueil** : approche, cours ou formules, planning, tarifs, présentation du ou des coachs, premier cours d'essai si le commerçant en propose un, contact.
- **Action principale** : réserver un cours ou un essai.

## Autre métier
Raisonne avec trois questions : que cherche le client en premier, qu'est-ce qui le rassure, quelle action le fait devenir client ? Construis l'accueil dans cet ordre.
