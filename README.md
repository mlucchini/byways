# Byways

## Install

```
pip3 install -r requirements.txt
echo "GOOGLE_MAPS_API_KEY=<YOUR_GOOGLE_MAP_API_KEY>" > .env
```

## Convert all GeoJSON files to KML

From `geojson` directory to `kml` directory:

```
python3 src/geojson_to_kml.py
```

## Output

```
Success: geojson/dorset.json --> kml/dorset.json.kml
Success: geojson/isle-wight.json --> kml/isle-wight.json.kml
Success: geojson/kent.json --> kml/kent.json.kml
Success: geojson/east-sussex.json --> kml/east-sussex.json.kml
Success: geojson/west-sussex.json --> kml/west-sussex.json.kml
Success: geojson/devon.json --> kml/devon.json.kml
Success: geojson/surrey.json --> kml/surrey.json.kml
Success: geojson/somerset.json --> kml/somerset.json.kml
Success: geojson/hampshire.json --> kml/hampshire.json.kml
```
