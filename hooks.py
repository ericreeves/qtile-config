from libqtile import hook
import subprocess
import os

# Run These on Initial Startup
@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/scripts/autostart.sh'])

# Run at Every Restart
@hook.subscribe.startup
def start_always():
    processes = [
        ['autorandr', '--change'],
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
