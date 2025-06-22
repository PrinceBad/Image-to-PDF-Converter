import tkinter as tk
from tkinter import filedialog, messagebox, font
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

class ImageToPDFConverter:
    """
    A class to represent the Image to PDF Converter application.
    """
    def __init__(self, root):
        """
        Initialize the application window and widgets with a dark theme.
        """
        self.root = root
        self.root.title("Image to PDF Converter")
        self.root.geometry("550x400")
        
        # --- Theme and Font Definitions ---
        self.BG_COLOR = "#2e2e2e"
        self.FG_COLOR = "#d0d0d0"
        self.BTN_BG = "#4a4a4a"
        self.BTN_FG = "#ffffff"
        self.BTN_ACCENT_BG = "#007acc"
        self.LIST_BG = "#3c3c3c"
        self.LIST_FG = "#e0e0e0"

        self.title_font = font.Font(family="Segoe UI", size=20, weight="bold")
        self.button_font = font.Font(family="Segoe UI", size=12, weight="bold")
        self.body_font = font.Font(family="Segoe UI", size=10)

        self.root.configure(bg=self.BG_COLOR)

        self.image_paths = []

        # --- UI Elements ---
        main_frame = tk.Frame(root, bg=self.BG_COLOR, padx=25, pady=25)
        main_frame.pack(expand=True, fill=tk.BOTH)

        title_label = tk.Label(main_frame, text="Image to PDF Converter", font=self.title_font, bg=self.BG_COLOR, fg=self.FG_COLOR)
        title_label.pack(pady=(0, 25))

        select_button = tk.Button(main_frame, text="Select Images", command=self.select_images, font=self.button_font, bg=self.BTN_BG, fg=self.BTN_FG, relief=tk.FLAT, width=22, padx=10, pady=5)
        select_button.pack(pady=10)

        self.file_listbox = tk.Listbox(main_frame, selectmode=tk.SINGLE, font=self.body_font, height=8, bg=self.LIST_BG, fg=self.LIST_FG, highlightthickness=0, borderwidth=0)
        self.file_listbox.pack(pady=10, fill=tk.X, expand=True)

        convert_button = tk.Button(main_frame, text="Convert to PDF", command=self.convert_to_pdf, font=self.button_font, bg=self.BTN_ACCENT_BG, fg=self.BTN_FG, relief=tk.FLAT, width=22, padx=10, pady=5)
        convert_button.pack(pady=15)


    def select_images(self):
        """
        Open a file dialog to select one or more image files.
        """
        files = filedialog.askopenfilenames(
            title="Select Images",
            filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp *.gif"), ("All files", "*.*")]
        )

        if files:
            self.image_paths.extend(list(files)) # Append to list instead of replacing
            self.update_listbox()
            messagebox.showinfo("Images Added", f"{len(files)} image(s) added to the list.")

    def update_listbox(self):
        """
        Refreshes the listbox with the current image paths.
        """
        self.file_listbox.delete(0, tk.END)
        for file_path in self.image_paths:
            self.file_listbox.insert(tk.END, os.path.basename(file_path))

    def convert_to_pdf(self):
        """
        Convert the selected images into a single PDF file.
        """
        if not self.image_paths:
            messagebox.showwarning("No Images", "Please select images before converting.")
            return

        pdf_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF Documents", "*.pdf")],
            title="Save PDF As..."
        )

        if not pdf_path:
            return
            
        try:
            c = canvas.Canvas(pdf_path, pagesize=letter)
            width, height = letter 

            for image_path in self.image_paths:
                img = Image.open(image_path)
                # Convert RGBA images (like some PNGs) to RGB
                if img.mode == 'RGBA':
                    img = img.convert('RGB')
                    
                img_width, img_height = img.size

                aspect = img_height / float(img_width)
                new_width = width
                new_height = width * aspect
                
                if new_height > height:
                    new_height = height
                    new_width = height / aspect

                x = (width - new_width) / 2
                y = (height - new_height) / 2
                
                c.drawImage(image_path, x, y, width=new_width, height=new_height)
                c.showPage()

            c.save()
            messagebox.showinfo("Success", f"PDF successfully created at:\n{pdf_path}")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
        finally:
            self.image_paths = []
            self.update_listbox()


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageToPDFConverter(root)
    root.mainloop()
