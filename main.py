from geojson import Feature, Polygon, load
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
import numpy as np
import random

f = open('input/syd-teams.geojson')

coords = load(f)

def make_aggregate_lat_lon(suburb):
  individual_coords = suburb['geometry']['coordinates']

  # geojson goes long/lat
  # we aggregate the latitudes and longitudes of the polygon,
  # and then use those independently
  agg_lon = list(map(lambda x: x[0], individual_coords[0]))
  agg_lat = list(map(lambda x: x[1], individual_coords[0]))

  return agg_lon, agg_lat

# In the format: [edgecolor, facecolor]
COLORS = [
  # Blue
  ['#2A80B9', (41/255, 128/255, 185/255, 0.4)],
  # Red
  [(231/255, 76/255, 60/255, 1.0), (231/255, 76/255, 60/255,0.4)],
  # Slytherin
  [(66 / 255, 133 / 255, 30 / 255, 1.0), (66 / 255, 133 / 255, 30 / 255, 0.4)],
  # Hufflepuff
  [(1, 220/255, 0, 1.0), (1, 220/255, 0, 0.4)],
  # And purple
  [(177/255, 13/255, 201/255, 1.0), (177/255, 13/255, 201/255, 0.4)]
]

def make_suburb_map(suburb):
  ax = plt.axes()
  agg_lon, agg_lat = make_aggregate_lat_lon(suburb)
  edgecolor, facecolor = random.choice(COLORS)
  
  plt.fill(agg_lon, agg_lat,
          edgecolor=edgecolor,
          linewidth=2,
          facecolor=facecolor
          # transform=ccrs.Geodetic()
          )
  ax.axis('off')
  
  """
  # I started doing this but it's not working
  # and I don't understand why
  print(np.column_stack([agg_lat, agg_lon]))
  poly = Polygon(np.column_stack([agg_lat, agg_lon]),
    color="#2A80B9",
    fill=True
    # fill=True,
    # transform=ccrs.Geodetic()
  )

  ax.add_patch(poly)
  """

  save_map(suburb)
  plt.clf()

def save_map(suburb):
  suburb_name = suburb['properties']['name']
  plt.savefig(f'output/sydney/{suburb_name}.png', bbox_inches='tight')

for suburb in coords:
  make_suburb_map(suburb)
