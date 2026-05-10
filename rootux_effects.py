#!/usr/bin/env python3
# Rootux - Gestion des effets audio
# Créé par Cape003 avec l'aide de l'IA (Le Chat, Mistral AI)

import subprocess
import json
from pathlib import Path


class EffectsManager:
    """Gère les effets audio pour Rootux."""
    
    def __init__(self):
        self.config_dir = Path.home() / '.config/rootux/effects'
        self.config_dir.mkdir(parents=True, exist_ok=True)

    def apply_preset(self, preset_name):
        """Applique un preset Easy Effects."""
        try:
            subprocess.run(['flatpak', 'run', 'com.github.wwmm.easyeffects', '--preset', preset_name], check=True)
        except:
            subprocess.run(['easyeffects', '--preset', preset_name], check=False)

    def export_rootux_preset(self, preset_name, config):
        """Exporte une configuration Rootux vers Easy Effects."""
        ee_config = {
            'name': preset_name,
            'input': {'device': 'Rootux_Mic_Source', 'volume': 1.0, 'mute': False},
            'output': {'device': 'Rootux_Output', 'volume': 1.0, 'mute': False},
            'effects': {'input': [], 'output': []}
        }
        
        # Ajouter EQ
        eq_config = config.get('eq', {})
        if eq_config:
            ee_config['effects']['input'].append({
                'type': 'equalizer',
                'parameters': {
                    'bands': [
                        {'frequency': 60, 'gain': eq_config.get('60Hz', 0)},
                        {'frequency': 120, 'gain': eq_config.get('120Hz', 0)},
                        {'frequency': 250, 'gain': eq_config.get('250Hz', 0)},
                        {'frequency': 500, 'gain': eq_config.get('500Hz', 0)},
                        {'frequency': 1000, 'gain': eq_config.get('1kHz', 0)},
                        {'frequency': 2000, 'gain': eq_config.get('2kHz', 0)},
                        {'frequency': 4000, 'gain': eq_config.get('4kHz', 0)},
                        {'frequency': 8000, 'gain': eq_config.get('8kHz', 0)},
                        {'frequency': 12000, 'gain': eq_config.get('12kHz', 0)},
                        {'frequency': 16000, 'gain': eq_config.get('16kHz', 0)}
                    ]
                }
            })
        
        # Ajouter Compresseur
        comp_config = config.get('compressor', {})
        if comp_config:
            ee_config['effects']['input'].append({
                'type': 'compressor',
                'parameters': {
                    'ratio': comp_config.get('ratio', 4),
                    'threshold': comp_config.get('threshold', -20),
                    'attack': comp_config.get('attack', 10),
                    'release': comp_config.get('release', 100)
                }
            })
        
        # Ajouter Noise Gate
        gate_config = config.get('noise_gate', {})
        if gate_config:
            ee_config['effects']['input'].append({
                'type': 'gate',
                'parameters': {
                    'threshold': gate_config.get('threshold', -30),
                    'attack': gate_config.get('attack', 5),
                    'release': gate_config.get('release', 50)
                }
            })
        
        return ee_config

    def start_easyeffects(self):
        """Lance Easy Effects."""
        try:
            subprocess.Popen(['easyeffects'])
        except FileNotFoundError:
            subprocess.Popen(['flatpak', 'run', 'com.github.wwmm.easyeffects'])


if __name__ == '__main__':
    em = EffectsManager()
    print('EffectsManager prêt')