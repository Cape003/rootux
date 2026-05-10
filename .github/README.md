# 🎛️ Rootux

> **Un studio audio tout-en-un pour Linux, inspiré de SteelSeries Sonar**
> *Créé par **Cape003** avec l'aide de l'IA (Le Chat, Mistral AI).*

---

**Rootux** est une alternative open-source à **SteelSeries Sonar**, conçue pour les gamers, streamers et créateurs de contenu sous Linux. Elle offre un **mixeur audio avancé**, des **effets en temps réel** (EQ, compressions, noise gate), un **routage flexible** via PipeWire, et une **intégration parfaite avec OBS/Streamlabs**.

✅ 100% open-source | ✅ Compatibilité multi-distributions | ✅ Interface intuitive

---

## 📌 Fonctionnalités

- Mixeur 5 canaux (Game, Chat, Media, Aux, Mic)
- Effets audio (EQ 10 bandes, Compresseur, Noise Gate)
- Routage avancé via PipeWire
- Presets personnalisables
- Intégration OBS/Streamlabs

---

## 📥 Installation

### Installation automatique
```bash
git clone https://github.com/Cape003/rootux.git
cd rootux
chmod +x install.sh
./install.sh
python3 rootux_gui.py
```

### Installation manuelle

#### Debian/Ubuntu
```bash
sudo apt update && sudo apt install -y git python3 python3-gi gir1.2-gtk-4.0 gir1.2-libadwaita-1 pipewire easyeffects qpwgraph
pip3 install --user pygobject pycairo numpy pyaudio dbus-python
systemctl --user enable --now pipewire pipewire-pulse wireplumber
```

#### Arch Linux
```bash
sudo pacman -Syu --needed git python python-gobject python-cairo python-numpy python-pyaudio pipewire easyeffects qpwgraph
systemctl --user enable --now pipewire pipewire-pulse wireplumber
```

---

## 🚀 Lancement
```bash
python3 rootux_gui.py
```

---

## 🙏 Remerciements
- SteelSeries pour l'inspiration (Sonar)
- PipeWire et GTK4 pour les outils open-source
- Mistral AI (Le Chat) pour l'aide au développement
- Cape003 pour la création et la maintenance

---
> Rootux: Le Sonar pour Linux, par la communauté, pour la communauté. 🚀
