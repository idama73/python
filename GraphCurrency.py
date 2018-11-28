#Name: Arnold Okumagba
#Course: CST 205
#Title: Currency History
#Abstract: Plots the data that is retrieved from a JSON data that getes pulled
#from fixer.io and plots them in a graph of the previous 10 days with the different
#currency fluctuation of selected currency.

import matplotlib
import datetime
import urlGrab
matplotlib.use('TkAgg')

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

#checks system version and imports proper Tkinter module
import sys
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk
def destroy(e):
    sys.exit()

class Graph:
	def __init__(self, dollars, currency):
		root = Tk.Tk()
		root.wm_title("Currency Trends")
		#converts the function data into a list.
		x = dollars.getTimeSeriesData(currency)
		y = dollars.getCurrencies()
		f = Figure(figsize=(7, 6), dpi=100)
		a = f.add_subplot(111)
		a.plot(range(10,0,-1), x)
		#Set the labels of the graph
		a.set_title('Currency History')
		a.set_xlabel('Days')
		a.set_ylabel('Amount')

		#tk drawing area for the canvas
		canvas = FigureCanvasTkAgg(f, master=root)
		canvas.show()
		canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

		canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

		Tk.mainloop()
