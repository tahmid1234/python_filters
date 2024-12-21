from PIL import Image

image = Image.open('6224262396751495697.jpg')

width, height = image.size

print(f"Width: {width} pixels")
print(f"Height: {height} pixels")

resized_image = image.resize((300, 80))

# Save the resized image
resized_image.save('whitebg.jpg')
image2 = Image.open('whitebg.jpg')
print(image2.size)
