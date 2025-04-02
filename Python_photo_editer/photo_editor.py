'''
    Program to edit photos to replace photoshop
    Uses pillow library

'''
from PIL import Image, ImageEnhance, ImageFilter
import os 

path = "./original_images"
# pathOut = "./edited_images"
pathOut = os.path.join(os.getcwd(), 'edited_images')
os.makedirs(pathOut, exist_ok=True)

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    edit = img.filter(ImageFilter.SHARPEN).rotate(0).convert('L')

    factor = 1.3
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)
    clean_name = os.path.splitext(filename)[0]
    
    #edit.save(f'.{pathOut}/{clean_name}_edited.jpg')
    edit.save(os.path.join(pathOut, f'{clean_name}_edited.jpg'))