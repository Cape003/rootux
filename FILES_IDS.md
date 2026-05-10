# Rootux - Liste des fichiers et SHAs

Cree par Cape003 avec l aide de l IA (Le Chat, Mistral AI)
Derniere mise a jour: 10 mai 2026

## Fichiers principaux

Fichier | SHA | Taille | Description
------- | --- | ------ | -----------
README.md | 328ed88c25dbeb1a416a7b2361952f1a4480f65d | 9.2 Ko | Documentation principale
LICENSE | 02d1d71072d4a237ec9ff5482a0c1ed452ef9f1b | 1.0 Ko | Licence MIT
install.sh | 29eab224c602cd29a3830875881d6f0806bb835c | 1.4 Ko | Script d installation - A CORRIGER
rootux_gui.py | f2eb05dfdd2c45fbf8e23e50cb45fc2c31e6d3b3 | 4.2 Ko | Interface GTK4 - A CORRIGER
rootux_pw.py | 12a2dce63e7370cf247c794dff17f41976074e43 | 10.5 Ko | Gestion PipeWire
rootux_effects.py | 6e5db68f66dd759e8af61c3683b0e06223897772 | 11.0 Ko | Gestion des effets
INSTALL.md | ba1592648d9f3bb90befca6a82553261080a46b5 | 9.5 Ko | Guide d installation
CONTRIBUTING.md | d9dce4feca1715d4587123f5794e80c3c64107f0 | 4.4 Ko | Guide de contribution
CHANGELOG.md | 369faacff70ac806d310ab43c722246eafcf2241 | 2.5 Ko | Historique des versions
.gitignore | 6da5b85223ace1318bfb6f8f4687e9270725dfae | 0.1 Ko | Fichiers a ignorer

## Problèmes identifiés

1. rootux_gui.py (SHA: f2eb05dfdd2c45fbf8e23e50cb45fc2c31e6d3b3)
   - Problème: Utilise set_margin_all() qui n existe pas en GTK4
   - Solution: Utiliser des classes CSS a la place
   - Statut: En attente de correction

2. install.sh (SHA: 29eab224c602cd29a3830875881d6f0806bb835c)
   - Problème: Ne détecte pas CachyOS
   - Solution: Ajouter cachyos dans la liste des distros Arch
   - Statut: En attente de correction

## Fichiers corrigés disponibles

Les versions corrigées sont disponibles dans:
- /tmp/rootux_gui_fixed.py
- /tmp/install_fixed.sh

## Statistiques
- Total fichiers: 10
- A corriger: 2
- OK: 8
- Taille totale: ~40 Ko
