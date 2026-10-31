# Feuille de route V2 — Filtrage par fonctionnalité (Feature-based Reducer)

## Objectif V2
Permettre à l'outil de réduire un projet Python non seulement par analyse statique des imports et des symboles, mais également en ciblant des **fonctionnalités spécifiques** (ex: `feature_a`, `feature_b`) via un fichier de configuration (`reducer.toml`) ou des décorateurs/tags dans le code.

## Architecture envisagée
1. **Fichier de configuration (`reducer.toml`) / Arguments CLI `--features`** :
   - L'utilisateur spécifie les fonctionnalités souhaitées.
2. **Analyseur de graphe sémantique / Tags** :
   - Marquage des fonctions/modules associés à des fonctionnalités (`@feature("feature_a")` ou analyse par point d'entrée).
3. **Réducteur contextuel** :
   - Élagage des branches du code et des modules non requis par les fonctionnalités activées.
