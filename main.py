from rembg import remove
from PIL import Image

input_path = './input/1.jpeg'
output_path = './output/1.png'

input = Image.open(input_path)
output = remove(input)
output.save(output_path)
