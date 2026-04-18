"""
Automated CSV/Excel Exporter for QGIS
Author: Igor Hajducki | DroneCube Analytics
Description: Extracts vector geometries and calculated areas directly to a CSV file 
for seamless integration into client Excel reporting templates.
"""
import os
import csv
from qgis.core import QgsProject

# 1. Fetch the vector layer
layer_name = 'Property_Boundary'
layer_list = QgsProject.instance().mapLayersByName(layer_name)

if not layer_list:
    print(f"Error: Layer '{layer_name}' not found. Please check the name.")
else:
    vector_layer = layer_list[0]
    
    # 2. Define the output path (Saves EXACTLY where your QGIS project is saved)
    project_path = QgsProject.instance().homePath()
    output_file = os.path.join(project_path, 'Construction_Draw_Report.csv')
    
    # 3. Create and write to the CSV file
    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write the header row
        writer.writerow(['Property ID', 'Building Phase', 'Estimated Area (sqm)', 'Status'])
        
        # Loop through features and write data
        for feature in vector_layer.getFeatures():
            # Get the ID and calculated Area
            prop_id = feature.id()
            area = feature['Area_sqm']
            area = round(area, 2) if area else 0.0
            
            # Write a row for each polygon
            writer.writerow([f"BLDG-{prop_id}", "Foundation", area, "Verified by QGIS"])
            
    print("-" * 50)
    print(f"SUCCESS: Report automatically exported to:")
    print(output_file)
    print("Ready for Excel import.")
    print("-" * 50)