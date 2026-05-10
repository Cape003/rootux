#!/bin/bash
# Rootux - Script d'installation
# Créé par Cape003 avec l'aide de l'IA (Le Chat, Mistral AI)

set -e

echo "=========================================="
echo "       Installation de Rootux"
echo "       Créé par Cape003"
echo "=========================================="
echo

detect_package_manager() {
    if command -v pacman &> /dev/null; then
        echo "pacman"
    elif command -v apt &> /dev/null; then
        echo "apt"
    elif command -v dnf &> /dev/null; then
        echo "dnf"
    elif command -v zypper &> /dev/null; then
        echo "zypper"
    else
        echo "unknown"
    fi
}

install_packages() {
    local pm=$1
    
    case "$pm" in
        pacman)
            echo "Détection de Arch Linux ou dérivé..."
            sudo pacman -Syu --needed --noconfirm
            sudo pacman -S --needed --noconfirm \
                git python python-pip python-gobject \
                python-cairo python-numpy python-pyaudio \
                pipewire pipewire-pulse wireplumber \
                easyeffects qpwgraph
            ;;
        apt)
            echo "Détection de Debian/Ubuntu ou dérivé..."
            sudo apt update -y
            sudo apt install -y git python3 python3-pip python3-gi python3-gi-cairo \
                gir1.2-gtk-4.0 gir1.2-libadwaita-1 gir1.2-pango-1.0 \
                pipewire pipewire-pulse wireplumber \
                easyeffects qpwgraph \
                libcanberra-gtk3-module libcanberra-pulse \
                python3-venv python3-setuptools python3-dbus \
                portaudio19-dev python3-pyaudio
            pip3 install --user pygobject pycairo numpy pyaudio dbus-python
            ;;
        dnf)
            echo "Détection de Fedora/RHEL ou dérivé..."
            sudo dnf update -y
            sudo dnf install -y git python3 python3-pip python3-gobject python3-cairo \
                python3-numpy pipewire pipewire-pulseaudio wireplumber \
                easyeffects qpwgraph libcanberra-gtk3 python3-pyaudio
            ;;
        zypper)
            echo "Détection d'openSUSE..."
            sudo zypper refresh
            sudo zypper install -y git python3 python3-pip python3-gobject \
                python3-cairo python3-numpy pipewire pipewire-pulse \
                wireplumber easyeffects qpwgraph libcanberra-gtk3
            pip3 install --user pyaudio
            ;;
        *)
            echo "Gestionnaire de paquets non détecté."
            return 1
            ;;
    esac
    
    systemctl --user enable --now pipewire pipewire-pulse wireplumber
}

pm=$(detect_package_manager)
echo "Gestionnaire de paquets détecté : $pm"
echo

install_packages "$pm"

echo
echo "=========================================="
echo "       Installation terminée !"
echo "=========================================="
echo
echo "Pour lancer Rootux :"
echo "  python3 rootux_gui.py"
