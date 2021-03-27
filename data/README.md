# Data Directory

This directory should contain all the data including things like the DEMs and 
initialization surfaces.  Please contact the maintainers of this repository for 
this data.

If you need to convert GeoTiff data to NetCDF then use the following command

```
gdal_translate -of NetCDF <input filename> <output filename>
```