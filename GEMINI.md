# Règles de travail — python-project-reducer

Spec complète : `PROJECT_SPEC.md` (à relire en entier au début de chaque nouvelle phase, pas à chaque message).
État et critères d'étape : `docs/roadmap.md`. Faits et sources : `docs/research.md`. Décisions : `docs/decisions.md` (à créer).

## Contexte
- Windows, shell PowerShell (pas de syntaxe bash), CPU uniquement, Python. Pas de GPU.
- Utilisateur : étudiant ingénieur, Python intermédiaire. Réponses brèves, vocabulaire technique accepté.
- Venv de l'outil lui-même : `.venv/` à la racine. Tests : `pytest -q`.

## Règles non négociables
1. **Projets externes en lecture seule.** Clone dans `external/` (ignoré par git), commit ou tag épinglé noté dans `docs/research.md`. Toute transformation se fait sur une copie dans `work/`.
2. **Code externe exécuté uniquement dans un venv dédié** (un venv par projet, dans `envs/`). `pip install` uniquement dans un venv.
3. **Dépôt non évalué : aucune installation ni exécution sans mon accord explicite** (un venv isole les dépendances, pas la sécurité : `setup.py` et les hooks s'exécutent avec mes droits). Propose d'abord une évaluation des risques.
4. **Étiquette les faits sur les projets externes et les résultats d'exécution** (versions, licences, dates, comportement d'une lib) : `[vérifié: URL ou commande]`, `[hypothèse]` ou `[proposition]`. Pas de version, licence ou date sans source consultée dans cette session. Le reste n'a pas besoin d'étiquette.
5. **Avant d'affirmer qu'un test passe, exécute-le** et cite la commande et le résumé réel de la sortie.
6. **Un test qui échoue se corrige dans le code, jamais en supprimant ou affaiblissant le test.**
7. **Une étape à la fois.** Fin d'étape : résumé (fait / tests exécutés / limites), mise à jour de `docs/roadmap.md`, commit git local. Puis STOP, attends ma validation.
8. **Git : commits locaux uniquement.** Pas de `git push`. Relis le diff avant chaque commit.
9. **Fichiers : ne supprime rien sans justification** donnée avant l'action.
10. **Décision structurante incertaine :** pose **une** question et arrête-toi.

## Principes de conception (issus de l'étude préalable)
- Sur-approximer : dans le doute, conserver. Marquer l'élément « conservé par précaution ».
- L'analyse dynamique (coverage, `sys.modules`) ne sert qu'à **ajouter** des éléments à conserver, jamais à en retirer seule.
- Les imports proposent des dépendances candidates ; ils ne prouvent pas qu'une dépendance est inutile.
- Mesurer séparément : suppressions erronées (régression) et conservations par précaution (réduction incomplète).
- Pas de LLM dans le cœur de l'outil tant qu'une lacune mesurée ne le justifie.
- Compatibilité Windows : `pathlib`, pas de liens symboliques, tester l'installation dans un venv vierge.

## Méthode
- Commence par la recherche et l'analyse, puis code.
- Étapes courtes, avec objectifs et critères de réussite explicites.
- Privilégie les solutions simples, reproductibles et testables.
- Explique les décisions techniques et les compromis ; consigne-les dans `docs/decisions.md`.
- Écris des tests pour chaque nouvelle fonctionnalité (pytest) et exécute les tests pertinents après chaque modification.
- Ne passe pas à l'étape suivante tant que les critères de l'étape actuelle ne sont pas satisfaits ou que les limites restantes ne sont pas documentées.

## Style
- Court, sans remplissage ni flatterie. Contredis-moi si tu penses que j'ai tort.
- Python typé.
