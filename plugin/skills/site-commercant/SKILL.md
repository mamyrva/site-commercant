---
name: site-commercant
description: Crée, avec le commerçant et de A à Z, le site professionnel et personnalisé d'un petit commerce ou d'un artisan (boulangerie, coiffeur, restaurant, boutique, bijouterie, artisan, beauté, sport…) : entretien sur son idée du site, design sur mesure, animations, vidéo en motion design, fonctions dynamiques (réservation, formulaires, galerie, actualités, contenu modifiable). Utilise ce skill dès qu'un commerçant, un indépendant ou un artisan veut un site, une page web, une vitrine en ligne ou une « présence sur internet », même s'il ne dit pas « site vitrine ». Il gère l'entretien, les pages adaptées au métier, les mentions légales françaises, le référencement local et la mise en ligne gratuite. Le design passe par le skill impeccable.
argument-hint: "[métier, nom, ville, style voulu, pour qui]"
---

# Site commerçant

Tu fabriques le site d'un commerçant qui n'a pas le budget d'une agence mais mérite un site qui a l'air fait par une agence. Ton interlocuteur n'est souvent pas technicien : parle-lui simplement, sans jargon, **dans sa langue** (le français par défaut), et fais le travail technique à sa place. Les obligations légales décrites ici sont celles de la France. Pour un commerce situé dans un autre pays, dis-le et adapte la partie légale en vérifiant la loi locale.

Le résultat attendu : un site **personnalisé de A à Z**, qui ressemble au commerce et à l'idée que la personne s'en fait, et non un modèle rempli. Il peut être animé, contenir une vidéo en motion design et des fonctions dynamiques (réservation, formulaires, galerie, actualités, contenu modifiable). Il reste hébergé gratuitement en statique (HTML, CSS, JavaScript, sans serveur à entretenir), charge vite, s'affiche bien sur téléphone, respecte la loi française et fait venir des clients.

## Règle d'or : ne jamais inventer

Un faux avis client, un faux prix, une fausse adresse ou un faux numéro de SIRET peuvent coûter cher au commerçant : publicité trompeuse, perte de confiance, mentions légales fausses. Tout fait que tu n'as pas reçu devient un repère visible `[À COMPLÉTER : …]` dans la page. À la fin, tu en donnes la liste complète. Tu peux rédiger des textes d'ambiance (accroches, présentation), mais jamais affirmer un fait non confirmé : « depuis 1987 », « 4,9 étoiles », « produits 100 % bio »…

## Étape 1 : l'entretien

Lis d'abord ce que la personne a déjà donné : le brief en argument, une `fiche-commerce.md` remplie, des photos, un logo, des vidéos. Puis mène l'entretien décrit dans [references/entretien.md](references/entretien.md), avec l'outil de questions structurées (AskUserQuestion), en trois tours au plus :

1. **l'essentiel**, s'il manque : métier, nom, ville, clientèle, action principale (détail dans [references/questionnaire.md](references/questionnaire.md)) ;
2. **la vision** : ce que le client doit ressentir, les sites que la personne aime, le niveau d'animation, une vidéo en motion design ou non, et l'idée, l'objet ou le souvenir qui représente vraiment le commerce ;
3. **les fonctions** : ce que le site doit permettre (réserver, demander un devis, galerie, actualités, carte modifiable, langues, avis…) et qui le mettra à jour.

Ne pose que les questions dont la réponse manque, et termine par une phrase qui résume ce que tu as compris. Les faits pratiques (horaires, SIRET, adresse…) peuvent rester `[À COMPLÉTER]` : ne bloque pas le travail pour ça.

## Étape 2 : préparer le projet

1. Crée le dossier du projet `<nom-du-commerce-en-minuscules-avec-tirets>/` dans le dossier courant, sauf si la personne a indiqué un autre endroit. Les fichiers de travail (`PRODUCT.md`, `DESIGN.md`) vont à sa racine, et le site publiable dans son sous-dossier `site/`, selon [references/structure-site.md](references/structure-site.md).
2. Choisis les pages avec [references/metiers.md](references/metiers.md). Vise peu de pages, mais complètes. Pour la plupart des commerces, une page d'accueil riche, plus les mentions légales et la confidentialité, suffisent.
3. Prévois chaque fonction choisie selon [references/fonctionnalites.md](references/fonctionnalites.md) : quel service, quel compte à créer, quels fichiers (`site/contenu/*.json`, formulaire, interface d'administration).
4. Écris `PRODUCT.md` à la racine du site, au format impeccable. Le modèle prérempli est dans [references/questionnaire.md](references/questionnaire.md#product-md). Inscris `static HTML/CSS` sous `## Stack` et `web` sous `## Platform`. Mets le style voulu, les sites de référence et l'idée unique dans `## Brand Commitments` : ce sont des choix de la personne, et impeccable doit les respecter. Mets les fonctions, le niveau d'animation et la vidéo dans `## Capabilities and Constraints`.

## Étape 3 : le design avec impeccable

**Partir d'une référence de style.** Si la personne cite un site qu'elle aime, ou colle une fiche de style, suis [references/reference-style.md](references/reference-style.md) : trouve son `DESIGN.md` (par exemple sur styles.refero.design), traduis-le dans l'univers du commerce, puis transmets-le à impeccable comme direction imposée.

**Vise l'exceptionnel, pas le correct.** Avant de construire, lis [references/excellence.md](references/excellence.md) : le test de l'image fixe, les images, le mouvement mis en scène et la performance. Repasse sa liste de contrôle avant de livrer. Un site sans images paraît inachevé : règle la question des photos avec la personne dès l'entretien.

Charge le skill `impeccable` (outil Skill, nom `impeccable:impeccable`) et fais une demande de nouvelle surface (new-work) : la page d'accueil du commerce, en mode **Persuade**. Donne-lui :

- le fichier `PRODUCT.md` que tu viens d'écrire. Comme il existe déjà, impeccable n'a pas besoin de refaire son entretien produit ;
- le style demandé par le commerçant, tel quel ;
- les contraintes de [references/structure-site.md](references/structure-site.md) : HTML/CSS statique, pas de framework, pas de CDN obligatoire, polices hébergées sur le site ;
- la liste des pages et des sections choisies à l'étape 2 ;
- le niveau d'animation (sobre, animé ou spectaculaire) et l'idée unique qui doit nourrir la direction visuelle.

Suis ensuite les étapes d'impeccable (direction visuelle, `DESIGN.md`, construction). Si impeccable pose des questions de direction artistique, transmets-les à la personne avec des mots simples. Si la personne rejette une direction parce qu'elle « ne fait pas pro » ou « pas comme une vraie marque », prends la voie classique de la catégorie (la carte « standard » d'impeccable) et demande-lui 2 ou 3 sites de référence qu'elle aime. Construis toutes les pages dans le même univers visuel.

**Si le skill impeccable n'est pas installé**, dis-le en une phrase et donne la commande : `/plugin marketplace add pbakaus/impeccable`, puis `/plugin install impeccable@impeccable`. Continue ensuite avec les règles de [references/structure-site.md](references/structure-site.md), en particulier sa section « Design ».

## Étape 4 : fonctions, animations et vidéo

- **Fonctions dynamiques** : construis chacune comme décrit dans [references/fonctionnalites.md](references/fonctionnalites.md), dans l'univers visuel d'impeccable. Teste chaque fonction pour de vrai : envoi du formulaire, ouverture de la galerie au clavier et au doigt, affichage des actualités depuis le fichier JSON.
- **Animations** : au niveau choisi, toujours avec `prefers-reduced-motion`.
- **Vidéo en motion design** : si elle a été demandée, suis [references/motion.md](references/motion.md). Le skill `hyperframes` sert à la produire s'il est installé ; sinon, l'animation se fait en SVG et CSS.

## Étape 5 : la couche commerçant

Ces éléments distinguent un site pro d'un site amateur. Impeccable ne les connaît pas, alors ajoute-les toi-même :

- **Obligations légales françaises** : lis [references/legal-fr.md](references/legal-fr.md). Les mentions légales, la page de confidentialité et la question des cookies sont obligatoires.
- **Référencement local** : lis [references/seo-local.md](references/seo-local.md). Il couvre les balises title et description, les données structurées `LocalBusiness`, Open Graph, `sitemap.xml`, `robots.txt` et le lien Google Maps.
- **Contact en un geste** : un numéro de téléphone cliquable (`tel:`), un bouton d'itinéraire, et les horaires visibles sans avoir à chercher.

## Étape 6 : vérifier

1. Lance `python3 "${CLAUDE_SKILL_DIR}/scripts/verifier.py" <dossier-du-site>` et corrige tout ce qui est marqué ERREUR. Les éléments marqués À COMPLÉTER sont normaux et seront listés à la livraison.
2. Lance `/impeccable audit` sur le site (accessibilité, performance, responsive), puis `/impeccable polish`.
3. Regarde le rendu à 390 px (téléphone) et à 1440 px (ordinateur). La plupart des visiteurs d'un commerce de quartier arrivent sur téléphone, donc vérifie surtout qu'aucun texte ne déborde à droite. Attention : Chrome sans interface (`--headless`) n'affiche pas une page à moins d'environ 500 px de large, et une capture « 390 px » faite directement est donc fausse. La bonne méthode :
   - lance `python3 -m http.server 8765 --bind 127.0.0.1` depuis le dossier du projet, en arrière-plan ;
   - crée une page d'encadrement qui contient `<iframe src="/site/index.html" style="border:0;width:390px;height:3600px;display:block;margin:0 auto">` ;
   - capture-la avec `--window-size=800,3600 --force-device-scale-factor=1`, puis recadre le centre sur 390 px de large (`sips -c 3600 390` sur macOS).
   - Une capture « pleine page » faite avec une fenêtre très haute fausse tout ce qui dépend de la hauteur de l'écran (`vh`, scènes collantes animées au défilement). Prévois dans le site un mode `?capture` qui affiche l'état statique (le même que le mouvement réduit). Capture ensuite les moments animés à la vraie taille d'écran (1440×900, 390×844), en faisant défiler une iframe par script avec `scrollTo({ top, behavior: "instant" })`.
4. Teste chaque fonction pour de vrai dans le navigateur (suivi, galerie, formulaire…) en la pilotant par script dans une iframe, puis regarde la capture. Un formulaire Netlify ne peut pas s'envoyer en local : vérifie qu'il affiche un message d'erreur utile (« appelez-nous ») plutôt que rien.

## Étape 7 : livrer

Termine par un message court et simple, qui contient :

1. ce qui a été créé (les pages, les fonctions, la vidéo) et comment ouvrir le site en local (double-clic sur `index.html`) ;
2. **la liste des `[À COMPLÉTER]`**, regroupés par page, formulés comme des questions simples : « Quel est votre numéro de SIRET ? » ;
3. la mise en ligne gratuite, en suivant [references/deploiement.md](references/deploiement.md). Propose la méthode la plus simple (Netlify Drop, un glisser-déposer) et offre de le faire avec la personne ;
4. ce que la personne doit faire pour les fonctions : comptes à créer, comment mettre à jour son contenu (et `GUIDE-MISE-A-JOUR.md` si une interface d'administration a été installée) ;
5. la checklist Google de [references/seo-local.md](references/seo-local.md#après-la-mise-en-ligne--la-checklist-google), surtout la fiche Google Business Profile, la Search Console et les avis de vrais clients.

Si la personne fournit plus tard les informations manquantes, remplace les repères, relance le script de vérification et redonne la liste de ce qui reste.
