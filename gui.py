import tkinter as tk
from tkinter import filedialog, messagebox

from video import Video
from editors import VideoEditor
from effects import ZoomEffect, RotateEffect, SpeedEffect, CropEffect, BlurEffect


def start():
    window = tk.Tk()
    window.title("Video Effects Editor")
    window.geometry("1000x650")
    video = None
    editor = None


#the interface ---------------------------------------------------------------

    title = tk.Label(
        window,
        text="VIDEO EFFECTS EDITOR",
        font=("Arial", 20, "bold")
    )
#the command .pack basically makes Tkinter to it put widget into parent window/container 
    title.pack(pady=15)

    main_frame = tk.Frame(window)
    main_frame.pack(fill="both", expand=True, padx=20, pady=10)

    video_frame = tk.LabelFrame(
        main_frame,
        text="Video",
        font=("Arial", 12, "bold")
    )
    video_frame.pack(side="left", fill="both", expand=True, padx=10)

    controls_frame = tk.LabelFrame(
        main_frame,
        text="Editing",
        font=("Arial", 12, "bold")
    )
    controls_frame.pack(side="right", fill="y", padx=10)
    status_label = tk.Label(
        controls_frame,
        text="Ready",
        font=("Arial", 10)
    )
    status_label.pack(pady=5)

    video_info = tk.Label(
        video_frame,
        text="No video loaded",
        font=("Arial", 14)
    )

    def open_video():
    #nonlocal to reference that we actually mean to change the variable video, not make a new one
        nonlocal video, editor

        filepath = filedialog.askopenfilename(
            title="Select a video",
            filetypes=[
                ("Video files", "*.mp4 *.mov *.avi"),
                ("All files", "*.*")
            ]
        )

        if filepath:
            video = Video(filepath)
            editor = VideoEditor(video)

            video_info.config(
                text=f"{video.title}\n"
                     f"Duration: {video.duration:.2f} seconds\n"
                     f"Size: {video.size[0]} x {video.size[1]}"
            )


#the effects side ---------------------------------------------------------------

    open_button = tk.Button(
        controls_frame,
        text="Open Video",
        width=18,
        command=open_video
    )
    open_button.pack(pady=10)

    effects_label = tk.Label(
        controls_frame,
        text="Effects",
        font=("Arial", 14, "bold")
    )
    effects_label.pack(pady=(20, 10))

    selected_label = tk.Label(
        controls_frame,
        text="Selected Effects",
        font=("Arial", 12, "bold")
    )
    selected_label.pack(pady=(10, 5))

    selected_effects = tk.Listbox(
        controls_frame,
        width=25,
        height=6
    )
    selected_effects.pack(pady=5)

#ZOOM ---------------------------------------------------------------

    def add_zoom():
        if editor is not None:
            editor.add_effect(ZoomEffect())
            selected_effects.insert(tk.END, "Zoom")

    zoom_button = tk.Button(
        controls_frame,
        text="Add Zoom",
        width=18,
        command=add_zoom
    )
    zoom_button.pack(pady=5)

#ROTATE ---------------------------------------------------------------

    def add_rotate():
        if editor is not None:
            editor.add_effect(RotateEffect())
            selected_effects.insert(tk.END, "Rotate")

    rotate_button = tk.Button(
        controls_frame,
        text="Add Rotate",
        width=18,
        command=add_rotate
    )
    rotate_button.pack(pady=5)

#BLUR ---------------------------------------------------------------
    def add_blur():
        if editor is not None:
            editor.add_effect(BlurEffect())
            selected_effects.insert(tk.END, "Blur")

    blur_button = tk.Button(
        controls_frame,
        text="Add Blur",
        width=18,
        command=add_blur
    )
    blur_button.pack(pady=5)

    def add_speed():
        if editor is not None:
            speed_window = tk.Toplevel(window)
            #Toplevel creates a new window
            speed_window.title("Change Speed")
            speed_window.geometry("300x150")

            tk.Label(
                speed_window,
                text="Speed factor:"
            ).pack(pady=10)

            speed_entry = tk.Entry(speed_window)
            speed_entry.pack()

            def confirm_speed():
                try:
                    factor = float(speed_entry.get())

                    if factor <= 0:
                        messagebox.showerror(
                            "Invalid Speed",
                            "Speed must be greater than 0."
                        )
                        return

                    editor.add_effect(SpeedEffect(factor))
                    selected_effects.insert(
                        tk.END,
                        f"Speed ({factor}x)"
                    )

                    speed_window.destroy()

                except ValueError:
                    messagebox.showerror(
                        "Invalid Speed",
                        "Please enter a number, for example 2 or 0.5."
                    )

            tk.Button(
                speed_window,
                text="OK",
                command=confirm_speed
            ).pack(pady=10)

    speed_button = tk.Button(
        controls_frame,
        text="Change Speed",
        width=18,
        command=add_speed
    )
    speed_button.pack(pady=5)

    def add_crop():
        if editor is not None:
            crop_window = tk.Toplevel(window)
            crop_window.title("Crop Video")
            crop_window.geometry("300x250")

            tk.Label(crop_window, text="X1:").pack()
            x1_entry = tk.Entry(crop_window)
            x1_entry.pack()

            tk.Label(crop_window, text="Y1:").pack()
            y1_entry = tk.Entry(crop_window)
            y1_entry.pack()

            tk.Label(crop_window, text="X2:").pack()
            x2_entry = tk.Entry(crop_window)
            x2_entry.pack()

            tk.Label(crop_window, text="Y2:").pack()
            y2_entry = tk.Entry(crop_window)
            y2_entry.pack()

            def confirm_crop():
                try:
                    x1 = int(x1_entry.get())
                    y1 = int(y1_entry.get())
                    x2 = int(x2_entry.get())
                    y2 = int(y2_entry.get())

                    if x2 <= x1 or y2 <= y1:
                        messagebox.showerror(
                            "Invalid Crop",
                            "X2 must be greater than X1 and Y2 must be greater than Y1."
                        )
                        return

                    editor.add_effect(
                        CropEffect(x1, y1, x2, y2)
                    )

                    selected_effects.insert(
                        tk.END,
                        f"Crop ({x1}, {y1}, {x2}, {y2})"
                    )

                    crop_window.destroy()

                except ValueError:
                    messagebox.showerror(
                        "Invalid Crop",
                        "Please enter whole numbers for the crop values."
                    )

            tk.Button(
                crop_window,
                text="OK",
                command=confirm_crop
            ).pack(pady=10)

    crop_button = tk.Button(
        controls_frame,
        text="Add Crop",
        width=18,
        command=add_crop
    )
    crop_button.pack(pady=5)

#THE EDITING PART ---------------------------------------------------------------

    editing_label = tk.Label(
        controls_frame,
        text="Editing",
        font=("Arial", 14, "bold")
    )
    editing_label.pack(pady=(30, 10))

#APPLY EFFECTS ---------------------------------------------------------------

    def apply_effects():
        if editor is not None:
            status_label.config(text="Applying effects...")
            window.update_idletasks()

            editor.apply_effects()

            status_label.config(text="Effects applied!")
            messagebox.showinfo(
                "Complete",
                "The effects have been applied successfully."
            )

    apply_button = tk.Button(
        controls_frame,
        text="Apply Effects",
        width=18,
        command=apply_effects
    )
    apply_button.pack(pady=5)

#TRIMMING THE VIDEO

    def trim_video():
        if editor is not None:
            trim_window = tk.Toplevel(window)
            trim_window.title("Trim Video")
            trim_window.geometry("300x180")

            tk.Label(
                trim_window,
                text="Start time (seconds):"
            ).pack(pady=5)

            start_entry = tk.Entry(trim_window)
            start_entry.pack()

            tk.Label(
                trim_window,
                text="End time (seconds):"
            ).pack(pady=5)

            end_entry = tk.Entry(trim_window)
            end_entry.pack()

            def confirm_trim():
                try:
                    start = float(start_entry.get())
                    end = float(end_entry.get())

                    if start < 0 or end <= start or end > video.duration:
                        messagebox.showerror(
                            "Invalid Trim",
                            "Please enter a valid start and end time."
                        )
                        return

                    editor.trim(start, end)

                    selected_effects.insert(
                        tk.END,
                        f"Trim ({start}s - {end}s)"
                    )

                    trim_window.destroy()

                except ValueError:
                    messagebox.showerror(
                        "Invalid Trim",
                        "Please enter numbers for the start and end time."
                    )

            tk.Button(
                trim_window,
                text="OK",
                command=confirm_trim
            ).pack(pady=10)

    trim_button = tk.Button(
        controls_frame,
        text="Trim Video",
        width=18,
        command=trim_video
    )
    trim_button.pack(pady=5)

    def export_video():
        if editor is not None:
            filepath = filedialog.asksaveasfilename(
                title="Save edited video",
                defaultextension=".mp4",
                filetypes=[
                    ("MP4 video", "*.mp4"),
                    ("All files", "*.*")
                ]
            )

            if filepath:
                status_label.config(text="Exporting video...")
                window.update_idletasks()

                editor.export(filepath)

                status_label.config(text="Export complete!")

                messagebox.showinfo(
                    "Export Complete",
                    "Your edited video has been saved successfully."
                )


    export_button = tk.Button(
        controls_frame,
        text="Export Video",
        width=18,
        command=export_video
    )
    export_button.pack(pady=30)

    video_info.pack(pady=50)

    #after clicking the X button we make Tkinter to run close_window()
    def close_window():
        if video is not None:
            video.close()
        window.destroy()

    window.protocol("WM_DELETE_WINDOW", close_window)

    window.mainloop()