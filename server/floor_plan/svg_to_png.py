import os 

vipshome = r'C:\vips-dev-8.11\bin'
os.environ['path'] = vipshome + ';' + os.environ['PATH']

import pyvips

# Execute in floorplan
files = os.listdir()
for fn in files:
    if ".svg" in fn:
        output_filename = fn.split(".svg")[0] + '.png'
        image = pyvips.Image.new_from_file(fn, dpi=72)
        image.write_to_file(output_filename)
