#!/bin/bash

# Start Process
run() {
	if ! pgrep "$1" ; then
		"$@" &
	fi
}

# Start or Restart Process
run-or-restart() {
	if ! pgrep "$1" ; then
		"$@" &
	else
		process-restart "$@"
	fi
}

# UI Compositor
run picom --dbus --backend glx -bc --experimental-backends  # Picom

# Applications That Only Run Once On Their Own
run lxpolkit                          # lxpokit for sudo
run albert                            # Albert Launcher
run sxhkd                             # Start Keybinding Daemon - sxhkd
run xcape -e 'Caps_Lock=Escape'       # Caps Lock is Escape if tapped
run variety                           # Wallpaper
run dunst                             # Notifications
run nm-applet                         # Systray - Network Management 
run blueman-applet                    # Systray - Bluetooth
run flameshot                         # Systray - Screenshots
run volumeicon                        # Systray - Volume Icon
run cbatticon                         # Systray - Battery Icon
#run /usr/lib/geoclue-2.0/demos/agent  # GoeLocation Service
#run redshift                          # Late-Night Redshift Diplay