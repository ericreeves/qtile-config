# coding: utf-8
from libqtile.config import Screen
from libqtile import widget, bar

from Xlib import display as xdisplay

import re # for string sanitization
import unicodedata
import os
home = os.path.expanduser('~')

# Solarized light
# theme = dict(
#     base03 = '#002b36',
#     base02 = '#073642',
#     base01 = '#586e75',
#     base00 = '#657b83',
#     base0 = '#839496',
#     base1 = '#93a1a1',
#     base2 = '#eee8d5',
#     base3 = '#fdf6e3',
#     yellow = '#b58900',
#     orange = '#cb4b16',
#     red = '#dc322f',
#     magenta = '#d33682'
# )

# Theme Colors
theme = dict(
    base03 = '#111111',
    base02 = '#222222',
    base01 = '#eeeeee',
    base00 = '#657b83',
    base0 = '#839496',
    base1 = '#93a1a1',
    base2 = '#eee8d5',
    base3 = '#fdf6e3',
    base4 = '#4c566a',
    base5 = '#555555',
    current = '#7f86ce',
    updates = '#ef937d',
    urgent = '#cb4b16',
)

color_schemes = [
    dict(
        background = theme['base03'],
        arrow_color = theme['base02'],
        foreground = theme['base01']
    ),
    dict(
        background = theme['base02'],
        arrow_color = theme['base03'],
        foreground = theme['base01']
    )
]

dim_color_scheme = dict(
    background = theme['base03'],
    arrow_color = theme['base02'],
    foreground = theme['base5']
)

# Separator-related functions and variables

def separator(right_looking = True):
    global color_scheme
    if right_looking:
        separator.current_scheme = 1 - separator.current_scheme
        color_scheme = color_schemes[separator.current_scheme]

        return widget.TextBox(
            u'\ue0b0', 
            **separator_defaults,
            background = color_scheme["background"],
            foreground = color_scheme["arrow_color"]
        )
    else:
        ret = widget.TextBox(
            u'\ue0b2', 
            **separator_defaults,
            background = color_scheme["background"],
            foreground = color_scheme["arrow_color"]
        )

        separator.current_scheme = 1 - separator.current_scheme
        color_scheme = color_schemes[separator.current_scheme]

        return ret

color_scheme = color_schemes[1]
separator.current_scheme = 1

font_default = 'Segoe UI Nerd Font'
font_bold_default = 'Segoe UI Bold Nerd Font'

separator_defaults = dict(
    font=font_default,
    fontsize=24,
    padding=0,
)

widget_defaults = dict(
    font=font_default,
    fontsize=14,
    padding=6,
)
extension_defaults = widget_defaults.copy()

icon_defaults = dict(
    font=font_default,
    fontsize = 18,
    padding = 6,
)

widget_small_defaults = dict(
    font=font_default,
    fontsize=12,
    padding=6,
)

tasklist_widget_defaults = dict(
    font=font_default,
    fontsize=13,
)

battery_widget_defaults = dict(
    battery=0,
#    format='{char}[{percent:2.0%}]  ',
    format='{char} {percent:2.0%} {hour:d}h:{min:02d}m',
#    format='{char} {hour:d}h:{min:02d}m',
    low_percentage=0.2,
    update_interval=5,
    show_short_text=True,
    charge_char='',
    empty_char='',
    discharge_char='',
    hide_threshold=0
)

def sanitize_string(s):
    # return s.encode('ascii', 'ignore').decode('ascii', 'ignore')
    ns=str(s)
    return ns.replace('\xe2\x80\x8b', '')
    # return s.encode('ascii', 'ignore').decode('unicode_escape')

#    return input_string.decode('utf8').encode('ascii', errors='ignore')
#    clean_string = re.sub('<[^<]+>', "", input_string)
    # bstring = b'str(my_byte_str, 'utf-8')
    # clean_string = re.sub('[^0-9a-zA-Z\s]+', "", input_string)
    # return clean_string

# def sanitize_string2(input_string):
#     clean_string = [s for s in input_string if s.isascii()]
#     clean_string = "".join(clean_string)
#     return clean_string


bar_widgets = [

    widget.CurrentLayoutIcon(
        **widget_defaults,scale=0.7,
        **color_scheme,
    ),

    widget.CurrentLayout(
        **widget_defaults,
        **color_scheme,
        width=80,
    ),

    separator(),

    widget.Spacer(
        length = 5,
        **color_scheme,
    ),

widget.GroupBox(
        **widget_defaults,
        **color_scheme,
        disable_drag=True,
        hide_unused=True,
        rounded=True,
        padding_x=2,
        padding_y=2,
        # Text colors
        active=theme["base01"],
        inactive=theme["base5"],
        # Current screen colors
        highlight_method='line',
        highlight_color=theme["base4"],
        this_current_screen_border=theme["current"],
        # Urgent colors
        urgent_alert_method="line",
        urgent_border=theme["urgent"]
    ),

    widget.Spacer(
        length = 8,
        **color_scheme,
    ),

    separator(),

    widget.Spacer(
        length = 4,
        **color_scheme,
    ),

    # widget.TextBox(
    #     '|',
    #     **icon_defaults,
    #     **color_scheme,
    # ),

    # widget.WindowList(
    #     **widget_defaults,
    #     **color_scheme,
    #     # selected=('<b>[ ', ' ]</b>')
    # ),


    widget.TaskList(
        **tasklist_widget_defaults,
        **color_scheme,
        highlight_method='border',
        borderwidth=1,
        max_title_width=800,
        margin_x=1,
        margin_y=1,
        padding_x=8,
        padding_y=2,
    ),


    # widget.TextBox(
    #     '|',
    #     **icon_defaults,
    #     **color_scheme,
    # ),

    # separator(),

    # widget.Spacer(
    #     length = 4,
    #     **color_scheme,
    # ),

    # widget.WindowTabs(
    #     **widget_defaults,
    #     **color_scheme,
    # ),


    separator(right_looking = False),

    widget.Net(
        **widget_small_defaults,
        **color_scheme,
        interface="wlp115s0",
        format='{down} ↓↑ {up}',
    ),

    # separator(right_looking = False),
    
    # widget.CPUGraph(
    #     **widget_defaults,
    #     **color_scheme,
    #     frequency=0.33,
    #     samples=300,
    #     border_width=0,
    #     line_width=1,
    #     fill_color=theme['base4'],
    #     margin_x=12
    # ),

    separator(right_looking = False),

    widget.Clock(
        **widget_defaults,
        **color_scheme,
        font_size=16,
        fontshadow="#FFFFFF",
        format='%A %B %d, %Y',
#        format='%A %B %d, %Y  |  %H:%M:%S',
    ),

    separator(right_looking = False),

    widget.Clock(
        **widget_defaults,
        **color_scheme,
        font_size=16,
        fontshadow="#FFFFFF",
        format='%H:%M:%S',
    ),

    separator(right_looking = False),

    widget.CheckUpdates(
        **widget_defaults,
        **color_scheme,
        distro="Arch",
        exec='pamac-manager --updates',
        display_format='',
        no_update_string='',
        update_interval=1800,
        colour_no_updates=color_scheme["foreground"],
        colour_have_updates=theme["updates"],
    ),

    widget.Systray(
        icon_size=24,
        **widget_defaults,
        **color_scheme,
    ),


    # separator(right_looking = False),

    widget.LaunchBar( [
            ('', 'qshell:self.qtile.cmd_shutdown()', 'logout from qtile')
        ],
        **widget_defaults,
        **color_scheme,
    ),

    # widget.Spacer(
    #     length = 16,
    #     **color_scheme,
    # ),

    # separator(right_looking = False),

    # # Volume icon and widget
    # widget.TextBox(
    #     u'\ue8ef',
    #     **icon_defaults,
    #     **color_scheme,
    # ),
    # widget.Volume(
    #     **widget_defaults,
    #     **color_scheme,
    #     device = "sysdefault",
    #     format='[{percent:2.0%}]  '
    # ),


    # widget.Spacer(
    #     length = 16,
    #     **color_scheme,
    # ),

    # separator(right_looking = False),
    
    # # Brightness icon and widget
    # widget.TextBox(
    #     u'\u263c',
    #     **icon_defaults,
    #     **color_scheme,
    # ),
    # widget.Backlight(
    #     **widget_defaults,
    #     **color_scheme,
    #     backlight_name='intel_backlight',
    #     format='[{percent:2.0%}]  '
    # ),

    # separator(right_looking = False),
    
    # widget.Battery(
    #     **widget_defaults,
    #     **battery_widget_defaults,
    #     **color_scheme
    # ),

    # separator(right_looking = False),
    
    # # Battery icon and widget
    # widget.TextBox(
    #     u'\ue832', 
    #     **icon_defaults,
    #     **color_scheme,
    # ),
    # widget.BatteryIcon(
    #     **widget_defaults,
    #     **battery_widget_defaults,
    #     **color_scheme,
    #     battery=1
    # ),

]

# Second screen bar
separator.current_scheme = 0

second_bar_widgets = [
    widget.GroupBox(
        **widget_defaults,
        **color_scheme,
    ),

    separator(),

    widget.Spacer(
        length = 16,
        **color_scheme,
    ),

    widget.CurrentLayout(
        **widget_defaults,
        **color_scheme,
    ),

    widget.CurrentLayoutIcon(
        **widget_defaults,scale=0.5,
        **color_scheme,
    ),

    separator(),

    widget.Spacer(
        length = 16,
        **color_scheme,
    ),

    widget.WindowName(
        **widget_defaults,
        **color_scheme,
    ),

    separator(right_looking = False),

    widget.CurrentScreen(
        **widget_defaults,
        **color_scheme,
        active_text = "active",
        inactive_text = "inactive"
    ),
]

screens = [
    Screen(
        top=bar.Bar(
            bar_widgets,
            24,
        ),
    ),
]

def get_num_monitors():
    num_monitors = 0
    try:
        display = xdisplay.Display()
        screen = display.screen()
        resources = screen.root.xrandr_get_screen_resources()

        for output in resources.outputs:
            monitor = display.xrandr_get_output_info(output, resources.config_timestamp)
            preferred = False
            if hasattr(monitor, "preferred"):
                preferred = monitor.preferred
            elif hasattr(monitor, "num_preferred"):
                preferred = monitor.num_preferred
            if preferred:
                num_monitors += 1
    except Exception as e:
        # always setup at least one monitor
        return 1
    else:
        return num_monitors

if get_num_monitors() > 1:
    screens.append(
            Screen(
                    bottom=bar.Bar(
                    second_bar_widgets,
                    24,
            ),
        )
    )
