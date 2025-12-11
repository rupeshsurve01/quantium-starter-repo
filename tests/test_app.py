import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import importlib
import app

def test_header_is_present():
    layout = app.app.layout
    header = layout.children[0].children
    assert "Pink Morsel Sales Visualiser" in header

def test_graph_is_present():
    layout = app.app.layout
    graph = layout.children[2]
    assert graph.id == "line-chart"

def test_region_picker_is_present():
    layout = app.app.layout
    radio_items = layout.children[1].children[1]
    assert radio_items.id == "region-picker"
