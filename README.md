# Rootux

> Créé par Cape003 avec l'aide de l'IA (Le Chat, Mistral AI)

Alternative open-source à SteelSeries Sonar pour Linux avec interface GTK4, routage PipeWire et intégration OBS/Streamlabs.

## Installation

git clone https://github.com/Cape003/rootux.git
cd rootux
chmod +x install.sh
./install.sh
python3 rootux_gui.py

## Fonctionnalités
- Mixeur 5 canaux (Game, Chat, Media, Aux, Mic)
- Effets audio (EQ, Compresseur, Noise Gate)
- Routage PipeWire
- Intégration OBS/Streamlabs
- Interface GTK4

## Intégration OBS
1. Créez un nœud Rootux_Output dans Rootux
2. Ajoutez une source PipeWire dans OBS
3. Sélectionnez Rootux_Output
4. Désactivez la capture audio par défaut d'OBS

## Licence
MIT - Voir LICENSE

## Remerciements
- SteelSeries pour l'inspiration (Sonar)
- PipeWire et GTK4
- Mistral AI (Le Chat)
- Cape003