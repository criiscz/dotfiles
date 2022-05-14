import os
import subprocess

from libqtile import layout, hook
from libqtile.config import Click, Drag, Match
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

from groups import groups, layouts
from keys import keys
from screens import screens


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.run([home + '/.config/qtile/scripts/autostart.sh'])


mod = "mod4"
terminal = guess_terminal()
xf = "ttf-jetbrains-mono"

widget_defaults = dict(
    font="ttf-jetbrains-mono",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

auto_minimize = True

wmname = "LG3D"
