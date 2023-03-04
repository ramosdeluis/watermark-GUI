from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image, ImageDraw, ImageFont


root = Tk()
root.title('Watermark Creator')
root.minsize(750, 625)
file_path = ''


def convert_image():
    global file_path, watermark_text

    opened_image = Image.open(file_path)

    image_width, image_height = opened_image.size
    draw = ImageDraw.Draw(opened_image)

    font_size = int(image_width / (5 + (len(watermark_text.get())**(1/2))))

    font = ImageFont.truetype('Arial.ttf', font_size)

    x, y = int(image_width/2), int(image_height/2)

    draw.text((x, y), watermark_text.get(), font=font, fill='#FFF', stroke_width=5, stroke_fill='#222', anchor='ms')
    opened_image.show()


def open_file():
    global file_path
    file_path = filedialog.askopenfilename()
    img = Image.open(file_path)
    img = img.resize((500, 500), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(root, image=img)
    panel.image = img
    panel.place(relx=.175, rely=.15)


wa_text = Label(root, text='Watermark Text: ')
wa_text.place(relx=.225, rely=.075)

watermark_text = Entry(root, width=35)
watermark_text.place(relx=.375, rely=.075)

get_file_button = Button(root, text='Select Image', command=open_file)
get_file_button.place(relx=.3, rely=.025)

watermark_button = Button(root, text='Create Watermarked File', command=convert_image)
watermark_button.place(relx=.475, rely=.025)

if __name__ == '__main__':
    root.mainloop()
