import tkinter as tk
import sys

class Keylog(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Keylog")

        self.button1 = tk.Button(self, text="HOOK", command=self.hook)
        self.button1.pack()

        self.button2 = tk.Button(self, text="UNHOOK", command=self.unhook)
        self.button2.pack()

        self.button3 = tk.Button(self, text="PRINT", command=self.print_data)
        self.button3.pack()

        self.txtKQ = tk.Text(self, width=50, height=10)
        self.txtKQ.pack()

        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def hook(self):
        s = "HOOK"
        # Send the message to the server
        # Program.nw.WriteLine(s); Program.nw.Flush()
        print(s)

    def unhook(self):
        s = "UNHOOK"
        # Send the message to the server
        # Program.nw.WriteLine(s); Program.nw.Flush()
        print(s)

    def print_data(self):
        s = "PRINT"
        # Send the message to the server
        # Program.nw.WriteLine(s); Program.nw.Flush()
        data = "Sample data from server"  # Replace with actual received data
        self.txtKQ.insert(tk.END, data)

    def on_close(self):
        s = "QUIT"
        # Send the message to the server
        # Program.nw.WriteLine(s); Program.nw.Flush()
        self.destroy()

    def clear_text(self):
        self.txtKQ.delete(1.0, tk.END)

if __name__ == "__main__":
    app = Keylog()
    app.mainloop()