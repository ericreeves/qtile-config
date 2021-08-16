from libqtile import layout

from plasma import Plasma

layout_defaults = dict(
    margin = 10,
    border_width = 1,
    border_focus="#1e90ff",
    grow_amount = 3,
    )

floating_layout_defaults = layout_defaults.copy()
floating_layout_defaults["border_width"] = 1

layouts = [
    layout.MonadTall(**layout_defaults),
    layout.MonadWide(**layout_defaults),
    layout.Max(**layout_defaults),
    Plasma(**layout_defaults),
    layout.Bsp(name="bsp", **layout_defaults),
    layout.Columns(**layout_defaults),
    layout.Stack(num_stacks=2),
    layout.Matrix(**layout_defaults),
    layout.RatioTile(**layout_defaults),
    layout.Tile(**layout_defaults),
    layout.TreeTab(
        sections=['FIRST', 'SECOND'],
        bg_color='#141414',
        active_bg='#0000ff',
        inactive_bg='#1e90ff',
        padding_y=5,
        section_top=10,
        panel_width=280),
    layout.VerticalTile(**layout_defaults),
    layout.Zoomy(**layout_defaults),
]

floating_layout = layout.Floating(auto_float_typesR=[
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'notify'},
    {'wmclass': 'popup_menu'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitkm
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
], **floating_layout_defaults)
