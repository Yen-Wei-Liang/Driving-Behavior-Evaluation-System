# 目錄
* [一、資料集介紹](#1-資料集介紹)
  * [1.1 取樣路線](#11-取樣路線)
  * [1.2 取樣時間](#12-取樣時間)
  * [1.3 取樣設備](#13-取樣設備)
* [二、Semi-automatic labeling](#2-semi-automatic-labeling)
  * [2.1 Silhouette Score](#21-silhouette-score)
  * [2.2 Calinski-Harabasz Index](#22-calinski-harabasz-index)
  * [2.3 Davies-Bouldin Index](#23-davies-bouldin-index)
  * [2.4 Elbow Method](#24-elbow-method)
* [三、動作元素個數與VOMM建模預測](#3-動作元素個數與vomm建模預測)
  * [3.1 輸入4段序列動作資料進行訓練](#31-輸入4段序列動作資料進行訓練)
    * [3.1.1 動作元素4群探討](#311-動作元素4群探討)
    * [3.1.2 動作元素8群探討](#312-動作元素8群探討)
    * [3.1.3 動作元素10群探討](#313-動作元素10群探討)
  * [3.2 訓練輸入該動作8段序列資料](#32-訓練輸入該動作8段序列資料)
    * [3.2.1 動作元素4群探討](#321-動作元素4群探討)
    * [3.2.2 動作元素8群探討](#322-動作元素8群探討)
    * [3.2.3 動作元素10群探討](#323-動作元素10群探討)
  * [3.3 觀察小結](#33-觀察小結)
* [四、其他進度](#4-其他進度)

# 一、資料集介紹 <a name="1-資料集介紹"></a>
**＊本資料集(DataSet_Rotation_submean_Normaliation_f6.csv)為2023年4月17日下午14時16分<br>
　開始採集採集時間為26分鐘，取樣頻率1秒6筆，共計5516筆資料(此資料集已做過校正)。<br><br>
＊動作元素分4群資料集(DataSet_Rotation_submean_Normaliation_f6_4cluster.csv)<br><br>
＊動作元素分5群資料集(DataSet_Rotation_submean_Normaliation_f6_5cluster.csv)<br><br>
＊動作元素分8群資料集(DataSet_Rotation_submean_Normaliation_f6_8cluster.csv)**<br><br>

## 1.1 取樣路線 <a name="11-取樣路線"></a>
**採集路線的GPS詳細資訊可見檔案20230417_GPS.csv，該檔案包含經度、緯度、海拔、時間戳以及速度等資訊。**<br>
## 1.2 取樣時間 <a name="12-取樣時間"></a>
**採集時間為14:16非尖峰時刻，如圖所示。**<br><br>
![](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/blob/main/Data_Set/20230417_DataSet/Off-peak%20time%20on%20the%20afternoon%20of%20April%2017th.jpg?raw=true)
## 1.3 取樣設備 <a name="13-取樣設備"></a>
**本次採集使用的設備為平板，其放置位置如圖所示。**<br><br>
![](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/blob/main/Data_Set/20230417_DataSet/Place_The_Luggage_In_The_Trunk.jpg?raw=true)

# 二、Semi-automatic labeling <a name="2-semi-automatic-labeling"></a>

## 2.1 Silhouette Score <a name="#21-silhouette-score"></a>
  **The best value is 1 and the worst value is -1. Values near 0 indicate overlapping clusters. Negative values generally indicate that a sample has been assigned to the wrong cluster, as a different cluster is more similar.**

![Silhouette score - 畫圈](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/afcc1f3e-f824-447e-9257-8e3919623fe3)

## 2.2 Calinski-Harabasz Index <a name="#22-calinski-harabasz-index"></a>
  **The score is higher when clusters are dense and well separated, which relates to a standard concept of a cluster.**

![Calinski-Harabasz Index - 畫圈](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/29c08450-cc52-42c7-9642-2954df6d68bf)


             
## 2.3 Davies-Bouldin Index <a name="#23-davies-bouldin-index"></a>
  **This index signifies the average ‘similarity’ between clusters, where the similarity is a measure that compares the distance between clusters with the size of the clusters themselves.
  Zero is the lowest possible score. Values closer to zero indicate a better partition.**

![Davies-Bouldin score - 畫圖](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/f4bfd34e-d380-4072-bed3-d1b9fc895c8c)


## 2.4 Elbow Method <a name="#24-elbow-method"></a>
![Elbow Method](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/14b6d796-273c-4fd6-8501-d99fd17661fc)





# 三、動作元素個數與VOMM建模預測 <a name="3-動作元素個數與VOMM建模預測"></a> 

**參考演算法 - VOMM (Variable Order Markov Models)** <br>
**該演算法的實現參考了[rpgomez/vomm](https://github.com/rpgomez/vomm)項目。** <br>
**感謝[rpgomez](https://github.com/rpgomez)的貢獻和開源精神！可拜訪該項目的GitHub頁面以獲取更多關於VOMM算法的詳細信息和代碼實現。** <br>

[訓練輸入與測試輸入請參考 VOMM_Input.txt]()


## 3.1 輸入4段序列動作資料進行訓練<a name="31-輸入4段序列動作資料進行訓練"></a>


### 3.1.1 動作元素4群探討 <a name="311-動作元素4群"></a>
| Model\Action   |   Go Straight Model |   Idle Model |   Turn Left Model |   Turn Right Model |   Two-Stage Left Model |   U-turn Model |
|:--------------:|:-------------------:|:------------:|:-----------------:|:------------------:|:----------------------:|:--------------:|
| Go Straight    |    **-20.05**           |       -22.21 |            -28.76 |             -22.47 |                 -22.11 |         -29.45 |
| Idle           |              -92.73 |     **-88.52**   |           -105.47 |             -92.05 |                -104    |        -114.46 |
| Turn Left      |              -17.32 |       -17.9  |            **-15.32** |             -18.98 |                 -23.41 |         -24.25 |
| Turn Right     |              -18.14 |       -17.98 |            -16.32 |            **-13.57** |                 -21.24 |         -18.31 |
| Two-Stage Left |              -57.87 |       -49.5  |            -43.74 |             -50.73 |                 **-25.53** |         -30.67 |
| U-turn         |              -57.72 |       -48.73 |            -43.8  |             -47.71 |                 -16.02 |         **-12.63** |
### 3.1.2 動作元素8群探討 <a name="312-動作元素8群"></a>
| Model\Action   |   Go Straight Model |   Idle Model |   Turn Left Model |   Turn Right Model |   Two-Stage Left Model |   U-turn Model |
|:--------------:|:-------------------:|:------------:|:-----------------:|:------------------:|:----------------------:|:--------------:|
| Go Straight    |              **-23.63** |       -28.73 |            -30.61 |             -27.55 |                 -26.98 |         -26.02 |
| Idle           |             -100.9  |      -166.86 |           -119.82 |            -119.71 |                **-97.71** |        -133.69 |
| Turn Left      |              -26.94 |       -28.43 |            -26.13 |             -27.88 |                 -30.17 |         **-25.32** |
| Turn Right     |              -24.96 |       -19.25 |            **-17.92** |             -18.57 |                 -25.26 |         -19.27 |
| Two-Stage Left |              -66.58 |       -63.92 |            -57.76 |             -58.03 |                 **-27.13** |         -63.06 |
| U-turn         |              -37.29 |       -33.88 |            -29.78 |             -38.49 |                 -33.49 |         **-18.01** |
### 3.1.3 動作元素10群探討 <a name="313-動作元素10群"></a>
| Model\Action   |   Go Straight Model |   Idle Model |   Turn Left Model |   Turn Right Model |   Two-Stage Left Model |   U-turn Model |
|:--------------:|:-------------------:|:------------:|:-----------------:|:------------------:|:----------------------:|:--------------:|
| Go Straight    |              **-33.97** |       -46    |            -38.95 |             -40.35 |                 -36.2  |         -49.81 |
| Idle           |             **-134.29** |      -177.38 |           -197.77 |            -203.78 |                -160.65 |        -212.08 |
| Turn Left      |              -43.15 |       **-34.11** |            -36.16 |             -38.73 |                 -44.93 |         -40.56 |
| Turn Right     |              -36.12 |       -33.1  |            **-32.1**  |             -32.62 |                 -38.47 |         -39.41 |
| Two-Stage Left |              -76.11 |       -68.34 |            -73.21 |             -73.05 |                 **-41.88** |         -46.66 |
| U-turn         |              -73.71 |       -60.91 |            -63.99 |             -64.36 |                 **-22.69** |         -24.47 |




## 3.2 輸入8段序列動作資料進行訓練<a name="32-輸入8段序列動作資料進行訓練"></a>

### 3.2.1 動作元素4群探討 <a name="321-動作元素4群"></a>
| Model\Action   |   Go Straight Model |   Idle Model |   Turn Left Model |   Turn Right Model |   Two-Stage Left Model |   U-turn Model |
|:--------------:|:-------------------:|:------------:|:-----------------:|:------------------:|:----------------------:|:--------------:|
| Go Straight    |              -14.51 |       -13.26 |            -15.5  |             **-12.03** |                 -15.56 |         -15.55 |
| Idle           |              **-83**    |       -91.08 |            -93.24 |             -89.12 |                 -95.15 |        -103.21 |
| Turn Left      |              -19.54 |       -21.81 |            **-19.52** |             -19.85 |                 -27.4  |         -23.19 |
| Turn Right     |              -19.71 |       -21.94 |            -21.86 |             -21.22 |                 **-14.71** |         -20.98 |
| Two-Stage Left |              -25.72 |       -47.97 |            -46.11 |             -46.65 |                 **-24.54** |         -27    |
| U-turn         |              -28.33 |       -56.16 |            -51.74 |             -56.22 |                 -19.85 |         **-17.98** |
### 3.2.2 動作元素8群探討 <a name="322-動作元素8群"></a>
| Model\Action   |   Go Straight Model |   Idle Model |   Turn Left Model |   Turn Right Model |   Two-Stage Left Model |   U-turn Model |
|:--------------:|:-------------------:|:------------:|:-----------------:|:------------------:|:----------------------:|:--------------:|
| Go Straight    |              -23.39 |       **-18.39** |            -23.09 |             -23.58 |                 -22.35 |         -21.97 |
| Idle           |             **-103.33** |      -190.84 |           -173.43 |            -164.64 |                -132.97 |        -169.27 |
| Turn Left      |              -34.65 |       -35.91 |            -36.28 |             **-32.5**  |                 -35.6  |         -48.4  |
| Turn Right     |              -38.55 |       -33.63 |            -35.23 |             **-30.15** |                 -42.85 |         -41.29 |
| Two-Stage Left |              -44.91 |       -63.12 |            -64.84 |             -62.83 |                 **-32.23** |         -37.15 |
| U-turn         |              -36.54 |       -62.09 |            -64.86 |             -65.15 |                 **-21.79** |         -24.41 |
### 3.2.3 動作元素10群探討 <a name="323-動作元素10群"></a>
| Model\Action   |   Go Straight Model |   Idle Model |   Turn Left Model |   Turn Right Model |   Two-Stage Left Model |   U-turn Model |
|:--------------:|:-------------------:|:------------:|:-----------------:|:------------------:|:----------------------:|:--------------:|
| Go Straight    |              -27.75 |       **-18.7**  |            -22.16 |             -21.21 |                 -28.46 |         -26.66 |
| Idle           |             **-124.19** |      -183.94 |           -231.74 |            -195.43 |                -158.03 |        -206.77 |
| Turn Left      |              -43.3  |       -37.53 |            -43.38 |             -42.51 |                 **-36.51** |         -58.97 |
| Turn Right     |              -42.21 |       -41.3  |            **-39.77** |             -40.74 |                 -42.95 |         -45.34 |
| Two-Stage Left |              -53.77 |       -62.82 |            -76.38 |             -68.61 |                 -46.76 |         **-46.35** |
| U-turn         |              -39.83 |       -64.48 |            -65.9  |             -65.79 |                 **-20.94** |         -24.47 |



## 3.3 觀察小結 <a name="33-觀察小結"></a>
**觀察使用6種動作模型預測，是否能準確預測成功**<br><br>
**符合分群演算法驗證效果，分成4群效果最佳**<br><br>

| Accuracy\Number   |   4 cluster |   8 cluster |   10 cluster |
|:--------------:|:-------------------:|:------------:|:-----------------:|
| 訓練 Data 4筆   | 100%  (6/6)| 50% (3/6)| 50% (3/6)|
| 訓練 Data 8筆   |  50% (3/6)| 33% (2/6)| 0% (0/6)|

**也觀察出輸入訓練Data越多，準確度也會開始下降**




# 四、其他進度 <a name="4-其他進度"></a> 

- 分群輸入自動化並轉呈markdown
- Attention-Based Deep Learning Framework for Human Activity Recognition With User Adaptation 環境建立
- 書報討論準備











<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
