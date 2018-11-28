from tkinter import*
import urlGrab
import Graph
real_name={
        'EUR' : 'Euro',
        'AUD' : 'Austrialian Dollar',
        'BGN' : 'Bulgarian Lev',
        'BRL' : 'Brazilian Real',
        'CAD' :'Canadian Dollar',
        'CHF' : 'Swiss France',
        'CNY' : 'Cypriot Euros',
        'CZK' : 'Czech Republic Koruna',
        'DKK' : 'Danish Krone',
        'GBP' : 'British Pound',
        'HKD' : 'Hong Kong Dollar',
        'HRK' : 'Croatian Kuna',
        'HUF' : 'Hungarian Forint',
        'IDR' : 'Indonesian Rupiah',
        'ILS' : 'Israeli Shekel',
        'INR' : 'Indian rupee',
        'JPY' : 'Japanese Yen',
        'KRW' : 'South Korean Won',
        'MXN' : 'Mexican peso',
        'MYR' : 'Malaysian ringgit',
        'NOK' : 'Norwegian Krone',
        'NZD' : 'New Zealand Dollar',
        'PHP' : 'Philippine Peso',
        'PLN' : 'Polish Zloty',
        'RON' : 'Romanian leu',
        'RUB' : 'Russian ruble',
        'SEK' : 'Swedish Krona',
        'SGD' : 'Singapore Dollar',
        'THB' : 'Thai Baht',
        'TRY' : 'Turkish Lira',
        'USD' : 'US Dollar',
        'ZAR' : 'South African rand'
   } 
    
 
class App:
    def __init__(self, root):
        self.root = root
        self.data=urlGrab.UrlGrabber()
        for i in (real_name):
            labelstring=str(i)+" / "+str(real_name[i])
            link = Label(text=labelstring, foreground="#0000ff")
            link.bind("<1>", lambda event, text=labelstring,i=i: self.click_link(event,i))
            link.pack()




    def click_link(self, event, abv):
       g=Graph.Graph(self.data,abv)



