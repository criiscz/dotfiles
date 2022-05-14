from libqtile import layout
from libqtile.config import Group, Key, Match
from libqtile.lazy import lazy

from keys import keys

mod = "mod4"
groups = [
    Group("1", label="📁"),
    Group("2", label=""),
    Group("3", label="📚"),
    Group("4", label="🗎"),
    Group("5", label="", spawn="spotify"),
    Group("6", label="·"),
    Group("7", label="·"),
    Group("8", label="·", spawn="mailspring")
]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
        ]
    )

layouts = [
    layout.Columns(border_focus="#ffffff", border_normal="#000000", border_width=1, margin=5),
    # layout.Max(border_focus="#ffffff", border_normal="#000000", border_width=1, margin=5),
    layout.Stack(num_stacks=1, margin=5, border_width=0),
    layout.Tile(margin=5, border_width=1, border_focus="#ffffff.4", border_on_single=False),
]

b  =2
a = 1
