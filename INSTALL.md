# Installation de Rootux

> Créé par Cape003 avec l'aide de l'IA (Le Chat, Mistral AI)

## Installation rapide

```bash
git clone https://github.com/Cape003/rootux.git
cd rootux
chmod +x install.sh
./install.sh
python3 rootux_gui.py
```

## Installation manuelle

### Debian/Ubuntu
```bash
sudo apt update && sudo apt install -y git python3 python3-gi gir1.2-gtk-4.0 gir1.2-libadwaita-1 pipewire easyeffects qpwgraph
pip3 install --user pygobject pycairo numpy pyaudio dbus-python
systemctl --user enable --now pipewire pipewire-pulse wireplumber
```

### Arch Linux
```bash
sudo pacman -Syu --needed git python python-gobject python-cairo python-numpy python-pyaudio pipewire easyeffects qpwgraph
systemctl --user enable --now pipewire pipewire-pulse wireplumber
```

## Configuration OBS
1. Dans Rootux, créez un nœud Rootux_Output
2. Dans OBS, ajoutez une source audio PipeWire avec Rootux_Output
3. Désactivez la capture audio par défaut d'OBS