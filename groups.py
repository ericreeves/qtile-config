from libqtile.config import Group, EzKey as Key
from libqtile.lazy import lazy

from keys import keys

# GROUP Configuration
group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
group_layouts = ["monadtall", "monadtall", "monadtall", "monadtall",
                 "monadtall", "monadtall", "monadtall", "treetab", "floating", "monadwide"]
group_labels = ["1 ", "2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 ", "9 ", "0"]
#group_labels = ["Web", "Edit/chat", "Image", "Gimp", "Meld", "Video", "Vb", "Files", "Mail", "Music",]
#group_labels = ["", "", "", "", "", "", "", "", "", "",]

groups = []

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
        ))
groups = [Group(i) for i in "1234567890"]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key(f"M-{i.name}", lazy.group[i.name].toscreen()),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key(f"M-S-{i.name}", lazy.window.togroup(i.name, switch_group=True)),
        # mod1 + control + shift + letter of group = move focused window to group
        Key(f"M-S-C-{i.name}", lazy.window.togroup(i.name, switch_group=False)),
    ])