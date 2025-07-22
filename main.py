import customtkinter
from components import KeysFrame, ValuesFrame
from data.TranslationManager import TManager

customtkinter.set_default_color_theme("./theme.json")


class EditorFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame, for example:
        self.label = customtkinter.CTkLabel(self, text="Edit")
        self.label.grid(row=0, column=0, padx=20)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__(className="translation-manager")
        self.geometry("870x600")
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(1, weight=3)
        self.grid_columnconfigure(0, weight=1)

        self.manager = TManager.get_instance()

        self.values_frame = ValuesFrame.ValueFrame(
            master=self, manager=self.manager)
        self.values_frame.grid(row=0, column=1, padx=10,
                               pady=10, sticky="nsew")

        self.my_frame = KeysFrame.KeysFrame(
            master=self, manager=TManager, values_frame=self.values_frame)
        self.my_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")


if __name__ == "__main__":
    app = App()
    app.mainloop()
