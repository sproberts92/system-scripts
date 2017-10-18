#!/home/sprob/Code/Scripts/i3/venv/bin/python
# To do: install python-i3-py with pacman and
# use system python (no venv).

import i3

# retrieve only active outputs
outputs = (w for w in i3.get_outputs() if w['active'])

# set current workspace to output 0
for w in outputs:
	i3.workspace(w['current_workspace'])
	i3.command('move', 'workspace to output right')
