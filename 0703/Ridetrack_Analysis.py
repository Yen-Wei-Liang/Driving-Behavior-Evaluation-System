import vomm
import time
import math
import joblib
import warnings
import numpy as np 
import pandas as pd
from statistics import mode
from tqdm import tqdm, trange
from datetime import datetime
from datetime import timedelta
import matplotlib.pyplot as plt
from filterpy.kalman import KalmanFilter
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score, f1_score, recall_score
from sklearn.metrics import silhouette_score, calinski_harabasz_score, davies_bouldin_score
from sklearn import svm, metrics
from sklearn import tree, metrics
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler
from sklearn.neural_network import MLPClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.gaussian_process import GaussianProcessClassifier

# 方便在觀察圖片時不會被warning訊息擋住
warnings.filterwarnings("ignore")

class RideTrackAnalyzer:

    def __init__(self):
        self.Go_Model = None
        self.Idle_Model = None
        self.Left_Model = None
        self.Right_Model = None
        self.Two_Model = None
        self.U_Model = None

    # 處理9軸資料
    def Axis_Process(self, Data_Path, Data_Save_Path, Save):
    
        """

        Function: Used for processing data from a car-mounted Axis.

        Parameters:

            Data_Path: Path of the CSV file containing the data from the car-mounted device.

            Data_Save_Path: Path of the CSV file to save the processed data.

        Python Libraries:

            pandas: Used for handling CSV data.

            numpy: Used for performing scientific computing.

            tqdm: Used for displaying progress bars.

        """
        
        start_time = time.time()  # Start time

        Axis_Raw_Data = pd.read_csv(Data_Path, header=None)
        Reverse_Axis_Data_Feature = ["Absolute Time", "X-axis Angular Velocity", "Y-axis Angular Velocity", "Z-axis Angular Velocity", "X-axis Acceleration", "Y-axis Acceleration", "Z-axis Acceleration", "X-axis Angle", "Y-axis Angle", "Z-axis Angle"]
        Axis_Raw_Data = np.array(Axis_Raw_Data)
        row_lengh, column_lengh = Axis_Raw_Data.shape
        Axis_Raw_Data = Axis_Raw_Data.reshape(int(column_lengh/len(Reverse_Axis_Data_Feature)),len(Reverse_Axis_Data_Feature))
        
        
        Reverse_Axis_Data = []
        for x in range(int(column_lengh/len(Reverse_Axis_Data_Feature))):
            Reverse_Axis_Data.append(x)
        Reverse_Axis_Data = pd.DataFrame(columns = Reverse_Axis_Data_Feature ,index=Reverse_Axis_Data)
        
        
        print("\nReading 3-axis data in part1 (1/2)")
        for row in tqdm(range(int(column_lengh/len(Reverse_Axis_Data_Feature)))):
            for column in range(len(Reverse_Axis_Data_Feature)):    
                Reverse_Axis_Data.iloc[row][column] = Axis_Raw_Data[row][column]
        
        
        print("\nReading sampling time in part2 (2/2)")
        for row in tqdm(range (len(Reverse_Axis_Data)-1)):
            Reverse_Axis_Data['Absolute Time'][row] = Reverse_Axis_Data['Absolute Time'][row][2:len(Reverse_Axis_Data['Absolute Time'][row])]
            Reverse_Axis_Data['Absolute Time'].iloc[row] = pd.to_datetime(Reverse_Axis_Data['Absolute Time'].iloc[row],unit='ms',utc=True).tz_convert('Asia/Taipei') 
            Reverse_Axis_Data['Z-axis Angle'][row] = Reverse_Axis_Data['Z-axis Angle'][row][1:len(Reverse_Axis_Data['Z-axis Angle'][row])-1]
        
        Reverse_Axis_Data['Z-axis Angle'][(len(Reverse_Axis_Data)-1)] = Reverse_Axis_Data['Z-axis Angle'][(len(Reverse_Axis_Data)-1)][1:len(Reverse_Axis_Data['Z-axis Angle'][(len(Reverse_Axis_Data)-1)])-2]

        if Save:
            Reverse_Axis_Data.to_csv(Data_Save_Path)   

        end_time = time.time()
        execution_time = end_time - start_time
        hours = int(execution_time // 3600)
        minutes = int((execution_time % 3600) // 60)
        seconds = int(execution_time % 60)
        print(f"Axis處理所花費時間：{hours}小時{minutes}分鐘{seconds}秒")
        
        return Reverse_Axis_Data

    # 處理ECU資料
    def ECU_Reverse(self, Data_Path, Data_Save_Path, Save):

        start_time = time.time()  # Start time

        ECU_Raw_Data = pd.read_csv(Data_Path, header=None)
        ECU_Raw_Data = ECU_Raw_Data.drop(ECU_Raw_Data.index[0:2])
        ECU_Raw_Data_0F = ECU_Raw_Data[ECU_Raw_Data.index%2 == 0 ]
        ECU_Raw_Data_0E = ECU_Raw_Data[ECU_Raw_Data.index%2 == 1 ]

        Reverse_ECU_Data_Feature = ["ECU Absolute Time", "Atmospheric Pressure", "Inclination Switch", "Fault Code Count", "Ignition Coil Current Diagnosis", "Fault Light Mileage", "Engine Operating Time", "Ignition Advance Angle", "Idling Correction Ignition Angle", "Fuel Injection Prohibition Mode", "Injection Mode", "Bypass Delay Correction", "ABV Opening", "ABV Idling Correction", "ABV Learning Value",  "Lambda Setting", "Air-Fuel Ratio Rich", "Closed Loop Control", "Air Flow", "Throttle Valve Air Flow", "Intake Manifold Pressure", "Intake Manifold Front Pressure", "MFF_AD_ADD_MMV_REL", "MFF_AD_FAC_MMV_REL", "MFF_AD_ADD_MMV", "MFF_AD_FAC_MMV", "Fuel Injection Quantity", "MFF_WUP_COR", "Ignition Mode", "Engine RPM", "Engine RPM Limit", "Idling Target RPM", "Fuel Injection Start Angle", "Fuel Pump State", "Engine State", "Engine Temperature", "Water Temperature PWM", "Ignition Magnetization Time", "Fuel Injection Time", "Closed Loop Fuel Correction","Intake Temperature", "Combustion Chamber Intake Temperature", "TPS Opening", "TPS Idling Learning Value", "Battery Voltage", "O2 Voltage", "Vehicle Speed", "TPS Voltage", "Seat Switch State"]
        Reverse_ECU_Data = []

        for row in range(min(len(ECU_Raw_Data_0E),len(ECU_Raw_Data_0F))):
            Reverse_ECU_Data.append(row)
            
        Reverse_ECU_Data = pd.DataFrame(columns = Reverse_ECU_Data_Feature ,index=Reverse_ECU_Data)


        print("\n【Reverse Engineering Restores ECU Data Part 1 (1/2)】")
        for row in tqdm(range(min(len(ECU_Raw_Data_0E),len(ECU_Raw_Data_0F)))):
            Reverse_ECU_Data['ECU Absolute Time'].iloc[row] = pd.to_datetime(ECU_Raw_Data_0E[2].iloc[row], unit='s',utc=True).tz_convert('Asia/Taipei')
            Reverse_ECU_Data['Intake Temperature'].iloc[row] = ECU_Raw_Data_0F[0].iloc[row][22:24]
            Reverse_ECU_Data['Combustion Chamber Intake Temperature'].iloc[row] = ECU_Raw_Data_0F[0].iloc[row][24:26]
            Reverse_ECU_Data['TPS Opening'].iloc[row] = ECU_Raw_Data_0F[0].iloc[row][26:30]
            Reverse_ECU_Data['TPS Idling Learning Value'].iloc[row] = ECU_Raw_Data_0F[0].iloc[row][30:34]
            Reverse_ECU_Data['Battery Voltage'].iloc[row] = ECU_Raw_Data_0F[0].iloc[row][34:36]
            Reverse_ECU_Data['O2 Voltage'].iloc[row] = ECU_Raw_Data_0F[0].iloc[row][36:40]
            Reverse_ECU_Data['Vehicle Speed'].iloc[row] = ECU_Raw_Data_0F[0].iloc[row][40:42]
            Reverse_ECU_Data['TPS Voltage'].iloc[row] = ECU_Raw_Data_0F[0].iloc[row][42:46]
            Reverse_ECU_Data['Seat Switch State'].iloc[row] = ECU_Raw_Data_0F[0].iloc[row][46:48]
            Reverse_ECU_Data['Inclination Switch'].iloc[row] = ECU_Raw_Data_0E[1].iloc[row][26:30]
            Reverse_ECU_Data['Fault Code Count'].iloc[row] = ECU_Raw_Data_0E[1].iloc[row][30:32]
            Reverse_ECU_Data['Ignition Coil Current Diagnosis'].iloc[row] = ECU_Raw_Data_0E[1].iloc[row][32:36]
            Reverse_ECU_Data['Fault Light Mileage'].iloc[row] = ECU_Raw_Data_0E[1].iloc[row][36:40]
            Reverse_ECU_Data['Engine Operating Time'].iloc[row] = ECU_Raw_Data_0E[1].iloc[row][40:44]
            Reverse_ECU_Data['Ignition Advance Angle'].iloc[row] = ECU_Raw_Data_0E[1].iloc[row][44:46]
            Reverse_ECU_Data['Idling Correction Ignition Angle'].iloc[row] = ECU_Raw_Data_0E[1].iloc[row][46:48]
            Reverse_ECU_Data['Fuel Injection Prohibition Mode'].iloc[row] = ECU_Raw_Data_0E[1].iloc[row][48:50]
            Reverse_ECU_Data['Injection Mode'].iloc[row] = ECU_Raw_Data_0E[1].iloc[row][50:52]   
            Reverse_ECU_Data['Bypass Delay Correction'].iloc[row] = ECU_Raw_Data_0E[1].iloc[row][52:54]
            Reverse_ECU_Data['ABV Opening'].iloc[row] = ECU_Raw_Data_0E[1].iloc[row][54:58]
            Reverse_ECU_Data['ABV Idling Correction'].iloc[row] = ECU_Raw_Data_0E[1].iloc[row][58:60]
            Reverse_ECU_Data['ABV Learning Value'].iloc[row] = ECU_Raw_Data_0E[1].iloc[row][60:62]
            Reverse_ECU_Data['Lambda Setting'].iloc[row] = ECU_Raw_Data_0E[1].iloc[row][62:64]
            Reverse_ECU_Data['Air-Fuel Ratio Rich'].iloc[row] = ECU_Raw_Data_0E[1].iloc[row][64:66]
            Reverse_ECU_Data['Closed Loop Control'].iloc[row] = ECU_Raw_Data_0E[1].iloc[row][66:68]
            Reverse_ECU_Data['Air Flow'].iloc[row] = ECU_Raw_Data_0E[1].iloc[row][68:72]
            Reverse_ECU_Data['Throttle Valve Air Flow'].iloc[row] = ECU_Raw_Data_0E[1].iloc[row][72:76]
            Reverse_ECU_Data['Intake Manifold Pressure'].iloc[row] = ECU_Raw_Data_0E[1].iloc[row][76:80]
            Reverse_ECU_Data['Intake Manifold Front Pressure'].iloc[row] = ECU_Raw_Data_0E[1].iloc[row][80:84]   
            Reverse_ECU_Data['MFF_AD_ADD_MMV_REL'].iloc[row] = ECU_Raw_Data_0E[1].iloc[row][84:88]
            Reverse_ECU_Data['MFF_AD_FAC_MMV_REL'].iloc[row] = ECU_Raw_Data_0E[1].iloc[row][88:92]
            Reverse_ECU_Data['MFF_AD_ADD_MMV'].iloc[row] = ECU_Raw_Data_0E[1].iloc[row][92:96]
            Reverse_ECU_Data['MFF_AD_FAC_MMV'].iloc[row] = ECU_Raw_Data_0E[1].iloc[row][96:100]    
            Reverse_ECU_Data['Fuel Injection Quantity'].iloc[row] = ECU_Raw_Data_0E[1].iloc[row][100:104]
            Reverse_ECU_Data['MFF_WUP_COR'].iloc[row] = ECU_Raw_Data_0E[1].iloc[row][104:106]
            Reverse_ECU_Data['Ignition Mode'].iloc[row] = ECU_Raw_Data_0E[1].iloc[row][106:108]
            Reverse_ECU_Data['Engine RPM'].iloc[row] = ECU_Raw_Data_0E[1].iloc[row][108:112]
            Reverse_ECU_Data['Engine RPM Limit'].iloc[row] = ECU_Raw_Data_0E[1].iloc[row][112:116]
            Reverse_ECU_Data['Idling Target RPM'].iloc[row] = ECU_Raw_Data_0E[1].iloc[row][116:120]
            Reverse_ECU_Data['Fuel Injection Start Angle'].iloc[row] = ECU_Raw_Data_0E[1].iloc[row][120:124]
            Reverse_ECU_Data['Fuel Pump State'].iloc[row] = ECU_Raw_Data_0E[1].iloc[row][124:126]
            Reverse_ECU_Data['Engine State'].iloc[row] = ECU_Raw_Data_0E[1].iloc[row][126:128]
            Reverse_ECU_Data['Engine Temperature'].iloc[row] = ECU_Raw_Data_0E[1].iloc[row][128:130]
            Reverse_ECU_Data['Water Temperature PWM'].iloc[row] = ECU_Raw_Data_0E[1].iloc[row][130:132]
            Reverse_ECU_Data['Ignition Magnetization Time'].iloc[row] = ECU_Raw_Data_0E[1].iloc[row][132:136]
            Reverse_ECU_Data['Fuel Injection Time'].iloc[row] = ECU_Raw_Data_0E[1].iloc[row][136:140]
            Reverse_ECU_Data['Closed Loop Fuel Correction'].iloc[row] = ECU_Raw_Data_0E[1].iloc[row][140:144]
            Reverse_ECU_Data['Atmospheric Pressure'].iloc[row] = ECU_Raw_Data_0E[1].iloc[row][22:26]
    
        print("\n【Reverse Engineering Restores ECU Data Part 2 (2/2)】")

        for row in tqdm(range(min(len(ECU_Raw_Data_0E),len(ECU_Raw_Data_0F)))): 
            Reverse_ECU_Data['ECU Absolute Time'].iloc[row] = Reverse_ECU_Data['ECU Absolute Time'].iloc[row]
            Reverse_ECU_Data['Atmospheric Pressure'].iloc[row] = int(Reverse_ECU_Data['Atmospheric Pressure'].iloc[row],16)
            Reverse_ECU_Data['Inclination Switch'].iloc[row] = int(Reverse_ECU_Data['Inclination Switch'].iloc[row],16)*0.004887107
            Reverse_ECU_Data['Fault Code Count'].iloc[row] = int(Reverse_ECU_Data['Fault Code Count'].iloc[row],16)
            Reverse_ECU_Data['Ignition Coil Current Diagnosis'].iloc[row] = int(Reverse_ECU_Data['Ignition Coil Current Diagnosis'].iloc[row],16)*0.004882796      
            Reverse_ECU_Data['Fault Light Mileage'].iloc[row] = int(Reverse_ECU_Data['Fault Light Mileage'].iloc[row],16)
            Reverse_ECU_Data['Engine Operating Time'].iloc[row] = int(Reverse_ECU_Data['Engine Operating Time'].iloc[row],16)*0.083333333  
            Reverse_ECU_Data['Ignition Advance Angle'].iloc[row] = (int(Reverse_ECU_Data['Ignition Advance Angle'].iloc[row],16)*0.468745098)-30
            Reverse_ECU_Data['Idling Correction Ignition Angle'].iloc[row] =  (int(Reverse_ECU_Data['Idling Correction Ignition Angle'].iloc[row],16)*0.468745098)-30 
            Reverse_ECU_Data['Fuel Injection Prohibition Mode'].iloc[row] =  int(Reverse_ECU_Data['Fuel Injection Prohibition Mode'].iloc[row],16)
            Reverse_ECU_Data['Injection Mode'].iloc[row] =  int(Reverse_ECU_Data['Injection Mode'].iloc[row],16)
            Reverse_ECU_Data['Bypass Delay Correction'].iloc[row] =  (int(Reverse_ECU_Data['Bypass Delay Correction'].iloc[row],16)*0.1)-12.8
            Reverse_ECU_Data['ABV Opening'].iloc[row] =  (int(Reverse_ECU_Data['ABV Opening'].iloc[row],16)*0.46875)
            Reverse_ECU_Data['ABV Idling Correction'].iloc[row] =  (int(Reverse_ECU_Data['ABV Idling Correction'].iloc[row],16)*0.937490196)-120
            Reverse_ECU_Data['ABV Learning Value'].iloc[row] =  (int(Reverse_ECU_Data['ABV Learning Value'].iloc[row],16)*0.937490196)-120
            Reverse_ECU_Data['Lambda Setting'].iloc[row] =  (int(Reverse_ECU_Data['Lambda Setting'].iloc[row],16)*0.003905882)+0.5
            Reverse_ECU_Data['Air-Fuel Ratio Rich'].iloc[row] =  int(Reverse_ECU_Data['Air-Fuel Ratio Rich'].iloc[row],16)                                                                   
            Reverse_ECU_Data['Closed Loop Control'].iloc[row] =  int(Reverse_ECU_Data['Closed Loop Control'].iloc[row],16)                                      
            Reverse_ECU_Data['Air Flow'].iloc[row] =  (int(Reverse_ECU_Data['Air Flow'].iloc[row],16)*0.015624994)    
            Reverse_ECU_Data['Throttle Valve Air Flow'].iloc[row] =  (int(Reverse_ECU_Data['Throttle Valve Air Flow'].iloc[row],16)*0.015624994)    
            Reverse_ECU_Data['Intake Manifold Pressure'].iloc[row] =  int(Reverse_ECU_Data['Intake Manifold Pressure'].iloc[row],16)
            Reverse_ECU_Data['Intake Manifold Front Pressure'].iloc[row] =  int(Reverse_ECU_Data['Intake Manifold Front Pressure'].iloc[row],16)                                                                          
            Reverse_ECU_Data['MFF_AD_ADD_MMV_REL'].iloc[row] =  (int(Reverse_ECU_Data['MFF_AD_ADD_MMV_REL'].iloc[row],16)*0.003906249)-128                                         
            Reverse_ECU_Data['MFF_AD_FAC_MMV_REL'].iloc[row] =  (int(Reverse_ECU_Data['MFF_AD_FAC_MMV_REL'].iloc[row],16)*0.000976562)-32
            Reverse_ECU_Data['MFF_AD_ADD_MMV'].iloc[row] =  (int(Reverse_ECU_Data['MFF_AD_ADD_MMV'].iloc[row],16)*0.003906249)-128                                         
            Reverse_ECU_Data['MFF_AD_FAC_MMV'].iloc[row] =  (int(Reverse_ECU_Data['MFF_AD_FAC_MMV'].iloc[row],16)*0.000976562)-32                                                                                 
            Reverse_ECU_Data['Fuel Injection Quantity'].iloc[row] =  (int(Reverse_ECU_Data['Fuel Injection Quantity'].iloc[row],16)*0.003906249)                                                                                                                           
            Reverse_ECU_Data['MFF_WUP_COR'].iloc[row] =  (int(Reverse_ECU_Data['MFF_WUP_COR'].iloc[row],16)*0.003905882)                                    
            Reverse_ECU_Data['Ignition Mode'].iloc[row] =  int(Reverse_ECU_Data['Ignition Mode'].iloc[row],16)  
            Reverse_ECU_Data['Engine RPM'].iloc[row] =  int(Reverse_ECU_Data['Engine RPM'].iloc[row],16)
            Reverse_ECU_Data['Engine RPM Limit'].iloc[row] =  int(Reverse_ECU_Data['Engine RPM Limit'].iloc[row],16)                                                                    
            Reverse_ECU_Data['Idling Target RPM'].iloc[row] =  int(Reverse_ECU_Data['Idling Target RPM'].iloc[row],16)-32768
            Reverse_ECU_Data['Fuel Injection Start Angle'].iloc[row] =  (int(Reverse_ECU_Data['Fuel Injection Start Angle'].iloc[row],16)*0.46875)-180                                                                           
            Reverse_ECU_Data['Fuel Pump State'].iloc[row] =  int(Reverse_ECU_Data['Fuel Pump State'].iloc[row],16)
            Reverse_ECU_Data['Engine State'].iloc[row] =  int(Reverse_ECU_Data['Engine State'].iloc[row],16)                                                                            
            Reverse_ECU_Data['Engine Temperature'].iloc[row] =  int(Reverse_ECU_Data['Engine Temperature'].iloc[row],16)-40                                                                                                                                             
            Reverse_ECU_Data['Water Temperature PWM'].iloc[row] =  (int(Reverse_ECU_Data['Water Temperature PWM'].iloc[row],16)*0.390588235)                                                                                
            Reverse_ECU_Data['Ignition Magnetization Time'].iloc[row] =  (int(Reverse_ECU_Data['Ignition Magnetization Time'].iloc[row],16)*0.004)                                                                                    
            Reverse_ECU_Data['Fuel Injection Time'].iloc[row] =  (int(Reverse_ECU_Data['Fuel Injection Time'].iloc[row],16)*0.004)                                                                                                               
            Reverse_ECU_Data['Closed Loop Fuel Correction'].iloc[row] =  (int(Reverse_ECU_Data['Closed Loop Fuel Correction'].iloc[row],16)*0.000976428)-32                                                                                                                                  
            Reverse_ECU_Data['Intake Temperature'].iloc[row] =  int(Reverse_ECU_Data['Intake Temperature'].iloc[row],16)-40                                        
            Reverse_ECU_Data['Combustion Chamber Intake Temperature'].iloc[row] = int(Reverse_ECU_Data['Combustion Chamber Intake Temperature'].iloc[row],16)-40                                                                                                                                                                                                     
            Reverse_ECU_Data['TPS Opening'].iloc[row] = (int(Reverse_ECU_Data['TPS Opening'].iloc[row],16)*0.001953124)                                        
            Reverse_ECU_Data['TPS Idling Learning Value'].iloc[row] = (int(Reverse_ECU_Data['TPS Idling Learning Value'].iloc[row],16)*0.004882796)                                                                                
            Reverse_ECU_Data['Battery Voltage'].iloc[row] = (int(Reverse_ECU_Data['Battery Voltage'].iloc[row],16)*0.062498039)+4                                                                                                                       
            Reverse_ECU_Data['O2 Voltage'].iloc[row] = (int(Reverse_ECU_Data['O2 Voltage'].iloc[row],16)*0.004882796)                                      
            #Reverse_ECU_Data['Vehicle Speed'].iloc[row] = (int(Reverse_ECU_Data['Vehicle Speed'].iloc[row],16)*0.594417404)  
            Reverse_ECU_Data['Vehicle Speed'].iloc[row] = (Reverse_ECU_Data['Engine RPM'].iloc[row]*60*434*3.14)/10000000
            Reverse_ECU_Data['TPS Voltage'].iloc[row] = (int(Reverse_ECU_Data['TPS Voltage'].iloc[row],16)*0.004882796)                                       
            Reverse_ECU_Data['Seat Switch State'].iloc[row] = int(Reverse_ECU_Data['Seat Switch State'].iloc[row],16)                                       
        
        if Save:
            Reverse_ECU_Data.to_csv(Data_Save_Path)  


        end_time = time.time()
        execution_time = end_time - start_time
        hours = int(execution_time // 3600)
        minutes = int((execution_time % 3600) // 60)
        seconds = int(execution_time % 60)
        print(f"ECU逆向工程所花費時間：{hours}小時{minutes}分鐘{seconds}秒")

        return Reverse_ECU_Data

    # 合併資料
    def Data_Merge(self, ECU_Data_Path, Axis_Data_Path, Merge_Data_Path, Save):

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

        start_time = time.time()  # Start time

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

        if Save:
            Merge_Data.to_csv(Merge_Data_Path)


        end_time = time.time()
        execution_time = end_time - start_time
        hours = int(execution_time // 3600)
        minutes = int((execution_time % 3600) // 60)
        seconds = int(execution_time % 60)
        print(f"合併對齊Axis與ECU所花費時間：{hours}小時{minutes}分鐘{seconds}秒")

        return Merge_Data

    # 校正角度使用
    def Rotation(self, DataSet, Save):

        start_time = time.time()  # Start time

        # 定義原始角度矩陣
        angles = np.array([DataSet['X-axis Angle'].iloc[0], DataSet["Y-axis Angle"].iloc[0], DataSet['Z-axis Angle'].iloc[0]])   # 第一筆的3軸資料

        # 將角度轉換為弧度
        angles = np.radians(angles)

        # 定義旋轉矩陣
        rotation_x = np.array([[1, 0, 0],
                               [0, np.cos(angles[0]), -np.sin(angles[0])],
                               [0, np.sin(angles[0]), np.cos(angles[0])]])

        rotation_y = np.array([[np.cos(angles[1]), 0, np.sin(angles[1])],
                               [0, 1, 0],
                               [-np.sin(angles[1]), 0, np.cos(angles[1])]])

        rotation_z = np.array([[np.cos(angles[2]), -np.sin(angles[2]), 0],
                               [np.sin(angles[2]), np.cos(angles[2]), 0],
                               [0, 0, 1]])

        rotation_matrix = np.dot(rotation_z, np.dot(rotation_y, rotation_x))

        # 計算逆矩陣
        inv_rotation_matrix = np.linalg.inv(rotation_matrix)


        DataSet_finish = DataSet.copy()
        for row in tqdm(range (len(DataSet))):
            # 假設我們有一個三軸角度的資料集
            x_angle = DataSet["X-axis Angle"].iloc[row]  # X軸角度
            y_angle = DataSet["Y-axis Angle"].iloc[row]  # Y軸角度
            z_angle = DataSet["Z-axis Angle"].iloc[row]  # Z軸角度

            # 將角度轉換為弧度
            x_rad = np.radians(x_angle)
            y_rad = np.radians(y_angle)
            z_rad = np.radians(z_angle)

            # 原始角度資料
            angles = np.array([x_rad, y_rad, z_rad])

            # 將原始角度矩陣乘以逆矩陣
            new_angles = np.dot(inv_rotation_matrix, angles)

            # 將新的角度矩陣轉換為度數
            new_angles = np.degrees(new_angles)

            # 輸出歸零後的角度資料
            DataSet_finish["X-axis Angle"].iloc[row] = new_angles[0]
            DataSet_finish["Y-axis Angle"].iloc[row] = new_angles[1]
            DataSet_finish["Z-axis Angle"].iloc[row] = new_angles[2]
        
        if Save:
            DataSet_finish.to_csv('DataSet_Rotation.csv')

        end_time = time.time()
        execution_time = end_time - start_time
        hours = int(execution_time // 3600)
        minutes = int((execution_time % 3600) // 60)
        seconds = int(execution_time % 60)
        print(f"校正角度所花費時間：{hours}小時{minutes}分鐘{seconds}秒")

        return DataSet_finish

    # 校正加速度角速度使用
    def Init_Axis(self, DataSet, K, Save):

        start_time = time.time()  # Start time

        features = ['X-axis Angular Velocity', 'Y-axis Angular Velocity', 'Z-axis Angular Velocity', 'X-axis Acceleration', 'Y-axis Acceleration', 'Z-axis Acceleration']
        processed_data = DataSet.copy()  # 複製一份以保留原始資料集
    
        for feature in features:
            # 計算前k個值的平均值
            mean_value = np.mean(DataSet[feature][:K])
        
            # 减去特征的所有值
            processed_data[feature] -= mean_value
        
        if Save:
            processed_data.to_csv('DataSet_Rotation_Init.csv')

        end_time = time.time()
        execution_time = end_time - start_time
        hours = int(execution_time // 3600)
        minutes = int((execution_time % 3600) // 60)
        seconds = int(execution_time % 60)
        print(f"校正角速度與加速度所花費時間：{hours}小時{minutes}分鐘{seconds}秒")

    # 正規化使用
    def Normalized(self, DataSet, Feature, Save):

        start_time = time.time()  # Start time

        # 創建MinMaxScaler物件
        scaler = MinMaxScaler()

        # 對指定特徵進行最小-最大標準化
        normalized_data = scaler.fit_transform(DataSet[Feature])

        # 將正規化後的資料轉換為DataFrame
        normalized_df = pd.DataFrame(normalized_data, columns=Feature)

        # 將DataFrame保存為CSV檔案
        if Save:
            normalized_df.to_csv("DataSet_Rotation_Init_Normalized.csv")
        
        end_time = time.time()
        execution_time = end_time - start_time
        hours = int(execution_time // 3600)
        minutes = int((execution_time % 3600) // 60)
        seconds = int(execution_time % 60)
        print(f"正規化所花費時間：{hours}小時{minutes}分鐘{seconds}秒")

        return normalized_df


    def KalmanFilter(self, DataSet, Feature, Save):

        start_time = time.time()  # Start time

        # 定義卡爾曼濾波器
        kf = KalmanFilter(dim_x=len(Feature), dim_z=len(Feature))

        # 設定轉移矩陣
        kf.F = np.eye(len(Feature))

        # 設置測量矩陣
        kf.H = np.eye(len(Feature))

        # 設定噪聲
        kf.Q = np.eye(len(Feature)) * 0.0001  # 假設特徵之間的噪聲是獨立且相同的

        # 設定測量噪聲
        kf.R = np.eye(len(Feature)) * 0.001  # 假設測量噪聲是獨立且相同的

        # 初始化狀態
        kf.x = np.zeros((len(Feature), 1))  # 假設初始狀態為零向量

        # 設置初始協方差矩陣
        kf.P = np.eye(len(Feature))  # 假設對初始狀態的不確定性沒有太多信息

        Data = DataSet[Feature].values
        filtered_data = np.zeros_like(Data)

        for i in range(Data.shape[0]):
            measurement = Data[i, :].reshape(9, 1)

            # 預測下一個狀態
            kf.predict()
            # 更新狀態
            kf.update(measurement)
            # 濾波後結果
            filtered_data[i, :] = kf.x[:, 0]

        # 將濾波後的結果存回原始 DataFrame
        for i, column in enumerate(Feature):
            DataSet[column] = filtered_data[:, i]

        if Save:
            DataSet.to_csv(f'IMU_Kalman_{len(Feature)}_DataSet_Rotation_Init_Normalized_F30.csv')

        end_time = time.time()
        execution_time = end_time - start_time
        hours = int(execution_time // 3600)
        minutes = int((execution_time % 3600) // 60)
        seconds = int(execution_time % 60)
        print(f"使用卡爾曼濾波器所花費時間：{hours}小時{minutes}分鐘{seconds}秒")
        
        return DataSet

    # 分群使用
    def KMeans_Cluster(self, DataSet, Feature, K, Save): 

        start_time = time.time()  # Start time

        # 創建 KMeans
        kmeans = KMeans(n_clusters=K)

        # 訓練模型並進行分群
        kmeans.fit(DataSet[Feature])

        # 分群結果
        labels = kmeans.labels_
   
        DataSet['Action Element'] = labels

        # 儲存分群模型
        joblib.dump(kmeans, 'kmeans_model.pkl')

     
        # 儲存分群完資料成 CSV 檔案
        if Save:
            DataSet.to_csv(f'DataSet_Rotation_Init_Normalized_{K}_Cluster.csv')

        end_time = time.time()
        execution_time = end_time - start_time
        hours = int(execution_time // 3600)
        minutes = int((execution_time % 3600) // 60)
        seconds = int(execution_time % 60)
        print(f"分群所花費時間：{hours}小時{minutes}分鐘{seconds}秒")

        return DataSet

    # 利用載入K-means模型進行預測
    def KMeans_Cluster_Predict(self, DataSet, Feature, ModelName, Save): 

        # 載入模型
        loaded_kmeans = joblib.load(ModelName)

        #預測
        predicted_cluster = loaded_kmeans.predict(DataSet[Feature])

        DataSet['Action Element'] = predicted_cluster
        
        if Save:
            DataSet.to_csv("DataSet_Rotation_Init_Normalized_PredictCluster.csv")

        return DataSet

    # 計算分群最佳群數
    def Evaluate_Clustering_Algorithms(self, Dataset, K, Save):

        start_time = time.time()  # Start time

        scores = {
            'Silhouette Score': [],
            'Calinski-Harabasz Index': [],
            'Davies-Bouldin Index': []
        }

        # Elbow Method
        distortions = []

        for k in tqdm(range(2, K+1)):
            # Perform clustering
            kmeans = KMeans(n_clusters=k, random_state=0)
            labels = kmeans.fit_predict(Dataset)

            # Calculate evaluation metrics
            silhouette = silhouette_score(Dataset, labels)
            calinski_harabasz = calinski_harabasz_score(Dataset, labels)
            davies_bouldin = davies_bouldin_score(Dataset, labels)

            # Update scores dictionary
            scores['Silhouette Score'].append(silhouette)
            scores['Calinski-Harabasz Index'].append(calinski_harabasz)
            scores['Davies-Bouldin Index'].append(davies_bouldin)

            # Calculate distortion for Elbow Method
            distortions.append(kmeans.inertia_)

        # Create dataframe of scores
        df_scores = pd.DataFrame(scores)

        # Plotting
        fig, axs = plt.subplots(2, 2, figsize=(12, 10))

        # Silhouette Score
        axs[0, 0].plot(range(2, K+1), df_scores['Silhouette Score'], marker='o')
        axs[0, 0].set_xlabel('Number of Clusters (K)')
        axs[0, 0].set_ylabel('Silhouette Score')
        axs[0, 0].set_title('Silhouette Score')
        axs[0, 0].set_xticks(range(2, K+1, 1))

        # Calinski-Harabasz Index
        axs[0, 1].plot(range(2, K+1), df_scores['Calinski-Harabasz Index'], marker='o')
        axs[0, 1].set_xlabel('Number of Clusters (K)')
        axs[0, 1].set_ylabel('Calinski-Harabasz Index')
        axs[0, 1].set_title('Calinski-Harabasz Index')
        axs[0, 1].set_xticks(range(2, K+1, 1))

        # Davies-Bouldin Index
        axs[1, 0].plot(range(2, K+1), df_scores['Davies-Bouldin Index'], marker='o')
        axs[1, 0].set_xlabel('Number of Clusters (K)')
        axs[1, 0].set_ylabel('Davies-Bouldin Index')
        axs[1, 0].set_title('Davies-Bouldin Index')
        axs[1, 0].set_xticks(range(2, K+1, 1))

        # Elbow Method
        axs[1, 1].plot(range(2, K+1), distortions, marker='o')
        axs[1, 1].set_xlabel('Number of Clusters (K)')
        axs[1, 1].set_ylabel('Distortion')
        axs[1, 1].set_title('Elbow Method')
        axs[1, 1].set_xticks(range(2, K+1, 1))

        # Adjust spacing between subplots
        plt.tight_layout()

        # Save the figure
        if Save:
            plt.savefig('clustering_evaluation.png')

        # Display the dataframe
        #print(df_scores)

        end_time = time.time()
        execution_time = end_time - start_time
        hours = int(execution_time // 3600)
        minutes = int((execution_time % 3600) // 60)
        seconds = int(execution_time % 60)
        print(f"最佳分群數演算法所花費時間：{hours}小時{minutes}分鐘{seconds}秒")

        return df_scores

    # 計算對應元特徵權重
    def Evaluate_PCA(self, DataSet, K):
        pca = PCA(n_components=K)
        transformed_data = pca.fit_transform(DataSet)
        components = pca.components_
        explained_variance_ratio = pca.explained_variance_ratio_
        # 降维後的資料集和其他相關訊息
        print("降维後的資料集：")
        print(transformed_data)
        print("\n主成分：")
        print(components)
        print("\n對應原特徵權重比例：")
        print(explained_variance_ratio)

    # 計算分類的準確度與預測並儲存(2個檔案)
    def All_model(self, DataSet, Validation_DataSet, Label, Save):

        """

        Function: Perform classification tasks using support vector machines, K-nearest neighbors, decision trees, random forests,               neural networks, Gaussian process algorithms, and calculate accuracy, F1 score, and recall score.

        Parameters:

            DataSet: Input feature data, which can be a pandas DataFrame.

            Label: Label data, which refers to the classification label corresponding to each feature data, and can be a pandas Series.

        """

        start_time = time.time()  # Start time


        # SVM          
        train_feature, test_feature, train_label, test_label = train_test_split(DataSet, Label,test_size=0.2)
        svm_model = svm.SVC()
        svm_model.fit(train_feature, train_label)
        test_predict = svm_model.predict(test_feature)
        svm_model_acc = metrics.accuracy_score(test_label, test_predict)
        svm_model_f1 = f1_score(test_label, test_predict, average='weighted')
        svm_model_recall = recall_score(test_label, test_predict, average='weighted')

        
        # KNeighborsClassifier
        train_feature, test_feature, train_label, test_label = train_test_split(DataSet, Label,test_size=0.2)
        KNeighbors_model = KNeighborsClassifier(n_neighbors=6)
        KNeighbors_model.fit(train_feature, train_label)
        test_predict = KNeighbors_model.predict(test_feature)
        KNeighbors_model_acc = metrics.accuracy_score(test_label, test_predict)
        KNeighbors_model_f1 = f1_score(test_label, test_predict, average='weighted')
        KNeighbors_model_recall = recall_score(test_label, test_predict, average='weighted')


        # DecisionTree      
        train_feature, test_feature, train_label, test_label = train_test_split(DataSet, Label,test_size=0.2)
        DecisionTree_model = tree.DecisionTreeClassifier()
        DecisionTree_model.fit(train_feature, train_label)
        test_predict = DecisionTree_model.predict(test_feature)
        DecisionTree_model_acc = metrics.accuracy_score(test_label, test_predict)
        DecisionTree_model_f1 = f1_score(test_label, test_predict, average='weighted')
        DecisionTree_model_recall = recall_score(test_label, test_predict, average='weighted')


        # RandomForest
        train_feature, test_feature, train_label, test_label = train_test_split(DataSet, Label,test_size=0.2)
        RandomForest_model = RandomForestClassifier(n_estimators=10)
        RandomForest_model.fit(train_feature, train_label)
        test_predict = RandomForest_model.predict(test_feature)
        RandomForest_model_acc =  metrics.accuracy_score(test_label, test_predict)
        RandomForest_model_f1 = f1_score(test_label, test_predict, average='weighted')
        RandomForest_model_recall = recall_score(test_label, test_predict, average='weighted')


        # MLPClassifier
        train_feature, test_feature, train_label, test_label = train_test_split(DataSet, Label,test_size=0.2)
        MLP_model = MLPClassifier(solver='adam', 
                                  alpha=1e-5,
                                  hidden_layer_sizes=(100, ),
                                  random_state=42,
                                  activation='relu'
                                  )
        MLP_model.fit(train_feature, train_label)
        test_predict = MLP_model.predict(test_feature)
        MLP_model_acc =  metrics.accuracy_score(test_label, test_predict)
        MLP_model_f1 = f1_score(test_label, test_predict, average='weighted')
        MLP_model_recall = recall_score(test_label, test_predict, average='weighted')


        # GaussianProcessClassifier
        train_feature, test_feature, train_label, test_label = train_test_split(DataSet, Label,test_size=0.2)
        GaussianProcess_model = GaussianProcessClassifier()
        GaussianProcess_model.fit(train_feature, train_label)
        test_predict = GaussianProcess_model.predict(test_feature)
        GaussianProcess_model_acc  =  metrics.accuracy_score(test_label, test_predict)
        GaussianProcess_model_f1 = f1_score(test_label, test_predict, average='weighted')
        GaussianProcess_model_recall = recall_score(test_label, test_predict, average='weighted')

        models = pd.DataFrame({
            'Model': ['支持向量機(Support Vector Machines)', 
                      '最近的鄰居(Nearest Neighbors)', 
                      '決策樹(Decision Trees)',
                      '隨機森林(Forests of randomized trees)', 
                      '神經網路(Neural Network models)',
                      '高斯過程(GaussianProcess)'
                     ],
            'Accuracy': [svm_model_acc,
                      KNeighbors_model_acc,
                      DecisionTree_model_acc,
                      RandomForest_model_acc,
                      MLP_model_acc,
                      GaussianProcess_model_acc, 
                      ],
            'F1_Score': [svm_model_f1,
                      KNeighbors_model_f1,
                      DecisionTree_model_f1,
                      RandomForest_model_f1,
                      MLP_model_f1,
                      GaussianProcess_model_f1, 
                      ],
            'Recall': [svm_model_recall,
                      KNeighbors_model_recall,
                      DecisionTree_model_recall,
                      RandomForest_model_recall,
                      MLP_model_recall,
                      GaussianProcess_model_recall, 
                      ]
                       })
        

        Validation_predict_KNeighbors = KNeighbors_model.predict(Validation_DataSet)
        Validation_predict_SVM = svm_model.predict(Validation_DataSet)
        Validation_predict_DecisionTree = DecisionTree_model.predict(Validation_DataSet)
        Validation_predict_RandomForest = RandomForest_model.predict(Validation_DataSet)
        Validation_predict_MLP = MLP_model.predict(Validation_DataSet)
        Validation_predict_GaussianProcess = GaussianProcess_model.predict(Validation_DataSet)

        Validation_DataSet['SVM_Predict'] = Validation_predict_SVM
        Validation_DataSet['KNeighbors_Predict'] = Validation_predict_KNeighbors
        Validation_DataSet['DecisionTree_Predict'] = Validation_predict_DecisionTree
        Validation_DataSet['RandomForest_Predict'] = Validation_predict_RandomForest
        Validation_DataSet['MLP_Predict'] = Validation_predict_MLP
        Validation_DataSet['GaussianProcess_Predict'] = Validation_predict_GaussianProcess


        # 獲取當前日期和時間
        now = datetime.now()
        date = now.strftime('%Y%m%d')  # 格式化日期為YYYYMMDD
        current_time = now.strftime('%H%M')  # 格式化時間為HHMM


        if Save:
            Validation_DataSet.to_csv(f'{date}_Multi_model_classification_Predict_{current_time}.csv' , index=False)
            models.to_csv(f'{date}_Multi_model_classification_Accuracy_{current_time}.csv')

        end_time = time.time()
        execution_time = end_time - start_time
        hours = int(execution_time // 3600)
        minutes = int((execution_time % 3600) // 60)
        seconds = int(execution_time % 60)
        print(f"多模分類演算法所花費時間：{hours}小時{minutes}分鐘{seconds}秒")

        return models


    # 訓練Vomm模型使用
    def Train_Vomm(self, TrainData, L, K):
        """
        Train the VOMM model with the training data.

        parameter:
            - TrainData: Training data, which contains data for different actions and action elements.
            - k: Number of data groups.

         output:
             Returns no value, but creates and saves the trained VOMM model in the object.

        """
        start_time = time.time()
        Go_Straight = TrainData.loc[TrainData['Action'] == 'Go Straight', 'Action Element'].astype(int).tolist()
        self.Go_Model = vomm.ppm()
        self.Go_Model.fit(Go_Straight, d=L, alphabet_size=K)


        Idle = TrainData.loc[TrainData['Action'] == 'Idle', 'Action Element'].astype(int).tolist()
        self.Idle_Model = vomm.ppm()
        self.Idle_Model.fit(Idle, d=L, alphabet_size=K)


        Turn_Left = TrainData.loc[TrainData['Action'] == 'Turn Left', 'Action Element'].astype(int).tolist()
        self.Left_Model = vomm.ppm()
        self.Left_Model.fit(Turn_Left, d=L, alphabet_size=K)


        Turn_Right = TrainData.loc[TrainData['Action'] == 'Turn Right', 'Action Element'].astype(int).tolist()
        self.Right_Model = vomm.ppm()
        self.Right_Model.fit(Turn_Right, d=L, alphabet_size=K)


        Two = TrainData.loc[TrainData['Action'] == 'Two-Stage Left', 'Action Element'].astype(int).tolist()
        self.Two_Model = vomm.ppm()
        self.Two_Model.fit(Two, d=L, alphabet_size=K)


        U = TrainData.loc[TrainData['Action'] == 'U-turn', 'Action Element'].astype(int).tolist()
        self.U_Model = vomm.ppm()
        self.U_Model.fit(U, d=L, alphabet_size=K)

        # 計算執行時間
        end_time = time.time()
        execution_time = end_time - start_time
        hours = int(execution_time // 3600)
        minutes = int((execution_time % 3600) // 60)
        seconds = int(execution_time % 60)
        print(f"訓練模型所花費時間：{hours}小時{minutes}分鐘{seconds}秒")


    # 預測的結果並存下來 (不用輸入頻率也不用呼叫副程式)
    def Test_Vomm(self, DataSet, Frequency, Save):
        """
        Test the VOMM model on the test data.

        parameter:
            - TestData: Test data, containing the sequence of action elements to test.
            - frequency: How often the dataset is sampled.

        output:
            Returns no value, but saves the prediction to a file.

        """

        action_element_list = DataSet['Action Element'].values.tolist()
        

        start_time = time.time()

        predictions=[]
        for num in tqdm(range(len(action_element_list))):
            Max_Score = float('-inf')

            Selected_Model = None


            scores = []
            for i in range(6, 30):
                Idle_Model_Score = self.Idle_Model.logpdf(action_element_list[max(0, num-i):num])
                Idle_Model_Score = math.exp(Idle_Model_Score) ** (1/i)
                scores.append(Idle_Model_Score)
            Idle_Model_Score = max(scores)
           

            scores = []
            for i in range(6, 30):
                Go_Model_Score = self.Go_Model.logpdf(action_element_list[max(0, num-i):num])
                Go_Model_Score = math.exp(Go_Model_Score) ** (1/i)
                scores.append(Go_Model_Score)
            Go_Model_Score = max(scores)


            scores=[]
            for i in range(6, 30):
                Left_Model_Score = self.Left_Model.logpdf(action_element_list[max(0, num-i):num])
                Left_Model_Score = math.exp(Left_Model_Score) ** (1/i)
                scores.append(Left_Model_Score)
            Left_Model_Score = max(scores)

            
            scores=[]
            for i in range(6, 30):
               Right_Model_Score = self.Right_Model.logpdf(action_element_list[max(0, num-i):num])
               Right_Model_Score = math.exp(Right_Model_Score) ** (1/i)
               scores.append(Right_Model_Score)
            Right_Model_Score = max(scores)


            scores = []
            for i in range(6, 30):
                Two_Model_Score = self.Two_Model.logpdf(action_element_list[max(0, num-i):num])
                Two_Model_Score = math.exp(Two_Model_Score) ** (1/i)
                scores.append(Two_Model_Score)
            Two_Model_Score = max(scores)


            scores = []
            for i in range(6, 30):
                U_Model_Score = self.U_Model.logpdf(action_element_list[max(0, num-i):num])
                U_Model_Score = math.exp(U_Model_Score) ** (1/i)
                scores.append(U_Model_Score)
            U_Model_Score = max(scores)



            Score_Models = [Idle_Model_Score, Go_Model_Score, Left_Model_Score, Right_Model_Score, Two_Model_Score, U_Model_Score,]
            Models = ['Idle', 'Go Straight','Turn Left', 'Turn Right', 'Two-Stage Left', 'U-turn']    
            for Score, model in zip(Score_Models, Models):
                if Score > Max_Score:
                    Max_Score = Score
                    Selected_Model = model
            predictions.append(Selected_Model)
        
        DataSet['Predict'] = predictions
        DataSet['Filter_Predict'] = self.Filter_Actions(DataSet['Predict'], Frequency)


        # 獲取當前日期和時間
        now = datetime.now()
        date = now.strftime('%Y%m%d')  # 格式化日期為YYYYMMDD
        current_time = now.strftime('%H%M')  # 格式化時間為HHMM



        if Save:
            DataSet.to_csv(f'{date}_TestData_Predict_{current_time}.csv', index=False)

        # 計算執行時間
        end_time = time.time()
        execution_time = end_time - start_time
        hours = int(execution_time // 3600)
        minutes = int((execution_time % 3600) // 60)
        seconds = int(execution_time % 60)
        print(f"預測所花費時間：{hours}小時{minutes}分鐘{seconds}秒")

        return DataSet


    # Compute_Accuracy內呼叫使用
    def Filter_Actions(self, DataSet, Frequency):
        filtered_data = []
        previous_action = None
        for i, action in enumerate(DataSet):
            if action != previous_action:
                window = DataSet[i:i+(2*Frequency)]  # 取下 2 sec 資料
                if mode(window) == action:  # 判斷眾數是否與當前資料相同
                    pass
                else:
                    if mode(window + DataSet[i-Frequency:i+Frequency]) != action:  # 判斷眾數是否與前一個點的資訊相同
                        action = mode(window)  # 第一種情況，將當前點更改為眾數
                    else:
                        action = previous_action  # 第二種情況，將當前點更改為前一個點的值
            filtered_data.append(action)
            previous_action = action
        return filtered_data

    # 與手動標記比對各類動作準確度與整體準確度
    def Compute_Accuracy(self, DataSet, Frequency, Save):

        import pandas as pd
        DataSet['Filter_Predict'] = self.Filter_Actions(DataSet['Predict'], Frequency)
        column_names = ['Predict', 'Filter_Predict']
        Filtered_Data = DataSet[['Action', 'Predict', 'Filter_Predict']].dropna()
        match_percentages1 = []
        match_percentages2 = []

        # 比對個頻率準確度的程式碼
        for column in column_names:
            count = 0
            for x in range(len(Filtered_Data)):
                if Filtered_Data['Action'].iloc[x] == Filtered_Data[column].iloc[x]:
                    count += 1
            match_percentage = (count / len(Filtered_Data)) * 100
            match_percentages1.append(match_percentage)

        result_df1 = pd.DataFrame({'RideTrack': column_names, 'Match Percentage': match_percentages1})

        # 比對個動作準確度的程式碼
        class_labels = Filtered_Data['Action'].unique()
        match_percentages2 = []
        for column in column_names:
            column_match_percentages = []
            for label in class_labels:
                count = 0
                total = 0
                for x in range(len(Filtered_Data)):
                    if Filtered_Data['Action'].iloc[x] == label:
                        total += 1
                        if Filtered_Data[column].iloc[x] == label:
                            count += 1
                match_percentage = (count / total) * 100 if total != 0 else 0
                column_match_percentages.append(match_percentage)
            match_percentages2.append(column_match_percentages)

        result_df2 = pd.DataFrame(match_percentages2, columns=class_labels, index=column_names)
        result_df2.index.name = 'RideTrack'

        result_df2 = result_df2.reset_index()
        result_df2['Match Percentage'] = result_df1['Match Percentage']

        # 獲取當前日期和時間
        now = datetime.now()
        date = now.strftime('%Y%m%d')  # 格式化日期為YYYYMMDD
        time = now.strftime('%H%M')  # 格式化時間為HHMM

        if Save:
            result_df2.to_csv(f'{date}_Accuracy_Predict_{time}.csv', index=False)

        return result_df2

    def Calculate_Action_Prediction_Counts(self, DataSet):
    
        action_elements = []
    
        for action in DataSet['Action'].dropna().unique():
            counts = DataSet[DataSet['Action'] == action]['Predict'].value_counts().reset_index()
            counts.columns = ['Predict', 'Count']
            counts['Action'] = action
            action_elements.append(counts)

        Calculate_Action = pd.concat(action_elements, ignore_index=True)

        return Calculate_Action[['Action', 'Predict', 'Count']]

    # 傳統閥值分類並儲存檔案
    def Tradition_Category(self, DataSet, Quantiles, Feature, Save):

        Category=[]
        for feature in Feature:
            Variable_Category = f"{feature}_Category"
            Category.append(Variable_Category)
            Variable_thresholds = DataSet[feature].quantile(Quantiles).tolist()

            DataSet[Variable_Category] = pd.cut(DataSet[feature], bins=Variable_thresholds, labels=False)
    
        DataSet[Category] = DataSet[Category].fillna(0)

        if Save:
            DataSet.to_csv(f'Traditional_Threshold_{len(Quantiles)-1}^{len(Feature)}_groups.csv')
        
        return DataSet


    # Tradition_Encoding 呼叫使用轉成十進制
    def convert_to_decimal(self, Number, Base):
        decimal = 0
        power = 0
        while Number > 0:
            digit = Number % 10
            decimal += digit * (Base ** power)
            Number //= 10
            power += 1
        return decimal

    # 傳統閥值編碼並儲存檔案
    def Tradition_Encoding(self, DataSet, Feature, Save):
        for num in range(len(DataSet)):
            combined_string = ''.join(DataSet[Feature].iloc[num].astype(int).astype(str))
            converted_list = [int(char) for char in combined_string]
            max_value = max(converted_list)

            base = int(max_value) + 1
            decimal_number = self.convert_to_decimal(int(combined_string), base)
            DataSet['Action Element'].iloc[num] = decimal_number


        # 獲取當前日期和時間
        now = datetime.now()
        date = now.strftime('%Y%m%d')  # 格式化日期為YYYYMMDD
        time = now.strftime('%H%M')  # 格式化時間為HHMM

        if Save:
            DataSet.to_csv(f'{date}_Tradition_Encoding_{time}.csv', index=False)

        # 計算各類別的數量
        category_counts = DataSet['Action Element'].value_counts()

        # 繪製直方圖
        plt.bar(category_counts.index, category_counts.values)

        # 設定標題和軸標籤
        plt.title('Category Counts')
        plt.xlabel('Category')
        plt.ylabel('Count')
        plt.savefig(f'{date}_plot_Category_Counts_{time}.png', dpi=300, bbox_inches='tight')
        plt.show()  # 若不需要顯示圖形，請取消註解此行
        plt.close()

        return DataSet   
 

    # 輸入資料含蓋量，取出前K個類別
    def Tradition_Find_Top_K(self, DataSet, Target_Percentage):
        # 計算各類別的數量
        category_counts = DataSet['Action Element'].value_counts()

        # 繪製直方圖
        plt.bar(category_counts.index, category_counts.values)

        # 設定標題和軸標籤
        plt.title('Category Counts')
        plt.xlabel('Category')
        plt.ylabel('Count')

        # 顯示圖形
        plt.show()


        # 根據數量由高到低排序
        category_counts = category_counts.sort_values(ascending=False)

        # 計算數量百分比
        category_percentages = category_counts / len(DataSet) * 100

        # 計算累積百分比
        category_cumulative_percentages = category_percentages.cumsum()

        # 建立 DataFrame
        category_stats = pd.DataFrame({'Count': category_counts, 'Percentage': category_percentages, 'Cumulative Percentage': category_cumulative_percentages})

        # 找到累積百分比達到目標百分比的資料
        filtered_data = category_stats[category_stats['Cumulative Percentage'] <= Target_Percentage]

        print(f'Data with cumulative percentage up to {Target_Percentage}%:')
        print(f'{filtered_data}\nTop K：{len(filtered_data)}')

        return category_stats


    # 繪製動作元素所組成之動作
    def Plot_Action_Cluter(self, DataSet, Action1, Action2, Feature, Cluster, Length, Save):
        colors = {0: 'red', 1: 'green', 2: 'blue', 3: 'cyan', 4: 'yellow', 5: 'magenta', 6: 'black', 7: 'white', 8: 'orange', 9: 'purple'}

        DataSet_Action1 = DataSet[DataSet['Action'] == Action1][:Length]
        DataSet_Action2 = DataSet[DataSet['Action'] == Action2][:Length]
    
        # 設定 x 軸長度
        DataSet_Action1_Length  = np.arange(len(DataSet_Action1))
        DataSet_Action2_Length = np.arange(len(DataSet_Action2))


        for i in range(Cluster):
            plt.scatter([], [], c=colors[i], label=f"Action Element {i}")

        # 點
        plt.scatter(DataSet_Action1_Length,  DataSet_Action1[Feature], c=[colors[x] for x in DataSet_Action1 ['Action Element']], zorder=2)

        # 線 
        plt.plot(DataSet_Action1_Length, DataSet_Action1[Feature][DataSet_Action1['Action'] == Action1], c='LightBlue' , label=Action1, linewidth=10, zorder=1)    

        plt.scatter(DataSet_Action2_Length, DataSet_Action2[Feature], c=[colors[x] for x in DataSet_Action2['Action Element']], zorder=2)

        plt.plot(DataSet_Action2_Length, DataSet_Action2[Feature][DataSet_Action2['Action'] == Action2], c='LightGreen' , label=Action2, linewidth=10, zorder=1)

        plt.legend(loc='best',bbox_to_anchor=(1.55, 1))
        plt.title(f'{Feature}\n {Action1} vs {Action2}')

        plt.xlabel('Time Step')
        plt.ylabel('Value')
        

        if Save:
            plt.savefig(f'{Feature} {Action1} vs {Action2}（best）.png', bbox_inches='tight')

        plt.show()


    # 繪製駕駛行為軌跡
    def Plot_Action_Track(self, DataSet, Step_Column_Name, Slice_size, Save):

        start_time = time.time()

        DataSet = DataSet.fillna('Unlabeled')

        # 計算需要切割的次數
        num_slices = math.ceil(len(DataSet) / Slice_size)

        # 動態計算切割範圍
        slices = []
        for i in range(num_slices):
            start = i * Slice_size
            end = min((i + 1) * Slice_size, len(DataSet))
            slices.append((start, end))

        # 設定顏色映射
        colors = ['blue', 'green', 'red', 'purple', 'orange', 'yellow', 'cyan'] 

        # 繪製散點圖
        for i, (start, end) in enumerate(slices):
            # 切割資料
            Test_Data_slice = DataSet.iloc[start:end]
            Test_Data_slice.reset_index(drop=True, inplace=True)

            # 繪製第一張圖 (Test_Data_slice[Step_Column_Name])
            plt.figure(figsize=(12, 8))
            for j, condition in enumerate(['Go Straight', 'Idle', 'Turn Right', 'Turn Left', 'Two-Stage Left', 'U-turn', 'Transition']):
                condition_points = [idx for idx, val in enumerate(Test_Data_slice[Step_Column_Name]) if val == condition]
                plt.scatter(Test_Data_slice.index[condition_points], Test_Data_slice['Z-axis Angular Velocity'][condition_points],
                            color=colors[j], label=condition, alpha=0.5)

            plt.title(f'第 {i} Slice - {Step_Column_Name}')
            plt.xlabel('Time Step')
            plt.ylabel('Z-axis Angular Velocity')
            plt.xticks(range(0, len(Test_Data_slice)+1, 500))
            plt.yticks(np.arange(0, 1.1, 0.1))
            plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left')
            if Save:
                plt.savefig(f'plot_{i+1}_step.png', dpi=300, bbox_inches='tight')
            plt.show()
            plt.close()

            # 繪製第二張圖 (Test_Data_slice['Action'])
            plt.figure(figsize=(12, 8))
            for j, condition in enumerate(['Go Straight', 'Idle', 'Turn Right', 'Turn Left', 'Two-Stage Left', 'U-turn', 'Unlabeled']):
                condition_points = [idx for idx, val in enumerate(Test_Data_slice['Action']) if val == condition]
                plt.scatter(Test_Data_slice.index[condition_points], Test_Data_slice['Z-axis Angular Velocity'][condition_points],
                            color=colors[j], label=condition, alpha=0.5)

            plt.title(f'第 {i} Slice - Action')
            plt.xlabel('Time Step')
            plt.ylabel('Z-axis Angular Velocity')
            plt.xticks(range(0, len(Test_Data_slice)+1, 500))
            plt.yticks(np.arange(0, 1.1, 0.1))
            plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left')
            if Save:            
                plt.savefig(f'plot_{i+1}_action.png', dpi=300, bbox_inches='tight')
            plt.show()
            plt.close()

        # 計算執行時間
        end_time = time.time()
        execution_time = end_time - start_time
        hours = int(execution_time // 3600)
        minutes = int((execution_time % 3600) // 60)
        seconds = int(execution_time % 60)
        print(f"繪製動作序列所花費時間：{hours}小時{minutes}分鐘{seconds}秒")

        return


    # 影片中標記換算時間使用
    def Calculating_Time(self, Video_Ecu_Time, Video_Mark_Time, Real_Ecu_Time):


        Video_Ecu_Time = Video_Ecu_Time.split(':', 4)
        Hours_1   = int(Video_Ecu_Time[0])
        Minutes_1 = int(Video_Ecu_Time[1])
        Seconds_1 = int(Video_Ecu_Time[2])
        Frames_1  = int(Video_Ecu_Time[3])

        Video_Mark_Time = Video_Mark_Time.split(':', 4)
        Hours_2   = int(Video_Mark_Time[0])
        Minutes_2 = int(Video_Mark_Time[1])
        Seconds_2 = int(Video_Mark_Time[2])
        Frames_2  = int(Video_Mark_Time[3])

        Diff_Hours   = Hours_2   - Hours_1
        Diff_Minutes = Minutes_2 - Minutes_1
        Diff_Seconds = Seconds_2 - Seconds_1

        if Frames_2 >= Frames_1:
            Diff_Frames = Frames_2 - Frames_1
        else:
            Diff_Seconds = Diff_Seconds - 1 
            Diff_Frames = Frames_2 - Frames_1 + 25
    

        Real_Ecu_Time = datetime.strptime(Real_Ecu_Time, "%H:%M:%S")
        Real_Ecu_Time = Real_Ecu_Time.strftime('%H:%M:%S')
        Real_Ecu_Time = datetime.strptime(Real_Ecu_Time, "%H:%M:%S")

        real_diff_time = timedelta(hours=Diff_Hours, minutes=Diff_Minutes, seconds=Diff_Seconds)#, milliseconds=Diff_Frames*40
        real_mark_time = Real_Ecu_Time + real_diff_time

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


    def Convolve(self, Data_Set, File_Name, Data, Window_Size, Save):


        """

        Function: This function performs smoothing on the input feature data by replacing the original data with the average value within a window of size Window_Size. It plots the data of turning left and right in different colors on the same graph, and saves the result as a file.
    
        Parameters:

            Data_Set: pandas DataFrame, contains the feature and label data of the dataset

            File_Name: string, used to name the saved image file

            Data: numpy array, the numerical values of feature data

            Window_Size: integer, the size of the smoothing window


        """        
        Smoothed_Data = np.convolve(Data, np.ones(Window_Size)/Window_Size, mode='same')
        Data = Smoothed_Data
        
        x1 = np.arange(len(Data[Data_Set['Action']== 'left']))
        x2 = np.arange(len(Data[Data_Set['Action']== 'right']))

        plt.figure()
        plt.plot(x1, Data[Data_Set['Action']== 'left'] , c='r' , label='Turn left')
        plt.plot(x2, Data[Data_Set['Action'] == 'right'], c='g', label='Turn right')
        plt.legend(loc='lower right')
        
        if Save:
            plt.savefig(File_Name+'_Window_Size_'+str(Window_Size)+'.png')
        
        return 



