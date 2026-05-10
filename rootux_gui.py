#!/usr/bin/env python3
# Rootux - Studio audio tout-en-un pour Linux
# Créé par Cape003 avec l'aide de l'IA
# Licence MIT

import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')

from gi.repository import Gtk, Adw, Gdk
import subprocess


class PipeWireManager:
    def create_virtual_sink(self, name):
        subprocess.run([
            'pw-cli', 'create-node',
            f'{{"factory": {{"name": "libpipewire-module-loopback"}}, "properties": {{"node.name": "{name}"}}}}'
        ], check=False)

    def connect_nodes(self, source, target):
        subprocess.run(['pw-loopback', f'--capture={source}', f'--playback={target}'], check=False)


class RootuxWindow(Adw.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_title('Rootux Studio')
        self.set_default_size(900, 650)
        
        # Forcer le mode sombre pour un look "Pro Audio"
        Adw.StyleManager.get_default().set_color_scheme(Adw.ColorScheme.PREFER_DARK)
        
        self.pw_manager = PipeWireManager()
        
        # Amélioration drastique du CSS
        css = """
        .mixer-channel {
            background-color: @card_bg_color;
            border-radius: 12px;
            padding: 15px 20px;
            margin: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.3);
        }
        .mixer-channel label {
            font-size: 14px;
        }
        .fader {
            min-height: 280px;
            margin: 15px 0;
        }
        .fader highlight {
            background-color: @accent_bg_color;
        }
        .mute-btn {
            border-radius: 50%;
            min-width: 45px;
            min-height: 45px;
            background-color: @view_bg_color;
        }
        .mute-btn:checked {
            background-color: @error_bg_color;
            color: white;
            box-shadow: 0 0 10px @error_bg_color;
        }
        """
        provider = Gtk.CssProvider()
        provider.load_from_data(css.encode())
        Gtk.StyleContext.add_provider_for_display(
            Gdk.Display.get_default(), 
            provider, 
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )
        
        # Conteneur principal
        self.main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.set_content(self.main_box)
        
        # HeaderBar avec sélecteur de vue (onglets modernes)
        self.header = Adw.HeaderBar()
        self.main_box.append(self.header)
        
        self.stack = Adw.ViewStack()
        self.stack.set_vexpand(True)
        self.main_box.append(self.stack)
        
        self.switcher = Adw.ViewSwitcher()
        self.switcher.set_stack(self.stack)
        self.switcher.set_policy(Adw.ViewSwitcherPolicy.WIDE)
        self.header.set_title_widget(self.switcher)
        
        # Génération des pages
        self._create_mixer_tab()
        self._create_routing_tab()

    def _create_mixer_tab(self):
        # Utilisation d'un ScrolledWindow au cas où l'écran est trop petit
        scroll = Gtk.ScrolledWindow()
        scroll.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.NEVER)
        
        # L'astuce est ici : on aligne les canaux HORIZONTALEMENT
        mixer_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        mixer_box.set_halign(Gtk.Align.CENTER)
        mixer_box.set_valign(Gtk.Align.CENTER)
        scroll.set_child(mixer_box)
        
        # Données des canaux (Nom, Icône GNOME, Volume par défaut)
        channels = [
            ('Game', 'applications-games-symbolic', 100),
            ('Chat', 'user-available-symbolic', 80),
            ('Media', 'audio-x-generic-symbolic', 75),
            ('Aux', 'audio-speakers-symbolic', 50),
            ('Mic', 'audio-input-microphone-symbolic', 90)
        ]
        
        for name, icon, default_vol in channels:
            # Conteneur du canal (la "tranche" de la table de mixage)
            channel_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
            channel_box.add_css_class("mixer-channel")
            
            # En-tête du canal (Icône + Nom)
            icon_img = Gtk.Image.new_from_icon_name(icon)
            icon_img.set_pixel_size(32)
            label = Gtk.Label(label=f"<b>{name}</b>", use_markup=True)
            
            channel_box.append(icon_img)
            channel_box.append(label)
            
            # Fader (Slider vertical)
            fader = Gtk.Scale(
                orientation=Gtk.Orientation.VERTICAL,
                adjustment=Gtk.Adjustment(lower=0, upper=100, value=default_vol, step_increment=1)
            )
            fader.set_inverted(True) # Met le 100% en haut et le 0% en bas
            fader.set_draw_value(True)
            fader.set_value_pos(Gtk.PositionType.BOTTOM)
            fader.add_css_class("fader")
            channel_box.append(fader)
            
            # Bouton Mute
            mute_btn = Gtk.ToggleButton()
            mute_btn.set_icon_name("audio-volume-muted-symbolic")
            mute_btn.add_css_class("mute-btn")
            mute_btn.set_tooltip_text(f"Mute {name}")
            mute_btn.connect('toggled', lambda b, n=name: print(f'Mute {n} : {"Actif" if b.get_active() else "Inactif"}'))
            
            # Centrer le bouton Mute
            btn_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
            btn_box.set_halign(Gtk.Align.CENTER)
            btn_box.append(mute_btn)
            channel_box.append(btn_box)
            
            mixer_box.append(channel_box)
        
        # Ajout à la stack avec une icône pour l'onglet
        page = self.stack.add_titled(scroll, 'mixer', 'Mixeur')
        page.set_icon_name('audio-volume-high-symbolic')

    def _create_routing_tab(self):
        # Utilisation des composants natifs Adwaita pour un look "Paramètres" propre
        page = Adw.PreferencesPage()
        
        # Section 1 : Création des flux
        group_create = Adw.PreferencesGroup(title="Création de nœuds virtuels", description="Générez vos points de routage PipeWire")
        page.add(group_create)
        
        sinks = ['Game_Sink', 'Chat_Sink', 'Media_Sink', 'Rootux_Output']
        for name in sinks:
            row = Adw.ActionRow(title=f"Créer l'interface {name}")
            row.set_subtitle(f"Génère un libpipewire-module-loopback pour {name}")
            
            btn = Gtk.Button(label='Créer', valign=Gtk.Align.CENTER)
            btn.add_css_class("suggested-action")
            btn.connect('clicked', lambda b, n=name: self.pw_manager.create_virtual_sink(n))
            
            row.add_suffix(btn)
            group_create.add(row)
        
        # Section 2 : Monitoring des nœuds
        group_nodes = Adw.PreferencesGroup(title="Nœuds PipeWire Actifs")
        
        refresh_btn = Gtk.Button(label="Rafraîchir la liste", valign=Gtk.Align.CENTER)
        refresh_btn.set_icon_name("view-refresh-symbolic")
        refresh_btn.connect('clicked', self._refresh_nodes)
        
        header_row = Adw.ActionRow(title="Liste des objets actuels")
        header_row.add_suffix(refresh_btn)
        group_nodes.add(header_row)
        
        # Conteneur pour la liste des nœuds
        self.nodes_list = Gtk.ListBox()
        self.nodes_list.add_css_class("boxed-list") # Style natif GNOME pour les listes
        group_nodes.add(self.nodes_list)
        
        page.add(group_nodes)
        
        stack_page = self.stack.add_titled(page, 'routing', 'Routage')
        stack_page.set_icon_name('network-workgroup-symbolic')

    def _refresh_nodes(self, btn):
        self.nodes_list.remove_all()
        try:
            result = subprocess.run(['pw-cli', 'list-objects'], capture_output=True, text=True)
            for node in result.stdout.splitlines()[:50]: # Limiter l'affichage pour ne pas geler l'UI
                if node.strip():
                    row = Adw.ActionRow(title=node.strip()[:60] + ("..." if len(node)>60 else ""))
                    self.nodes_list.append(row)
        except Exception as e:
            row = Adw.ActionRow(title="Erreur lors de la récupération des nœuds")
            row.set_subtitle(str(e))
            self.nodes_list.append(row)


class RootuxApp(Adw.Application):
    def __init__(self):
        super().__init__(application_id='com.github.Cape003.rootux')
        self.connect('activate', self.on_activate)
    
    def on_activate(self, app):
        win = RootuxWindow(application=app)
        win.present()


if __name__ == '__main__':
    app = RootuxApp()
    app.run(None)
