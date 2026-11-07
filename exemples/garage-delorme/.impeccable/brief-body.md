# Surface : accueil Garage Delorme (+ suivi, + version anglaise)

Scope : site/index.html, site/suivi.html, site/en/index.html, site/en/suivi.html, pages légales. Mode : Persuade.
Audience : automobilistes de la région ; touristes en panne orientés par leur assistance, stressés, sur téléphone. Action : rassurer, montrer les services, prendre rendez-vous / devis, appeler, suivre sa réparation.
Contraintes : statique (Netlify Forms, contenu/*.json), polices auto-hébergées, aucune ressource externe, pas de photos (emplacements prévus), rien d'inventé, bandeau « exemple fictif ».

## Direction contract

THESIS: La page est le pont élévateur de l'atelier : au défilement, la voiture monte et on voit dessous ; les services apparaissent comme des pièces qu'on inspecte, étiquetées sur la voiture. Rien n'est caché. Elle refuse la photo d'atelier générique avec « Votre garage de confiance ».

OWN-WORLD: Anthracite de sol époxy (#111418) et blanc atelier (#E9ECEF) en grandes zones ; jaune sécurité (#F2C230) réservé aux bras du pont, à l'action principale et à l'état actif ; acier (#5B6573) pour le dessin technique au trait. Archivo (variable, largeur étendue pour les titres, normale pour le texte), chiffres tabulaires. Dessin au trait précis, pas d'illustration décorative.

STORY: Le visiteur lit « Votre voiture est entre de bonnes mains », voit tout de suite Appeler et Prendre rendez-vous, puis fait monter la voiture : les quatre services s'épinglent dessus. Ensuite : « En panne sur la route ? », le formulaire rendez-vous/devis, le suivi de réparation, les horaires et l'adresse.

FIRST VIEWPORT: En-tête : logotype animé (deux colonnes de pont et une traverse jaune qui monte, puis DELORME), téléphone toujours visible, lien EN. Scène plein écran anthracite : titre étendu à gauche, deux actions (Prendre rendez-vous en jaune, Appeler en filet) ; à droite (dessous sur téléphone), la voiture au trait posée sur les bras jaunes du pont, au sol.

ADAPTATIONS : sur téléphone (moins de 40 rem), le numéro de l'en-tête est réduit à l'icône téléphone (la largeur de 390 px ne tient pas logotype + numéro + EN sur une ligne) ; le numéro complet reste dans les deux boutons Appeler du premier écran. Les étiquettes du pont s'étagent sur quatre lignes sous la voiture.

FORM: Le pont élévateur, ma candidate n° 1 (carte IMPECCABLE’S PICK choisie par l'utilisateur). seed:47f8320c979ab44f. Signature : la voiture monte avec le défilement (scène collante), le dessous se révèle, quatre étiquettes de services s'épinglent tour à tour sur les pièces concernées. Mouvement réduit : état final statique.

FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance
