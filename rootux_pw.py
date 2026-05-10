#!/usr/bin/env python3
# Rootux - Gestion PipeWire
# Créé par Cape003 avec l'aide de l'IA (Le Chat, Mistral AI)

import subprocess


class PipeWireManager:
    """Gère les nœuds et connexions PipeWire pour Rootux."""
    
    def list_nodes(self):
        """Liste tous les nœuds PipeWire."""
        result = subprocess.run(['pw-cli', 'list-objects'], capture_output=True, text=True)
        return result.stdout.splitlines()

    def create_virtual_sink(self, name):
        """Crée un sink virtuel."""
        subprocess.run([
            'pw-cli', 'create-node',
            f'{{"factory": {{"name": "libpipewire-module-loopback"}}, "properties": {{"node.name": "{name}"}}}}'
        ], check=False)

    def create_virtual_source(self, name):
        """Crée une source virtuelle."""
        subprocess.run([
            'pw-cli', 'create-node',
            f'{{"factory": {{"name": "libpipewire-module-loopback"}}, "properties": {{"node.name": "{name}"}}}}'
        ], check=False)

    def connect_nodes(self, source, target):
        """Connecte un nœud source à un nœud cible."""
        subprocess.run(['pw-loopback', f'--capture={source}', f'--playback={target}'], check=False)

    def destroy_all_nodes(self):
        """Détruit tous les nœuds."""
        subprocess.run(['pw-cli', 'destroy-all'], check=False)


if __name__ == '__main__':
    pw = PipeWireManager()
    print('Nœuds disponibles:', pw.list_nodes())