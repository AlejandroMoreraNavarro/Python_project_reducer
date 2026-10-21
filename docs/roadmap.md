# Feuille de route — critères de passage

Règle : on ne passe à l'étape suivante qu'après ma validation explicite. Cocher une case = preuve écrite (commande, sortie ou lien).

## Étape 0 — Vérification de la recherche
- [ ] Chaque ligne « H » ou « À faire » de `docs/research.md` est vérifiée avec une source ou une commande
- [ ] Pour chaque projet candidat : commit épinglé, licence, commande de test, résultat des tests **sur l'original**
- [ ] Installation testée dans un venv vierge sous Windows
- **Gate** : au moins pypdf et un projet ML (mnist ou glue-factory) reproductibles sur CPU. Sinon remplacer le candidat.

## Étape 1 — Projet contrôlé + harnais
- [ ] Projet contrôlé : modules indépendants, partagés, import dynamique, registre/décorateur, ressource, dépendance optionnelle
- [ ] Harnais : exécute une commande de référence sur l'original et la copie, compare sorties, erreurs, tolérances numériques
- [ ] Test méta : le harnais détecte au moins 3 régressions injectées volontairement
- **Gate** : harnais fiable (3/3 régressions détectées). Sinon, on ne développe pas le réducteur.

## Étape 2 — Réducteur module-niveau (MVP)
- [ ] Entrées supportées : commande CLI + arguments, fonction Python `module:fonction`
- [ ] Copie dans `work/`, original intact (vérifié par hash avant/après)
- [ ] Rapport : conservé / supprimé / incertain, chaque conservation étiquetée « démontrée nécessaire » ou « par précaution »
- [ ] Contrôle sur le projet contrôlé : 0 suppression erronée
- [ ] Puis pypdf : lecture + fusion conservées, chiffrement exclu
- **Gate** : tests de référence 100 % sur le projet contrôlé et pypdf.

## Étape 3 — Comparaison aux outils existants (décision go/no-go)
- [ ] Mêmes scénarios avec `tree-shaking` et PyTrim (et `treeshaker` si il fonctionne encore)
- [ ] Tableau comparatif : réduction réelle, erreurs, effort manuel
- **Gate** : si les outils existants font aussi bien sans axe de différenciation, arrêter ou pivoter.

## Étape 4 — Dépendances
- [ ] Dépendances candidates depuis les imports, installation en venv vierge, tests d'exécution
- [ ] Rapport : raison, preuve et niveau d'incertitude par dépendance retirée

## Étape 5 — Niveau symbole
- [ ] Suppression de fonctions/classes non référencées (signaux vulture, sur-approximation)
- [ ] mnist avec arguments fixés (évaluation partielle)

## Étape 6 — Projet ML
- [ ] glue-factory réduit vers l'inférence ; comparaison principale à l'original, LightGlue en complément

## Étape 7 — Expérience LLM (seulement si une lacune mesurée la justifie)

## Étape 8 — Documentation et publication
