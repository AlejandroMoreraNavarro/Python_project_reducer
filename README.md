# Python Project Reducer — Version 1 (V1)

`python-project-reducer` est un outil d'analyse statique et de réduction de projets Python (**Version 1 - V1**, centrée sur l'analyse statique module-niveau et l'élagage symbolique par AST) conçu pour alléger des bases de code sans compromettre leur intégrité fonctionnelle.

## Architecture de l'outil

1. **Analyseur & Réducteur Module-Niveau (`reducer_core.py`, `reducer.py`)** :
   - Analyse statique des instructions `import` et `from ... import ...`.
   - Sur-approximation prudente (conservation par précaution des modules dynamiques/ambigus).
   - Copie sécurisée vers un répertoire de travail `work/` avec vérification d'intégrité SHA-256 et génération de rapports détaillés.

2. **Analyseur & Réducteur de Symboles par AST (`symbol_analyzer.py`, `symbol_reducer.py`)** :
   - Analyseur AST pour identifier les définitions de classes/fonctions et leurs références.
   - Élagage des fonctions et classes non référencées au sein des modules Python à l'aide d'analyses de portée et de réécriture AST (`ast.unparse`).

3. **Interface Ligne de Commande (`cli.py`)** :
   - CLI unifiée combinant la réduction au niveau module et l'élagage au niveau symbole.
   - Harnais de test et validation (`harness.py`).

### Instructions d'utilisation

### Lancer la CLI

Pour afficher l'aide de la CLI :
```powershell
python cli.py --help
```

Pour exécuter une réduction de projet :
```powershell
python cli.py --project <chemin_projet> --entry <point_entree> --output <chemin_sortie> [--symbols]
```

### Description des arguments

- `--project` : Le chemin vers le dossier racine du projet à réduire.
- `--entry` : Le fichier ou point d'entrée principal (ex: `main.py`). Il sert de point de départ à l'analyse statique des imports.
- `--output` : Le dossier de destination où sera créée la copie réduite du projet.
- `--symbols` (optionnel) : Active l'élagage au niveau des symboles (suppression des fonctions et classes internes non référencées) via AST sur les fichiers conservés.

### Exécuter les tests unitaires

```powershell
python -m pytest -q
```
