# Recherche préalable — état de vérification (mis à jour le 22 oct. 2026)

Statuts : **V** = lu dans une source citée, **H** = hypothèse / de mémoire, **À faire** = à vérifier localement par l'agent.
Les « À faire » exigent ta machine (clone, installation, exécution). Le reste a été vérifié en ligne.

## Outils existants

| Outil | Ce qu'il fait | Statut | Source / remarque |
|---|---|---|---|
| PyTrim | Retire imports et déclarations de dépendances inutilisées (requirements.txt, setup.py…) ; composante d'analyse dynamique ; 98,3 % de fidélité sur 37 PR (ASE 2025) | **V** | Papier : https://arxiv.org/abs/2510.00674v2 ; code : https://github.com/TrimTeam/PyTrim ; PyPI `pytrim` 0.2.0, licence MIT ; dépend de deptry, fawltydeps, ruff, pipdeptree… ; PyCG optionnel ; ~100 téléchargements/mois (faible adoption). **Baseline pour l'étape dépendances uniquement.** À faire : installation sous Windows, date de la dernière release |
| deptry, FawltyDeps | Détection de dépendances inutiles/manquantes | **V** (utilisés comme détecteurs par PyTrim) | Licences, maintenance : À faire |
| autoflake, pylint | Imports inutilisés dans un fichier | H | |
| vulture | Code mort, confiance 60–100 %, rate du code mort à cause du dynamisme | **V** | https://github.com/jendrikseipp/vulture |
| treeshaker | Copie des modules nécessaires + requirements réduit (modulegraph) | **V** | https://pypi.org/project/treeshaker/ — dernière release 16 mai 2020, alpha, imports relatifs fragiles. Référence conceptuelle, **pas une baseline**. |
| tree-shaking | À partir d'entrées et de `search_paths`, produit une copie réduite des **bibliothèques** (typiquement `site-packages`) pour réduire la taille d'un paquet | **V** | https://pypi.org/project/tree-shaking/ — dernière release 0.4.2 le 20 sept. 2026 (actif), 1 mainteneur, Python ≥ 3.12, README anglais « en construction » (chinois disponible). Dépôt : https://github.com/likianta/python-tree-shaking. Licence : non vue, À faire. **Cible les dépendances, pas le code du projet** : baseline pour la réduction de dépendances. |
| PyCG | Graphe d'appels statique | V (existence) | Limites précision/rappel : À faire |
| Drosos et al. FSE'24 | Analyse de bloat méthode-niveau sur 1 302 projets PyPI | **V** | https://2024.esec-fse.org/details/fse-2024-research-papers/104/ |
| LEADER (LLM + debloating) | LLM décideur sur conseils de debloating | **V** (résumé) | https://arxiv.org/abs/2503.08969 ; orientation C : H |

## Projets de test candidats

| Niveau | Projet | Licence | Ce que l'on teste | Statut |
|---|---|---|---|---|
| 1, 3 | Projet contrôlé (à écrire) | — | Vérité terrain connue | À créer |
| 2, 3 | pypdf | **BSD-3 (V)** — fichiers `_encryption.py` et `_crypt_providers/*` sous BSD-3 (Debian copyright) | Garder lecture/fusion, exclure chiffrement | Voir ci-dessous |
| 4 | pytorch/examples `mnist` | **BSD-3 (V)** (ecosyste.ms ; dossier `mnist/` listé dans le README) | Script mixant train/test | Commit, exécution CPU, téléchargement du jeu MNIST au premier lancement (H) : À faire |
| 5 | cvg/glue-factory | **Apache-2.0 (V)** ; `gluefactory_nonfree` à exclure | Entraînement + évaluation + matching | Choix d'un matcher sans modèle non libre, poids, exécution CPU : À faire |
| 5 (complément) | cvg/LightGlue | Apache-2.0 ; **SuperPoint : licence restrictive** | Référence externe secondaire | https://github.com/cvg/lightglue |

### Découvertes sur pypdf
- **V** (version 3.17.4, via listing de fichiers) : le chiffrement est déjà isolé dans `pypdf/_encryption.py` et `pypdf/_crypt_providers/` avec `_cryptography.py`, `_pycryptodome.py` et `_fallback.py`. La structure de la version actuelle n'est pas vérifiée.
- **H** : `_reader.py` et `_writer.py` importent `_encryption.py` ; retirer le chiffrement oblige donc à modifier ces fichiers, pas seulement à supprimer des modules. C'est le vrai test du réducteur.
- **Risque (source indirecte)** : un paquet de distribution signale que la suite de tests nécessite de gros PDF téléchargés depuis Internet. À vérifier dans `tests/` : si les tests ne sont pas reproductibles hors ligne, il faudra mettre en cache ou fixer les fichiers de référence.

## Protocole de validation (décisions provisoires)
- Oracle principal : version originale vs version réduite du **même** pipeline, mêmes entrées, poids, paramètres.
- LightGlue : référence externe secondaire, pas preuve d'équivalence.
- Tests de référence : sous-ensemble défini et justifié **avant** l'expérience, exclusions documentées.
- Baselines : tree-shaking (dépendances) et PyTrim (imports et déclarations) ; treeshaker abandonné.

## À vérifier localement (tâches pour l'agent)
1. Clone épinglé (hash) de pypdf, mnist, glue-factory.
2. Commande de test et résultat **sur l'original**, hors ligne si possible.
3. Installation de pytrim et tree-shaking dans des venv séparés sous Windows.
4. Dernière release de pytrim.
