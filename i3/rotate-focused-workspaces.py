#!/bin/python
import i3

# retrieve only active outputs
outputs = (w for w in i3.get_outputs() if w['active'])

# set current workspace to output 0
for w in outputs:
	i3.workspace(w['current_workspace'])
	i3.command('move', 'workspace to output right')

