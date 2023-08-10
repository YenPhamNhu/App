import tkinter as tk
from tkinter import filedialog
import sys

class Registry(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Registry")

        self.butSend = tk.Button(self, text="Send", command=self.send_registry)
        self.butSend.pack()

        self.txtReg = tk.Entry(self)
        self.txtReg.pack()

        self.butBro = tk.Button(self, text="Browse", command=self.browse_file)
        self.butBro.pack()

        self.opApp = tk.OptionMenu(self, "Get value", "Set value", "Delete value", "Create key", "Delete key")
        self.opApp.pack()
        self.opApp.bind("<Button-1>", self.on_option_selected)

        self.txtNameValue = tk.Entry(self)
        self.txtNameValue.pack()

        self.txtValue = tk.Entry(self)
        self.txtValue.pack()

        self.opTypeValue = tk.OptionMenu(self, "REG_SZ", "REG_DWORD", "REG_BINARY", "REG_EXPAND_SZ", "REG_MULTI_SZ")
        self.opTypeValue.pack()

        self.button1 = tk.Button(self, text="SEND", command=self.send_command)
        self.button1.pack()

        self.txtKQ = tk.Text(self, width=50, height=10)
        self.txtKQ.pack()

        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def send_registry(self):
        s = "REG"
        # Send the message to the server
        # Program.nw.WriteLine(s); Program.nw.Flush()
        s = self.txtReg.get()
        # Program.nw.Write(s); Program.nw.Flush()
        response = "Sample response from server"  # Replace with actual response from the server
        tk.messagebox.showinfo("Response", response)

    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Registry Files", "*.reg")])
        if file_path:
            self.txtReg.insert(tk.END, file_path)
            with open(file_path, "r") as file:
                data = file.read()
                self.txtReg.delete(0, tk.END)
                self.txtReg.insert(tk.END, data)

    def on_option_selected(self, event):
        selected_option = self.opApp.get()
        if selected_option == "Get value" or selected_option == "Set value" or selected_option == "Delete value":
            self.txtNameValue.configure(state="normal")
            self.txtValue.configure(state="normal")
            self.opTypeValue.configure(state="normal")
        else:
            self.txtNameValue.configure(state="disabled")
            self.txtValue.configure(state="disabled")
            self.opTypeValue.configure(state="disabled")

    def send_command(self):
        s = "SEND"
        # Send the message to the server
        # Program.nw.WriteLine(s); Program.nw.Flush()
        s = self.opApp.get()
        # Program.nw.WriteLine(s); Program.nw.Flush()
        s = self.txtLink.get()
        # Program.nw.WriteLine(s); Program.nw.Flush()
        s = self.txtNameValue.get()
        # Program.nw.WriteLine(s); Program.nw.Flush()
        s = self.txtValue.get()
        # Program.nw.WriteLine(s); Program.nw.Flush()
        s = self.opTypeValue.get()
        # Program.nw.WriteLine(s); Program.nw.Flush()
        response = "Sample response from server"  # Replace with actual response from the server
        self.txtKQ.insert(tk.END, response + "\n")

    def on_close(self):
        s = "QUIT"
        # Send the message to the server
        # Program.nw.WriteLine(s); Program.nw.Flush()
        self.destroy()

    def clear_text(self):
        self.txtKQ.delete(1.0, tk.END)

if __name__ == "__main__":
    app = Registry()
    app.mainloop()