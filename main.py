from geojson import Feature, Polygon, load
import cartopy.crs as ccrs
import matplotlib.pyplot as plt

# ax.stock_img()

f = open('input/mel-teams.geojson')

coords = load(f)

def make_aggregate_lat_lon(suburb):
  individual_coords = suburb['geometry']['coordinates']

  # geojson goes long/lat
  agg_lon = list(map(lambda x: x[0], individual_coords[0]))
  agg_lat = list(map(lambda x: x[1], individual_coords[0]))

  return agg_lon, agg_lat

def make_suburb_map(suburb):
  ax = plt.axes(projection=ccrs.PlateCarree())

  agg_lon, agg_lat = make_aggregate_lat_lon(suburb)

  plt.plot(agg_lon, agg_lat,
          color='blue', linewidth=2,
          transform=ccrs.Geodetic(),
          )
  save_map(suburb)
  plt.clf()

def save_map(suburb):
  suburb_name = suburb['properties']['name']
  plt.savefig(f'output/{suburb_name}.png')

for suburb in coords[:100]:
  make_suburb_map(suburb)
