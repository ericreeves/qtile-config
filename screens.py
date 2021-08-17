# coding: utf-8
from libqtile.config import Screen
from libqtile import widget, bar
from theming import theme as qtile_theme

from Xlib import display as xdisplay


theme = qtile_theme.theme

color_schemes = [
    dict(
        # background = theme['background'],
        background = "#000000.1",
        arrow_color = "#666666",
        # arrow_color = theme['color8'],
        foreground = theme['color15']
    ),
    dict(
        # background = theme['color8'],
        background = "#000000.1",
        arrow_color = "#666666",
        # arrow_color = theme['color8'],
        foreground = theme['color15']
    )
]

# Separator-related functions and variables

def separator(right_looking = True):
    global color_scheme
    if right_looking:
        separator.current_scheme = 1 - separator.current_scheme
        color_scheme = color_schemes[separator.current_scheme]

        return widget.TextBox(
            "",
            # u'\ue0b0', 
            **separator_defaults,
            background = color_scheme["background"],
            foreground = color_scheme["arrow_color"]
        )
    else:
        ret = widget.TextBox(
            "",
            # u'\ue0b2', 
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

bar_defaults = dict(
    opacity=0.1,
    background='#000000',
)

widget_defaults = dict(
    font=font_default,
    fontsize=13,
    padding=6,
    opacity=0,
)
extension_defaults = widget_defaults.copy()

icon_defaults = dict(
    font=font_default,
    fontsize=18,
    padding=6,
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

bar_widgets = [

    widget.CurrentLayoutIcon(
        **widget_defaults,scale=0.7,
        **color_scheme,
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
        borderwidth=1,
        spacing=3,
        padding_x=2,
        padding_y=2,
        # Text colors
        active=theme["foreground"],
        inactive=theme["background"],
        # Current screen colors
        highlight_method='border',
        highlight_color=theme["color4"],
        block_highlight_text_color=theme["foreground"],
        this_current_screen_border=theme["color5"],
        # Urgent colors
        urgent_alert_method="line",
        urgent_border=theme["color1"]
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

    widget.TaskList(
        **tasklist_widget_defaults,
        **color_scheme,
        highlight_method='border',
        borderwidth=1,
        icon_size=20,
        max_title_width=800,
        margin_x=1,
        margin_y=1,
        padding_x=8,
        padding_y=4,
    ),

    widget.Net(
        **widget_small_defaults,
        **color_scheme,
        interface="wlp115s0",
        format='{down} ↓↑ {up}',
    ),

    separator(right_looking = False),

    widget.Clock(
        **widget_defaults,
        **color_scheme,
        format='%A %B %d, %Y',
    ),

    separator(right_looking = False),

    widget.Clock(
        **widget_defaults,
        **color_scheme,
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
        colour_have_updates=theme["color1"],
    ),

    widget.Systray(
        icon_size=24,
        **widget_defaults,
        **color_scheme,
    ),

    widget.LaunchBar( [
            ('', 'qshell:self.qtile.cmd_shutdown()', 'logout from qtile')
        ],
        **widget_defaults,
        **color_scheme,
    ),
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
            32,
            **bar_defaults
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
                    **bar_defaults
                    ),
            )
    )
