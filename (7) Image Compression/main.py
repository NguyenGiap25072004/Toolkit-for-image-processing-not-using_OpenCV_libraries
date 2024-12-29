# main.py
import tkinter as tk
from tkinter import filedialog, messagebox, ttk, simpledialog
from PIL import Image, ImageTk

from image_processing.compression import compress_jpeg_no_pil, compress_png_no_pil

class ImageCompressionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Compression")

        # Variables
        self.image_path = tk.StringVar()
        self.output_path = tk.StringVar()
        self.compression_method = tk.StringVar(value="JPEG")
        self.jpeg_quality = tk.IntVar(value=75)
        self.png_compression_level = tk.IntVar(value=6)
        self.original_image = None
        self.processed_image = None

        self.create_widgets()

    def create_widgets(self):
        # Style for ttk widgets
        style = ttk.Style()
        style.configure("TButton", padding=6, relief="flat", background="#4CAF50", foreground="black")
        style.configure("TLabel", background="#f0f0f0", font=("Arial", 11))
        style.configure("TEntry", fieldbackground="#f0f0f0", font=("Arial", 11))
        style.configure("TRadiobutton", background="#f0f0f0", font=("Arial", 11))

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

        # Method Selection Frame
        method_frame = ttk.Frame(self.root)
        method_frame.pack(pady=10, padx=20, fill="x")

        ttk.Label(method_frame, text="Method:", style="TLabel").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        ttk.Radiobutton(method_frame, text="JPEG", variable=self.compression_method, value="JPEG", command=self.update_ui, style="TRadiobutton").grid(row=0, column=1, padx=5, pady=5, sticky="w")
        ttk.Radiobutton(method_frame, text="PNG", variable=self.compression_method, value="PNG", command=self.update_ui, style="TRadiobutton").grid(row=0, column=2, padx=5, pady=5, sticky="w")

        # JPEG Options Frame
        self.jpeg_options_frame = ttk.Frame(self.root)
        self.jpeg_options_frame.pack(pady=10, padx=20, fill="x")

        ttk.Label(self.jpeg_options_frame, text="Quality (0-100):", style="TLabel").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        ttk.Entry(self.jpeg_options_frame, textvariable=self.jpeg_quality, width=10, style="TEntry").grid(row=0, column=1, padx=5, pady=5)

        # PNG Options Frame
        self.png_options_frame = ttk.Frame(self.root)
        self.png_options_frame.pack(pady=10, padx=20, fill="x")

        ttk.Label(self.png_options_frame, text="Compression Level (0-9):", style="TLabel").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        ttk.Entry(self.png_options_frame, textvariable=self.png_compression_level, width=10, style="TEntry").grid(row=0, column=1, padx=5, pady=5)

        # Process Button
        ttk.Button(self.root, text="Process Image", command=self.process_image, style="TButton").pack(pady=20)

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

        self.update_ui()

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
            defaultextension=".jpg",
            filetypes=(("JPEG", "*.jpg"), ("PNG", "*.png"), ("All files", "*.*")),
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

    def update_ui(self):
        # Ẩn/hiện các options tùy theo phương pháp nén được chọn
        if self.compression_method.get() == "JPEG":
            self.jpeg_options_frame.pack(pady=10, padx=20, fill="x")
            self.png_options_frame.pack_forget()
        else:
            self.jpeg_options_frame.pack_forget()
            self.png_options_frame.pack(pady=10, padx=20, fill="x")

    def process_image(self):
        input_path = self.image_path.get()
        output_path = self.output_path.get()

        if not input_path or not output_path:
            messagebox.showerror("Error", "Please select input and output paths.")
            return

        method = self.compression_method.get()

        try:
            if method == "JPEG":
                quality = self.jpeg_quality.get()
                compress_jpeg_no_pil(input_path, output_path, quality)
            elif method == "PNG":
                compress_level = self.png_compression_level.get()
                compress_png_no_pil(input_path, output_path, compress_level)
            else:
                messagebox.showerror("Error", "Invalid compression method selected.")
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

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageCompressionApp(root)
    root.mainloop()
