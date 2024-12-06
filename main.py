#!/usr/bin/env python
# coding: utf-8

# In[4]:


import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont, ImageTk

def upload_image():
    global img, image_path
    image_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")]
    )
    if image_path:
        img = Image.open(image_path)
        img.thumbnail((400, 400))
        tk_img = ImageTk.PhotoImage(img)
        canvas.create_image(200, 200, image=tk_img)
        canvas.image = tk_img
        status_label.config(text="Image uploaded successfully!")

def add_watermark():
    global img
    if not img:
        status_label.config(text="Please upload an image first!")
        return
    
    watermark_text = watermark_entry.get()
    if not watermark_text:
        status_label.config(text="Please enter watermark text!")
        return
    
    # Add watermark
    img_copy = img.copy()
    draw = ImageDraw.Draw(img_copy)
    font = ImageFont.truetype("arial.ttf", 20)  # Adjust font size if needed
    width, height = img_copy.size

    # Calculate text size using textbbox
    text_bbox = draw.textbbox((0, 0), watermark_text, font=font)
    text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]

    position = (width - text_width - 10, height - text_height - 10)  # Bottom-right corner
    draw.text(position, watermark_text, fill="white", font=font)
    
    # Show the watermarked image
    tk_img = ImageTk.PhotoImage(img_copy)
    canvas.create_image(200, 200, image=tk_img)
    canvas.image = tk_img
    
    # Save watermarked image
    save_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All Files", "*.*")]
    )
    if save_path:
        img_copy.save(save_path)
        status_label.config(text=f"Watermarked image saved at {save_path}")

# GUI setup
root = tk.Tk()
root.title("Watermarking App")
root.geometry("500x600")
root.resizable(False, False)

# Canvas to display the image
canvas = tk.Canvas(root, width=400, height=400, bg="lightgray")
canvas.pack(pady=10)

# Buttons and inputs
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

upload_btn = tk.Button(btn_frame, text="Upload Image", command=upload_image)
upload_btn.pack(side=tk.LEFT, padx=5)

watermark_label = tk.Label(root, text="Watermark Text:")
watermark_label.pack()

watermark_entry = tk.Entry(root, width=30)
watermark_entry.pack()

add_btn = tk.Button(root, text="Add Watermark", command=add_watermark)
add_btn.pack(pady=10)

status_label = tk.Label(root, text="", fg="green")
status_label.pack()

# Run the application
img = None  # To store the uploaded image
image_path = ""
root.mainloop()
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont, ImageTk

def upload_image():
    global img, image_path
    image_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")]
    )
    if image_path:
        img = Image.open(image_path)
        img.thumbnail((400, 400))
        tk_img = ImageTk.PhotoImage(img)
        canvas.create_image(200, 200, image=tk_img)
        canvas.image = tk_img
        status_label.config(text="Image uploaded successfully!")

def add_watermark():
    global img
    if not img:
        status_label.config(text="Please upload an image first!")
        return
    
    watermark_text = watermark_entry.get()
    if not watermark_text:
        status_label.config(text="Please enter watermark text!")
        return
    
    # Add watermark
    img_copy = img.copy()
    draw = ImageDraw.Draw(img_copy)
    font = ImageFont.truetype("arial.ttf", 20)  # Adjust font size if needed
    width, height = img_copy.size

    # Calculate text size using textbbox
    text_bbox = draw.textbbox((0, 0), watermark_text, font=font)
    text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]

    position = (width - text_width - 10, height - text_height - 10)  # Bottom-right corner
    draw.text(position, watermark_text, fill="white", font=font)
    
    # Show the watermarked image
    tk_img = ImageTk.PhotoImage(img_copy)
    canvas.create_image(200, 200, image=tk_img)
    canvas.image = tk_img
    
    # Save watermarked image
    save_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All Files", "*.*")]
    )
    if save_path:
        img_copy.save(save_path)
        status_label.config(text=f"Watermarked image saved at {save_path}")

# GUI setup
root = tk.Tk()
root.title("Watermarking App")
root.geometry("500x600")
root.resizable(False, False)

# Canvas to display the image
canvas = tk.Canvas(root, width=400, height=400, bg="lightgray")
canvas.pack(pady=10)

# Buttons and inputs
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

upload_btn = tk.Button(btn_frame, text="Upload Image", command=upload_image)
upload_btn.pack(side=tk.LEFT, padx=5)

watermark_label = tk.Label(root, text="Watermark Text:")
watermark_label.pack()

watermark_entry = tk.Entry(root, width=30)
watermark_entry.pack()

add_btn = tk.Button(root, text="Add Watermark", command=add_watermark)
add_btn.pack(pady=10)

status_label = tk.Label(root, text="", fg="green")
status_label.pack()

# Run the application
img = None  # To store the uploaded image
image_path = ""
root.mainloop()


# In[ ]:




