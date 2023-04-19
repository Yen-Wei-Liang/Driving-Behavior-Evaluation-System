class Engineering:
   """

    Function: Used for processing data from a car-mounted Axis.

    """
    
    def Process(self, Data_Path, Data_Save_Path):

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

        import pandas as pd
        import numpy as np 
        from tqdm import tqdm, trange
        
        
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

        Reverse_Axis_Data.to_csv(Data_Save_Path)    