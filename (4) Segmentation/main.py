# main.py (tiếp tục)
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk
import cv2

from image_processing.segmentation import thresholding_no_opencv, canny_edge_detection_no_opencv

class SegmentationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Segmentation")

        # Variables
        self.image_path = tk.StringVar()
        self.output_path = tk.StringVar()
        self.threshold_value = tk.IntVar(value=127)
        self.max_value = tk.IntVar(value=255)
        self.threshold_method = tk.StringVar(value="BINARY")
        self.canny_threshold1 = tk.IntVar(value=100)
        self.canny_threshold2 = tk.IntVar(value=200)
        self.original_image = None
        self.processed_image = None

        self.create_widgets()

    def create_widgets(self):
        # Style for ttk widgets
        style = ttk.Style()
        style.configure("TButton", padding=6, relief="flat", background="#4CAF50", foreground="white")
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
        ttk.Radiobutton(method_frame, text="Thresholding", variable=self.threshold_method, value="THRESHOLDING", command=self.update_ui, style="TRadiobutton").grid(row=0, column=1, padx=5, pady=5, sticky="w")
        ttk.Radiobutton(method_frame, text="Canny Edge Detection", variable=self.threshold_method, value="CANNY", command=self.update_ui, style="TRadiobutton").grid(row=0, column=2, padx=5, pady=5, sticky="w")

        # Thresholding Options Frame
        self.thresholding_options_frame = ttk.Frame(self.root)
        self.thresholding_options_frame.pack(pady=10, padx=20, fill="x")

        ttk.Label(self.thresholding_options_frame, text="Threshold Value:", style="TLabel").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        ttk.Entry(self.thresholding_options_frame, textvariable=self.threshold_value, width=10, style="TEntry").grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.thresholding_options_frame, text="Max Value:", style="TLabel").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        ttk.Entry(self.thresholding_options_frame, textvariable=self.max_value, width=10, style="TEntry").grid(row=1, column=1, padx=5, pady=5)

        # Thresholding method options
        self.thresholding_method_options = {
            "BINARY": "BINARY",
            "BINARY_INV": "BINARY_INV",
            "TRUNC": "TRUNC",
            "TOZERO": "TOZERO",
            "TOZERO_INV": "TOZERO_INV",
        }
        self.threshold_method_option = tk.StringVar(value="BINARY")

        ttk.Label(self.thresholding_options_frame, text="Method:", style="TLabel").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        threshold_method_combobox = ttk.Combobox(self.thresholding_options_frame, textvariable=self.threshold_method_option, values=list(self.thresholding_method_options.keys()), state="readonly", style="TCombobox")
        threshold_method_combobox.grid(row=2, column=1, padx=5, pady=5)
        threshold_method_combobox.current(0)

        # Canny Options Frame
        self.canny_options_frame = ttk.Frame(self.root)
        self.canny_options_frame.pack(pady=10, padx=20, fill="x")

        ttk.Label(self.canny_options_frame, text="Threshold 1:", style="TLabel").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        ttk.Entry(self.canny_options_frame, textvariable=self.canny_threshold1, width=10, style="TEntry").grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.canny_options_frame, text="Threshold 2:", style="TLabel").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        ttk.Entry(self.canny_options_frame, textvariable=self.canny_threshold2, width=10, style="TEntry").grid(row=1, column=1, padx=5, pady=5)

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

    def update_ui(self):
        # Ẩn/hiện các options tùy theo phương pháp được chọn
        if self.threshold_method.get() == "THRESHOLDING":
            self.thresholding_options_frame.pack(pady=10, padx=20, fill="x")
            self.canny_options_frame.pack_forget()
        else:
            self.thresholding_options_frame.pack_forget()
            self.canny_options_frame.pack(pady=10, padx=20, fill="x")

    def process_image(self):
        input_path = self.image_path.get()
        output_path = self.output_path.get()

        if not input_path or not output_path:
            messagebox.showerror("Error", "Please select input and output paths.")
            return

        method = self.threshold_method.get()

        try:
            if method == "THRESHOLDING":
                threshold_value = self.threshold_value.get()
                max_value = self.max_value.get()
                thresholding_method = self.threshold_method_option.get()
                thresholding_no_opencv(input_path, output_path, threshold_value, max_value, thresholding_method)
                self.status_bar.config(text="Image processed successfully!")
                self.display_processed_image(output_path)
            elif method == "CANNY":
                threshold1 = self.canny_threshold1.get()
                threshold2 = self.canny_threshold2.get()
                canny_edge_detection_no_opencv(input_path, output_path, threshold1, threshold2)
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
    app = SegmentationApp(root)
    root.mainloop()