from geojson import Feature, Polygon, load
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
import numpy as np

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

def make_numpy_array_from_vertices(suburb):
  individual_coords = suburb['geometry']['coordinates'][0]

  return np.array(individual_coords)

def make_suburb_map(suburb):
  ax = plt.axes(projection=ccrs.PlateCarree())

  agg_lon, agg_lat = make_aggregate_lat_lon(suburb)
  plt.plot(agg_lon, agg_lat,
          color='#2A80B9',
          linewidth=2,
          transform=ccrs.Geodetic()
          )

  """
  I started doing this but it's not working
  and I don't understand why
  print(np.column_stack([agg_lat, agg_lon]))
  poly = Polygon(np.column_stack([agg_lat, agg_lon]),
    color="#2A80B9",
    # fill=True,
    transform=ccrs.Geodetic()
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
