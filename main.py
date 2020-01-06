from geojson import Feature, Polygon, load
import cartopy.crs as ccrs
import matplotlib.pyplot as plt

ax = plt.axes(projection=ccrs.PlateCarree())
# ax.stock_img()

f = open('suburb-2-nsw.geojson')

coords = load(f)

selected_suburb = coords["features"][0]
print(selected_suburb)

def make_aggregate_lat_lon(suburb):
  individual_coords = suburb['geometry']['coordinates']
  # print(individual_coords)
  # geojson goes long/lat
  agg_lon = list(map(lambda x: x[0], individual_coords[0]))
  agg_lat = list(map(lambda x: x[1], individual_coords[0]))

  return agg_lon, agg_lat

def make_suburb_map(suburb):
  agg_lon, agg_lat = make_aggregate_lat_lon(suburb)

  plt.plot(agg_lon, agg_lat,
          color='blue', linewidth=2,
          transform=ccrs.Geodetic(),
          )

  plt.cla()

for suburb in coords["features"][:100]:
  make_suburb_map(suburb)

plt.show()