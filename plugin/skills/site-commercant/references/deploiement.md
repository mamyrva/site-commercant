# Mise en ligne gratuite

Propose d'abord la méthode A. Elle ne demande aucune connaissance technique. Accompagne la personne étape par étape et attends qu'elle confirme avant de passer à la suite.

## A. Netlify Drop : le plus simple (5 minutes)

1. Aller sur **app.netlify.com/drop**.
2. Créer un compte gratuit (avec une adresse e-mail ou un compte GitHub).
3. Glisser-déposer le dossier **`site/`**, et pas le dossier parent : `PRODUCT.md` et `DESIGN.md` n'ont pas à être publiés.
4. Netlify donne une adresse du type `nom-aleatoire.netlify.app`. Dans *Site configuration › Change site name*, la remplacer par `nom-du-commerce.netlify.app`.
5. Pour une mise à jour : *Deploys*, puis glisser à nouveau le dossier `site/`.

**Hébergeur** pour les mentions légales : Netlify, Inc., 101 2nd Street, San Francisco, CA 94105, États-Unis. Site : netlify.com. Vérifie ces coordonnées sur netlify.com avant de livrer.

## B. GitHub Pages : si la personne a déjà un compte GitHub

1. Créer un dépôt public, par exemple `nom-du-commerce`.
2. Y envoyer **le contenu** du dossier `site/` (avec le bouton *Add file › Upload files*, ou `git`).
3. *Settings › Pages* : source « Deploy from a branch », branche `main`, dossier `/ (root)`.
4. L'adresse : `https://<pseudo>.github.io/nom-du-commerce/`.

**Hébergeur** : GitHub, Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, États-Unis. Vérifie ces coordonnées avant de livrer.

## Après la mise en ligne

1. Remplacer tous les `[À COMPLÉTER : adresse du site]` (dans `canonical`, `og:image`, `sitemap.xml`, `robots.txt` et les données structurées) par l'adresse réelle, puis republier.
2. Renseigner le nom de l'hébergeur dans les mentions légales, s'il ne l'était pas encore.
3. Tester l'aperçu de partage : envoyer le lien à soi-même par WhatsApp ou Messenger.
4. Ajouter l'adresse du site sur la fiche **Google Business Profile** (business.google.com) et sur les réseaux sociaux.

## Nom de domaine (facultatif, environ 10 €/an)

Un `nom-du-commerce.fr` fait plus pro. On l'achète chez un registraire (OVHcloud, Gandi, Infomaniak…), puis on le relie à Netlify (*Domain management › Add a domain*, qui guide pour la configuration) ou à GitHub Pages (*Settings › Pages › Custom domain*). Le domaine est la seule dépense de tout le projet.
