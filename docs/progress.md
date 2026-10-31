# Suivi de progression (docs/progress.md)

## Étape 0 — Vérification de la recherche
- [x] Clone (`external/pypdf`, URL: https://github.com/py-pdf/pypdf.git)
- [x] Commit noté (`70eab9bcbfae5b6cbfa18d1c559be26169dd69f0`)
- [x] Licence lue (BSD 3-Clause / Mathieu Fenniak)
- [x] Commande de test / évaluation validée
- [x] Installation testée dans un venv vierge sous Windows

## Étape 1 — Projet contrôlé + harnais
- [x] Projet contrôlé : modules indépendants, partagés, imports dynamiques, registre/décorateur, ressource, dépendance optionnelle (`tests/controlled_project/`)
- [x] Harnais : exécute la commande de référence sur l'original et la copie, compare les sorties et erreurs (`harness.py`)
- [x] Test méta : le harnais détecte avec succès au moins 3 régressions injectées volontairement (3/3 détectées, Gate validée)

## Étape 2 — Réducteur module-niveau (MVP)
- [x] Micro-étape 2a : Module `reducer_core.py` (analyse statique des imports) et test unitaire `tests/test_reducer.py` validés par pytest.
- [x] Micro-étape 2b : Fonction de réduction et copie vers `work/` avec vérification d'intégrité par hash SHA-256 et exclusion des modules non atteints, validé par test unitaire.
- [x] Micro-étape 2c : Génération de rapport détaillé (`generate_reduction_report`) catégorisant les fichiers testé et validé.

## Étape 3 — Application pypdf
- [x] Réduction réussie de pypdf : 319 fichiers scannés, 51 conservés (nécessaires), 208 conservés par précaution, 60 supprimés, intégrité source vérifiée par SHA-256. Rapport consigné dans `docs/pypdf_reduction_report.md`.

## Étape 5 — Niveau symbole & CLI (V1 Complétée)
- [x] Micro-étape 4a : Module `symbol_analyzer.py` créé pour l'extraction AST des classes, fonctions et références, validé par test unitaire dans `tests/test_symbol_reducer.py`.
- [x] Micro-étape 4b : Module `symbol_reducer.py` créé pour la réécriture et l'élimination des définitions mortes via AST (`DeadCodeRemover` + `ast.unparse`), validé par test unitaire.
- [x] Micro-étape 4c : Module de test `module_with_dead.py` ajouté dans `tests/controlled_n1/`, test d'intégration AST validé.
- [x] Micro-étape 5a : Script CLI `cli.py` créé combinant réduction module-niveau et élagage symbole, validé par test d'intégration dans `tests/test_cli.py`.
- [x] Micro-étape 5b : Validation finale, mise à jour du README et de la documentation de progression.
