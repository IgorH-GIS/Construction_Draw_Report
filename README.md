[README.txt](https://github.com/user-attachments/files/26858474/README.txt)

# QGIS to Excel Exporter: Construction Draw Reports

**Author:** Igor Hajducki | DroneCube Analytics
**Tech Stack:** Python, PyQGIS, QGIS 3.x

## Overview
This Python script automates the extraction of vector geometries and precise area calculations (sqm) from QGIS directly into a `.csv` format. It is specifically designed to streamline the creation of **lender-facing construction draw reports** by eliminating manual data entry and human error.

## Features
* **Automated Data Extraction:** Pulls polygon IDs and calculated areas directly from the active `Property_Boundary` layer.
* **Excel-Ready Output:** Generates a structured CSV file that seamlessly integrates with standard construction "fill-in" Excel templates.
* **Conservative Accuracy:** Ensures that the data reported to lenders is based on exact digital footprints (e.g., poured foundations) rather than visual estimations.

## Usage
1. Run the script within the QGIS Python Console.
2. The script targets the specific vector layer and extracts the `$area` values.
3. A `Construction_Draw_Report.csv` file is automatically saved to the active QGIS project directory.
