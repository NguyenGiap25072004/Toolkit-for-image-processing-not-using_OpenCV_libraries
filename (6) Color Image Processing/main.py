# main.py (tiếp tục)
import tkinter as tk
from tkinter import filedialog, messagebox, ttk, simpledialog
from PIL import Image, ImageTk

from image_processing.color_processing import (
    convert_to_grayscale_no_pil,
    adjust_brightness_no_pil,
    adjust_contrast_no_pil,
    adjust_saturation_no_pil
)

class ColorProcessingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Color Image Processing")

        # Variables
        self.image_path = tk.StringVar()
        self.output_path = tk.StringVar()
        self.original_image = None
        self.processed_image = None

        self.create_widgets()

    def create_widgets(self):
        # Style for ttk widgets
        style = ttk.Style()
        style.configure("TButton", padding=6, relief="flat", background="#4CAF50", foreground="white")
        style.configure("TLabel", background="#f0f0f0", font=("Arial", 11))
        style.configure("TEntry", fieldbackground="#f0f0f0", font=("Arial", 11))

        # Input Frame
        input_frame = ttk.Frame(self.root)
        input_frame.pack(pady=10, padx=20, fill="x")

        ttk.Label(input_frame, text="Input Image:", style="TLabel").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        ttk.Entry(input_frame, textvariable=self.image_path, width=40, style="TEntry").grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(input_frame, text="Browse", command=self.browse_image, style="TButton").grid(row=0, column=2, padx=5, pady=5)

        # Output Frame
        output_frame = ttk.Frame(self.root)
        output_frame.pack(pady=10, padx=20, fill="x")

        ttk.Label(output_frame, text="Output Path:", style="TLabel").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        ttk.Entry(output_frame, textvariable=self.output_path, width=40, style="TEntry").grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(output_frame, text="Browse", command=self.browse_output, style="TButton").grid(row=0, column=2, padx=5, pady=5)

        # Button Frame
        button_frame = ttk.Frame(self.root)
        button_frame.pack(pady=10, padx=20, fill="x")
        
        ttk.Button(button_frame, text="Convert to Grayscale", command=lambda: self.process_image("grayscale"), style="TButton").pack(side="left", padx=5)
        ttk.Button(button_frame, text="Adjust Brightness", command=lambda: self.process_image("brightness"), style="TButton").pack(side="left", padx=5)
        ttk.Button(button_frame, text="Adjust Contrast", command=lambda: self.process_image("contrast"), style="TButton").pack(side="left", padx=5)
        ttk.Button(button_frame, text="Adjust Saturation", command=lambda: self.process_image("saturation"), style="TButton").pack(side="left", padx=5)

        # Image Display Frame
        image_frame = ttk.Frame(self.root)
        image_frame.pack(pady=20, padx=20, fill="both", expand=True)

        self.original_canvas = tk.Canvas(image_frame, width=300, height=300, bg="#d3d3d3")
        self.original_canvas.pack(side="left", padx=10)

        self.processed_canvas = tk.Canvas(image_frame, width=300, height=300, bg="#d3d3d3")
        self.processed_canvas.pack(side="left", padx=10)

        # Status Bar
        self.status_bar = ttk.Label(self.root, text="Ready", anchor="w", style="TLabel")
        self.status_bar.pack(side="bottom", fill="x")

    def browse_image(self):
        filepath = filedialog.askopenfilename(
            initialdir="./",
            title="Select Image",
            filetypes=(("Image files", "*.png *.jpg *.jpeg *.bmp"), ("All files", "*.*")),
        )
        if filepath:
            self.image_path.set(filepath)
            self.display_original_image(filepath)

    def browse_output(self):
        filepath = filedialog.asksaveasfilename(
            initialdir="./",
            title="Save Processed Image",
            defaultextension=".png",
            filetypes=(("PNG", "*.png"), ("JPEG", "*.jpg"), ("All files", "*.*")),
        )
        if filepath:
            self.output_path.set(filepath)

    def display_original_image(self, image_path):
        try:
            img = Image.open(image_path)
            img.thumbnail((300, 300))
            photo = ImageTk.PhotoImage(img)
            self.original_canvas.create_image(150, 150, anchor="center", image=photo)
            self.original_canvas.image = photo
            self.original_image = img
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load image: {e}")

    def process_image(self, operation):
        input_path = self.image_path.get()
        output_path = self.output_path.get()

        if not input_path or not output_path:
            messagebox.showerror("Error", "Please select input and output paths.")
            return

        try:
            if operation == "grayscale":
                convert_to_grayscale_no_pil(input_path, output_path)
            elif operation == "brightness":
                factor = simpledialog.askfloat("Brightness Factor", "Enter brightness factor (0.0 - 2.0):", parent=self.root, minvalue=0.0, maxvalue=2.0)
                if factor is not None:
                    adjust_brightness_no_pil(input_path, output_path, factor)
            elif operation == "contrast":
                factor = simpledialog.askfloat("Contrast Factor", "Enter contrast factor (0.0 - 2.0):", parent=self.root, minvalue=0.0, maxvalue=2.0)
                if factor is not None:
                    adjust_contrast_no_pil(input_path, output_path, factor)
            elif operation == "saturation":
                factor = simpledialog.askfloat("Saturation Factor", "Enter saturation factor (0.0 - 2.0):", parent=self.root, minvalue=0.0, maxvalue=2.0)
                if factor is not None:
                    adjust_saturation_no_pil(input_path, output_path, factor)
            else:
                messagebox.showerror("Error", "Invalid operation selected.")
                return

            self.status_bar.config(text="Image processed successfully!")
            self.display_processed_image(output_path)

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred during processing: {e}")

    def display_processed_image(self, image_path):
        try:
            img = Image.open(image_path)
            img.thumbnail((300, 300))
            photo = ImageTk.PhotoImage(img)
            self.processed_canvas.create_image(150, 150, anchor="center", image=photo)
            self.processed_canvas.image = photo
            self.processed_image = img
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load processed image: {e}")

    def show_about(self):
        messagebox.showinfo("About", "Color Image Processing App\nVersion 1.0\nDeveloped by Nguyen Huu Giap")

if __name__ == "__main__":
    root = tk.Tk()
    app = ColorProcessingApp(root)
    root.mainloop()