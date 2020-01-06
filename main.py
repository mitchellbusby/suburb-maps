from geojson import Feature, Polygon, load
import cartopy.crs as ccrs
import matplotlib.pyplot as plt

# ax.stock_img()

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

def make_suburb_map(suburb):
  ax = plt.axes(projection=ccrs.PlateCarree())

  agg_lon, agg_lat = make_aggregate_lat_lon(suburb)
  plt.plot(agg_lon, agg_lat,
          color='#2A80B9',
          linewidth=2,
          transform=ccrs.Geodetic(),
          )
  """
  plt.fill_between(agg_lon, agg_lat,
          facecolor='#2A80B9',
          transform=ccrs.Geodetic(),
  )
  """
  save_map(suburb)
  plt.clf()

def save_map(suburb):
  suburb_name = suburb['properties']['name']
  plt.savefig(f'output/sydney/{suburb_name}.png', bbox_inches='tight')

for suburb in coords:
  make_suburb_map(suburb)
