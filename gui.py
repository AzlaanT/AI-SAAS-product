import customtkinter as ctk
import ai2  # This imports your ai2.py file
import threading

# --- GUI Appearance Settings ---
ctk.set_appearance_mode("dark")  
ctk.set_default_color_theme("blue") 

class BusinessAIApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window Setup
        self.title("Business Intelligence Manager v2.0")
        self.geometry("950x700")
        self.configure(fg_color="#212121") # Deep Grey Background

        # Layout Configuration
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # 1. Chat Display Area
        self.chat_display = ctk.CTkTextbox(
            self, 
            corner_radius=15, 
            fg_color="#2b2b2b", # Lighter Grey for text area
            border_color="#3d3d3d",
            border_width=2,
            font=("Inter", 14)
        )
        self.chat_display.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="nsew")
        self.chat_display.configure(state="disabled")

        # 2. Input Frame
        self.input_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.input_frame.grid(row=1, column=0, padx=20, pady=(10, 20), sticky="ew")
        self.input_frame.grid_columnconfigure(0, weight=1)

        # User Entry Field
        self.user_entry = ctk.CTkEntry(
            self.input_frame, 
            placeholder_text="Ask me to analyze inventory, sales, or trends...", 
            height=50, 
            corner_radius=10,
            fg_color="#333333",
            border_color="#444444"
        )
        self.user_entry.grid(row=0, column=0, padx=(0, 10), sticky="ew")
        self.user_entry.bind("<Return>", lambda e: self.send_to_ai())

        # Execute Button
        self.exec_button = ctk.CTkButton(
            self.input_frame, 
            text="EXECUTE", 
            width=140, 
            height=50, 
            corner_radius=10,
            font=("Inter Bold", 13),
            command=self.send_to_ai
        )
        self.exec_button.grid(row=0, column=1)

    def append_chat(self, sender, text):
        self.chat_display.configure(state="normal")
        self.chat_display.insert("end", f"{sender.upper()}:\n", "header")
        self.chat_display.insert("end", f"{text}\n\n")
        self.chat_display.configure(state="disabled")
        self.chat_display.see("end")

    def send_to_ai(self):
        user_text = self.user_entry.get().strip()
        if not user_text:
            return

        self.user_entry.delete(0, 'end')
        self.append_chat("You", user_text)
        
        # Set a processing status
        self.append_chat("System", "Analyzing data and searching market trends...")

        # Run in a thread so the UI doesn't freeze during API/Search calls
        threading.Thread(target=self.process_ai_request, args=(user_text,), daemon=True).start()

    def process_ai_request(self, user_text):
        try:
            # THIS IS THE KEY: Calling your exact function name from ai2.py
            response = ai2.ask_ai_pro(user_text)
            
            # Use .after to update the UI from the background thread safely
            self.after(0, lambda: self.append_chat("AI Manager", response))
        except Exception as e:
            self.after(0, lambda: self.append_chat("Error", str(e)))

if __name__ == "__main__":
    app = BusinessAIApp()
    app.mainloop()