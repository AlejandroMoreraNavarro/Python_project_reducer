# Suivi de progression (docs/progress.md)

## Étape 0 — Vérification de la recherche

### pypdf
- [x] Clone (`external/pypdf`, URL: https://github.com/py-pdf/pypdf.git)
- [x] Commit noté (`70eab9bcbfae5b6cbfa18d1c559be26169dd69f0`)
- [x] Licence lue (BSD 3-Clause / Mathieu Fenniak)
- [ ] Commande de test trouvée et documentée

### pytorch/examples (mnist / simple)
- [ ] Clone (`external/pytorch-examples`)
- [ ] Commit noté
- [ ] Licence lue
- [ ] Commande de test trouvée et documentée

### glue-factory
- [ ] Clone (`external/glue-factory`)
- [ ] Commit noté
- [ ] Licence lue
- [ ] Commande de test trouvée et documentée

### Général
- [ ] Installation testée dans un venv vierge sous Windows

## Étape 1 — Projet contrôlé + harnais
- [x] Projet contrôlé : modules indépendants, partagés, imports dynamiques, registre/décorateur, ressource, dépendance optionnelle (`tests/controlled_project/`)
- [x] Harnais : exécute la commande de référence sur l'original et la copie, compare les sorties et erreurs (`harness.py`)
- [x] Test méta : le harnais détecte avec succès au moins 3 régressions injectées volontairement (3/3 détectées, Gate validée)

## Étape 2 — Réducteur module-niveau (MVP)
- [x] Micro-étape 2a : Module `reducer_core.py` (analyse statique des imports) et test unitaire `tests/test_reducer.py` validés par pytest.
- [ ] Entrées supportées : commande CLI + arguments, fonction Python `module:fonction`
- [ ] Copie dans `work/`, original intact (vérifié par hash avant/après)
- [ ] Rapport : conservé / supprimé / incertain, chaque conservation étiquetée « démontrée nécessaire » ou « par précaution »
- [ ] Contrôle sur le projet contrôlé : 0 suppression erronée
