import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator

class TranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Language Translator")
        self.root.geometry("600x400")

        # Create a translator instance (default target English)
        self.translator = GoogleTranslator(source='auto', target='en')

        # Get supported languages from the instance
        self.lang_list = self.translator.get_supported_languages()

        # UI Layout
        tk.Label(root, text="Enter Text:", font=("Arial", 12)).pack(pady=5)
        self.source_text = tk.Text(root, height=5, width=60)
        self.source_text.pack(pady=5)

        # Language Selection
        lang_frame = tk.Frame(root)
        lang_frame.pack(pady=10)

        self.dest_lang = ttk.Combobox(lang_frame, values=self.lang_list, state="readonly")
        self.dest_lang.set("english")  # Default target
        self.dest_lang.pack()

        # Action Buttons
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Translate", command=self.translate_text,
                  bg="blue", fg="white").grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Copy", command=self.copy_to_clipboard).grid(row=0, column=1, padx=5)

        # Output
        tk.Label(root, text="Translation:", font=("Arial", 12)).pack(pady=5)
        self.result_text = tk.Text(root, height=5, width=60, state="disabled", bg="#f0f0f0")
        self.result_text.pack(pady=5)

    def translate_text(self):
        text = self.source_text.get("1.0", tk.END).strip()
        target = self.dest_lang.get()

        if not text:
            messagebox.showwarning("Warning", "Please enter text to translate.")
            return

        try:
            # Automatic source detection and translation
            translation = GoogleTranslator(source='auto', target=target).translate(text)

            self.result_text.config(state="normal")
            self.result_text.delete("1.0", tk.END)
            self.result_text.insert(tk.END, translation)
            self.result_text.config(state="disabled")
        except Exception as e:
            messagebox.showerror("Error", f"Translation failed: {e}")

    def copy_to_clipboard(self):
        content = self.result_text.get("1.0", tk.END).strip()
        if content:
            self.root.clipboard_clear()
            self.root.clipboard_append(content)
            messagebox.showinfo("Success", "Text copied to clipboard!")

if __name__ == "__main__":
    root = tk.Tk()
    app = TranslatorApp(root)
    root.mainloop()
