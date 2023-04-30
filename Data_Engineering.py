class Preprocessing:

    """

    Function: Data engineering pre-processing, performing data smoothing and merging of ECU and Axis data.    

    """

    def convolve(self, Data_Set, File_Name, Data, Window_Size):

        """

        Function: This function performs smoothing on the input feature data by replacing the original data with the average value within a window of size Window_Size. It plots the data of turning left and right in different colors on the same graph, and saves the result as a file.
    
        Parameters:

            Data_Set: pandas DataFrame, contains the feature and label data of the dataset

            File_Name: string, used to name the saved image file

            Data: numpy array, the numerical values of feature data

            Window_Size: integer, the size of the smoothing window


        """

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

        return plt.savefig(File_Name+'_Window_Size_'+str(Window_Size)+'.png')

    def Merge(self, ECU_Data_Path, Axis_Data_Path, Merge_Data_Path):

        """

        Function: used to merge two CSV files into one file.

        Parameters:
            
            ECU_Data_Path: the file path of the CSV file containing ECU data.

            Axis_Data_Path: the file path of the CSV file containing instrument data.

            Merge_Data_Path: the file path where the merged file will be stored.

        Libraries:

            pandas: used for CSV data processing.

            numpy: used for scientific computing.

            tqdm: used for displaying progress bar.

        """

        import pandas as pd
        import numpy as np 
        from tqdm import tqdm, trange

        ECU_Raw_Data = pd.read_csv(ECU_Data_Path)
        ECU_Raw_Data = ECU_Raw_Data.drop('Unnamed: 0',axis=1)

        Axis_Raw_Data = pd.read_csv(Axis_Data_Path)
        Axis_Raw_Data = Axis_Raw_Data.drop('Unnamed: 0',axis=1)

    
        Merge_Data_No_Feature = ['No']
        Merge_Data_No = []
        for row in range(len(ECU_Raw_Data['ECU Absolute Time'])):
            Merge_Data_No.append(row)

        Merge_Data_No = pd.DataFrame(columns = Merge_Data_No_Feature ,index=Merge_Data_No)


        print ("\n【Data Engineering Megre Data Part 1 (1/2)】")
 
        for row in tqdm(range (len(ECU_Raw_Data['ECU Absolute Time'])-1)):
            Merge_Data_No['No'].iloc[row] = (Axis_Raw_Data['Absolute Time'] < ECU_Raw_Data['ECU Absolute Time'][row]).sum()

        Merge_Data_No = Merge_Data_No.fillna(0)


        Merge_Data_Number_Feature = ['Number']
        Merge_Data_Number = []
        for row in range(len(ECU_Raw_Data['ECU Absolute Time'])):
            Merge_Data_Number.append(row)

        Merge_Data_Number = pd.DataFrame(columns = Merge_Data_Number_Feature ,index=Merge_Data_Number)


        print ("\n【Data Engineering Megre Data Part 2 (2/2)】")

        for row in tqdm(range (len(ECU_Raw_Data['ECU Absolute Time'])-1)):
            Merge_Data_Number['Number'].iloc[row] = (Axis_Raw_Data['Absolute Time'] < ECU_Raw_Data['ECU Absolute Time'][row+1]).sum() - (Axis_Raw_Data['Absolute Time'] < ECU_Raw_Data['ECU Absolute Time'][row]).sum()

        Merge_Data_Number = Merge_Data_Number.fillna(0)

        Merge_ECU_Data_Feature = ["ECU Absolute Time", "Atmospheric Pressure", "Inclination Switch", "Fault Code Count", "Ignition Coil Current Diagnosis", "Fault Light Mileage", "Engine Operating Time", "Ignition Advance Angle", "Idling Correction Ignition Angle", "Fuel Injection Prohibition Mode", "Injection Mode", "Bypass Delay Correction", "ABV Opening", "ABV Idling Correction", "ABV Learning Value",  "Lambda Setting", "Air-Fuel Ratio Rich", "Closed Loop Control", "Air Flow", "Throttle Valve Air Flow", "Intake Manifold Pressure", "Intake Manifold Front Pressure", "MFF_AD_ADD_MMV_REL", "MFF_AD_FAC_MMV_REL", "MFF_AD_ADD_MMV", "MFF_AD_FAC_MMV", "Fuel Injection Quantity", "MFF_WUP_COR", "Ignition Mode", "Engine RPM", "Engine RPM Limit", "Idling Target RPM", "Fuel Injection Start Angle", "Fuel Pump State", "Engine State", "Engine Temperature", "Water Temperature PWM", "Ignition Magnetization Time", "Fuel Injection Time", "Closed Loop Fuel Correction", "Intake Temperature", "Combustion Chamber Intake Temperature", "TPS Opening", "TPS Idling Learning Value", "Battery Voltage", "O2 Voltage", "Vehicle Speed", "TPS Voltage", "Seat Switch State"]

        Merge_ECU_Data = []

    
        lenght = len(Axis_Raw_Data) - Merge_Data_No["No"].iloc[0]

        for row in range(lenght):
            Merge_ECU_Data.append(row)

        Merge_ECU_Data = pd.DataFrame(columns = Merge_ECU_Data_Feature ,index=Merge_ECU_Data)

        count=0
        for row in range(len(ECU_Raw_Data)):
            for column in range (int(Merge_Data_Number["Number"].iloc[row])):
                Merge_ECU_Data.iloc[count] = ECU_Raw_Data.iloc[row]
                count = count + 1 
        
        Merge_ECU_Data  = Merge_ECU_Data.reset_index(drop=True)


        Merge_ECU_Data = Merge_ECU_Data.dropna(axis=0)

        last = len(ECU_Raw_Data)-1
        Max = len(Axis_Raw_Data) -  (ECU_Raw_Data['ECU Absolute Time'][last] < Axis_Raw_Data['Absolute Time']).sum()

        Merge_Axis_Data = Axis_Raw_Data.iloc[Merge_Data_No['No'].iloc[0]:Max]
        Merge_Axis_Data = Merge_Axis_Data.reset_index(drop=True)
        Merge_Data = pd.concat([Merge_ECU_Data, Merge_Axis_Data], axis=1)

        Merge_Data.to_csv(Merge_Data_Path)



    def Calculating_Time(self, video_ecu_time, video_mark_time, real_ecu_time):

        from datetime import datetime
        from datetime import timedelta

        video_ecu_time = video_ecu_time.split(':', 4)
        Hours_1   = int(video_ecu_time[0])
        Minutes_1 = int(video_ecu_time[1])
        Seconds_1 = int(video_ecu_time[2])
        Frames_1  = int(video_ecu_time[3])

        video_mark_time = video_mark_time.split(':', 4)
        Hours_2   = int(video_mark_time[0])
        Minutes_2 = int(video_mark_time[1])
        Seconds_2 = int(video_mark_time[2])
        Frames_2  = int(video_mark_time[3])

        Diff_Hours   = Hours_2   - Hours_1
        Diff_Minutes = Minutes_2 - Minutes_1
        Diff_Seconds = Seconds_2 - Seconds_1

        if Frames_2 >= Frames_1:
            Diff_Frames = Frames_2 - Frames_1
        else:
            Diff_Seconds = Diff_Seconds - 1 
            Diff_Frames = Frames_2 - Frames_1 + 25
    

        real_ecu_time = datetime.strptime(real_ecu_time, "%H:%M:%S")
        real_ecu_time = real_ecu_time.strftime('%H:%M:%S')
        real_ecu_time = datetime.strptime(real_ecu_time, "%H:%M:%S")

        real_diff_time = timedelta(hours=Diff_Hours, minutes=Diff_Minutes, seconds=Diff_Seconds)#, milliseconds=Diff_Frames*40
        real_mark_time = real_ecu_time + real_diff_time

        real_mark_time = real_mark_time.strftime('%H:%M:%S')


        real_mark_time = str(real_mark_time)
        real_mark_time = real_mark_time.split(':', 3)
        Hours   = int(real_mark_time[0])
        Minutes = int(real_mark_time[1])
        Seconds = float(real_mark_time[2])


        real_time_error = 0.68
        frames_time_error = Diff_Frames*0.04

        Seconds = Seconds + real_time_error + frames_time_error

        real_mark_time = str(Hours)+':'+str(Minutes)+':'+str(Seconds)
    
        return real_mark_time
