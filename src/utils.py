import os
import matplotlib.pyplot as plt
from types import SimpleNamespace

PYVIS_NETWORK_OPTIONS = """
    var options = {
      "edges": {
        "color": {
          "inherit": false
        },
        "smooth": false
      },
      "layout": {
        "hierarchical": {
          "enabled": true
        }
      },
      "physics": {
        "hierarchicalRepulsion": {
          "centralGravity": 0,
          "nodeDistance": 160
        },
        "minVelocity": 0.75,
        "solver": "hierarchicalRepulsion"
      }
    }
    """

COLORS = SimpleNamespace(**{
    'light_yellow': '#fffaed',
    'light_red': '#f4cccc',
    'light_purple': '#d9d2e9',
    'light_blue': '#cfe2f3',
    'light_pink': '#f8e7ee',
    'amaranth': '#f57382',
    'orange': '#faaf96',
    'gray': '#9996a1',
    'yellow': '#f3bd19',
    'blue': '#2478b7',
    'green': '#4abb5f',
    'red': '#da472d'
    })


def display_png_image(network, filename):
    network.show(filename)
    os.system(f"python convert.py {filename} {filename.replace('.html', '.png')}")
    os.remove(filename)
    img = plt.imread(filename.replace('.html', '.png'))
    plt.figure(figsize=(20, 10))
    plt.axis('off')
    fig = plt.imshow(img)
    return fig
