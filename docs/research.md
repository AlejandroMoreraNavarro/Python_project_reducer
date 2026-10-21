# Recherche préalable — état de vérification

Source : conversation d'étude préalable (Claude, relu par ChatGPT). Statuts : **V** = lu dans une source citée, **H** = hypothèse / de mémoire, **À faire** = à vérifier par l'agent.
L'agent doit vérifier chaque ligne « À faire » ou « H » et mettre à jour la colonne Statut avec une URL ou une sortie de commande.

## Outils existants

| Outil | Ce qu'il fait | Statut | Source / remarque |
|---|---|---|---|
| PyTrim | Retire imports et déclarations de dépendances inutilisées ; 98,3 % de fidélité sur 37 PR (ASE 2025) | V (papier) | https://arxiv.org/abs/2510.00674 ; code : https://github.com/TrimTeam/PyTrim ; installation et licence : À faire |
| deptry, FawltyDeps | Détection de dépendances inutiles/manquantes, sans suppression | V (via papier PyTrim) | Maintenance et licences : À faire |
| autoflake, pylint | Imports inutilisés dans un fichier | V (via papier PyTrim) | |
| vulture | Code mort, confiance 60–100 %, rate du code mort à cause du dynamisme | V | https://github.com/jendrikseipp/vulture |
| treeshaker | Copie des modules nécessaires + requirements réduit (modulegraph) | V | https://pypi.org/project/treeshaker/ — dernière release 16 mai 2020, alpha, réécriture d'imports « rudimentaire », imports relatifs probablement cassés. **Référence conceptuelle, pas baseline.** |
| tree-shaking (PyPI) | Entrées + search_paths → arbre réduit ; Python ≥ 3.12 | V (README) | Date de dernière release, fiabilité : À faire |
| PyCG | Graphe d'appels statique Python | V (existence) | Limites précision/rappel : À faire (papier PyCG) |
| Drosos et al. FSE'24 | Analyse de bloat méthode-niveau sur 1 302 projets PyPI | V | https://2024.esec-fse.org/details/fse-2024-research-papers/104/ |
| LEADER (LLM + debloating) | LLM décideur sur conseils de debloating ; orienté C d'après les exemples | V (résumé) | https://arxiv.org/abs/2503.08969 ; orientation C : H |

## Projets de test candidats

| Niveau | Projet | Licence | Ce que l'on teste | Statut |
|---|---|---|---|---|
| 1, 3 | Projet contrôlé (à écrire) | — | Vérité terrain connue | À créer |
| 2, 3 | pypdf | BSD-3 (V via paquets distribution) | Garder lecture/fusion, exclure chiffrement AES ; extras `crypto`, `image` | Version exacte, commande de test, isolement du code de chiffrement (H), installation Windows : À faire |
| 4 | pytorch/examples `mnist` | BSD-3 (H, de mémoire) | Script mixant train/test/main | Licence upstream, commit, exécution CPU : À faire |
| 5 | cvg/glue-factory | Apache-2.0 (V) ; `gluefactory_nonfree` à exclure | Entraînement + évaluation + matching | Choix du matcher sans modèle non libre (SIFT, DISK, ALIKED), poids, exécution CPU : À faire |
| 5 (complément) | cvg/LightGlue | Apache-2.0 ; **SuperPoint : licence restrictive** | Référence externe secondaire uniquement | https://github.com/cvg/lightglue |

## Protocole de validation (décisions provisoires)
- Oracle principal : version originale vs version réduite du **même** pipeline, mêmes entrées, poids, paramètres.
- LightGlue : référence externe secondaire, pas preuve d'équivalence.
- Tests de référence : sous-ensemble défini et justifié **avant** l'expérience, exclusions documentées.

## Questions ouvertes
- Existe-t-il un projet réel de niveau 1 adapté ? (aucun vérifié)
- Le besoin existe-t-il face à tree-shaking et PyTrim ? (comparaison à mesurer, étape 3 de la feuille de route)
