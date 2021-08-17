from libqtile.config import EzKey as Key, EzDrag as Drag, EzClick as Click
from libqtile.lazy import lazy

from datetime import datetime as time
import subprocess

# BSP resizing taken from https://github.com/qtile/qtile/issues/1402
def resize(qtile, direction):
    layout = qtile.current_layout
    child = layout.current
    parent = child.parent

    while parent:
        if child in parent.children:
            layout_all = False

            if (direction == "left" and parent.split_horizontal) or (direction == "up" and not parent.split_horizontal):
                parent.split_ratio = max(5, parent.split_ratio - layout.grow_amount)
                layout_all = True
            elif (direction == "right" and parent.split_horizontal) or (direction == "down" and not parent.split_horizontal):
                parent.split_ratio = min(95, parent.split_ratio + layout.grow_amount)
                layout_all = True

            if layout_all:
                layout.group.layout_all()
                break

        child = parent
        parent = child.parent

@lazy.function
def resize_left(qtile):
    resize(qtile, "left")

@lazy.function
def resize_right(qtile):
    resize(qtile, "right")

@lazy.function
def resize_up(qtile):
    resize(qtile, "up")

@lazy.function
def resize_down(qtile):
    resize(qtile, "down")

@lazy.function
def float_to_front(qtile):
    for group in qtile.groups:
        for window in group.windows:
            if window.floating:
                window.cmd_bring_to_front()

def screenshot(to_clip = False, rect_select = False):
    def f(qtile):
        command = []
        
        if to_clip:
            # Requires to write one-line script `maim_to_clip` and have it in $PATH
            command += ["maim_to_clip"]
        else:
            command += ["maim", f"/home/pierre/Pictures/{time.now().isoformat()}.png"]

        if rect_select:
            command += ["-s"]

        subprocess.run(command)

    return f

keys = [
    # Layout change
    Key("M-<Tab>", lazy.next_layout()),
    Key("M-C-<Tab>", lazy.prev_layout()),
    
    # All Layouts
    # Change focus
    Key("M-j", lazy.layout.down()),
    Key("M-k", lazy.layout.up()),
    Key("M-h", lazy.layout.left()),
    Key("M-l", lazy.layout.right()),
    # Move window
    Key("M-S-j", lazy.layout.shuffle_down().when(layout='bsp')),
    Key("M-S-k", lazy.layout.shuffle_up().when(layout='bsp')),
    Key("M-S-h", lazy.layout.shuffle_left().when(layout='bsp')),
    Key("M-S-l", lazy.layout.shuffle_right().when(layout='bsp')),
    # Move window
    Key("M-A-j", lazy.layout.flip_down().when(layout='bsp')),
    Key("M-A-k", lazy.layout.flip_up().when(layout='bsp')),
    Key("M-A-h", lazy.layout.flip_left().when(layout='bsp')),
    Key("M-A-l", lazy.layout.flip_right().when(layout='bsp')),
    # Resize window
    Key("M-C-j", lazy.function(resize, 'down').when(layout='bsp')),
    Key("M-C-k", lazy.function(resize, 'up').when(layout='bsp')),
    Key("M-C-h", lazy.function(resize, 'left').when(layout='bsp')),
    Key("M-C-l", lazy.function(resize, 'right').when(layout='bsp')),
    # Reset
    Key("M-S-n", lazy.layout.normalize()),
    # Toggle split
    Key("M-<slash>", lazy.layout.toggle_split()),

    # Programs shortcuts
    Key("M-<Return>", lazy.spawn("alacritty")),
    Key("M-S-<Return>", lazy.spawn("alacritty -e tmux")),
    Key("M-e", lazy.spawn("dolphin")),

    Key("M-r", lazy.spawn("rofi -show combi")),
#    Key("M-r", lazy.spawn("albert show")),
    Key("A-<Tab>", lazy.spawn("rofi -show window")),

    Key("M-f", lazy.spawn("microsoft-edge-dev")),
    Key("M-S-f", lazy.spawn("firefox --private-window")),

    Key("<XF86Calculator>", lazy.spawn("gnome-calculator")),
    
    # Screen capture (Shift => selection, Ctrl => to clipboard)
    Key("<Print>", lazy.function(screenshot())),
    Key("C-<Print>", lazy.function(screenshot(to_clip = True))),
    Key("S-<Print>", lazy.function(screenshot(rect_select = True))),
    Key("C-S-<Print>", lazy.function(screenshot(to_clip = True, rect_select = True))),

    Key("M-<bracketright>", lazy.spawn("variety -n")),
    Key("M-<bracketleft>", lazy.spawn("variety -p")),
    Key("M-<backslash>", lazy.spawn("variety -f")),
    Key("M-S-<backslash>", lazy.spawn("variety -t")),
    Key("M-C-<backslash>", lazy.spawn("/home/eric/.local/bin/variety-random")),

    Key("M-q", lazy.window.kill()),
    Key("M-C-r", lazy.restart()),
    Key("M-C-q", lazy.shutdown()),
    Key("M-x", lazy.spawn("/home/eric/.local/bin/rofi-power-menu")),
    Key("M-z", lazy.spawn("/home/eric/.local/bin/lock-screen")),

#    Key("M-S-C-q", lqtile plasma iconawn("shutdown 0")),

    Key("M-A-l", lazy.spawn("/home/eric/.local/bin/lock-screen")),

    # Volume (hold shift for lighter adjustments)
    Key("<XF86AudioLowerVolume>", lazy.spawn("i3-volume -x 100 -X 1 down 5")),
    Key("S-<XF86AudioLowerVolume>", lazy.spawn("i3-volume -x 100 -X 1 down 1")),
    Key("<XF86AudioRaiseVolume>", lazy.spawn("i3-volume -x 100 -X 1 up 5")),
    Key("S-<XF86AudioRaiseVolume>", lazy.spawn("i3-volume -x 100 -X 1 up 1")),
    Key("<XF86AudioMute>", lazy.spawn("i3-volume -x 100 -X 1 mute")),

    # Brightness (hold shift for lighter adjustments)
    Key("<XF86MonBrightnessUp>", lazy.spawn("light -A 5")),
    Key("S-<XF86MonBrightnessUp>", lazy.spawn("light -A 1")),
    Key("<XF86MonBrightnessDown>", lazy.spawn("light -U 5")),
    Key("S-<XF86MonBrightnessDown>", lazy.spawn("light -U 1")),

    # Multi-screen test (not very convincing)
    Key("M-<Escape>", lazy.next_screen()),
#    Key("M-p", lazy.spawn("sh -c ~/scripts/monitor_layout.sh")),
#    Key("M-S-p", lazy.spawn("sh -c ~/scripts/rotate_secondary_display.sh")),

    # Key("<KP_End>",    lazy.group["1"].toscreen(), desc="Switch to group 1"),
    # Key("<KP_Down>",   lazy.group["2"].toscreen(), desc="Switch to group 2"),
    # Key("<KP_Next>",   lazy.group["3"].toscreen(), desc="Switch to group 3"),
    # Key("<KP_Left>",   lazy.group["4"].toscreen(), desc="Switch to group 4"),
    # Key("<KP_Begin>",  lazy.group["5"].toscreen(), desc="Switch to group 5"),
    # Key("<KP_Right>",  lazy.group["6"].toscreen(), desc="Switch to group 6"),
    # Key("<KP_Home>",   lazy.group["7"].toscreen(), desc="Switch to group 7"),
    # Key("<KP_Up>",     lazy.group["8"].toscreen(), desc="Switch to group 8"),
    # Key("<KP_Prior>",  lazy.group["9"].toscreen(), desc="Switch to group 9"),
    # Key("<KP_Insert>", lazy.group["0"].toscreen(), desc="Switch to group 0"),
]

mouse = [
    Drag("M-1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag("M-3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click("M-2", lazy.window.bring_to_front()),
    Click("M-S-1", lazy.window.toggle_floating()),
]

