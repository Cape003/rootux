#!/bin/bash
# Rootux - Script d'installation
# Créé par Cape003 avec l'aide de l'IA (Le Chat, Mistral AI)

set -e

echo "=========================================="
echo "       Installation de Rootux"
echo "       Créé par Cape003"
echo "=========================================="
echo

detect_distro() {
    if [ -f /etc/os-release ]; then
        . /etc/os-release
        case "$ID" in
            debian|ubuntu|pop|linuxmint|kali|deepin|neon|raspbian)
                echo "debian"
                ;;
            arch|manjaro|endeavouros|garuda|artix|cachyos)
                echo "arch"
                ;;
            fedora|rhel|centos|rocky|almalinux)
                echo "fedora"
                ;;
            opensuse*|suse*|tumbleweed|leap)
                echo "opensuse"
                ;;
            gentoo)
                echo "gentoo"
                ;;
            alpine)
                echo "alpine"
                ;;
            void)
                echo "void"
                ;;
            *)
                echo "unknown"
                ;;
        esac
    else
        echo "unknown"
    fi
}

install_debian() {
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
    systemctl --user enable --now pipewire pipewire-pulse wireplumber
    echo "Installation terminée pour Debian/Ubuntu!"
}

install_arch() {
    echo "Détection d'Arch Linux ou dérivé (y compris CachyOS)..."
    sudo pacman -Syu --needed --noconfirm
    sudo pacman -S --needed --noconfirm git python python-pip python-gobject \
        python-cairo python-numpy python-pyaudio \
        pipewire pipewire-pulse wireplumber \
        easyeffects qpwgraph libcanberra-gtk3
    systemctl --user enable --now pipewire pipewire-pulse wireplumber
    echo "Installation terminée pour Arch Linux!"
}

install_fedora() {
    echo "Détection de Fedora/RHEL ou dérivé..."
    sudo dnf update -y
    sudo dnf install -y git python3 python3-pip python3-gobject python3-cairo \
        python3-numpy pipewire pipewire-pulseaudio wireplumber \
        easyeffects qpwgraph libcanberra-gtk3 python3-pyaudio
    systemctl --user enable --now pipewire pipewire-pulse wireplumber
    echo "Installation terminée pour Fedora/RHEL!"
}

install_opensuse() {
    echo "Détection d'openSUSE..."
    sudo zypper refresh
    sudo zypper install -y git python3 python3-pip python3-gobject \
        python3-cairo python3-numpy pipewire pipewire-pulse \
        wireplumber easyeffects qpwgraph libcanberra-gtk3
    pip3 install --user pyaudio
    systemctl --user enable --now pipewire pipewire-pulse wireplumber
    echo "Installation terminée pour openSUSE!"
}

install_unknown() {
    echo "Distribution non détectée automatiquement."
    echo "Essayons une installation générique..."
    
    if command -v apt &> /dev/null; then
        echo "APT détecté, tentative d'installation Debian..."
        install_debian
    elif command -v pacman &> /dev/null; then
        echo "Pacman détecté, tentative d'installation Arch..."
        install_arch
    elif command -v dnf &> /dev/null; then
        echo "DNF détecté, tentative d'installation Fedora..."
        install_fedora
    elif command -v zypper &> /dev/null; then
        echo "Zypper détecté, tentative d'installation openSUSE..."
        install_opensuse
    else
        echo "Impossible de détecter le gestionnaire de paquets."
        echo "Veuillez installer manuellement les dépendances."
        return 1
    fi
}

distro=$(detect_distro)
echo "Distribution détectée : $distro"
echo

case "$distro" in
    debian) install_debian ;;
    arch) install_arch ;;
    fedora) install_fedora ;;
    opensuse) install_opensuse ;;
    *) install_unknown ;;
esac

echo
echo "=========================================="
echo "       Installation terminée !"
echo "=========================================="
echo
echo "Pour lancer Rootux :"
echo "  python3 rootux_gui.py"
