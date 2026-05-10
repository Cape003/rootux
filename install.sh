#!/bin/bash
# Rootux - Script d'installation
# Créé par Cape003 avec l'aide de l'IA (Le Chat, Mistral AI)

set -e

detect_distro() {
    if [ -f /etc/os-release ]; then
        . /etc/os-release
        case "$ID" in
            debian|ubuntu|pop|linuxmint) echo "debian";;
            arch|manjaro) echo "arch";;
            fedora|rhel|centos) echo "fedora";;
            opensuse*) echo "opensuse";;
            *) echo "unknown";;
        esac
    else
        echo "unknown"
    fi
}

install_debian() {
    sudo apt update -y
    sudo apt install -y git python3 python3-pip python3-gi python3-gi-cairo \
        gir1.2-gtk-4.0 gir1.2-libadwaita-1 pipewire pipewire-pulse wireplumber \
        easyeffects qpwgraph libcanberra-gtk3-module python3-dbus portaudio19-dev python3-pyaudio
    pip3 install --user pygobject pycairo numpy pyaudio dbus-python
    systemctl --user enable --now pipewire pipewire-pulse wireplumber
}

install_arch() {
    sudo pacman -Syu --needed git python python-gobject python-cairo python-numpy python-pyaudio \
        pipewire pipewire-pulse wireplumber easyeffects qpwgraph libcanberra-gtk3
    systemctl --user enable --now pipewire pipewire-pulse wireplumber
}

distro=$(detect_distro)
case "$distro" in
    debian) install_debian;;
    arch) install_arch;;
    *) echo "Distribution non supportée. Voir README.md" && exit 1;;
esac

echo "Installation terminée. Lancez Rootux avec: python3 rootux_gui.py"