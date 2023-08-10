import tkinter as tk
import sys

class ListApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ListApp")

        self.button2 = tk.Button(self, text="Kill", command=self.kill_process)
        self.button2.pack()

        self.button1 = tk.Button(self, text="Xem", command=self.view_processes)
        self.button1.pack()

        self.listView1 = tk.Listbox(self, width=50, height=10)
        self.listView1.pack()

        self.button3 = tk.Button(self, text="Start", command=self.start_process)
        self.button3.pack()

        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def kill_process(self):
        temp = "KILL"
        # Send the message to the server
        # Program.nw.WriteLine(temp); Program.nw.Flush()
        viewkill = Kill()  # Replace with appropriate code to display the Kill form
        viewkill.show()

    def view_processes(self):
        temp = "XEM"
        # Send the message to the server
        # Program.nw.WriteLine(temp); Program.nw.Flush()
        s1 = "name application"
        s2 = "ID"
        s3 = "count"
        temp = "Sample response from server"  # Replace with actual response from the server
        soprocess = int(temp)
        # reset list?
        for i in range(soprocess):
            s1 = "Sample response from server"  # Replace with actual response from the server
            if s1 == "ok":
                s1 = "Sample response from server"  # Replace with actual response from the server
                s2 = "Sample response from server"  # Replace with actual response from the server
                s3 = "Sample response from server"  # Replace with actual response from the server
                self.listView1.insert(tk.END, (s1, s2, s3))

    def start_process(self):
        temp = "START"
        # Send the message to the server
        # Program.nw.WriteLine(temp); Program.nw.Flush()
        viewstart = Start()  # Replace with appropriate code to display the Start form
        viewstart.show()

    def on_close(self):
        s = "QUIT"
        # Send the message to the server
        # Program.nw.WriteLine(s); Program.nw.Flush()
        self.destroy()

    def clear_list(self):
        self.listView1.delete(0, tk.END)

if __name__ == "__main__":
    app = ListApp()
    app.mainloop()