# Projet open source : outil intelligent de réduction de projets Python

## 1. Présentation et objectif général

Je souhaite développer un outil open source capable de prendre un projet Python existant et fonctionnel, puis d'en générer une version réduite qui ne conserve que les éléments nécessaires à une fonctionnalité choisie par l'utilisateur.

L'idée de départ est simple : prendre un projet qui fonctionne déjà, avec son code, ses ressources, ses configurations et, le cas échéant, ses poids de modèles, puis en extraire une version plus légère qui conserve uniquement ce dont on a besoin.

Je ne souhaite pas reconstruire le projet à partir de zéro ni créer une nouvelle implémentation de ses fonctionnalités. Je veux partir d'un projet existant et le réduire.

La réduction ne doit pas se limiter à supprimer des fichiers. Lorsque cela est possible, l'outil doit aussi simplifier le code source et éliminer les dépendances qui ne sont plus nécessaires après la suppression des fonctionnalités inutiles.

**Le projet original ne doit jamais être modifié.** Toutes les opérations doivent être réalisées sur une copie distincte, qui constituera le projet réduit.

L'objectif est de créer un outil réellement utile aux développeurs, techniquement sérieux, testable et suffisamment ambitieux pour constituer un projet de portfolio d'ingénieur en intelligence artificielle.

Je souhaite étudier la possibilité d'utiliser l'analyse statique, des règles déterministes et éventuellement des LLM pour automatiser une partie du processus. Cependant, je ne veux pas introduire de l'IA ou une architecture agentique simplement parce que ce sont les technologies que je connais.

Il faut d'abord déterminer quelles parties du problème peuvent être résolues de manière fiable et si le projet répond à un besoin réel.

## 2. Exemple illustratif

Imaginons un projet Python de machine learning qui contient plusieurs modèles, des scripts d'entraînement, des scripts d'inférence, des configurations, des outils d'évaluation et différentes dépendances.

Je souhaite conserver uniquement l'inférence d'un modèle préentraîné.

L'outil devrait alors produire une copie réduite contenant :
- Le code nécessaire au chargement du modèle.
- Les poids préentraînés et les ressources indispensables.
- Le prétraitement des entrées.
- Le code réalisant l'inférence.
- Les fonctions auxiliaires nécessaires.
- Les configurations utiles.
- Un point d'entrée simple pour utiliser la fonctionnalité.
- Les dépendances nécessaires au fonctionnement du résultat.

Il devrait pouvoir supprimer les autres modèles, le code d'entraînement, les outils d'évaluation inutiles, les configurations sans rapport avec la fonctionnalité retenue et les dépendances qui ne sont plus utilisées.

Un cas plus intéressant serait celui d'un script qui mélange entraînement et inférence. Si ce script contient le chargement du modèle, la boucle d'entraînement, le calcul de la loss, l'optimiseur et le code d'inférence, l'outil devrait pouvoir, lorsque c'est techniquement possible, conserver le chemin d'inférence et supprimer les parties exclusivement liées à l'entraînement.

Cela pourrait permettre de retirer certaines bibliothèques devenues inutiles.

Cet exemple illustre le résultat recherché, mais il ne faut pas en déduire que cette transformation est toujours possible. Elle devra être étudiée et validée sur des projets réels.

## 3. Définition précise du problème

Le projet combine plusieurs problèmes distincts qui doivent être étudiés séparément.

### 3.1. Réduction des fichiers

Identifier les fichiers nécessaires à une fonctionnalité et produire une copie qui élimine les fichiers inutiles.

### 3.2. Analyse des dépendances internes

Comprendre les relations entre les modules, fonctions, classes et composants du projet afin d'éviter de supprimer un élément nécessaire indirectement.

### 3.3. Simplification du code source

Supprimer des fonctions, imports, classes, branches de code ou portions de scripts qui ne servent plus aux fonctionnalités conservées.

Cette opération est plus risquée que la suppression de fichiers, car le code peut contenir des effets de bord, des imports dynamiques ou des comportements qui ne sont pas visibles dans le graphe d'appels.

### 3.4. Réduction des dépendances externes

Identifier les bibliothèques qui restent nécessaires après transformation, puis réduire les dépendances déclarées dans le projet.

Il faut distinguer les dépendances directes, les dépendances transitives, les dépendances optionnelles et les dépendances système.

La suppression d'un import dans un fichier ne prouve pas qu'une bibliothèque est devenue inutile ailleurs dans le projet.

### 3.5. Préservation du fonctionnement

Vérifier que la copie réduite réalise toujours correctement la fonctionnalité choisie.

Les tests doivent comparer, lorsque cela est possible, le comportement du projet original et celui du projet réduit sur les mêmes entrées.

Il faut reconnaître qu'un ensemble de tests réussis ne prouve pas une équivalence fonctionnelle complète.

### 3.6. Traçabilité

L'outil doit expliquer les modifications réalisées, les éléments supprimés, les dépendances conservées et les incertitudes restantes.

Les transformations doivent être inspectables et, autant que possible, réversibles.

## 4. Choix des projets de test : une priorité du projet

Je ne souhaite pas commencer avec un projet de machine learning complexe comme MatchAnything.

Un dépôt de cette nature peut combiner plusieurs modèles, des configurations complexes, des dépendances spécifiques et des mécanismes de chargement difficiles à analyser. En cas d'échec, il serait difficile de déterminer si le problème vient de l'outil de réduction ou de la complexité du projet testé.

MatchAnything peut éventuellement devenir un cas de validation avancé, mais il ne doit pas être le premier projet utilisé pour développer l'outil.

Je souhaite plutôt sélectionner plusieurs projets open source Python, déjà fonctionnels, de difficulté croissante.

### 4.1. Critères de sélection

Les projets de test doivent être évalués selon les critères suivants :

- **Fonctionnement initial vérifiable :** le projet doit pouvoir fonctionner avant toute transformation, sans modification préalable de son code.
- **Reproductibilité :** il doit être possible d'installer ses dépendances et de reproduire un comportement de référence.
- **Tests ou exemples :** des tests automatisés, des exemples de référence ou des sorties attendues doivent permettre de vérifier les résultats.
- **Fonctionnalités isolables :** il doit être possible d'identifier des fonctionnalités qui peuvent être conservées ou supprimées.
- **Dépendances identifiables :** le projet doit permettre d'étudier la réduction des dépendances.
- **Complexité adaptée :** chaque projet doit permettre de tester une difficulté particulière sans introduire trop de variables inconnues.
- **Compatibilité matérielle :** les premiers tests doivent être réalisables principalement sur CPU, idéalement sous Windows.
- **Licence vérifiée :** la licence doit être compatible avec l'utilisation et la redistribution envisagées.

Il ne faut pas exiger que tous les projets remplissent parfaitement tous les critères. Il faut comparer les candidats et expliciter leurs avantages et leurs limites.

### 4.2. Progression des tests

Je souhaite construire une suite de tests progressive.

**Niveau 1 — Projets Python simples**

Des projets avec plusieurs modules, quelques fonctions et un nombre limité de dépendances.

Objectif : tester l'identification des fichiers, modules et imports manifestement inutiles.

**Niveau 2 — Projets à fonctionnalités indépendantes**

Des applications ou bibliothèques qui proposent plusieurs fonctionnalités distinctes.

Objectif : conserver une fonctionnalité tout en supprimant les autres, sans casser les composants partagés.

**Niveau 3 — Projets avec des dépendances internes partagées**

Des projets dans lesquels plusieurs fonctionnalités utilisent les mêmes modules.

Objectif : vérifier que l'outil conserve les composants communs nécessaires et ne supprime pas des éléments utilisés indirectement.

**Niveau 4 — Projets nécessitant une simplification du code**

Des projets qui contiennent des scripts ou fonctions mélangeant plusieurs responsabilités.

Objectif : évaluer la capacité à séparer les chemins d'exécution et à retirer du code devenu inutile.

**Niveau 5 — Projets de machine learning**

Des projets comprenant des modèles préentraînés, des poids, des configurations et des dépendances plus complexes.

Objectif : tester la conservation de l'inférence d'un modèle et l'élimination des composants d'entraînement ou d'évaluation devenus inutiles.

Cette progression est une proposition initiale. Il faudra vérifier que les projets retenus permettent réellement de tester les capacités correspondantes.

### 4.3. Un projet de référence contrôlé

Je souhaite également envisager la création d'un petit projet Python spécifiquement conçu pour tester l'outil.

Ce projet contiendrait plusieurs fonctionnalités, des modules partagés, des dépendances différentes selon les fonctionnalités et des composants volontairement inutiles pour certains scénarios.

Comme sa structure serait connue à l'avance, il permettrait de vérifier objectivement si l'outil conserve les éléments nécessaires et supprime les éléments qui ne le sont pas.

Ce projet contrôlé compléterait les projets open source réels ; il ne devrait pas les remplacer.

### 4.4. Travail de recherche demandé

Avant de choisir les projets, recherche et compare plusieurs candidats open source existants.

Pour chacun, examine :
- Sa structure réelle et ses fonctionnalités.
- Ses dépendances.
- Ses tests et sa facilité d'installation.
- Les fonctionnalités que l'on pourrait isoler.
- Les opérations de réduction qu'il permettrait de tester.
- Les risques et difficultés particulières.
- Sa licence.
- Les preuves disponibles que le projet fonctionne sans modifications préalables.

Privilégie des projets suffisamment simples pour permettre une validation objective, plutôt que des dépôts populaires mais difficiles à reproduire.

Cite les sources utilisées et distingue les informations vérifiées des hypothèses.

À l'issue de cette recherche, propose une petite suite de référence composée de plusieurs projets complémentaires. Explique ce que chaque projet permet de tester et pourquoi il est préférable aux autres candidats.

Ne commence pas par MatchAnything et ne considère pas ce dépôt comme indispensable à la réussite du projet.

## 5. Architecture technique à étudier

Je ne souhaite pas imposer une architecture à l'avance. Il faut comparer les approches disponibles et retenir la plus simple qui permet d'obtenir des résultats fiables.

Les composants suivants constituent des pistes à étudier, et non des décisions déjà prises.

### 5.1. Analyse statique

Étudier notamment :
- L'analyse de l'AST Python.
- L'extraction des imports et des références.
- La construction d'un graphe de dépendances.
- L'analyse des appels de fonctions et des classes.
- L'identification des points d'entrée.
- L'analyse des fichiers de configuration.
- La détection du code potentiellement inutilisé.

Évaluer les limites de ces techniques face aux imports dynamiques, aux décorateurs, aux registres de composants, aux plugins et aux effets de bord.

### 5.2. Analyse dynamique

Étudier l'intérêt d'exécuter les projets et de collecter des informations sur les modules chargés, les fonctions appelées et les chemins réellement utilisés.

Expliquer pourquoi l'exécution instrumentée peut compléter l'analyse statique, mais ne permet pas à elle seule de prouver qu'un composant n'est jamais nécessaire.

### 5.3. Transformations du code

Comparer plusieurs stratégies :
- Suppression de fichiers entiers.
- Suppression d'imports inutilisés.
- Suppression de fonctions ou classes non référencées.
- Simplification de scripts.
- Séparation des fonctionnalités mélangées.
- Réécriture assistée de certaines parties du code.

Identifier les opérations qui peuvent être automatisées de façon relativement sûre et celles qui nécessitent une validation humaine.

### 5.4. Utilisation éventuelle d'un LLM

Étudier si un modèle de langage peut apporter une valeur ajoutée pour :
- Comprendre le rôle de composants ambigus.
- Identifier des responsabilités mélangées dans un script.
- Proposer des transformations du code.
- Expliquer les modifications.
- Aider à diagnostiquer les tests qui échouent après une transformation.

Le LLM doit rester facultatif si possible.

Il ne doit pas être considéré comme une source de vérité ni pouvoir supprimer arbitrairement des composants. Ses propositions doivent être inspectées, testées et rejetées si elles ne satisfont pas les critères de validation.

Comparer le gain potentiel de l'IA à une approche déterministe, en tenant compte du coût, de la reproductibilité, de la confidentialité du code et du risque d'erreur.

### 5.5. Validation automatique

Étudier les mécanismes permettant de vérifier :
- La cohérence des imports.
- L'installation des dépendances dans un environnement propre.
- L'exécution de la fonctionnalité conservée.
- La préservation des résultats sur un ensemble d'entrées de référence.
- La réduction effective du projet.
- Les régressions introduites par les transformations.

Le système doit produire un rapport distinguant les tests réussis, les tests échoués et les aspects qui n'ont pas pu être vérifiés.

## 6. Contraintes de développement

Les contraintes suivantes doivent être prises en compte dès le début.

- Le développement doit fonctionner principalement sous Windows.
- Mon ordinateur ne possède pas de GPU dédié.
- Les analyses statiques, transformations et tests initiaux doivent privilégier le CPU.
- Kaggle peut être utilisé ponctuellement pour des expérimentations nécessitant un GPU, mais ne doit pas être indispensable.
- La première version doit cibler Python.
- Le projet original doit rester strictement inchangé.
- La copie réduite doit être produite dans un répertoire distinct.
- Les modifications doivent pouvoir être inspectées au moyen d'un diff.
- Les transformations risquées doivent être signalées ou soumises à validation.
- L'outil doit éviter d'exécuter du code inconnu sans isolation adaptée.
- Les résultats doivent être reproductibles et documentés.
- La licence des projets analysés doit être prise en compte, notamment lorsque du code ou des ressources sont redistribués.

Pour la première version, il est acceptable de supposer que l'utilisateur dispose déjà d'un environnement Python adapté. L'objectif initial n'est pas nécessairement d'embarquer l'interpréteur Python, le système d'exploitation et toutes les bibliothèques.

Il faudra néanmoins définir clairement ce qui est inclus dans le projet réduit et ce qui reste fourni par l'environnement d'exécution.

## 7. Définition d'un MVP réaliste

Après l'étude de faisabilité et la sélection des projets de test, propose un MVP progressif.

Un premier périmètre envisageable serait :

1. Recevoir le chemin d'un projet Python fonctionnel.
2. Recevoir une description de la fonctionnalité à conserver.
3. Analyser les fichiers et les imports.
4. Construire un graphe de dépendances initial.
5. Identifier les éléments manifestement nécessaires et ceux potentiellement inutiles.
6. Générer une copie réduite sans toucher à l'original.
7. Éliminer les fichiers et imports inutiles avec un niveau de confiance suffisant.
8. Réduire les dépendances déclarées lorsque cela est justifié.
9. Tester le fonctionnement de la copie.
10. Produire un rapport des modifications et des incertitudes.

La simplification automatique de scripts complexes pourrait constituer une deuxième étape du développement, après validation de la réduction des fichiers et des dépendances.

Il faut toutefois déterminer si ce découpage est effectivement le meilleur au regard des outils existants et des résultats de l'étude de faisabilité.

## 8. Critères de réussite

Le succès du projet ne doit pas être mesuré uniquement par la réduction du nombre de fichiers ou de lignes de code.

Définis des métriques pertinentes, notamment :

- La proportion de transformations correctement réalisées.
- Le nombre de suppressions incorrectes.
- La préservation des fonctionnalités ciblées.
- Le taux de réussite des tests après réduction.
- La réduction du nombre de dépendances réellement nécessaires.
- La taille du projet avant et après transformation, en tenant compte des ressources conservées.
- Le temps nécessaire à l'analyse et à la transformation.
- La reproductibilité de l'installation.
- La quantité d'interventions humaines nécessaires.
- La capacité à détecter les situations où l'outil ne peut pas conclure de manière fiable.

Les métriques doivent être mesurables sur les projets de référence.

Il faut également définir des conditions d'échec explicites : un projet réduit qui ne fonctionne plus ne constitue pas une réussite, même s'il est beaucoup plus petit.

## 9. Feuille de route souhaitée

Je souhaite une feuille de route progressive, avec des critères de décision à chaque étape.

**Étape 1 : étude de l'existant.** Identifier les outils, bibliothèques et approches déjà disponibles.

**Étape 2 : sélection des projets de test.** Choisir plusieurs dépôts open source simples, complémentaires et reproductibles, ainsi qu'un éventuel projet contrôlé.

**Étape 3 : définition du MVP.** Fixer les fonctionnalités, les limites et les critères de réussite.

**Étape 4 : premier prototype.** Mettre en place l'analyse, la copie du projet et la suppression des éléments dont l'inutilité peut être établie.

**Étape 5 : réduction des dépendances.** Étudier et tester la génération de fichiers de dépendances adaptés à la fonctionnalité conservée.

**Étape 6 : validation automatique.** Comparer le fonctionnement du projet original et de la version réduite.

**Étape 7 : simplification du code.** Ajouter progressivement des transformations plus complexes, en commençant par les cas les plus sûrs.

**Étape 8 : expérimentation de l'IA.** Évaluer l'apport d'un LLM sur les cas ambigus, avec des mesures comparatives.

**Étape 9 : tests sur des projets plus complexes.** Passer à des bibliothèques de machine learning ou à d'autres projets présentant des difficultés réelles.

**Étape 10 : publication.** Documenter les capacités, les limites, les résultats expérimentaux et les cas non pris en charge.

Cette feuille de route doit être adaptée en fonction des résultats de l'étude préalable. Il ne faut pas poursuivre une étape si les précédentes n'ont pas démontré leur fiabilité.

## 10. Ce que j'attends de cette conversation

Je ne souhaite pas commencer immédiatement à coder.

Je veux d'abord conduire une étude sérieuse du problème, des outils existants, de la faisabilité et des projets de test.

Procède dans cet ordre :

### Étape A — Reformulation et analyse du problème

Reformule le projet et distingue les difficultés techniques qu'il combine.

Identifie les hypothèses qui doivent être vérifiées avant de commencer le développement.

### Étape B — Recherche des solutions existantes

Recherche des outils open source et des travaux pertinents sur l'analyse de dépendances, la détection de code inutilisé, la réduction de projets Python, l'analyse dynamique et les transformations automatiques du code.

Cite les sources et évalue les limites des solutions existantes.

### Étape C — Sélection des projets de test

Recherche plusieurs projets open source Python adaptés à la progression décrite dans la section 4.

Propose une suite de référence concrète et explique pourquoi chaque projet a été retenu.

N'impose pas MatchAnything comme premier cas de test.

### Étape D — Étude de faisabilité

Évalue les approches techniques, leurs limites, les risques de régression et la possibilité de valider les transformations.

Distingue les opérations sûres, les opérations heuristiques et les opérations qui nécessitent une intervention humaine.

### Étape E — Définition du MVP

Propose un périmètre initial précis, des critères de réussite mesurables et des tests permettant de déterminer objectivement si le prototype fonctionne.

### Étape F — Feuille de route

Propose une stratégie de développement adaptée à mes contraintes matérielles, avec les outils à utiliser, les étapes de validation et les critères permettant de décider si le projet mérite d'être poursuivi.

## 11. Principes de travail

Sois rigoureux, critique et précis.

Ne pars pas du principe que mon idée est originale, réalisable dans tous les cas ou suffisamment utile pour justifier un projet open source. Si des outils existants couvrent déjà une grande partie du besoin, explique-le et identifie une éventuelle différenciation pertinente.

Ne présente pas comme un fait une fonctionnalité qui n'a pas été vérifiée. Distingue les faits documentés, les résultats expérimentaux, les hypothèses et tes propres recommandations.

Ne propose pas une architecture complexe simplement pour utiliser des agents ou des LLM. Privilégie la solution la plus simple qui permet de résoudre le problème de manière fiable.

Ne commence pas par du code, ne choisis pas immédiatement un framework agentique et ne sélectionne pas un dépôt complexe comme benchmark initial.

**La priorité est de déterminer si l'outil répond à un besoin réel, de trouver les meilleurs projets de test et de démontrer progressivement qu'il est possible de réduire un projet Python fonctionnel sans altérer la fonctionnalité conservée.**