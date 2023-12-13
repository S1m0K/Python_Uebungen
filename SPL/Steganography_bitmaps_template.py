# tkinter provides GUI objects and commands
import tkinter as tk
import tkinter.ttk as ttk

from Messages import Messages
from SteganoMethods import SteganoMethods

# math provides some functions (ceil, floor)
# Python Imaging Library (PIL) provides commands
# to comfortably open and save bitmap files

# An object (root) is created which represents the window.
# Its title and full screen property are set.
root = tk.Tk()
root.title("Steganography with bitmaps")
root.wm_state("zoomed")


# The labels used to interact with the user are cleared.
def ClearFeedbackLabels():
    label_secret_feedback["text"] = ""
    label_mode_feedback["text"] = ""


# This function is invoked when the user clicks the button
# "Load secret from file".
# It tries to open a textfile with the name specified in the
# corresponding entry field. Further, it tells the user
# whether the loading of the textfile succeeded and, if so,
# prints its contents in the text field below.
def button_secret_load_click():
    ClearFeedbackLabels()
    try:
        with open(path_secret.get(), mode="rt", encoding="utf-8") as tf:
            secret = tf.read()
    except:
        label_secret_feedback["text"] = "An error occurred while reading the file."
        text_secret.delete("1.0", "end")
    else:
        if secret == "":
            label_secret_feedback["text"] = "File empty"
        else:
            label_secret_feedback["text"] = "File loaded successfully."
        text_secret.delete("1.0", "end")
        text_secret.insert("1.0", secret)


# This function is invoked when the user clicks the button
# "Save secret to file".
# It tries to create or rewrite a textfile with the name
# specified in the corresponding entry field and to write
# the contents of the text field below into the file.
# Further, it tells the user whether the writing to the
# textfile succeeded.
def button_secret_save_click():
    ClearFeedbackLabels()
    secret = text_secret.get("1.0", "end")[:-1]
    if secret == "":
        label_secret_feedback["text"] = "Nothing to save"
        return
    try:
        with open(path_secret.get(), mode="wt", encoding="utf-8") as tf:
            if tf.write(secret) != len(secret):
                raise Exception
    except:
        label_secret_feedback["text"] = "An error occurred while saving to file."
    else:
        label_secret_feedback["text"] = "Secret saved successfully."


# This function is invoked by ButtonModeHideClick()
# after the secret was hidden successfully.
###### ENTER YOUR CODE HERE ######
def print_image_comparison(ImageDataOffset):
    text_mode.delete("1.0", "end")
    pass


# The following code lines try to display both
# bitmaps. They are not necessary for the program
# to work properly and may remain commented out.
#    try:
#        image = Image.open(PathImage.get())
#        width, height = image.size
#        ratio = min(LabelImageVirgin.winfo_width() / width,
#                    LabelImageVirgin.winfo_height() / height)
#        image = image.resize((math.floor(ratio * width),
#                              math.floor(ratio * height)))
#        image = ImageTk.PhotoImage(image)
#        LabelImageVirgin["image"] = image
#        LabelImageVirgin.image = image
#        image = Image.open(PathImage.get()[:-4] + "Hiding.bmp")
#        image = image.resize((math.floor(ratio * width),
#                              math.floor(ratio * height)))
#        image = ImageTk.PhotoImage(image)
#        LabelImageHiding["image"] = image
#        LabelImageHiding.image = image
#    except:
#        LabelModeFeedback["text"] = "An error occurred displaying the two images"
# This function is invoked when the user presses
# the button "Hide secret in image".
###### ENTER YOUR CODE HERE ######
def on_message_not_ok(message):
    print("Message !!!")
    pass


def button_mode_hide_click():
    ClearFeedbackLabels()
    bit_map_bytes_arr = SteganoMethods.get_bit_map_bytes_arr(path_image.get())

    important_values_dic = SteganoMethods.get_important_values(bit_map_bytes_arr)
    secret_word_char_arr = [char for char in text_secret.get("1.0", "end")]
    message = SteganoMethods.check_for_necessary_conventions(important_values_dic, secret_word_char_arr)

    if message != Messages.OK:
        on_message_not_ok(message)
        return

    finished_bit_map_arr = SteganoMethods.plant_secret_in_bit_map_arr(bit_map_bytes_arr, secret_word_char_arr,
                                                                      important_values_dic)


# This function is invoked when the user presses
# the button "Disclose secret from image".
###### ENTER YOUR CODE HERE ######
def button_mode_disclose_click():
    ClearFeedbackLabels()
    pass


# The window is divided into three frames.
frame_secret = ttk.Frame(master=root)
frame_secret["borderwidth"] = 5
frame_secret["relief"] = "sunken"
frame_mode = ttk.Frame(master=root)
frame_mode["borderwidth"] = 5
frame_mode["relief"] = "sunken"
frame_image = ttk.Frame(master=root)
frame_image["borderwidth"] = 5
frame_image["relief"] = "sunken"
frame_secret.pack(side="left", fill="both", expand=True)
frame_mode.pack(side="left", fill="y")
frame_image.pack(side="left", fill="both", expand=True)

# The labels, entries, buttons and text fields
# are defined and adjusted.
label_secret_caption = ttk.Label(master=frame_secret, text="Secret text")
label_secret_caption.pack(side="top", pady=5)
path_secret = tk.StringVar(value="./text.txt")
entry_secret = ttk.Entry(master=frame_secret, text=path_secret)
entry_secret.pack(side="top", padx=25, fill="x")
frame_secret_buttons = ttk.Frame(master=frame_secret)
frame_secret_buttons.pack(side="top", padx=15, pady=5, fill="x")
button_secret_load = ttk.Button(master=frame_secret_buttons,
                                text="Load secret from file",
                                command=button_secret_load_click)
button_secret_save = ttk.Button(master=frame_secret_buttons,
                                text="Save secret to file",
                                command=button_secret_save_click)
button_secret_load.pack(side="left", padx=10, fill="x", expand=True)
button_secret_save.pack(side="right", padx=10, fill="x", expand=True)
label_secret_feedback = ttk.Label(master=frame_secret, text="")
label_secret_feedback.pack(side="top", padx=25, pady=5, fill="x")
text_secret = tk.Text(master=frame_secret, width=10)
text_secret.pack(side="bottom", fill="both", expand=True, padx=25, pady=10)

label_mode_caption = ttk.Label(master=frame_mode, text="Mode")
label_mode_caption.pack(side="top", pady=5)
path_image = tk.StringVar(value="./image.bmp")
entry_image = ttk.Entry(master=frame_mode, text=path_image)
entry_image.pack(side="top", padx=25, fill="x")
frame_image_buttons = ttk.Frame(master=frame_mode)
frame_image_buttons.pack(side="top", padx=15, pady=5, fill="x")
button_mode_disclose = ttk.Button(master=frame_image_buttons,
                                  text="Disclose secret from image",
                                  width=25,
                                  command=button_mode_disclose_click)
button_mode_hide = ttk.Button(master=frame_image_buttons,
                              text="Hide secret in image",
                              width=button_mode_disclose.cget("width"),
                              command=button_mode_hide_click)
button_mode_disclose.pack(side="right", padx=10, fill="x", expand=True)
button_mode_hide.pack(side="left", padx=10, fill="x", expand=True)
label_mode_feedback = ttk.Label(master=frame_mode, text="")
label_mode_feedback.pack(side="top", padx=25, pady=5, fill="x")
text_mode = tk.Text(master=frame_mode, width=10)
text_mode.pack(side="bottom", fill="both", expand=True, padx=25, pady=10)

label_image_hiding_caption = ttk.Label(master=frame_image,
                                       text="Image containing the secret")
label_image_hiding_caption.pack(side="top", pady=5)
label_image_hiding = ttk.Label(master=frame_image)
label_image_hiding.pack(side="top", pady=5, fill="both", expand=True)
label_image_virgin_caption = ttk.Label(master=frame_image,
                                       text="Virgin image")
label_image_virgin_caption.pack(side="top", pady=5)
label_image_virgin = ttk.Label(master=frame_image)
label_image_virgin.pack(side="top", pady=5, fill="both", expand=True)

root.mainloop()
