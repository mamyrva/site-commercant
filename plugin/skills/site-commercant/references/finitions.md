# Les finitions qui se sentent

Le visiteur ne remarque jamais une bonne finition. Il remarque seulement que le site « fait pro », ou au contraire qu'il « fait bricolé », sans savoir dire pourquoi. Ce fichier rassemble ces détails invisibles : quand animer et comment, ce qui trahit un site web sur un téléphone, et les vraies données d'un commerce qui cassent une mise en page.

Lis-le à l'étape 4 (fonctions et animations), puis repasse sa liste de contrôle avant de livrer.

## 1. Animer, ou pas

Avant chaque animation, pose-toi deux questions.

**Combien de fois le visiteur va-t-il la voir ?**

| Fréquence | Décision |
|---|---|
| À chaque clic ou presque (menu du téléphone, onglets, filtres de la carte) | Très courte (moins de 0,2 s) ou aucune |
| De temps en temps (fenêtre de réservation, galerie qui s'ouvre, message envoyé) | Une animation normale |
| Une fois par visite (le grand moment du haut de page, la séquence filmée) | C'est là qu'on peut se faire plaisir |

Une action faite au clavier (Échap, Tab, flèches) ne s'anime jamais : l'animation la rend lente.

**À quoi sert-elle ?** Il faut pouvoir répondre en une phrase :
- **réagir** : le bouton s'enfonce sous le doigt, le site a « entendu » ;
- **montrer d'où vient un élément** : le menu sort du bouton qui l'a ouvert, la photo s'agrandit depuis sa vignette ;
- **montrer un changement d'état** : « Envoyé », « Ouvert maintenant » ;
- **raconter le métier** : la voiture qui monte sur le pont.

« C'est joli » ne suffit pas pour un élément vu souvent. Pour le moment fort du haut de page, si : c'est sa raison d'être.

## 2. Courbes et durées

- **Une chose qui arrive ou qui part : une courbe qui démarre vite et ralentit** (*ease-out*). Le site garde celle d'`excellence.md` : `cubic-bezier(.16,1,.3,1)`.
- **Jamais de courbe qui démarre lentement** (*ease-in*) pour une interface : le début est justement le moment où l'œil regarde, et le site paraît mou.
- **Une chose qui se déplace à l'écran** (un onglet qui glisse) : une courbe qui accélère puis ralentit (*ease-in-out*).
- **Un mouvement continu** (bandeau qui défile, barre de progression) : vitesse constante (*linear*).
- **Les durées :**

| Élément | Durée |
|---|---|
| Appui sur un bouton | 0,1 à 0,16 s |
| Info-bulle, petit menu | 0,12 à 0,2 s |
| Menu déroulant, liste | 0,15 à 0,25 s |
| Fenêtre, tiroir, menu du téléphone | 0,2 à 0,4 s |
| Scène qui raconte (haut de page, séquence filmée) | libre, pilotée par le défilement |

Règle simple : **une interface reste sous 0,3 s.** Plus c'est court, plus le site paraît rapide, même quand il ne l'est pas.

## 3. Ce qui se sent sous le doigt

- **Chaque élément cliquable s'enfonce un peu** quand on appuie : `transform: scale(.97)` sur `:active`, en 0,1 à 0,16 s. C'est le détail le plus rentable de tout ce fichier.
- **Rien n'apparaît à partir de rien.** Ne pars jamais de `scale(0)` : pars de `scale(.95)` avec `opacity: 0`. Un objet réel ne naît pas d'un point.
- **Un menu ou une info-bulle grandit depuis son bouton** (`transform-origin` du côté du bouton). Exception : une fenêtre centrée (réservation, photo agrandie) grandit depuis le centre.
- **Une animation doit pouvoir s'interrompre.** Si le visiteur rouvre le menu pendant qu'il se ferme, il doit repartir de là où il en est. Les transitions CSS le font ; les animations `@keyframes` repartent de zéro. Garde `@keyframes` pour ce qui se joue une seule fois.
- **Faire apparaître un élément sans JavaScript** : `@starting-style` décrit son état de départ, dans les navigateurs qui le gèrent. Ailleurs, l'élément apparaît sans animation, et c'est très bien.
- **Pour un fondu entre deux états qui « fait deux images superposées »**, un léger flou (2 à 4 px) pendant la transition fait croire à une seule transformation. Reste sous 20 px : le flou coûte cher, surtout sur iPhone.
- **Le survol n'existe pas au doigt** : tout ce qui est réservé au survol (un prix qui apparaît, une légende) doit aussi être visible ou accessible sans lui.

## 4. Fluide sur un vieux téléphone

- **N'anime que `transform` et `opacity`.** `filter`, `clip-path` et la couleur de fond passent bien aussi dans les navigateurs récents. Jamais `width`, `height`, `top`, `left` ni `margin` : chaque image redessine toute la page.
  - pour grandir ou rétrécir : `scale()` ;
  - pour déplacer : `translate()`. En pourcentage, il se calcule sur la taille de l'élément lui-même : `translateY(100%)` cache un tiroir quelle que soit sa hauteur ;
  - pour une ombre qui grandit : une ombre posée sur un pseudo-élément (`::after`) dont on anime l'opacité.
- **Jamais `transition: all`.** Écris les propriétés une par une, sinon des choses imprévues s'animent.
- **`will-change`** seulement si tu vois un saut d'un pixel au début ou à la fin d'une animation. Pas par habitude.
- **Le défilement reste celui du navigateur.** Une scène pilotée par le défilement lit la position, elle ne la contrôle jamais.

## 5. Ce qui trahit un site web sur un téléphone

C'est sur téléphone que les clients cherchent un commerce. Ces défauts ne se voient **pas** dans le mode « téléphone » d'un navigateur d'ordinateur : ils n'apparaissent que sur un vrai téléphone. Si tu ne peux pas tester, dis au commerçant lesquels vérifier sur le sien.

| Ce qu'on voit | La correction |
|---|---|
| Un bouton reste « survolé » après qu'on l'a touché | Mets tous les `:hover` dans `@media (hover: hover) and (pointer: fine)` |
| Un flash gris ou bleu quand on touche un lien | `html { -webkit-tap-highlight-color: transparent; }`, et un vrai `:active` partout |
| Le haut de page déborde sous la barre d'adresse | `min-height: 100svh` (pas `100vh`) pour le premier écran |
| La page zoome quand on touche un champ du formulaire | Champs en 16 px minimum. **Jamais** `user-scalable=no` : bloquer le zoom gêne les malvoyants |
| Le clic semble en retard | `touch-action: manipulation` sur les boutons et les liens |
| Un appui long sélectionne le texte du bouton | `user-select: none` **sur les boutons seulement**, jamais sur le texte : le client doit pouvoir copier l'adresse et le téléphone |
| Le menu du téléphone fait défiler la page derrière lui | `overscroll-behavior: contain` sur le menu |
| Une barre en bas d'écran passe sous la barre de l'iPhone | `viewport-fit=cover` dans la balise `viewport`, puis `padding-bottom: env(safe-area-inset-bottom, 0px)` |
| Un carrousel de photos fait bouger la page de haut en bas | Défilement natif avec `scroll-snap-type: x mandatory` |
| La barre du navigateur n'a pas la couleur du site | Une balise `theme-color` par thème (clair et sombre), de la couleur du **haut** de page |

Les champs du formulaire appellent le bon clavier : `type="tel"` pour le téléphone, `type="email"`, `inputmode="numeric"` pour un code postal, `autocomplete` renseigné (`name`, `tel`, `email`) pour que le téléphone remplisse tout seul.

Un site vitrine est un document : **laisse le « tirer pour actualiser »**. Ne mets `overscroll-behavior: none` sur toute la page que pour une vraie application.

## 6. Les vraies données d'un commerce

Une maquette est toujours belle avec des données choisies pour elle : « Chez Paul », 3 horaires, 4 produits. Les vraies données cassent la mise en page. Avant de livrer, remplace un instant le contenu par **le pire cas réaliste**, regarde à 320 px de large et avec le zoom du navigateur à 200 %, puis remets le vrai contenu.

**Le pire cas d'un commerce :**
- un nom long : « Boulangerie-Pâtisserie du Faubourg Saint-Nicolas » ;
- un nom très court : « Lo » ;
- une adresse e-mail sans coupure possible : `contact@boulangerie-patisserie-faubourg-saint-nicolas.fr` ;
- une adresse sur trois lignes, avec un bâtiment et un lieu-dit ;
- des horaires coupés le midi, un jour fermé, des horaires d'été, un jour férié ;
- un prix à quatre chiffres (« 1 249,00 € ») et un prix « sur devis » ;
- un seul avis (« 1 avis », pas « 1 avis(s) »), puis aucun ;
- une photo manquante, ou une photo en hauteur là où on en attendait une en largeur ;
- la version anglaise, souvent 20 à 30 % plus longue sur les boutons ;
- un plat ou un produit au nom très long dans la carte.

**Ce qui casse, et la correction :**

| Ce qu'on voit | La cause | La correction |
|---|---|---|
| Une icône ou un logo écrasé en ovale | L'élément rétrécit dans une ligne flexible | `flex-shrink: 0` sur l'icône |
| Le texte déborde au lieu d'aller à la ligne | Une colonne flexible ou de grille garde sa largeur minimale | `min-width: 0` sur la colonne de texte (`minmax(0, 1fr)` en grille) |
| L'e-mail sort de l'écran | Aucune coupure possible dans le mot | `overflow-wrap: anywhere` sur cet élément |
| Un mot de titre coupé n'importe où | `word-break: break-all` | `overflow-wrap: anywhere`, qui ne coupe que si c'est nécessaire |
| Un bouton traduit déborde | Largeur fixe | Largeur selon le contenu, avec un `min-width` |
| Les prix et horaires ne s'alignent pas | Chiffres de largeurs différentes | `font-variant-numeric: tabular-nums` |
| « 1249 », « NaN », « undefined » | Nombre affiché brut | `Intl.NumberFormat('fr-FR', …)` et une valeur de secours |
| « 1 avis(s) », « 0 avis » mal accordé | Pluriel écrit en dur | Une phrase par cas (aucun, un, plusieurs) |
| Un tiret ou une ligne vide là où manquait une info | On affiche un remplissage pour un champ vide | On n'affiche pas la ligne |
| Une icône d'image cassée | Pas de solution de secours | Un fond aux couleurs du site, et `object-fit: cover` |

**Couper, aller à la ligne, ou limiter :**
- **aller à la ligne** pour ce qui identifie (nom du commerce, nom d'un produit) ;
- **couper avec « … »** seulement pour un texte secondaire (un extrait d'avis), avec un moyen de lire la suite ;
- **limiter à 2 ou 3 lignes** (`line-clamp`) pour les descriptions dans des cartes, pour que les cartes gardent la même hauteur ;
- **ne jamais couper** un prix, un horaire, un numéro de téléphone ou une adresse.

## Le contrôle avant livraison

- [ ] Chaque animation a une raison, et celles qu'on voit souvent durent moins de 0,3 s.
- [ ] Aucune courbe *ease-in*, aucun `scale(0)`, aucun `transition: all`.
- [ ] Les boutons s'enfoncent sous le doigt.
- [ ] Seuls `transform` et `opacity` (ou `filter`, `clip-path`) sont animés.
- [ ] Les `:hover` sont réservés aux souris, le flash au toucher est supprimé, les champs font 16 px.
- [ ] Le zoom n'est pas bloqué, l'adresse et le téléphone restent copiables.
- [ ] Le pire cas réaliste ne casse rien à 320 px et avec un zoom à 200 %.
- [ ] Les défauts qu'on ne voit que sur un vrai téléphone sont signalés au commerçant s'ils n'ont pas pu être testés.

Ce guide s'inspire des principes de design d'interface publiés par Emil Kowalski (`emilkowalski/skills`, consulté le 2026-11-08). Il est réécrit avec nos mots et adapté aux sites de commerçants.
