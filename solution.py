"""A program that encodes and decodes hidden messages in images through LSB steganography"""
from PIL import Image, ImageFont, ImageDraw
import textwrap

#def decode_image(file_location="photos/o.png"):


def decode_image(file_location):
   #open the image containing secret message
    encoded_image = Image.open(file_location)
   # get the red channel of RGB
    red_channel = encoded_image.split()[0]

    #get size of image, its given in 2-tuple (width, height).
    x_size = encoded_image.size[0]
    y_size = encoded_image.size[1]

    #create new image to store the recoevered pixels of hidden message in it
    decoded_image = Image.new("RGB", encoded_image.size)
    pixels = decoded_image.load()

    for i in range(x_size):
        for j in range(y_size):
            if bin(red_channel.getpixel((i, j)))[-1] == '0':
                pixels[i, j] = (255, 255, 255)
            else:
                pixels[i, j] = (0,0,0)

    decoded_image.save("recovered/recovered.png")

# def write_text(text_to_write, image_size):
#     """Writes text to an RGB image. Automatically line wraps
#
#     text_to_write: the text to write to the image
#     """
#     image_text = Image.new("RGB", image_size)
#     font = ImageFont.load_default().font
#     drawer = ImageDraw.Draw(image_text)
#
#     #Text wrapping. Change parameters for different text formatting
#     margin = offset = 10
#     for line in textwrap.wrap(text_to_write, width=60):
#         drawer.text((margin,offset), line, font=font)
#         offset += 10
#     return image_text

def encode_image(secret_image, template_image):

    template_image = Image.open(template_image)
    red_template = template_image.split()[0]
    green_template = template_image.split()[1]
    blue_template = template_image.split()[2]

    x_size = template_image.size[0]
    y_size = template_image.size[1]

    # #text draw
    # image_text = write_text(text_to_encode, template_image.size)

    image_sec = Image.open(secret_image)
    secret_image_pixel = image_sec.convert('1')

    #this is a new image that has  secret image hidden in original image
    encoded_image = Image.new("RGB", (x_size, y_size))
    pixels = encoded_image.load()

    for i in range(x_size):
        for j in range(y_size):
            red_template_pix = bin(red_template.getpixel((i,j)))
            tencode_pix = bin(secret_image_pixel.getpixel((i,j)))

            if tencode_pix[-1] == '1':
                red_template_pix = red_template_pix[:-1] + '1'
            else:
                red_template_pix = red_template_pix[:-1] + '0'
            pixels[i, j] = (int(red_template_pix, 2), green_template.getpixel((i,j)), blue_template.getpixel((i,j)))

    encoded_image.save("hidden/encoded_image.png")

if __name__ == '__main__':

    #decode_image()
    #encode_image()
    while True:
        print('press 1 to encode, 2 to decode, 0 to exit')
        action = int(input())
        if action == 1:  #hide message
            print("encode mode")
            encode_image("secret/secret1.png","images/samoyed.jpg")
            print("message hidden succesfully")
        elif action == 2:  #find message
            print("decode")
            print("dino 1, fox 2")
            photo = int(input())
            if photo == 1:
              decode_image("hidden/o.png")
              print("recovered message from the dino")
            elif photo ==2:
                decode_image("hidden/encoded_image.png")
                print("recovered message from the fox")

        elif action == 0:
          print("exiting program")
          break



