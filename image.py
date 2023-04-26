from PIL import Image
import os

input_dir = 'static/ranked-emblems/ranked-emblem'
output_dir = 'static/rank-icons'

# Set the desired width and height of the cropped images
width, height = 72*4.5, 72*4

# Loop over all images in a directory
for filename in os.listdir(input_dir):
    if filename.endswith('.png'):
        img = Image.open(os.path.join(input_dir, filename))
        
        # Get the current width and height of the image
        current_width, current_height = img.size
        
        # Calculate the x and y coordinates of the top left corner of the cropped image
        x = (current_width - width) / 2
        y = (current_height - height) / 2
        
        # Crop the image
        img = img.crop((x, y, x+width, y+height))
        
        # Save the cropped image with a new filename
        img.save(os.path.join(output_dir, filename))