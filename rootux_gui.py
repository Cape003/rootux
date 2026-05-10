#!/usr/bin/env python3
# Rootux - Studio audio tout-en-un pour Linux
# Créé par Cape003 avec l'aide de l'IA (Le Chat, Mistral AI)
# Licence MIT
# VERSION COMPLÈTEMENT CORRIGÉE POUR GTK4

import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')

from gi.repository import Gtk, Adw, Gdk
import subprocess


class PipeWireManager:
    """Gère les nœuds PipeWire."""
    
    def create_virtual_sink(self, name):
        """Crée un sink virtuel."""
        subprocess.run([
            'pw-cli', 'create-node',
            f'{{"factory": {{"name": "libpipewire-module-loopback"}}, "properties": {{"node.name": "{name}"}}}}'
        ], check=False)

    def connect_nodes(self, source, target):
        """Connecte deux nœuds."""
        subprocess.run(['pw-loopback', f'--capture={source}', f'--playback={target}'], check=False)


class RootuxWindow(Gtk.ApplicationWindow):
    """Fenêtre principale de Rootux."""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_title('Rootux')
        self.set_default_size(1000, 700)
        self.pw_manager = PipeWireManager()
        
        # CSS pour les styles (pas de set_margin_all !)
        css = (
            '.rootux-box { margin: 10px; } '
            '.fader { background: #2a2a2a; border-radius: 5px; min-height: 150px; } '
            '.mute-button { background: #3a3a3a; color: white; border-radius: 20px; } '
            '.mute-button:checked { background: #ff4444; } '
            'label { color: #eee; }'
        )
        provider = Gtk.CssProvider()
        provider.load_from_data(css.encode())
        Gtk.StyleContext.add_provider_for_display(
            Gdk.Display.get_default(), 
            provider, 
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )
        
        # Layout principal
        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        main_box.get_style_context().add_class("rootux-box")
        self.set_child(main_box)
        
        # HeaderBar
        header = Adw.HeaderBar()
        main_box.append(header)
        
        # Stack pour les onglets (pas de set_child_name !)
        self.stack = Gtk.Stack()
        self.stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        main_box.append(self.stack)
        
        # Créer les onglets
        self._create_mixer_tab()
        self._create_routing_tab()
        
        # Boutons pour changer d'onglet
        for name, page in [('Mixeur', 'mixer'), ('Routage', 'routing')]:
            btn = Gtk.ToggleButton(label=name)
            btn.connect('toggled', lambda b, p=page: self.stack.set_visible_child_name(p))
            header.pack_start(btn)

    def _create_mixer_tab(self):
        """Crée l'onglet Mixeur."""
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        box.get_style_context().add_class("rootux-box")
        
        # Canaux audio
        for name in ['Game', 'Chat', 'Media', 'Aux', 'Mic']:
            hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
            hbox.append(Gtk.Label(label=name))
            
            # Fader
            fader = Gtk.Scale(
                orientation=Gtk.Orientation.VERTICAL,
                adjustment=Gtk.Adjustment(lower=0, upper=100, value=75)
            )
            fader.set_size_request(30, 150)
            fader.get_style_context().add_class("fader")
            hbox.append(fader)
            
            # Bouton Mute
            mute_btn = Gtk.ToggleButton()
            mute_btn.get_style_context().add_class("mute-button")
            mute_btn.connect('toggled', lambda b, n=name: print(f'Mute {n}'))
            hbox.append(mute_btn)
            
            box.append(hbox)
        
        # Ajouter au Stack avec un nom (add_titled, pas add_child + set_child_name)
        self.stack.add_titled(box, 'mixer', 'Mixeur')

    def _create_routing_tab(self):
        """Crée l'onglet Routage."""
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        box.get_style_context().add_class("rootux-box")
        
        # Boutons pour créer des nœuds
        for name in ['Game_Sink', 'Chat_Sink', 'Media_Sink', 'Rootux_Output']:
            btn = Gtk.Button(label=f'Créer {name}')
            btn.connect('clicked', lambda b, n=name: self.pw_manager.create_virtual_sink(n))
            box.append(btn)
        
        # Bouton Rafraîchir
        refresh_btn = Gtk.Button(label='Rafraîchir')
        refresh_btn.connect('clicked', self._refresh_nodes)
        box.append(refresh_btn)
        
        # Liste des nœuds
        self.nodes_list = Gtk.ListBox()
        box.append(self.nodes_list)
        
        # Ajouter au Stack avec un nom (add_titled, pas add_child + set_child_name)
        self.stack.add_titled(box, 'routing', 'Routage')

    def _refresh_nodes(self, btn):
        """Rafraîchit la liste des nœuds PipeWire."""
        self.nodes_list.remove_all()
        result = subprocess.run(['pw-cli', 'list-objects'], capture_output=True, text=True)
        for node in result.stdout.splitlines():
            if node.strip():
                self.nodes_list.append(Gtk.Label(label=node))


class RootuxApp(Adw.Application):
    """Application Rootux."""
    
    def __init__(self):
        super().__init__(application_id='com.github.Cape003.rootux')
        self.connect('activate', self.on_activate)
    
    def on_activate(self, app):
        """Appelé quand l'application est lancée."""
        win = RootuxWindow(application=app)
        win.present()


if __name__ == '__main__':
    app = RootuxApp()
    app.run(None)
