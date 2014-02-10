#!/usr/bin/env python

from pyplot_helper import barchart
from matplotlib import pyplot

chart = barchart.BarChart(ylabel="Awesomeness", title="Stacked BarChart", width=0.5)

chart.add_group_data("Group1", [("cat1", 1),
                                ("cat2", 2),
                                ("cat3", 3),
                                ("cat4", 4)])

chart.add_group_data("Group2", [("cat1", 2),
                                ("cat2", 3),
                                ("cat3", 3),
                                ("cat4", 1)])

chart.add_group_data("Group3", [("cat1", 2),
                                ("cat2", 1),
                                ("cat3", 1),
                                ("cat4", 2)])

chart.auto_add_categories()
chart.add_category("cat2", "2nd category")

fig, ax = pyplot.subplots(1, 1)
#fig.subplots_adjust(bottom=0.15)
chart.plot(ax, stacked=True)

# output
pyplot.savefig("barchart-stacked.png")
