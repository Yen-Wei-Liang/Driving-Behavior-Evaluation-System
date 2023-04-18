# Data set introduction
本資料集為2023年4月17日下午14時16分開始採集，採集時間為26分鐘，共計27578筆資料。

# 採集路線
採集路線的GPS詳細資訊可見檔案20230417_GPS.csv，該檔案包含經度、緯度、海拔、時間戳以及速度等資訊。

# 採集時間
採集時間為14:16非尖峰時刻，如圖所示。
![](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/blob/main/Data_Set/20230417_DataSet/Off-peak%20time%20on%20the%20afternoon%20of%20April%2017th.jpg?raw=true)

# 採集設備
本次採集使用的設備為平板，其放置位置如圖所示。
![](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/blob/main/Data_Set/20230417_DataSet/Place_The_Luggage_In_The_Trunk.jpg?raw=true)

# 偏左或偏右行為
對於X與Z軸角速度執行Moving average後，可以明顯分類出偏左或偏右。
### X軸角速度
![](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/blob/main/Data_Set/20230417_DataSet/Data_Set_1st_X_axis_Angular_Velocity_Window_Size_10.png?raw=true)

### Z軸角速度
![](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/blob/main/Data_Set/20230417_DataSet/Data_Set_1st_Z_axis_Angular_Velocity_Window_Size_10.png?raw=true)

# 分類準確度
本資料集使用多模型進行分類，其準確度從之前的82%提升至多個模型都能達到90%以上。
![](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/blob/main/Data_Set/20230417_DataSet/Classification.png?raw=true)
