import serial #Serial kütüphanesi
# import numpy as np  #numpy kütüphanesi
# import matplotlib.pyplot as plt 
# from time import sleep #time kütüphanesi

#portu acmak icin kod satiri.....
port  = serial.Serial('/dev/tty.usbmodem14201', 9600)

getVal = str (port.readline())#değerleri al
uz = len(getVal)
    #veri = getVal[2:(uz-5)]
    # b'277.00\r\n' formatındaki veriden 277.00 elde edilir
print (uz)
    # liste.append(float(veri)) #verileri listeye ekle
   
    #     plt.plot(sure, liste, linewidth=3)
    #     plt.xlabel('Zaman')
    #     plt.ylabel ('Veri')
    #     plt.title('Arduino A0 dan okunan ilk 20 veri')
    #     plt.show()    
