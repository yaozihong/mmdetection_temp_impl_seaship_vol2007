import os
from xml.etree import ElementTree as ET

folder_path = "data/VOCdevkit/VOC2007/Annotations"

def modify_annotation_path(target_path):
    for filename in os.listdir(target_path):
        if filename.endswith(".xml"):
            # Read the XML file
            filepath = os.path.join(target_path, filename)
            tree = ET.parse(filepath)
            root = tree.getroot()

            path_element = root.find('path')

            original_path = path_element.text
            new_path = original_path.replace("VOC2007", "VOCdevkit/VOC2007")
            path_element.text = new_path

            # Write the modified XML file
            tree.write(filepath)

modify_annotation_path(folder_path)
print(f"Modified path in annotation XML files under {folder_path}")
