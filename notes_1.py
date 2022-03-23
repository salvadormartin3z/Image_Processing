from PIL import Image, ImageFilter

img = Image.open('./pokedex/pikachu.jpg')

"""
print(img)
print(img.format)
print(img.size)
print(img.mode)
"""

# new_image = filtered_img.show()
# new_image = filtered_img.rotate(90)
# new_image = filtered_img.resize((300, 300))
"""
box = (100, 100, 400, 400)
new_image = filtered_img.crop(box)
"""

filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save("blur.png", "png")

filtered_img = img.convert('L')
filtered_img.save("grey.png", "png")
