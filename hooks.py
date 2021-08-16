from libqtile import hook
import subprocess

# Run These on Initial Startup
@hook.subscribe.startup_once
def autostart():
    processes = [
        'autorandr --change && nitrogen --restore'.split(),
        'picom --dbus --backend glx -bc --experimental-backends'.split(),
        'setxkbmap -layout us'.split(),
        'setxkbmap -option caps:ctrl_modifier'.split(),
        'xsetroot -cursor_name left_ptr'.split(),
        'xcape -e Caps_Lock=Escape'.split(),
        'numlockx off'.split(),
        'dunst'.split(),
        'nm-applet'.split(),
        'blueman-applet'.split(),
        'flameshot'.split(),
        'volumeicon'.split(),
        'cbatticon'.split(),
        '/usr/lib/polkit-kde-authentication-agent-1'.split()
    ]
    for p in processes:
        subprocess.Popen(p)

# Run These at Every Restart
@hook.subscribe.startup
def start_always():
    processes = [
        ['autorandr', '--change', '&&', 'nitrogen', '--restore'],
        ['nitrogen', '--restore'],
        ['setxkbmap', '-layout', 'us'],
        ['setxkbmap', '-option', 'caps:ctrl_modifier'],
        ['xsetroot', '-cursor_name', 'left_ptr'],
        ['numlockx', 'off']
    ]
    for p in processes:
        subprocess.Popen(p)


# Always display launcher in current group
@hook.subscribe.client_new
def albert_open(window):
    if window.name == "Albert":
        window.cmd_togroup()

@hook.subscribe.client_new
def floating_dialogs(window):
    dialog = window.window.get_wm_type() == 'dialog'
    transient = window.window.get_wm_transient_for()
    if dialog or transient:
        window.floating = True
