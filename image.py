#  变黑白
from PIL import Image
image_file = Image.open("photo.jpg")  # open colour image
image_file = image_file.convert('L')  # convert image to black and white
# image_black_white.save('balck_white.png')
image_file.show()
image_file.save("result.jpg")
