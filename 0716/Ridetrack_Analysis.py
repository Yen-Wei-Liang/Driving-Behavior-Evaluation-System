import vomm
import time
import math
import joblib
from joblib import dump, load
import warnings
import numpy as np 
import pandas as pd
import pickle
from statistics import mode
from tqdm import tqdm, trange
from datetime import datetime
from datetime import timedelta
import matplotlib.pyplot as plt
from filterpy.kalman import KalmanFilter
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score, f1_score, recall_score, classification_report
from sklearn.metrics import silhouette_score, calinski_harabasz_score, davies_bouldin_score
from sklearn import svm, metrics
from sklearn import tree, metrics
from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN, MiniBatchKMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler
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
        self.features = ["Absolute Time", "X-axis Angular Velocity", "Y-axis Angular Velocity", 
                         "Z-axis Angular Velocity", "X-axis Acceleration", "Y-axis Acceleration", 
                         "Z-axis Acceleration", "X-axis Angle", "Y-axis Angle", "Z-axis Angle"]

    def Introduction(self):
        print('1. Axis_Process(讀取檔案目錄, 儲存檔案目錄, 是否儲存)\n'
              '2. ECU_Reverse(讀取檔案目錄, 儲存檔案目錄, 是否儲存)\n'
              '3. Data_Merge(讀取ECU檔案目錄, 讀取IMU檔案目錄, 合併儲存檔案目錄, 是否儲存)\n'
              '4. Rotation(輸入資料集, 是否儲存)\n'
              '5. Normalized(輸入資料集, 特徵, 是否儲存)\n'
              '6. KMeans_Cluster(輸入資料集, 特徵, 群數, 是否儲存)\n'
              '7. KMeans_Cluster_Predict(輸入資料集, 特徵, 模型名稱, 是否儲存)\n'
              '8. Evaluate_Clustering_Algorithms(輸入資料集, 最大群數, 是否儲存)\n'
              '9. Evaluate_PCA(輸入資料集, 元件個數)\n'
              '10. All_model(訓練資料集, 驗證資料集, 訓練資料集標籤, 是否儲存)\n'
              '11. Train_Vomm(訓練資料集, 樹高, 群數)\n'
              '12. Test_Vomm(測試資料集, 頻率, 是否儲存)\n'
              '13. Filter_Actions(資料集, 頻率)\n'
              '14. Compute_Accuracy(資料集, 頻率, 是否儲存)\n'
              '15. Compute_Accuracy_All(資料集, 特徵, 頻率, 是否儲存)\n'
              '16. Calculate_Action_Prediction_Counts(資料集)\n'
              '17. Tradition_Category(資料集, 分位數, 特徵, 是否儲存)\n'
              '18. Tradition_Category_Value(資料集, 分位數值, 特徵, 是否儲存)\n'
              '19. convert_to_decimal(數字, 進位數)\n'             
              '20. Tradition_Encoding(資料集, 特徵, 是否儲存)\n'
              '21. Tradition_Find_Top_K(資料集, 百分比)\n'
              '22. Plot_Action_Cluter(資料集, 動作1, 動作2, 特徵, 群數, 長度, 是否儲存)\n'   
              '23. Plot_Action_Track(資料集, 特徵名, 一次繪製步數, 是否儲存)\n'
              '24. Calculating_Time(影片ECU時間標記, 影片時間標記, 啟動真實時間)\n'
              '25. Convolve(資料集, 特徵名, 檔案, 視窗大小, 是否儲存)'
              )
 
    # 儲存檔案使用
    @staticmethod
    def _save_dataframe(df, path):
        """
        Function: Save dataframe to csv.

        Parameters:
            df: The dataframe to be saved.
            path: The path to save the dataframe.
        """
        df.to_csv(path)

    # 計算執行時間
    @staticmethod
    def _print_execution_time(start_time):
        """
        Function: Print the execution time from start_time to now.

        Parameters:
            start_time: The start time of execution.
        """
        # Compute and print the execution time
        execution_time = time.time() - start_time
        hours, rem = divmod(execution_time, 3600)
        minutes, seconds = divmod(rem, 60)
        print(f"Execution time: {hours} hours {minutes} minutes {seconds} seconds")


    # 處理IMU資料
    def Axis_Process(self, Data_Path, save_path=None):
    
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

        if save_path:
            try:
                self._save_dataframe(Reverse_Axis_Data, save_path)   
            except Exception as e:
                print(f"Failed to save data to {save_path}: {e}")      

        self._print_execution_time(start_time)
        
        return Reverse_Axis_Data

    # 處理ECU資料
    def ECU_Reverse(self, data_path, save_path=None):

        start_time = time.time()  # Start time

        ECU_Raw_Data = pd.read_csv(data_path, header=None)
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
        
        if save_path:
            try:
                self._save_dataframe(Reverse_ECU_Data, save_path)
            except Exception as e:
                print(f"Failed to save data to {save_path}: {e}")            
        self._print_execution_time(start_time)

        return Reverse_ECU_Data

    # 合併資料
    def Data_Merge(self, ecu_data_path, axis_data_path, save_path=None):

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

        ECU_Raw_Data = pd.read_csv(ecu_data_path)
        ECU_Raw_Data = ECU_Raw_Data.drop('Unnamed: 0',axis=1)

        Axis_Raw_Data = pd.read_csv(axis_data_path)
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

        if save_path:
            try:
                self._save_dataframe(Merge_Data, save_path)
            except Exception as e:
                print(f"Failed to save data to {save_path}: {e}")
        self._print_execution_time(start_time)

        return Merge_Data


    # 校正角度使用
    def calibrate_angles(self, dataset, save_path=None):
        """
        Function: Used for calibrating angle data.

        Parameters:
            dataset: DataFrame containing the angle data.
            save_path: Path of the CSV file to save the calibrated data.

        Python Libraries:
            pandas: Used for handling CSV data.
            numpy: Used for performing scientific computing.
        """
    
        start_time = time.time()  # Start time

        # Copy the dataset to prevent modifying the original one
        calibrated_data = dataset.copy()

        # Convert DataFrame to numpy array for efficiency
        angles_array = dataset[['X-axis Angle', 'Y-axis Angle', 'Z-axis Angle']].to_numpy()
        calibrated_angles_array = angles_array.copy()

        # Define the initial angles
        initial_angles = np.radians(angles_array[0, :])  # Convert to radians

        # Define the rotation matrix
        rotation_matrix = self.get_rotation_matrix(initial_angles)
        inv_rotation_matrix = np.linalg.inv(rotation_matrix)

        # Apply the inverse rotation matrix to each set of angles
        for i in tqdm(range(len(angles_array))):
            # Convert angles to radians
            angles = np.radians(angles_array[i, :])

            # Apply the inverse rotation matrix
            new_angles = np.dot(inv_rotation_matrix, angles)

            # Convert back to degrees and update the calibrated data
            calibrated_angles_array[i, :] = np.degrees(new_angles)

        # Update the DataFrame
        calibrated_data[['X-axis Angle', 'Y-axis Angle', 'Z-axis Angle']] = calibrated_angles_array

        if save_path:
            try:
                self._save_dataframe(calibrated_data, save_path)
            except Exception as e:
                print(f"Failed to save data to {save_path}: {e}")

        self._print_execution_time(start_time)

        return calibrated_data
    

    
    # 校正角度呼叫副程式
    def get_rotation_matrix(self, angles):
        """
        Function: Compute the rotation matrix.

        Parameters:
            angles: A numpy array containing the x, y, z angles in radians.
        """

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

        return rotation_matrix



    # 校正加速度角速度使用
    def calibrate_imu(self, dataset, k, save_path=None):
        """
        Function: Used for calibrating IMU data.

        Parameters:
            dataset: DataFrame containing the IMU data.
            k: Number of initial samples to use for calibration.
            save_path: Path of the CSV file to save the calibrated data.

        Python Libraries:
            pandas: Used for handling CSV data.
            numpy: Used for performing scientific computing.
        """
    
        start_time = time.time()  # Start time

        features = ['X-axis Angular Velocity', 'Y-axis Angular Velocity', 'Z-axis Angular Velocity', 
                    'X-axis Acceleration', 'Y-axis Acceleration', 'Z-axis Acceleration']
    
        # Copy the dataset to prevent modifying the original one
        calibrated_data = dataset.copy()  
    
        for feature in features:
            # Compute the mean of the first k samples
            mean_value = dataset[feature][:k].mean()
        
            # Subtract the mean from the entire column
            calibrated_data[feature] -= mean_value

        if save_path:
            try:
                self._save_dataframe(calibrated_data, save_path)
            except Exception as e:
                print(f"Failed to save data to {save_path}: {e}")

        self._print_execution_time(start_time)

        return calibrated_data



# IMU通常由陀螺儀、加速度計和（有時）磁力計組成。對於這些傳感器，校正通常涉及零點偏移（bias）和比例因子（scale factor）的調整。

# 陀螺儀（角速度）：陀螺儀在靜止時的讀數應該是零。因此，將靜止時的平均讀數作為零點偏移（bias）來校正陀螺儀是可行的。

# 加速度計：加速度計在靜止時，只應該感測到重力加速度（g）。因此，對於加速度計，你需要確認在靜止時，加速度讀數的長度（magnitude）是否與g相等。如果不相等，那麼你需要進行比例因子（scale factor）校正。然後，你可以使用靜止時的平均讀數來進行零點偏移（bias）校正。不過，由於加速度計可能有方向性的bias（例如，如果加速度計未完全水平），因此最好在各種方向上旋轉IMU以進行校正。

# 角度（儀慦角）：IMU通常不能直接測量角度。角度通常是通過整合角速度或者使用加速度計和磁力計的讀數來估計的。因此，角度的校正通常涉及到對陀螺儀、加速度計和磁力計的校正。

# 因此，對於你的問題，陀螺儀和加速度計可以使用你提供的方法進行零點偏移（bias）校正。然而，角度可能需要進一步的處理。具體的校正方法取決於你是如何計算角度的。



    def normalize_data(self, dataset, feature, method="minmax", save_path=None):
        """
        Function: Normalize specified feature in dataset.

        Parameters:
            dataset: The dataframe containing the data to normalize.
            feature: The column(s) in the dataframe to normalize.
            method: The normalization method to use. Options are "minmax", "standard", "robust".
            save_path: Path to save normalized data. If None, data will not be saved.

        Returns:
            normalized_df: The dataframe after normalization.
        """
        start_time = time.time()  # Start time

        # 定義一個字典來映射方法名稱到相應的類
        methods = {
            "minmax": MinMaxScaler,
            "standard": StandardScaler,
            "robust": RobustScaler
        }

        # 檢查指定的方法是否存在
        if method not in methods:
            raise ValueError(f"Invalid method. Expected one of: {list(methods.keys())}")

        # 創建相應的物件
        scaler = methods[method]()

        # 對指定特徵進行正規化
        normalized_data = scaler.fit_transform(dataset[feature])

        # 將正規化後的資料轉換為DataFrame
        normalized_df = pd.DataFrame(normalized_data, columns=feature)

        # 將DataFrame保存為CSV檔案
        if save_path:
            try:
                self._save_dataframe(normalized_df, save_path)
            except Exception as e:
                print(f"Failed to save data to {save_path}: {e}")

        self._print_execution_time(start_time)

        return normalized_df


    def initialize_kalman_filter(self, dim, q_noise=0.0001, r_noise=0.001):
        """Initializes a Kalman filter."""
    
        kf = KalmanFilter(dim_x=dim, dim_z=dim)
        kf.F = np.eye(dim)
        kf.H = np.eye(dim)
        kf.Q = np.eye(dim) * q_noise
        kf.R = np.eye(dim) * r_noise
        kf.x = np.zeros((dim, 1))
        kf.P = np.eye(dim)

        return kf

    def apply_kalman_filter(self, dataset, features, q_noise=0.0001, r_noise=0.001, save_path=None):
        """
        Apply Kalman filter to a dataset.

        Parameters:
            dataset: DataFrame containing the data.
            features: Features to apply the filter on.
            q_noise: Noise in the system.
            r_noise: Measurement noise.
            save_path: Path of the CSV file to save the filtered data.
        """
    
        start_time = time.time()

        # Initialize the Kalman filter
        kf = self.initialize_kalman_filter(len(features), q_noise, r_noise)

        # Convert DataFrame to numpy array for efficiency
        data_array = dataset[features].to_numpy()
        filtered_data_array = np.zeros_like(data_array)

        # Apply the Kalman filter
        for i in range(data_array.shape[0]):
            measurement = data_array[i, :].reshape(-1, 1)

            # Predict the next state
            kf.predict()

            # Update the state
            kf.update(measurement)

            # Save the filtered result
            filtered_data_array[i, :] = kf.x[:, 0]

        # Convert the filtered data back to DataFrame and update the original dataset
        filtered_df = pd.DataFrame(filtered_data_array, columns=features)
        for feature in features:
            dataset[feature] = filtered_df[feature]

        if save_path:
            try:
                self._save_dataframe(dataset, save_path)
            except Exception as e:
                print(f"Failed to save data to {save_path}: {e}")
        self._print_execution_time(start_time)

        return dataset






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








    #分群使用
    def cluster_data(self, dataset, feature, method="kmeans", n_clusters=3, model_path="model.pkl", save_path=None):
        """
        Function: Perform clustering on specified feature in dataset.

        Parameters:
            dataset: The dataframe containing the data to cluster.
            feature: The column(s) in the dataframe to cluster.
            method: The clustering method to use. Options are "kmeans", "agglomerative", "dbscan".
            n_clusters: The number of clusters to form.
            model_path: Path to save clustering model.
            save_path: Path to save clustered data. If None, data will not be saved.

        Returns:
            dataset: The dataframe after clustering.
        """
        start_time = time.time()  # Start time

        # 定義一個字典來映射方法名稱到相應的類
        methods = {
            "kmeans": KMeans,
            "agglomerative": AgglomerativeClustering,
            # DBSCAN 是基於密度的分群算法，並不需要給定分群數量
            # "dbscan": DBSCAN
        }

        # 檢查指定的方法是否存在
        if method not in methods:
            raise ValueError(f"Invalid method. Expected one of: {list(methods.keys())}")

        # 創建相應的物件
        if method == "dbscan":
            model = methods[method]()
        else:
            model = methods[method](n_clusters=n_clusters)

        # 訓練模型並進行分群
        model.fit(dataset[feature])

        # 分群結果
        dataset['Action Element'] = model.labels_

        # 儲存分群模型
        dump(model, model_path)

        # 儲存分群完資料成 CSV 檔案
        if save_path:
            try:
                self._save_dataframe(dataset, save_path)
            except Exception as e:
                print(f"Failed to save data to {save_path}: {e}")
        self._print_execution_time(start_time)

        return dataset

    # 利用載入訓練好分群模型進行預測
    def predict_cluster(self, dataset, feature, model_path, save_path=None):
        """
        Function: Predict cluster for specified feature in dataset using pre-trained model.

        Parameters:
            dataset: The dataframe containing the data to predict.
            feature: The column(s) in the dataframe to predict.
            model_path: Path to pre-trained clustering model.
            save_path: Path to save predicted data. If None, data will not be saved.

        Returns:
            dataset: The dataframe after prediction.
        """
        
        start_time = time.time()  # Start time

        # 載入模型
        model = load(model_path)

        # 預測
        dataset['Action Element'] = model.predict(dataset[feature])
        
        # 儲存預測後的資料成 CSV 檔案
        if save_path:
            try:
                self._save_dataframe(dataset, save_path)
            except Exception as e:
                print(f"Failed to save data to {save_path}: {e}")
            self._print_execution_time(start_time)

        return dataset



    # 計算分群最佳群數
    def evaluate_clustering(self, k, dataset):
        """
        Evaluate clustering performance.
        """
        kmeans = MiniBatchKMeans(n_clusters=k, random_state=0)
        labels = kmeans.fit_predict(dataset)
        scores = {
            'Silhouette Score': silhouette_score(dataset, labels),
            'Calinski-Harabasz Index': calinski_harabasz_score(dataset, labels),
            'Davies-Bouldin Index': davies_bouldin_score(dataset, labels),
            'Distortion': kmeans.inertia_
        }
        return scores

    def determine_optimal_clusters(self, dataset, max_k, save_path=None):
        """
        Determine the optimal number of clusters using various evaluation metrics.
        """
        start_time = time.time()
        half_max_k = max_k // 2
        evaluation_methods = ['Silhouette Score', 'Calinski-Harabasz Index', 'Davies-Bouldin Index', 'Distortion']
        
        # Initialize the scores list for each evaluation method
        scores = {method: [] for method in evaluation_methods}

        for k in tqdm(range(2, max_k+1)):
            new_scores = self.evaluate_clustering(k, dataset)
            for method in evaluation_methods:
                scores[method].append(new_scores[method])

        top_k = {}
        for method in evaluation_methods[:3]:  # Only the first 3 methods aim to be maximized
            top_k[method] = np.argsort(scores[method])[-half_max_k:] + 2  # +2 because k starts from 2
        top_k['Distortion'] = np.argsort(scores['Distortion'])[:half_max_k] + 2  # Distortion should be minimized

        # Calculate the intersection of the top half max_k clusters for the first 3 evaluation metrics
        intersection = set(top_k[evaluation_methods[0]])
        for method in evaluation_methods[1:3]:  # Exclude the 'Distortion' method
            intersection.intersection_update(top_k[method])

        df_scores = pd.DataFrame(scores, index=range(2, max_k+1))
        self._plot_scores(df_scores, save_path)  # Moved plotting to a separate method for clarity

        for method, ks in top_k.items():
            print(f"根據 {method}，前 {half_max_k} 個建議的分群數量分別為 {ks}")

        print(f"根據前三個評分標準推薦的分群數交集為 {intersection}")

        self._print_execution_time(start_time)
        return df_scores, top_k, intersection

    def _plot_scores(self, df_scores, save_path):
        """
        Plot the scores for each clustering evaluation method.
        """
        plt.figure(figsize=(12, 10))
        for i, method in enumerate(df_scores.columns, 1):
            plt.subplot(2, 2, i)
            plt.plot(df_scores.index, df_scores[method], marker='o')
            plt.xlabel('Number of Clusters (K)')
            plt.ylabel(method)
            plt.title(method)
            plt.xticks(df_scores.index)

        plt.tight_layout()

        if save_path:
            try:
                plt.savefig(save_path)
            except Exception as e:
                print(f"Failed to save figure to {save_path}: {e}")






    def apply_pca(self, df, n_components=None, save_model=None):
        """
        Function: Apply PCA on a dataframe and optionally save the model.
        
        Parameters: 
            df: DataFrame. The dataset to apply PCA.
            n_components: int or None. The number of components to keep. 
                          If None, keep components that explain 95% of the variance.
            model_path: str. The path to save the PCA model.
        
        Returns: 
            df_pca: DataFrame. The transformed dataset.
            pca: PCA object. The PCA model used for transformation.
        """
        start_time = time.time()  # Start time
        # Determine the number of components
        if n_components is None:
            pca_temp = PCA()
            pca_temp.fit(df)
            cumsum = np.cumsum(pca_temp.explained_variance_ratio_)
            n_components = np.argmax(cumsum >= 0.95) + 1
        print(f'適合降至{n_components}維度')
        # Apply PCA
        pca = PCA(n_components=n_components)
        df_pca = pca.fit_transform(df)

        # Save the PCA model
        if save_model:
            dump(pca, save_model)

        self._print_execution_time(start_time)
        return df_pca, pca

    def get_feature_weights(self, df, pca_path):
        """
        Function: Calculate and print the weight of each feature based on the PCA model.

        Parameters: 
            df: DataFrame. The original dataset.
            pca_path: str. The path of the PCA model used for transformation.

        Returns: 
            feature_weights_df: DataFrame. Sorted weights of the features.
        """

        start_time = time.time()  # Start time
        # Load the PCA model
        pca = load(pca_path)

        # Multiply the components by the explained variance ratio
        weighted_components = pca.components_.T * pca.explained_variance_ratio_

        # Get the absolute sum of weights for each original feature
        feature_weights = np.sum(np.abs(weighted_components), axis=1)

        # Create a DataFrame for better visualization
        feature_weights_df = pd.DataFrame({
            'Feature': df.columns,
            'Weight': feature_weights
        })

        # Sort by weight
        feature_weights_df = feature_weights_df.sort_values(by='Weight', ascending=False)
        
        self._print_execution_time(start_time)
        return feature_weights_df

    def load_and_transform_with_pca(self, pca_path, df):
        """
        Function: Load a PCA model and transform a dataframe.
    
        Parameters: 
            pca_path: str. The path to the PCA model.
            df: DataFrame. The dataset to transform.
    
        Returns: 
            df_pca: DataFrame. The transformed dataset.
        """
        # Load the model
        pca = load(pca_path)

        # Use the model to transform the dataframe
        df_pca = pca.transform(df)
        return df_pca

# 進行主成分分析 (PCA) 和直接選取原特徵的差異主要在於資料轉換的方式。

# 差異：

# PCA 是一種線性轉換，其產生的新特徵（主成分）是原特徵的線性組合，而非單純挑選原來的特徵。這種轉換可以在新特徵間消除相關性（即主成分間互相正交）。
# 直接選取原特徵是在原特徵空間中選取特定特徵，並沒有做特徵間的轉換，所以這些特徵可能仍有高度相關性。
# 對後續分群的影響：

# 對於一些對特徵線性可分性有嚴格要求的模型，如線性回歸或邏輯回歸，PCA可能有助於提高模型性能，因為PCA會去掉特徵間的共線性。
# 對於一些不對特徵線性可分性有嚴格要求的模型，如決策樹或隨機森林，直接選擇特徵可能更好，因為這些模型可以處理特徵間的相關性。
# 分群（如 K-means 分群）往往對特徵的尺度敏感，而 PCA 可以讓所有主成分的變異數相等，達到特徵尺度的一致。
# 影響的程度：

# 這取決於具體的模型和數據。如果原特徵間的共線性很強，那麼PCA可能會有較大的改進；如果原特徵間的共線性不強，PCA和直接選擇特徵可能效果相近。此外，決策樹或隨機森林這種對特徵間的相關性較不敏感的模型，可能對PCA和直接選擇特徵的差異反應較小。
# 結論，PCA 與直接選擇原特徵都有各自的優點和適用情境，具體應用時需要根據你的目標（例如精度、解釋性、計算效率等）以及你的數據特性（例如特徵間的相關性、特徵的尺度等）來決定。






# PCA（主成分分析）在其本質上是一種線性變換，將原始特徵變換為新的正交特徵（主成分），這些新特徵的方差依次遞減。在PCA中，components_對象包含了原始特徵空間到主成分空間的轉換矩陣。每一行表示一個主成分，列是原特徵，所以元素的值代表該主成分與原特徵的關係。

# 在給定的猜想中，你提出了基於PCA組件權重絕對值和的想法，這種方法可以給出一種特徵重要性的指標。然而，這種方法的一個限制是它沒有考慮到主成分的變異性貢獻（explained_variance_ratio_），這可能導致某些在解釋變異性中貢獻較少的成分被過分重視。

# 在你的第二段代碼中，你給出了一種改進的方法，即考慮到了主成分的變異性貢獻，這將對評估特徵的重要性提供更全面的視角。

# 在下面的程式碼中，我根據以上的討論做了一些修改，包括模塊化的改進以及增加一些代碼註釋以提高程式碼的可讀性：









    # 計算分類的準確度與預測並儲存(2個檔案)
    def All_model(self, DataSet, Validation_DataSet, Label, save_path=None):

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





        if save_path:
            self._save_dataframe(Validation_DataSet, save_path)

        self._print_execution_time(start_time)

        return models





    def All_model_v1(self, Train_Data, Train_Label, Test_Data, Test_Label, Validation_DataSet, Feature, save_path):

        """

        Function: Perform classification tasks using support vector machines, K-nearest neighbors, decision trees, random forests,               neural networks, Gaussian process algorithms, and calculate accuracy, F1 score, and recall score.

        Parameters:

            DataSet: Input feature data, which can be a pandas DataFrame.

            Label: Label data, which refers to the classification label corresponding to each feature data, and can be a pandas Series.

        """

        start_time = time.time()  # Start time


        # SVM          
        svm_model = svm.SVC()
        svm_model.fit(Train_Data, Train_Label)
        test_predict = svm_model.predict(Test_Data)
        svm_model_acc = metrics.accuracy_score(Test_Label, test_predict)
        svm_model_f1 = f1_score(Test_Label, test_predict, average='weighted')
        svm_model_recall = recall_score(Test_Label, test_predict, average='weighted')


        # 計算混淆矩陣
        conf_matrix = confusion_matrix(Test_Label, test_predict)

        # 類別標籤列表
        labels = svm_model.classes_

        # 創建空的DataFrame
        result_df = pd.DataFrame(columns=['SVM', 'Predicted: Idle', 'Predicted: Two-Stage Left', 'Predicted: Turn Right', 'Predicted: Turn Left', 'Predicted: Go Straight', 'Predicted: U-turn', 'Accuracy'])

        # 逐一計算每個類別的計數和準確度，並添加到DataFrame中
        for i in range(len(labels)):
            true_label = labels[i]
            true_label_count = conf_matrix[i, i]  # 對角線元素即為該類別的正確預測次數
            other_label_counts = conf_matrix[i, :].sum() - true_label_count  # 非對角線元素之和為該類別的錯誤預測次數
            accuracy = true_label_count / (true_label_count + other_label_counts) * 100

            result_df.loc[i] = [true_label, *conf_matrix[i], accuracy]

        # 設定SVM和Accuracy列的格式
        result_df['SVM'] = result_df['SVM'].astype(str)
        result_df['Accuracy'] = result_df['Accuracy'].apply(lambda x: f"{x:.2f}%" if not pd.isnull(x) else "-")

        # 將DataFrame以Markdown格式輸出
        markdown_output = result_df.to_markdown(index=False)

        print(markdown_output)

        
        # KNeighborsClassifier
        KNeighbors_model = KNeighborsClassifier(n_neighbors=6)
        KNeighbors_model.fit(Train_Data, Train_Label)
        test_predict = KNeighbors_model.predict(Test_Data)
        KNeighbors_model_acc = metrics.accuracy_score(Test_Label, test_predict)
        KNeighbors_model_f1 = f1_score(Test_Label, test_predict, average='weighted')
        KNeighbors_model_recall = recall_score(Test_Label, test_predict, average='weighted')



        # 計算混淆矩陣
        conf_matrix = confusion_matrix(Test_Label, test_predict)

        # 類別標籤列表
        labels = KNeighbors_model.classes_

        # 創建空的DataFrame
        result_df = pd.DataFrame(columns=['KNeighbors', 'Predicted: Idle', 'Predicted: Two-Stage Left', 'Predicted: Turn Right', 'Predicted: Turn Left', 'Predicted: Go Straight', 'Predicted: U-turn', 'Accuracy'])

        # 逐一計算每個類別的計數和準確度，並添加到DataFrame中
        for i in range(len(labels)):
            true_label = labels[i]
            true_label_count = conf_matrix[i, i]  # 對角線元素即為該類別的正確預測次數
            other_label_counts = conf_matrix[i, :].sum() - true_label_count  # 非對角線元素之和為該類別的錯誤預測次數
            accuracy = true_label_count / (true_label_count + other_label_counts) * 100

            result_df.loc[i] = [true_label, *conf_matrix[i], accuracy]

        # 設定SVM和Accuracy列的格式
        result_df['KNeighbors'] = result_df['KNeighbors'].astype(str)
        result_df['Accuracy'] = result_df['Accuracy'].apply(lambda x: f"{x:.2f}%" if not pd.isnull(x) else "-")

        # 將DataFrame以Markdown格式輸出
        markdown_output = result_df.to_markdown(index=False)

        print(markdown_output)


        # DecisionTree      
        DecisionTree_model = tree.DecisionTreeClassifier()
        DecisionTree_model.fit(Train_Data, Train_Label)
        test_predict = DecisionTree_model.predict(Test_Data)
        DecisionTree_model_acc = metrics.accuracy_score(Test_Label, test_predict)
        DecisionTree_model_f1 = f1_score(Test_Label, test_predict, average='weighted')
        DecisionTree_model_recall = recall_score(Test_Label, test_predict, average='weighted')




        # 計算混淆矩陣
        conf_matrix = confusion_matrix(Test_Label, test_predict)

        # 類別標籤列表
        labels = DecisionTree_model.classes_

        # 創建空的DataFrame
        result_df = pd.DataFrame(columns=['DecisionTree', 'Predicted: Idle', 'Predicted: Two-Stage Left', 'Predicted: Turn Right', 'Predicted: Turn Left', 'Predicted: Go Straight', 'Predicted: U-turn', 'Accuracy'])

        # 逐一計算每個類別的計數和準確度，並添加到DataFrame中
        for i in range(len(labels)):
            true_label = labels[i]
            true_label_count = conf_matrix[i, i]  # 對角線元素即為該類別的正確預測次數
            other_label_counts = conf_matrix[i, :].sum() - true_label_count  # 非對角線元素之和為該類別的錯誤預測次數
            accuracy = true_label_count / (true_label_count + other_label_counts) * 100

            result_df.loc[i] = [true_label, *conf_matrix[i], accuracy]

        # 設定SVM和Accuracy列的格式
        result_df['DecisionTree'] = result_df['DecisionTree'].astype(str)
        result_df['Accuracy'] = result_df['Accuracy'].apply(lambda x: f"{x:.2f}%" if not pd.isnull(x) else "-")

        # 將DataFrame以Markdown格式輸出
        markdown_output = result_df.to_markdown(index=False)

        print(markdown_output)


        # RandomForest
        RandomForest_model = RandomForestClassifier(n_estimators=10)
        RandomForest_model.fit(Train_Data, Train_Label)
        test_predict = RandomForest_model.predict(Test_Data)
        RandomForest_model_acc =  metrics.accuracy_score(Test_Label, test_predict)
        RandomForest_model_f1 = f1_score(Test_Label, test_predict, average='weighted')
        RandomForest_model_recall = recall_score(Test_Label, test_predict, average='weighted')

        # 計算混淆矩陣
        conf_matrix = confusion_matrix(Test_Label, test_predict)

        # 類別標籤列表
        labels = RandomForest_model.classes_

        # 創建空的DataFrame
        result_df = pd.DataFrame(columns=['RandomForest', 'Predicted: Idle', 'Predicted: Two-Stage Left', 'Predicted: Turn Right', 'Predicted: Turn Left', 'Predicted: Go Straight', 'Predicted: U-turn', 'Accuracy'])

        # 逐一計算每個類別的計數和準確度，並添加到DataFrame中
        for i in range(len(labels)):
            true_label = labels[i]
            true_label_count = conf_matrix[i, i]  # 對角線元素即為該類別的正確預測次數
            other_label_counts = conf_matrix[i, :].sum() - true_label_count  # 非對角線元素之和為該類別的錯誤預測次數
            accuracy = true_label_count / (true_label_count + other_label_counts) * 100

            result_df.loc[i] = [true_label, *conf_matrix[i], accuracy]

        # 設定SVM和Accuracy列的格式
        result_df['RandomForest'] = result_df['RandomForest'].astype(str)
        result_df['Accuracy'] = result_df['Accuracy'].apply(lambda x: f"{x:.2f}%" if not pd.isnull(x) else "-")

        # 將DataFrame以Markdown格式輸出
        markdown_output = result_df.to_markdown(index=False)

        print(markdown_output)




        # MLPClassifier
        MLP_model = MLPClassifier(solver='adam', 
                                  alpha=1e-5,
                                  hidden_layer_sizes=(100, ),
                                  random_state=42,
                                  activation='relu'
                                  )
        MLP_model.fit(Train_Data, Train_Label)
        test_predict = MLP_model.predict(Test_Data)
        MLP_model_acc =  metrics.accuracy_score(Test_Label, test_predict)
        MLP_model_f1 = f1_score(Test_Label, test_predict, average='weighted')
        MLP_model_recall = recall_score(Test_Label, test_predict, average='weighted')



        # 計算混淆矩陣
        conf_matrix = confusion_matrix(Test_Label, test_predict)

        # 類別標籤列表
        labels = MLP_model.classes_

        # 創建空的DataFrame
        result_df = pd.DataFrame(columns=['MLP', 'Predicted: Idle', 'Predicted: Two-Stage Left', 'Predicted: Turn Right', 'Predicted: Turn Left', 'Predicted: Go Straight', 'Predicted: U-turn', 'Accuracy'])

        # 逐一計算每個類別的計數和準確度，並添加到DataFrame中
        for i in range(len(labels)):
            true_label = labels[i]
            true_label_count = conf_matrix[i, i]  # 對角線元素即為該類別的正確預測次數
            other_label_counts = conf_matrix[i, :].sum() - true_label_count  # 非對角線元素之和為該類別的錯誤預測次數
            accuracy = true_label_count / (true_label_count + other_label_counts) * 100

            result_df.loc[i] = [true_label, *conf_matrix[i], accuracy]

        # 設定SVM和Accuracy列的格式
        result_df['MLP'] = result_df['MLP'].astype(str)
        result_df['Accuracy'] = result_df['Accuracy'].apply(lambda x: f"{x:.2f}%" if not pd.isnull(x) else "-")

        # 將DataFrame以Markdown格式輸出
        markdown_output = result_df.to_markdown(index=False)

        print(markdown_output)




        # GaussianProcessClassifier
        GaussianProcess_model = GaussianProcessClassifier()
        GaussianProcess_model.fit(Train_Data, Train_Label)
        test_predict = GaussianProcess_model.predict(Test_Data)
        GaussianProcess_model_acc  =  metrics.accuracy_score(Test_Label, test_predict)
        GaussianProcess_model_f1 = f1_score(Test_Label, test_predict, average='weighted')
        GaussianProcess_model_recall = recall_score(Test_Label, test_predict, average='weighted')

        # 計算混淆矩陣
        conf_matrix = confusion_matrix(Test_Label, test_predict)

        # 類別標籤列表
        labels = GaussianProcess_model.classes_

        # 創建空的DataFrame
        result_df = pd.DataFrame(columns=['GaussianProcess', 'Predicted: Idle', 'Predicted: Two-Stage Left', 'Predicted: Turn Right', 'Predicted: Turn Left', 'Predicted: Go Straight', 'Predicted: U-turn', 'Accuracy'])

        # 逐一計算每個類別的計數和準確度，並添加到DataFrame中
        for i in range(len(labels)):
            true_label = labels[i]
            true_label_count = conf_matrix[i, i]  # 對角線元素即為該類別的正確預測次數
            other_label_counts = conf_matrix[i, :].sum() - true_label_count  # 非對角線元素之和為該類別的錯誤預測次數
            accuracy = true_label_count / (true_label_count + other_label_counts) * 100

            result_df.loc[i] = [true_label, *conf_matrix[i], accuracy]

        # 設定SVM和Accuracy列的格式
        result_df['GaussianProcess'] = result_df['GaussianProcess'].astype(str)
        result_df['Accuracy'] = result_df['Accuracy'].apply(lambda x: f"{x:.2f}%" if not pd.isnull(x) else "-")

        # 將DataFrame以Markdown格式輸出
        markdown_output = result_df.to_markdown(index=False)

        print(markdown_output)



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
        

        Validation_predict_KNeighbors = KNeighbors_model.predict(Validation_DataSet[Feature])
        Validation_predict_SVM = svm_model.predict(Validation_DataSet[Feature])
        Validation_predict_DecisionTree = DecisionTree_model.predict(Validation_DataSet[Feature])
        Validation_predict_RandomForest = RandomForest_model.predict(Validation_DataSet[Feature])
        Validation_predict_MLP = MLP_model.predict(Validation_DataSet[Feature])
        Validation_predict_GaussianProcess = GaussianProcess_model.predict(Validation_DataSet[Feature])

        Validation_DataSet['SVM_Predict'] = Validation_predict_SVM
        Validation_DataSet['KNeighbors_Predict'] = Validation_predict_KNeighbors
        Validation_DataSet['DecisionTree_Predict'] = Validation_predict_DecisionTree
        Validation_DataSet['RandomForest_Predict'] = Validation_predict_RandomForest
        Validation_DataSet['MLP_Predict'] = Validation_predict_MLP
        Validation_DataSet['GaussianProcess_Predict'] = Validation_predict_GaussianProcess





        if save_path:
            self._save_dataframe(Validation_DataSet, save_path)

        self._print_execution_time(start_time)
        
        return models





    def All_model_v2(self, Train_Data, Train_Label, Test_Data, Test_Label, Validation_DataSet, Feature, save_path):
        start_time = time.time()  # Start time

        # Prepare the models
        models = {
            "SVM": svm.SVC(),
            "KNeighbors": KNeighborsClassifier(n_neighbors=6),
            "DecisionTree": tree.DecisionTreeClassifier(),
            "RandomForest": RandomForestClassifier(n_estimators=10),
            "MLP": MLPClassifier(solver='adam', alpha=1e-5, hidden_layer_sizes=(100, ), random_state=42, activation='relu'),
            "GaussianProcess": GaussianProcessClassifier()
        }

        # Prepare a dataframe to store the results
        result_df = pd.DataFrame(columns=['Model', 'Accuracy', 'F1 Score', 'Recall'])

        # Train and test the models
        for model_name, model in models.items():
            # Train model
            model.fit(Train_Data, Train_Label)
            # Test model
            test_predict = model.predict(Test_Data)
            model_acc = metrics.accuracy_score(Test_Label, test_predict)
            model_f1 = f1_score(Test_Label, test_predict, average='weighted')
            model_recall = recall_score(Test_Label, test_predict, average='weighted')
            # Append the results to the dataframe
            result_df = result_df.append({'Model': model_name, 'Accuracy': model_acc, 'F1 Score': model_f1, 'Recall': model_recall}, ignore_index=True)

            # Show classification report
            print(f"Classification Report for {model_name}:\n")
            print(classification_report(Test_Label, test_predict))

            # Confusion Matrix
            conf_matrix = confusion_matrix(Test_Label, test_predict)
            print(f"Confusion Matrix for {model_name}:\n")
            print(conf_matrix)
        
            # Validation prediction
            Validation_predict = model.predict(Validation_DataSet[Feature])
            Validation_DataSet[f'{model_name}_Predict'] = Validation_predict

        # Save the DataFrame if a save_path is provided
        if save_path:
            self._save_dataframe(Validation_DataSet, save_path)

        self._print_execution_time(start_time)

        # Print the result dataframe
        print(result_df)
        return models, result_df




    def load_vlmm_models(self, model_file):
        with open(model_file, 'rb') as f:
            self.models = pickle.load(f)

    def train_vomm(self, train_data, l, k, save_model=None):
        start_time = time.time()
        actions = ['Go Straight', 'Idle', 'Turn Left', 'Turn Right', 'Two-Stage Left', 'U-turn']

        self.models = []
        for action in actions:
            data = train_data.loc[train_data['Action'] == action, 'Action Element'].astype(int).tolist()
            model = vomm.ppm()
            model.fit(data, d=l, alphabet_size=k)
            self.models.append(model)

        if save_model:
            with open(save_model, 'wb') as f:
                pickle.dump(self.models, f)

        self._print_execution_time(start_time)

    def test_vomm(self, data_set, frequency, save_path=None):
        action_element_list = data_set['Action Element'].values.tolist()
        start_time = time.time()
        predictions = []
        actions = ['Go Straight', 'Idle','Turn Left', 'Turn Right', 'Two-Stage Left', 'U-turn']

        for num in tqdm(range(len(action_element_list))):
            max_score = float('-inf')
            selected_model = None

            for model, action in zip(self.models, actions):
                scores = [math.exp(model.logpdf(action_element_list[max(0, num-i):num])) ** (1/i) for i in range(6, 30)]
                model_score = max(scores)

                if model_score > max_score:
                    max_score = model_score
                    selected_model = action

            predictions.append(selected_model)

        data_set['Predict'] = predictions
        data_set['Filter_Predict'] = self.filter_actions(data_set['Predict'], frequency)

        if save_path:
            self._save_dataframe(data_set, save_path)

        self._print_execution_time(start_time)
        return data_set










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

        result_df1 = pd.DataFrame({'RideTrack': column_names, 'Accuracy (Total)': match_percentages1})

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
        result_df2['Accuracy (Total)'] = result_df1['Accuracy (Total)']

        # 獲取當前日期和時間
        now = datetime.now()
        date = now.strftime('%Y%m%d')  # 格式化日期為YYYYMMDD
        time = now.strftime('%H%M')  # 格式化時間為HHMM

        if Save:
            result_df2.to_csv(f'{date}_Accuracy_Predict_{time}.csv', index=False)
        

        print(result_df2)
        return result_df2












    # def Load_VLMM_Models(self, model_file):
    #     # 載入模型
    #     with open(model_file, 'rb') as f:
    #         self.Go_Model, self.Idle_Model, self.Left_Model, self.Right_Model, self.Two_Model, self.U_Model = pickle.load(f)


    # 訓練Vomm模型使用
    def Train_Vomm(self, TrainData, L, K, save_model=None):
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


        if save_model:
            with open(save_model, 'wb') as f:
                pickle.dump((self.Go_Model, self.Idle_Model, self.Left_Model, self.Right_Model, self.Two_Model, self.U_Model), f)

 
        self._print_execution_time(start_time)


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























    def Test_Vomm_v1(self, DataSet, Frequency, Save):
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
        lmax=[]

        for num in tqdm(range(len(action_element_list))):
            Max_Score = float('-inf')
            Max_length = None
            Selected_Model = None


            scores = []
            lengths = []
            for i in range(20, 35): 
            # for i in range(6, 30):
                Idle_Model_Score = self.Idle_Model.logpdf(action_element_list[max(0, num-i):num])
                Idle_Model_Score = math.exp(Idle_Model_Score) ** (1/i)
                scores.append(Idle_Model_Score)
                lengths.append(i)
            Idle_Model_Score = max(scores)
            Idle_Max_length = lengths[scores.index(max(scores))]

           

            scores = []
            lengths = []
            # 29  6
            for i in range (6, 30):
            # for i in range(23, 35):
            # for i in range(6, 30):
                Go_Model_Score = self.Go_Model.logpdf(action_element_list[max(0, num-i):num])
                Go_Model_Score = math.exp(Go_Model_Score) ** (1/i)
                scores.append(Go_Model_Score)
                lengths.append(i)
            Go_Model_Score = max(scores)
            Go_Max_length = lengths[scores.index(max(scores))]


            scores=[]
            lengths = []
            #27 3
            for i in range (18, 30):
            # for i in range(24, 30):
            # for i in range(6, 30):
                Left_Model_Score = self.Left_Model.logpdf(action_element_list[max(0, num-i):num])
                Left_Model_Score = math.exp(Left_Model_Score) ** (1/i)
                scores.append(Left_Model_Score)
                lengths.append(i)
            Left_Model_Score = max(scores)
            Left_Max_length = lengths[scores.index(max(scores))]

            
            scores=[]
            lengths = []
            # 37 8
            for i in range (6, 36):
            # for i in range(29, 45):
            # for i in range(6, 30):
               Right_Model_Score = self.Right_Model.logpdf(action_element_list[max(0, num-i):num])
               Right_Model_Score = math.exp(Right_Model_Score) ** (1/i)
               scores.append(Right_Model_Score)
               lengths.append(i)
            Right_Model_Score = max(scores)
            Right_Max_length = lengths[scores.index(max(scores))]


            scores = []
            lengths = []
            # 26 4
            for i in range (24, 30):
            # for i in range(22, 30):
            # for i in range(6, 30):
                Two_Model_Score = self.Two_Model.logpdf(action_element_list[max(0, num-i):num])
                Two_Model_Score = math.exp(Two_Model_Score) ** (1/i)
                scores.append(Two_Model_Score)
                lengths.append(i)
            Two_Model_Score = max(scores)
            Two_Max_length = lengths[scores.index(max(scores))]


            scores = []
            lengths = []
            #
            for i in range (18, 30):
            # for i in range(20, 26):
            # for i in range(6, 30):
                U_Model_Score = self.U_Model.logpdf(action_element_list[max(0, num-i):num])
                U_Model_Score = math.exp(U_Model_Score) ** (1/i)
                scores.append(U_Model_Score)
                lengths.append(i)
            U_Model_Score = max(scores)
            U_Max_length = lengths[scores.index(max(scores))]



            Score_Models = [Idle_Model_Score, Go_Model_Score, Left_Model_Score, Right_Model_Score, Two_Model_Score, U_Model_Score,]
            Models = ['Idle', 'Go Straight','Turn Left', 'Turn Right', 'Two-Stage Left', 'U-turn']    
            Max_length_Models = [Idle_Max_length, Go_Max_length, Left_Max_length, Right_Max_length, Two_Max_length, U_Max_length]
            for Score, model, length in zip(Score_Models, Models, Max_length_Models):
                if Score > Max_Score:
                    Max_Score = Score
                    Selected_Model = model
                    Max_length = length  # 取得該模型的最大長度

            predictions.append(Selected_Model)
            lmax.append(Max_length)
        
        DataSet['Predict'] = predictions
        DataSet['Filter_Predict'] = self.Filter_Actions(DataSet['Predict'], Frequency)
        DataSet['LMax'] = lmax






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



















































    @staticmethod
    def _mode_of_data(window):
        return mode(window)
        
    def filter_actions(self, dataset, frequency):
        filtered_data = []
        previous_action = None
        for i, action in enumerate(dataset):
            if action != previous_action:
                window = dataset[i:i+(2*frequency)]
                if self._mode_of_data(window) == action:
                    pass
                else:
                    if self._mode_of_data(window + dataset[i-frequency:i+frequency]) != action:
                        action = self._mode_of_data(window)
                    else:
                        action = previous_action
            filtered_data.append(action)
            previous_action = action
        return filtered_data

    def compute_accuracy(self, dataset, frequency, save_path=None):
        dataset['Filter_Predict'] = self.filter_actions(dataset['Predict'], frequency)
        filtered_data = dataset[['Action', 'Predict', 'Filter_Predict']].dropna()

        result_df1 = self._compute_total_accuracy(filtered_data, ['Predict', 'Filter_Predict'])
        result_df2 = self._compute_label_accuracy(filtered_data, ['Predict', 'Filter_Predict'])
        result_df2['Accuracy (Total)'] = result_df1['Accuracy (Total)']

        if save_path:
            self._save_dataframe(result_df2, save_path)
            
        return result_df2

    @staticmethod
    def _compute_total_accuracy(data, columns):
        match_percentages = []
        for column in columns:
            count = (data['Action'] == data[column]).sum()
            match_percentage = (count / len(data)) * 100
            match_percentages.append(match_percentage)
        return pd.DataFrame({'RideTrack': columns, 'Accuracy (Total)': match_percentages})

    @staticmethod
    def _compute_label_accuracy(data, columns):
        class_labels = data['Action'].unique()
        match_percentages = []
        for column in columns:
            column_match_percentages = []
            for label in class_labels:
                total = (data['Action'] == label).sum()
                count = ((data['Action'] == label) & (data[column] == label)).sum()
                match_percentage = (count / total) * 100 if total != 0 else 0
                column_match_percentages.append(match_percentage)
            match_percentages.append(column_match_percentages)
        return pd.DataFrame(match_percentages, columns=class_labels, index=columns).reset_index()

    @staticmethod
    def _save_dataframe(df, path):
        df.to_csv(path, index=False)
        
    def calculate_action_prediction_counts(self, test_label, test_predict):
        conf_matrix = confusion_matrix(test_label, test_predict)

        labels = np.unique(test_label)
        columns = [f'Predicted: {label}' for label in labels]

        result_df = pd.DataFrame(columns=['Action'] + columns + ['Accuracy'])

        for i, action in enumerate(labels):
            true_label_count = conf_matrix[i, i]
            other_label_counts = conf_matrix[i, :].sum() - true_label_count
            accuracy = true_label_count / (true_label_count + other_label_counts) * 100
            result_df.loc[i] = [action, *conf_matrix[i], accuracy]

        print(result_df.to_markdown(index=False))

        return result_df










































    # 與手動標記比對各類動作準確度與整體準確度 (給分類使用)
    def compute_accuracy_all(self, dataset, features, frequency, save_path):
        """
        Compute the overall and individual accuracy for each category and classifier.
        """

        column_names = []
        for feature in features:
            filtered_feature = self.filter_actions(dataset[feature], frequency)
            dataset[f'Filter_{feature}'] = filtered_feature
            column_names.extend([feature, f'Filter_{feature}'])
        
        filtered_data = dataset[['Action'] + column_names].dropna()

        match_percentages1 = [
            (filtered_data[column] == filtered_data['Action']).mean() * 100
            for column in column_names
        ]
        result_df1 = pd.DataFrame({
            'RideTrack': column_names,
            'Accuracy (Total)': match_percentages1
        })

        class_labels = filtered_data['Action'].unique()
        match_percentages2 = []
        for column in column_names:
            column_match_percentages = [
                ((filtered_data[column] == label) & (filtered_data['Action'] == label)).sum() / 
                (filtered_data['Action'] == label).sum() * 100 
                if (filtered_data['Action'] == label).sum() != 0 else 0
                for label in class_labels
            ]
            match_percentages2.append(column_match_percentages)

        result_df2 = pd.DataFrame(match_percentages2, columns=class_labels, index=column_names)
        result_df2.index.name = 'RideTrack'
        result_df2 = result_df2.reset_index()
        result_df2['Accuracy (Total)'] = result_df1['Accuracy (Total)']

        if save_path:
            self._save_dataframe(result_df2, save_path)

        return result_df2






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
    

    # 傳統閥值分類並儲存檔案
    def Tradition_Category_Value(self, DataSet, Quantiles_Value, Feature, Save):

        Category=[]
        for index, feature in enumerate(Feature):
            Variable_Category = f"{feature}_Category"
            Category.append(Variable_Category)
            Variable_thresholds = Quantiles_Value[index]

            DataSet[Variable_Category] = pd.cut(DataSet[feature], bins=Variable_thresholds, labels=False)
            # DataSet[Variable_Category] = DataSet[Variable_Category].fillna(0)
    
        DataSet[Category] = DataSet[Category].fillna(0)
        # DataSet['Action Element'] = DataSet['Action Element'].fillna(0)

        if Save:
            DataSet.to_csv(f'Traditional_Threshold_{len(Quantiles_Value)-1}^{len(Feature)}_groups.csv')
        
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

            plt.title(f'{i} Slice - {Step_Column_Name}')
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
            for j, condition in enumerate(['Go Straight', 'Idle', 'Turn Right', 'Turn Left', 'Two-Stage Left', 'U-turn', 'Transition']):
                condition_points = [idx for idx, val in enumerate(Test_Data_slice['Action']) if val == condition]
                plt.scatter(Test_Data_slice.index[condition_points], Test_Data_slice['Z-axis Angular Velocity'][condition_points],
                            color=colors[j], label=condition, alpha=0.5)

            plt.title(f'{i} Slice - Action')
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

    # 簡易平滑資料使用
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


    def Data_Smoothing(self, DataSet, Feature, Method, Slice_Size):
        if Method == 'Kalman':
            kf = KalmanFilter(dim_x=len(Feature), dim_z=len(Feature))
            kf.F = np.eye(len(Feature))
            kf.H = np.eye(len(Feature))
            kf.Q = np.eye(len(Feature)) * 0.0001
            kf.R = np.eye(len(Feature)) * 0.001
            kf.x = np.zeros((len(Feature), 1))
            kf.P = np.eye(len(Feature))
            Data = np.array(DataSet[Feature].values)
            filtered_data = np.zeros_like(Data)

            for i in range(Data.shape[0]):
                measurement = Data[i, :].reshape(len(Feature), 1)
                kf.predict()
                kf.update(measurement)
                filtered_data[i, :] = kf.x[:, 0]

            for i, column in enumerate(Feature):
                DataSet[column] = filtered_data[:, i]


            num_slices = math.ceil(len(DataSet) / Slice_Size)
            slices = []
            for i in range(num_slices):
                start = i * Slice_Size
                end = min((i + 1) * Slice_Size, len(DataSet))
                slices.append((start, end))

            for i, (start, end) in enumerate(slices):
                plt.figure()
                Test_Data_slice = DataSet.iloc[start:end]
                Test_Data_slice.reset_index(drop=True, inplace=True)
                Feature_Value = Test_Data_slice[Feature]
                plt.title(f'{i} Slice - {Method}')
                plt.xlabel('Time Step')
                plt.ylabel(f'{Feature}')
                plt.plot(range(len(Test_Data_slice)), Feature_Value, label=f'{Feature}')

            return DataSet

        if Method == 'Window_Average':
            Window_Size = 30
            Smoothed_Data = np.convolve(DataSet[Feature], np.ones(Window_Size)/Window_Size, mode='same')
            DataSet[Feature] = Smoothed_Data


            num_slices = math.ceil(len(DataSet) / Slice_Size)
            slices = []
            for i in range(num_slices):
                start = i * Slice_Size
                end = min((i + 1) * Slice_Size, len(DataSet))
                slices.append((start, end))

            for i, (start, end) in enumerate(slices):
                plt.figure()
                Test_Data_slice = DataSet.iloc[start:end]
                Test_Data_slice.reset_index(drop=True, inplace=True)
                Feature_Value = Test_Data_slice[Feature]
                plt.title(f'{i} Slice - {Method}')
                plt.xlabel('Time Step')
                plt.ylabel(f'{Feature}')
                plt.plot(range(len(Test_Data_slice)), Feature_Value, label=f'{Feature}')

            return Smoothed_Data
        
        if Method == 'None':
            num_slices = math.ceil(len(DataSet) / Slice_Size)
            slices = []
            for i in range(num_slices):
                start = i * Slice_Size
                end = min((i + 1) * Slice_Size, len(DataSet))
                slices.append((start, end))

            for i, (start, end) in enumerate(slices):
                plt.figure()
                Test_Data_slice = DataSet.iloc[start:end]
                Test_Data_slice.reset_index(drop=True, inplace=True)
                Feature_Value = Test_Data_slice[Feature]
                plt.title(f'{i} Slice - {Method}')
                plt.xlabel('Time Step')
                plt.ylabel(f'{Feature}')
                plt.plot(range(len(Test_Data_slice)), Feature_Value, label=f'{Feature}')

            return DataSet