import os
from psd_tools import PSDImage

# Open the Photoshop file
psd = PSDImage.open('existing_file.psd')

# Select the layer you want to modify
layer = psd.layers[0]

# Replace the layer's image data with the new photo
with open('new_photo.jpg', 'rb') as f:
    layer.replace_content(f.read())

# Save the modified PSD file
psd.save('modified_file.psd')

# Export the modified file as a PNG
os.system(f'convert modified_file.psd modified_file.png')

# Save the PNG to the specific location
os.system(f'mv modified_file.png /path/to/destination')