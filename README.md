# ArcGIS Python Toolbox: Data Management

A Python toolbox of repetion-reducing tools to help manage data in ArcGIS Pro/Enterprise.

Please note this is a work in progress. Additional tools and functionality will be added over time.

## Latest software versions tested:
Python 3.9.x

ArcGIS Pro 3.0.2

## Tools Included:

### Feature Layer Cloner
    - Copies 1 or more Feature Layers
        - Can be from multiple geodatabases
    - Appends current date string as YYYYMMDD to layer name
        - Four-digit year, two-digit month, two-digit day (example: 19991215)
        - This default valued can be edited by the user
    - The current ArcGIS Pro workspace environment is the default destination of the copied files
        - The workspace/target destination can be edited by the user
        - At this time, only one target destination is available
    - Shapefiles can be cloned, but the tool will convert them into geodatabase feature layers
        - Writing back to the shapefile format is not permitted
