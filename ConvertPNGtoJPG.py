#pip install PILLOW

from PIL import Image

im = Image.open("sample_image.png").convert("RGB")
im.save("sample_image.jpg", "jpeg")
