Elevation
-------

1. Download EU-DEM data: https://land.copernicus.eu/pan-european/satellite-derived-products/eu-dem/eu-dem-v1.1?tab=mapview (Paris E30N20)
2. Inside a container, `docker run -v $(pwd):/data -it geodata/gdal /bin/bash`
3. Extract bounding box
    ```
    from osgeo import gdal
    
    ds = gdal.Open('eu_dem_v11_E30N20.TIF')
    ds = gdal.Translate('out.tif', ds, projWin = [3752053.73535, 2894806.99222, 3767044.87711, 2885187.56956])
    ds = None
    ```
4. Project
    ```
    gdalwarp out.tif reprojected.tif -t_srs "+proj=longlat +ellps=WGS84"
    ```
5. Convert to ASC
   ```
   gdal_translate -of AAIGrid -ot Int32 reprojected.tif reprojected.asc
   gdal_calc.py reprojected.asc 1000*A
   sed -i "s/^ //" reprojected.asc
   sed -i "s/-2147483648/0/g" reprojected.asc
   tail -n+7 reprojected.asc
   ``` 
   
Information about reprojected.tif
----

```
Driver: GTiff/GeoTIFF
Files: out.tif
Size is 677, 312
Coordinate System is:
GEOGCS["WGS 84",
    DATUM["unknown",
        SPHEROID["WGS84",6378137,298.257223563]],
    PRIMEM["Greenwich",0],
    UNIT["degree",0.0174532925199433]]
Origin = (2.226407348458726,48.910165721774916)
Pixel Size = (0.000320470672179,-0.000320470672179)
Metadata:
  AREA_OR_POINT=Area
  DataType=Elevation
Image Structure Metadata:
  INTERLEAVE=BAND
Corner Coordinates:
Upper Left  (   2.2264073,  48.9101657) (  2d13'35.07"E, 48d54'36.60"N)
Lower Left  (   2.2264073,  48.8101789) (  2d13'35.07"E, 48d48'36.64"N)
Upper Right (   2.4433660,  48.9101657) (  2d26'36.12"E, 48d54'36.60"N)
Lower Right (   2.4433660,  48.8101789) (  2d26'36.12"E, 48d48'36.64"N)
Center      (   2.3348867,  48.8601723) (  2d20' 5.59"E, 48d51'36.62"N)
Band 1 Block=677x3 Type=Float32, ColorInterp=Gray
  Description = Band_1
  NoData Value=-3.4028234663852886e+38
  Metadata:
    BandName=Band_1
    RepresentationType=ATHEMATIC
```