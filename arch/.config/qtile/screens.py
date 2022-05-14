import os
from libqtile.config import Screen
from libqtile import layout, bar, widget, hook

screens = [
    Screen(
        top=bar.Bar(
            [
                # widget.CurrentLayout(),
                widget.GroupBox(highlight_method='text', disable_drag=True,
                                this_current_screen_border='#1fc1f2', padding=10,
                                visible_groups=["1", "2", "3", "4"]),
                widget.Prompt(),
                widget.WindowName(padding=20),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                # widget.Systray(padding=10),
               #widget.Net(interface="enp4s0f3u4", label="Et"),
                widget.Wlan(interface="wlp2s0", format="📶 {essid} |{quality}|",
                            background="#000000.2", padding=10),
                widget.Volume(emoji=True, background="#000000.2", fontsize=10, padding=10),


                widget.Battery(
                    format=" 🔋  {percent:0.1%} {char}",
                    update_interval=5,
                    low_percentage=0.10,
                    charge_char="🗱",
                    discharge_char="",
                    full_char="",
                    unknown_char="",
                    low_foreground="#ffffff",
                    low_background="#ff0000",
                    margin=10,
                    padding=10,
                    background="#000000.2"
                ),
                widget.Clock(format="%H:%M", padding=20, background="#000000.2"),

            ],
            24,
            margin=[5, 5, 0, 5],
            background="#000000.2",
        ),
        wallpaper='~/.wallpaper/wall.jpg',
        wallpaper_mode='fill',
    ),
]

