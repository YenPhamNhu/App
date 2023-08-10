import tkinter as tk

class Kill(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Kill")

        self.butNhap = tk.Button(self, text="Nhap", command=self.kill_process)
        self.butNhap.pack()

        self.txtID = tk.Entry(self)
        self.txtID.pack()

        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def kill_process(self):
        # Send the message to the server
        # Program.nw.WriteLine("KILLID"); Program.nw.Flush()
        # Program.nw.WriteLine(txtID.Text); Program.nw.Flush()
        s = "Sample response from server"  # Replace with actual response from the server
        tk.messagebox.showinfo("Response", s)

    def on_close(self):
        # Send the message to the server
        # Program.nw.WriteLine("QUIT"); Program.nw.Flush()
        self.destroy()

if __name__ == "__main__":
    app = Kill()
    app.mainloop()