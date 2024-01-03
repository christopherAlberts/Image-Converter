import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.ttk import Progressbar
import os
from PIL import ImageTk, Image
from PIL.ImageTk import PhotoImage


class ScreenManager(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Image Converter")
        self.geometry("670x320")
        # Set the window icon
        icon_path = "programs/image_converter/assets/convert.png"  # Replace with the path to your PNG icon file
        icon = ImageTk.PhotoImage(Image.open(icon_path))
        self.iconphoto(True, icon)
        self.frames = {}

        self.create_main_screen()

    def create_main_screen(self):
        main_screen = tk.Frame(self)
        main_screen.pack(fill=tk.BOTH, expand=True)
        self.frames["main_screen"] = main_screen

        label = tk.Label(main_screen, text="IMAGE CONVERTER")
        label.pack(pady=5)

        button_frame = tk.Frame(main_screen)
        button_frame.pack()

        # Add text above the buttons
        text_above_buttons = tk.Label(button_frame, text="  Convert a Single Image       Convert Multiple Images")
        text_above_buttons.pack(side=tk.TOP, padx=10)

        button2 = tk.Button(button_frame, text="Convert a Single Image", command=self.show_screen2, width=40, height=16)
        button2.pack(side=tk.LEFT, padx=10)

        button3 = tk.Button(button_frame, text="Convert Multiple Images", command=self.show_screen3, width=40, height=16)
        button3.pack(side=tk.LEFT, padx=10)

        # Load and set the icons
        icon2 = PhotoImage(file="programs/image_converter/assets/img.ico")
        icon3 = PhotoImage(file="programs/image_converter/assets/imgs.ico")
        button2.config(image=icon2, width=300, height=245)
        button3.config(image=icon3, width=300, height=245)

        # Keep a reference to the icons to avoid garbage collection
        button2.image = icon2
        button3.image = icon3

    def show_screen2(self):
        self.clear_current_screen()

        screen2 = tk.Frame(self)
        screen2.pack(fill=tk.BOTH, expand=True)
        self.frames["screen2"] = screen2

        label = tk.Label(screen2, text="CONVERT A SINGLE IMAGES")
        label.pack(pady=10)

        button_back = tk.Button(screen2, text="Go Back", command=self.show_main_screen)
        button_back.pack(side=tk.TOP, anchor=tk.W, padx=15)

        input_frame = tk.Frame(screen2)
        input_frame.pack()

        # Define an array of all the image formats
        image_formats = ['BMP', 'DDS', 'DIB', 'EPS', 'GIF', 'ICNS', 'ICO', 'I.M.', 'JPEG', 'JPEG 2000', 'MSP', 'PCX',
                         'PNG',
                         'PPM', 'SGI', 'SPIDER', 'TGA', 'TIF']

        path1_label = tk.Label(input_frame, text="Original Image: ")
        path1_label.grid(row=0, column=0, sticky=tk.E, padx=(10, 0))

        self.path1_entry = tk.Entry(input_frame, width=70)
        self.path1_entry.grid(row=0, column=1, pady=20)

        button1 = tk.Button(input_frame, text="Select Image", command=lambda: self.select_file(self.path1_entry))
        button1.grid(row=0, column=2, padx=(5, 10))

        # Create the output format dropdown menu
        output_format_label = tk.Label(input_frame, text="Output Format:", anchor="e")
        output_format_label.grid(row=3, column=0, sticky=tk.E, pady=10, padx=(30, 0))
        output_formats = image_formats
        self.output_format_dropdown = tk.StringVar()
        self.output_format_dropdown.set(output_formats[8])  # Set the default selected format
        output_format_menu = tk.OptionMenu(input_frame, self.output_format_dropdown, *output_formats)
        output_format_menu.grid(row=3, column=1, padx=(0, 10))

        # Create the submit button
        submit_button = tk.Button(input_frame, text="Submit", command=self.submit_single_image_conversion, width=20, bg="#76f1c8")
        submit_button.grid(row=4, column=0, columnspan=3, pady=10)

    def show_screen3(self):
        self.clear_current_screen()

        screen3 = tk.Frame(self)
        screen3.pack(fill=tk.BOTH, expand=True)
        self.frames["screen3"] = screen3

        label = tk.Label(screen3, text="CONVERT MULTIPLE IMAGES")
        label.pack(pady=10)

        button_back = tk.Button(screen3, text="Go Back", command=self.show_main_screen)
        button_back.pack(side=tk.TOP, anchor=tk.W, padx=15)

        input_frame = tk.Frame(screen3)
        input_frame.pack()

        # Define an array of all the image formats
        image_formats = ['BMP', 'DDS', 'DIB', 'EPS', 'GIF', 'ICNS', 'ICO', 'I.M.', 'JPEG', 'JPEG 2000', 'MSP', 'PCX',
                         'PNG',
                         'PPM', 'SGI', 'SPIDER', 'TGA', 'TIF']

        path1_label = tk.Label(input_frame, text="Original Directory: ")
        path1_label.grid(row=0, column=0, sticky=tk.E, padx=(10, 0))

        self.path1_entry = tk.Entry(input_frame, width=70)
        self.path1_entry.grid(row=0, column=1, pady=20)

        button1 = tk.Button(input_frame, text="Select Directory", command=lambda: self.select_directory(self.path1_entry))
        button1.grid(row=0, column=2, padx=(5, 10))

        path2_label = tk.Label(input_frame, text="New Directory: ")
        path2_label.grid(row=1, column=0, sticky=tk.E, padx=(10, 0))

        self.path2_entry = tk.Entry(input_frame, width=70)
        self.path2_entry.grid(row=1, column=1, pady=10)

        button2 = tk.Button(input_frame, text="Select Directory", command=lambda: self.select_directory(self.path2_entry))
        button2.grid(row=1, column=2, padx=(5, 10))

        # Create the input format dropdown menu
        input_format_label = tk.Label(input_frame, text="Input Format:", anchor="e")
        input_format_label.grid(row=2, column=0, sticky=tk.E, pady=10, padx=(30, 0))
        input_formats = image_formats
        self.input_format_dropdown = tk.StringVar()
        self.input_format_dropdown.set(input_formats[17])  # Set the default selected format
        # input_format_dropdown.trace('w', update_output_formats)  # Update the output format dropdown when input format changes
        input_format_menu = tk.OptionMenu(input_frame, self.input_format_dropdown, *input_formats)
        input_format_menu.grid(row=2, column=1, padx=(0, 10))

        # Create the output format dropdown menu
        output_format_label = tk.Label(input_frame, text="Output Format:", anchor="e")
        output_format_label.grid(row=3, column=0, sticky=tk.E, pady=10, padx=(30, 0))
        output_formats = image_formats
        self.output_format_dropdown = tk.StringVar()
        self.output_format_dropdown.set(output_formats[8])  # Set the default selected format
        output_format_menu = tk.OptionMenu(input_frame, self.output_format_dropdown, *output_formats)
        output_format_menu.grid(row=3, column=1, padx=(0, 10))

        # Create the submit button
        submit_button = tk.Button(input_frame, text="Submit", command=self.submit_multiple_image_conversion, width=20, bg="#76f1c8")
        submit_button.grid(row=4, column=0, columnspan=3, pady=10)

    def show_main_screen(self):
        self.clear_current_screen()
        self.frames["main_screen"].pack()

    def clear_current_screen(self):
        if self.frames["main_screen"].winfo_viewable():
            self.frames["main_screen"].pack_forget()

        if "screen2" in self.frames and self.frames["screen2"].winfo_viewable():
            self.frames["screen2"].pack_forget()

        if "screen3" in self.frames and self.frames["screen3"].winfo_viewable():
            self.frames["screen3"].pack_forget()

    def select_directory(self, entry):
        directory = filedialog.askdirectory()
        if directory:
            entry.delete(0, tk.END)
            entry.insert(tk.END, directory)

    def select_file(self, entry):
        file_path = filedialog.askopenfilename(
            filetypes=(("Image Files", "*.png;*.jpg;*.jpeg;*.gif"), ("All Files", "*.*")))
        if file_path:
            entry.delete(0, tk.END)
            entry.insert(tk.END, file_path)

    def convert_image(self, input_path, output_path, output_format):
        try:
            # Open the input image
            input_image = Image.open(input_path)

            # Convert and save the image to the specified output path and format
            input_image.save(output_path, format=output_format.upper())
            print(f"Successfully converted {input_path.upper()} to {output_path.upper()}.")

        except IOError:
            print("Unable to convert the image.")

    def submit_multiple_image_conversion(self):
        original_directory = self.path1_entry.get()
        new_directory = self.path2_entry.get()

        if original_directory and new_directory:
            input_format = self.input_format_dropdown.get()
            output_format = self.output_format_dropdown.get()

            files_to_convert = [
                file_name for file_name in os.listdir(original_directory)
                if file_name.endswith(input_format.lower())
            ]
            num_files = len(files_to_convert)

            # Open a new window for the progress bar
            progress_window = tk.Toplevel(self)
            progress_window.title("Conversion Progress")
            progress_window.geometry("300x100")

            # Create the progress bar in the new window
            progress_label = tk.Label(progress_window, text="Converting...")
            progress_label.pack(pady=10)
            progress_bar = Progressbar(progress_window, length=200, mode="determinate")
            progress_bar.pack(pady=5)

            for i, file_name in enumerate(files_to_convert, start=1):
                input_path = os.path.join(original_directory, file_name)
                output_path = os.path.join(new_directory, file_name.replace(input_format.lower(), output_format.lower()))

                # Perform the conversion
                print("Input Path:", input_path)
                print("Output Path:", output_path)

                self.convert_image(input_path, output_path, output_format)

                # Update the progress bar
                progress_bar["value"] = (i / num_files) * 100
                progress_window.update()

            # Close the progress window after completion
            progress_window.destroy()
            messagebox.showinfo("Conversion Complete", f"Successfully converted {num_files} files.")

        else:
            if not original_directory and not new_directory:
                messagebox.showwarning("Empty Fields", "Both fields are empty.")
            elif not original_directory:
                messagebox.showwarning("Empty Field", "Original Directory is empty.")
            else:
                messagebox.showwarning("Empty Field", "New Directory is empty.")

    def submit_single_image_conversion(self):

        output_format = self.output_format_dropdown.get().lower()
        image_path  = self.path1_entry.get()
        output_path = image_path.split('.')[0] + '.' + output_format

        # Perform the conversion
        print("Input Path:", image_path)
        print("Output Path:", output_path)

        self.convert_image(image_path, output_path, output_format)

        messagebox.showinfo("Conversion Complete", f"Successfully converted image.")


if __name__ == "__main__":
    screen_manager = ScreenManager()
    screen_manager.mainloop()
