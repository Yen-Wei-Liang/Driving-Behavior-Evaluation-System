class Preprocessing:
    def convolve(self, Data_Set, File_Name, Data, Window_Size):
        import pandas as pd
        import numpy as np
        import matplotlib.pyplot as plt
        
        Smoothed_Data = np.convolve(Data, np.ones(Window_Size)/Window_Size, mode='same')
        Data = Smoothed_Data
        
        x1 = np.arange(len(Data[Data_Set['Action']== 'left']))
        x2 = np.arange(len(Data[Data_Set['Action']== 'right']))

        plt.figure()
        plt.plot(x1, Data[Data_Set['Action']== 'left'] , c='r' , label='Turn left')
        plt.plot(x2, Data[Data_Set['Action'] == 'right'], c='g', label='Turn right')
        plt.legend(loc='lower right')



        #角速度
        plt.xlim(0, 175)
        plt.ylim(-15, 15)


        return plt.savefig(File_Name+'_Window_Size_'+str(Window_Size)+'.png')