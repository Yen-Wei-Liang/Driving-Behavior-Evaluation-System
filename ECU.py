class Engineering:

    def __init__(self):
        pass
    
    def Reverse(self, Data_Path, Data_Save_Path):

        import os
        import pandas as pd
        import numpy as np 
        from tqdm import tqdm, trange

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
   
        Reverse_ECU_Data.to_csv(Data_Save_Path)  