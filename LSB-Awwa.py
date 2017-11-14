
from PIL import Image, ImageFont, ImageDraw
import textwrap


def find_message(file_location):
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


def hide_message(secret_image, template_image):

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


    while True:
        print('press 1 to encode, 2 to decode, 0 to exit')
        action = int(input())
        if action == 1:  #hide message
            print("encode mode")
            hide_message("secret/secret1.png", "images/samoyed.jpg")
            print("message hidden succesfully")
        elif action == 2:  #find message
            print("decode")
            print("dino 1, fox 2")
            photo = int(input())
            if photo == 1:
              find_message("hidden/o.png")
              print("recovered message from the dino")
            elif photo ==2:
                find_message("hidden/encoded_image.png")
                print("recovered message from the fox")

        elif action == 0:
          print("exiting program")
          break



