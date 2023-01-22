from PIL import Image

# Open the image
image = Image.open("./readme/chessboard.png")

# Resize the image
image = image.resize((320, 320))

# Save the resized image
image.save("resized.png")