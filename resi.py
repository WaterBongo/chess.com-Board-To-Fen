from PIL import Image

# Open the image
image = Image.open("./example2.png")

# Resize the image
image = image.resize((320, 320))

# Save the resized image
image.save("example2.png")