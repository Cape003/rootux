# 🎛️ Rootux - Studio Audio Avancé pour Linux

> **Alternative open-source à SteelSeries Sonar, spécialement conçue pour Linux**
> *Créé par **Cape003** avec l'aide de l'IA (Le Chat, Mistral AI)*

---

## 📋 Description Technique Complète

**Rootux** est une application professionnelle de **mixage audio** et de **gestion des effets sonores en temps réel**, inspirée de SteelSeries Sonar mais entièrement repensée pour l'écosystème Linux. Contrairement aux solutions propriétaires, Rootux offre une intégration native avec **PipeWire** (le système audio moderne de Linux) et une interface utilisateur intuitive basée sur **GTK4** et **Libadwaita**.

### 🎯 Public Cible
- **Streamers** (Twitch, YouTube, Kick)
- **Créateurs de contenu** (podcasts, vidéos)
- **Gamers** (Discord, jeux en ligne)
- **Musiciens** (enregistrement, production)
- **Utilisateurs avancés** de Linux recherchant une alternative open-source

---

## 🚀 Fonctionnalités Principales

### 🎚️ Mixeur Audio 5 Canaux
- **Game** : Contrôle du volume des applications de jeu
- **Chat** : Gestion séparée des applications de communication (Discord, Teamspeak, etc.)
- **Media** : Contrôle des lecteurs multimédias (Spotify, VLC, navigateurs)
- **Aux** : Canal auxiliaire pour les applications personnalisées
- **Mic** : Contrôle du microphone avec effets en temps réel

**Caractéristiques :**
- Faders de volume verticaux avec indication visuelle
- Boutons de mute/démute instantanés
- Affichage du niveau audio (VU-mètre)
- Réglage fin du volume (-60dB à +12dB)
- Sauvegarde des paramètres par profil

### 🎛️ Effets Audio Professionnels (via Easy Effects)

#### Effets d'Entrée (Microphone)
- **Égaliseur 10 bandes** (60Hz - 16kHz) avec présélections
- **Compresseur** : Réduction de la dynamique, seuil réglable (-60dB à 0dB)
- **Noise Gate** : Élimination des bruits de fond, seuil réglable
- **De-esser** : Réduction des sibilances
- **Limiter** : Protection contre les distorsions

#### Effets de Sortie
- **Égaliseur graphique** 15 
bandes
- **Compresseur multibande**
- **Reverb** : Effets de réverbération
- **Delay** : Effets d'écho

#### Présélections
- Gaming (optimisé pour Discord/jeux)
- Streaming (voix claire pour les streams)
- Podcast (qualité studio)
- Musique (écoute optimale)
- Personnalisé (créer et sauvegarder vos réglages)

### 🔄 Routage Audio Avancé via PipeWire
- Création de nœuds virtuels pour le routage flexible
- Connexion entre applications sans latence
- Séparation des flux audio par application
- Redirection vers OBS/Streamlabs
- Compatibilité avec tous les périphériques audio

### 📹 Intégration OBS/Streamlabs
- Création automatique d'un nœud virtuel Rootux_Output
- Intégration native avec les sources audio PipeWire dans OBS
- Contrôle séparé des volumes pour le stream et le monitoring
- Élimination des échos grâce au routage intelligent

### 🎨 Interface Utilisateur (GTK4 + Libadwaita)
- Design moderne suivant les guidelines GNOME
- Thème sombre par défaut (adaptable)
- Responsive : adaptation automatique à la taille de la fenêtre
- Onglets organisés : Mixeur, Effets, Routage, Paramètres
- Notifications pour les événements importants
- Barre d'outils avec raccourcis clavier

---

## 📦 Prérequis Système

### Systèmes Supportés
✅ Arch Linux et dérivés (CachyOS, Manjaro, EndeavourOS, Garuda)
✅ Debian et dérivés (Ubuntu, Pop!_OS, Linux Mint, Kali)
✅ Fedora et dérivés (RHEL, CentOS Stream)
✅ openSUSE (Tumbleweed, Leap)

### Dépendances Obligatoires

| Catégorie | Arch | Debian/Ubuntu | Fedora | openSUSE |
|----------|------|---------------|--------|----------|
| Runtime | python, python-pip | python3, python3-pip | python3, python3-pip | python3, python3-pip |
| GTK4 | python-gobject, python-cairo | python3-gi, python3-gi-cairo | python3-gobject, python3-cairo | python3-gobject, python3-cairo |
| GTK4 Bindings | - | gir1.2-gtk-4.0, gir1.2-libadwaita-1 | - | - |
| PipeWire | pipewire, pipewire-pulse, wireplumber | pipewire, pipewire-pulse, wireplumber | pipewire, pipewire-pulsea
udio, wireplumber | pipewire, pipewire-pulse, wireplumber |
| Audio Apps | easyeffects, qpwgraph | easyeffects, qpwgraph | easyeffects, qpwgraph | easyeffects, qpwgraph |
| Son Système | - | libcanberra-gtk3-module, libcanberra-pulse | libcanberra-gtk3 | libcanberra-gtk3 |
| Python Audio | python-pyaudio | python3-pyaudio, portaudio19-dev | python3-pyaudio | - |

### Dépendances Python
```
pygobject>=3.40.0
pycairo>=1.20.0
numpy>=1.21.0
pyaudio>=0.2.11
dbus-python>=1.2.18
```

---

## 📥 Installation

### Méthode 1 : Installation Automatique (Recommandée)
```bash
git clone https://github.com/Cape003/rootux.git
cd rootux
chmod +x install.sh
./install.sh
python3 rootux_gui.py
```

### Méthode 2 : Installation Manuelle

#### Arch Linux et dérivés
```bash
sudo pacman -Syu --needed --noconfirm
sudo pacman -S --needed --noconfirm \
    git python python-pip python-gobject \
    python-cairo python-numpy python-pyaudio \
    pipewire pipewire-pulse wireplumber \
    easyeffects qpwgraph
systemctl --user enable --now pipewire pipewire-pulse wireplumber
pip install --user pygobject pycairo numpy pyaudio dbus-python
python3 rootux_gui.py
```

#### Debian/Ubuntu et dérivés
```bash
sudo apt update -y && sudo apt upgrade -y
sudo apt install -y git python3 python3-pip python3-gi python3-gi-cairo \
    gir1.2-gtk-4.0 gir1.2-libadwaita-1 gir1.2-pango-1.0 \
    pipewire pipewire-pulse wireplumber \
    easyeffects qpwgraph \
    libcanberra-gtk3-module libcanberra-pulse \
    python3-venv python3-setuptools python3-dbus \
    portaudio19-dev python3-pyaudio
pip3 install --user pygobject pycairo numpy pyaudio dbus-python
systemctl --user enable --now pipewire pipewire-pulse wireplumber
python3 rootux_gui.py
```

#### Fedora/RHEL et dérivés
```bash
sudo dnf update -y
sudo dnf install -y git python3 python3-pip python3-gobject python3-cairo \
    python3-numpy pipewire pipewire-pulseaudio wireplumber \
    easyeffects qpwgraph libcanberra-gtk3 python3-pyaudio
pip3 install --user pyaudio

systemctl --user enable --now pipewire pipewire-pulse wireplumber
python3 rootux_gui.py
```

#### openSUSE
```bash
sudo zypper refresh
sudo zypper install -y git python3 python3-pip python3-gobject \
    python3-cairo python3-numpy pipewire pipewire-pulse \
    wireplumber easyeffects qpwgraph libcanberra-gtk3
pip3 install --user pyaudio
systemctl --user enable --now pipewire pipewire-pulse wireplumber
python3 rootux_gui.py
```

---

## 🚀 Utilisation

### Lancement
```bash
python3 rootux_gui.py
```

### Raccourcis Clavier
| Raccourci | Action |
|-----------|--------|
| Ctrl+Q | Quitter |
| Ctrl+N | Nouveau profil |
| Ctrl+S | Sauvegarder |
| Ctrl+O | Charger profil |
| Ctrl+R | Rafraîchir nœuds |
| F1 | Aide |
| F12 | Plein écran |

### Intégration OBS/Streamlabs
1. **Dans Rootux** : Créer un nœud virtuel nommé Rootux_Output
2. **Dans OBS** : Ajouter une source Entrée Audio (PipeWire) et sélectionner Rootux_Output
3. **Désactiver** la capture audio par défaut d'OBS
4. **Tester** : Parler dans le micro ou lancer un son

---

## 🔧 Dépannage

### Problèmes Courants

**ModuleNotFoundError: No module named gi**
```bash
# Arch
sudo pacman -S python-gobject
# Debian/Ubuntu
sudo apt install python3-gi python3-gi-cairo
# Fedora
sudo dnf install python3-gobject python3-cairo
```

**PipeWire not running**
```bash
systemctl --user start pipewire pipewire-pulse wireplumber
systemctl --user enable pipewire pipewire-pulse wireplumber
```

**No audio devices found**
```bash
systemctl --user restart pipewire pipewire-pulse wireplumber
pw-cli list-objects
```

---

## 📊 Performances

| Composant | Utilisation Typique |
|-----------|---------------------|
| CPU | 2-5% (idle), 10-20% (traitement actif) |
| RAM | 50-100 Mo |
| Latence Audio | < 10ms |
| Taille Disque | ~50 Mo |

---

## 🤝 Contribuer

### Idées de Contributions
- Audio spatial (7.1, 5.1 surround)
- Détection automatique des applications
- Intégration Discord
- Support LADSPA/LV2 plugins
- Enregistrement audio intégré
- 
Interface Web

---

## 📜 Licence

**MIT License** - Copyright (c) 2026 Cape003

Voir [LICENSE](LICENSE) pour le texte complet.

---

## 🙏 Remerciements

- **Cape003** - Créateur et mainteneur
- **Le Chat (Mistral AI)** - Assistance au développement
- **SteelSeries Sonar** - Inspiration
- **PipeWire** - Infrastructure audio
- **GTK4** - Framework UI

---

Rootux: Le Sonar pour Linux, par la communauté, pour la communauté. 🎛️🐧