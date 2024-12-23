# main_closing.py
from image_processing.morphology import closing_no_opencv
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk

class ClosingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Closing")

        self.image_path = tk.StringVar()
        self.output_path = tk.StringVar()
        self.kernel_size = tk.IntVar(value=3)
        self.original_image = None
        self.processed_image = None

        self.create_widgets()

    def create_widgets(self):
        # Style for ttk widgets
        style = ttk.Style()
        style.configure("TButton", padding=6, relief="flat", background="#4CAF50", foreground="white")
        style.configure("TLabel", background="#f0f0f0", font=("Arial", 11))
        style.configure("TEntry", fieldbackground="#f0f0f0", font=("Arial", 11))

        # Frame for input
        input_frame = ttk.Frame(self.root)
        input_frame.pack(pady=20, padx=20, fill="x")

        ttk.Label(input_frame, text="Input Image:", style="TLabel").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        ttk.Entry(input_frame, textvariable=self.image_path, width=40, style="TEntry").grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        ttk.Button(input_frame, text="Browse", command=self.browse_image, style="TButton").grid(row=0, column=2, padx=5, pady=5)

        # Frame for output
        output_frame = ttk.Frame(self.root)
        output_frame.pack(pady=20, padx=20, fill="x")

        ttk.Label(output_frame, text="Output Path:", style="TLabel").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        ttk.Entry(output_frame, textvariable=self.output_path, width=40, style="TEntry").grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        ttk.Button(output_frame, text="Browse", command=self.browse_output, style="TButton").grid(row=0, column=2, padx=5, pady=5)

        # Frame for parameters
        param_frame = ttk.Frame(self.root)
        param_frame.pack(pady=20, padx=20, fill="x")

        ttk.Label(param_frame, text="Kernel Size:", style="TLabel").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        ttk.Entry(param_frame, textvariable=self.kernel_size, width=10, style="TEntry").grid(row=0, column=1, padx=5, pady=5)

        # Process button
        ttk.Button(self.root, text="Process Image", command=self.process_image, style="TButton").pack(pady=20)

        # Image display frame
        image_frame = ttk.Frame(self.root)
        image_frame.pack(pady=20, padx=20, fill="both", expand=True)

        self.original_canvas = tk.Canvas(image_frame, width=300, height=300, bg="#d3d3d3")
        self.original_canvas.pack(side="left", padx=10)

        self.processed_canvas = tk.Canvas(image_frame, width=300, height=300, bg="#d3d3d3")
        self.processed_canvas.pack(side="left", padx=10)

        # Status bar
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

    def process_image(self):
        input_path = self.image_path.get()
        output_path = self.output_path.get()
        kernel_size = self.kernel_size.get()

        if not input_path or not output_path:
            messagebox.showerror("Error", "Please select input and output paths.")
            return
        
        if kernel_size % 2 == 0:
            messagebox.showerror("Error", "Kernel size must be an odd number.")
            return

        try:
            closing_no_opencv(input_path, output_path, kernel_size)
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
    app = ClosingApp(root)
    root.mainloop()
