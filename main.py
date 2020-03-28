import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from matplotlib import style


import tkinter as tk
from tkinter import ttk

import pandas as pd

# Fonts
LARGE_FONT = ("Verdana", 12)
style.use("ggplot")


# doesn't work
def animate(i):
    data = pd.read_csv("https://covid.ourworldindata.org/data/ecdc/total_cases.csv")
    a.clear()
    a.plot(data[loc][data[loc] != 0])

# doesn't work either
def change_name(new):
    data = pd.read_csv("https://covid.ourworldindata.org/data/ecdc/total_cases.csv")
    a.clear()
    a.plot(data[new][data[new] != 0])

# root, core of a program
class CoronaVirus(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "CoronaVirus Cases")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {} # here are all the pages

        for F in (PageOne, GraphWorld, GraphPoland, GraphChina, GraphItaly, GraphUSA):
            frame = F(container, self)

            self.frames[F] = frame # actually here but whatever

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(PageOne)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

# next few classes are different pages

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page One", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        data = pd.read_csv("https://covid.ourworldindata.org/data/ecdc/total_cases.csv")

        label2 = ttk.Label(self, text=f"last update: {data['date'][data.index[-1]]}", font=LARGE_FONT)
        label2.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="See the graph",
                             command=lambda: controller.show_frame(GraphWorld))
        button1.pack()


class GraphWorld(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.name = "World"
        label = ttk.Label(self, text=self.name, font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(PageOne))
        button1.pack()

        button2 = ttk.Button(self, text="World",
                             command=lambda: controller.show_frame(GraphWorld))
        button2.pack()

        button3 = ttk.Button(self, text="Poland",
                             command=lambda: controller.show_frame(GraphPoland))
        button3.pack()

        button4 = ttk.Button(self, text="China",
                             command=lambda: controller.show_frame(GraphChina))
        button4.pack()

        button5 = ttk.Button(self, text="Italy",
                             command=lambda: controller.show_frame(GraphItaly))
        button5.pack()

        button6 = ttk.Button(self, text="USA",
                             command=lambda: controller.show_frame(GraphUSA))
        button6.pack()

        f = Figure(figsize=(5, 5), dpi=100)
        a = f.add_subplot(111)
        data = pd.read_csv("https://covid.ourworldindata.org/data/ecdc/total_cases.csv")
        a.clear()
        a.plot(data[self.name][data[self.name] != 0])

        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class GraphItaly(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.name = "Italy"
        label = ttk.Label(self, text=self.name, font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(PageOne))
        button1.pack()

        button2 = ttk.Button(self, text="World",
                             command=lambda: controller.show_frame(GraphWorld))
        button2.pack()

        button3 = ttk.Button(self, text="Poland",
                             command=lambda: controller.show_frame(GraphPoland))
        button3.pack()

        button4 = ttk.Button(self, text="China",
                             command=lambda: controller.show_frame(GraphChina))
        button4.pack()

        button5 = ttk.Button(self, text="Italy",
                             command=lambda: controller.show_frame(GraphItaly))
        button5.pack()

        button6 = ttk.Button(self, text="USA",
                             command=lambda: controller.show_frame(GraphUSA))
        button6.pack()

        f = Figure(figsize=(5, 5), dpi=100)
        a = f.add_subplot(111)
        data = pd.read_csv("https://covid.ourworldindata.org/data/ecdc/total_cases.csv")
        a.clear()
        a.plot(data[self.name][data[self.name] != 0])

        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class GraphUSA(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.name = "United States"
        label = ttk.Label(self, text=self.name, font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(PageOne))
        button1.pack()

        button2 = ttk.Button(self, text="World",
                             command=lambda: controller.show_frame(GraphWorld))
        button2.pack()

        button3 = ttk.Button(self, text="Poland",
                             command=lambda: controller.show_frame(GraphPoland))
        button3.pack()

        button4 = ttk.Button(self, text="China",
                             command=lambda: controller.show_frame(GraphChina))
        button4.pack()

        button5 = ttk.Button(self, text="Italy",
                             command=lambda: controller.show_frame(GraphItaly))
        button5.pack()

        button6 = ttk.Button(self, text="USA",
                             command=lambda: controller.show_frame(GraphUSA))
        button6.pack()

        f = Figure(figsize=(5, 5), dpi=100)
        a = f.add_subplot(111)
        data = pd.read_csv("https://covid.ourworldindata.org/data/ecdc/total_cases.csv")
        a.clear()
        a.plot(data[self.name][data[self.name] != 0])

        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class GraphPoland(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.name = "Poland"
        label = ttk.Label(self, text=self.name, font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(PageOne))
        button1.pack()

        button2 = ttk.Button(self, text="World",
                             command=lambda: controller.show_frame(GraphWorld))
        button2.pack()

        button3 = ttk.Button(self, text="Poland",
                             command=lambda: controller.show_frame(GraphPoland))
        button3.pack()

        button4 = ttk.Button(self, text="China",
                             command=lambda: controller.show_frame(GraphChina))
        button4.pack()

        button5 = ttk.Button(self, text="Italy",
                             command=lambda: controller.show_frame(GraphItaly))
        button5.pack()

        button6 = ttk.Button(self, text="USA",
                             command=lambda: controller.show_frame(GraphUSA))
        button6.pack()

        f = Figure(figsize=(5, 5), dpi=100)
        a = f.add_subplot(111)
        data = pd.read_csv("https://covid.ourworldindata.org/data/ecdc/total_cases.csv")
        a.clear()
        a.plot(data[self.name][data[self.name] != 0])

        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class GraphChina(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.name = "China"
        label = ttk.Label(self, text=self.name, font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(PageOne))
        button1.pack()

        button2 = ttk.Button(self, text="World",
                             command=lambda: controller.show_frame(GraphWorld))
        button2.pack()

        button3 = ttk.Button(self, text="Poland",
                             command=lambda: controller.show_frame(GraphPoland))
        button3.pack()

        button4 = ttk.Button(self, text="China",
                             command=lambda: controller.show_frame(GraphChina))
        button4.pack()

        button5 = ttk.Button(self, text="Italy",
                             command=lambda: controller.show_frame(GraphItaly))
        button5.pack()

        button6 = ttk.Button(self, text="USA",
                             command=lambda: controller.show_frame(GraphUSA))
        button6.pack()

        f = Figure(figsize=(5, 5), dpi=100)
        a = f.add_subplot(111)
        data = pd.read_csv("https://covid.ourworldindata.org/data/ecdc/total_cases.csv")
        a.clear()
        a.plot(data[self.name][data[self.name] != 0])

        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


# thanks to this it works :)
app = CoronaVirus()
app.mainloop()
