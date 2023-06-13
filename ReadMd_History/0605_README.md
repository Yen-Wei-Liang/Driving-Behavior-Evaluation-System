# 目錄
* [一、資料集介紹 ](#1-資料集介紹)
  * [1.1 採集路線](#1.1-採集路線) 
  * [1.2 採集時間](#1.2-採集時間) 
  * [1.3 採集設備](#1.3-採集設備)  
* [二、使用K-means將動作分群為動作元素](#2-使用K-means將動作分群為動作元素)
  * [2.1 探討K-means最佳分群數](#2.1-探討K-means最佳分群數)  
    * [2.1.1 Silhouette Score](#2.1.1-silhouettescore) 
    * [2.1.2 Calinski-Harabasz Index](#2.1.2-calinskiharabaszindex) 
    * [2.1.3 Davies-Bouldin Index](#2.1.3-daviesbouldinindex) 
    * [2.1.4 Elbow Method](#2.1.4-elbowmethod) 
* [三、六種駕駛行為與九軸特徵關係 ](#3-六種駕駛行為與九軸特徵關係)
* [四、各行為九軸特徵比較](#4-各行為九軸特徵比較)
  * [4.1 不相似動作比較](#4.1-不相似動作比較)  
    * [4.1.1 右轉vs左轉](#4.1.1-右轉vs左轉)
    * [4.1.2 右轉vs迴轉](#4.1.2-右轉vs迴轉)
    * [4.1.3 右轉vs待轉](#4.1.3-右轉vs待轉)
  * [4.2 相似動作比較](#4.2-相似動作比較)  
    * [4.2.1 左轉vs迴轉](#4.2.1-左轉vs迴轉)
    * [4.2.2 左轉vs待轉](#4.2.2-左轉vs待轉)
    * [4.2.3 直線vs怠速](#4.2.3-直線vs怠速)
* [五、動作元素個數與VOMM建模預測](#5-動作元素個數與VOMM建模預測)
  * [5.1 輸入4段序列動作資料進行訓練](#5.1-輸入4段序列動作資料進行訓練)
    * [5.1.1 動作元素4群探討](#5.1.1-動作元素4群探討)
    * [5.1.2 動作元素8群探討](#5.1.2-動作元素8群探討)
    * [5.1.3 動作元素10群探討](#5.1.3-動作元素10群探討)
  * [5.2 訓練輸入該動作8段序列資料](#5.2-訓練輸入該動作8段序列資料)
    * [5.2.1 動作元素4群探討](#5.2.1-動作元素4群探討)
    * [5.2.2 動作元素8群探討](#5.2.2-動作元素8群探討)
    * [5.2.3 動作元素10群探討](#5.2.3-動作元素10群探討)
  * [5.3 預測序列資料](#5.3-預測序列資料)
    * [5.3.1 動作元素4群預測](#5.3.1-動作元素4群預測)
    * [5.3.2 自動標記預測](#5.3.2-自動標記預測)
      * [5.3.2.1 觀察序列(怠速-待轉-怠速(無轉換時間))](#5.3.2.1-觀察序列(怠速-待轉-怠速(無轉換時間)))
      * [5.3.2.3 觀察序列(迴轉-左轉-怠速(轉換時間))](#5.3.2.2-觀察序列(迴轉-左轉-怠速(轉換時間)))






















 
 
# 一、資料集介紹 <a name="1-資料集介紹"></a>
本資料集為2023年4月17日下午14時16分開始採集，採集時間為26分鐘，共計27578筆資料(此資料集以做過正規化)。
## 1.1 採集路線 <a name="1.1-採集路線"></a>
採集路線的GPS詳細資訊可見檔案20230417_GPS.csv，該檔案包含經度、緯度、海拔、時間戳以及速度等資訊。
## 1.2 採集時間 <a name="1.2-採集時間"></a>
採集時間為14:16非尖峰時刻，如圖所示。
![採集資料集當下車流_2](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/d3aad80a-8e1b-4196-9e75-2e78e66bd810)
## 1.3 採集設備 <a name="1.3-採集設備"></a>
本次採集使用的設備為平板，其放置位置如圖所示。
![Place_The_Luggage_In_The_Trunk](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/7095f3ae-fc1a-4817-ab4c-79eaf80b2555)





# 二、使用K-means將動作分群為動作元素 <a name="2-使用K-means將動作分群為動作元素"></a>
## 2.1 探討K-means最佳分群數 <a name="2.1-探討K-means最佳分群數"></a>
### 2.1.1 Silhouette Score <a name="2.1.1-silhouettescore"></a>
  The best value is 1 and the worst value is -1. Values near 0 indicate overlapping clusters. Negative values generally indicate that a sample has been assigned to the wrong cluster, as a different cluster is more similar.
![Silhouette score - 畫圈](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/56795e12-8936-4300-b8e4-01b402d9aa06)
### 2.1.2 Calinski-Harabasz Index <a name="2.1.2-calinskiharabaszindex"></a>
  The score is higher when clusters are dense and well separated, which relates to a standard concept of a cluster.
![Calinski-Harabasz Index - 畫圈](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/84f98164-0c61-491a-8d0a-63e3127b5962)
### 2.1.3 Davies-Bouldin Index <a name="2.1.3-daviesbouldinindex"></a>
  This index signifies the average ‘similarity’ between clusters, where the similarity is a measure that compares the distance between clusters with the size of the clusters themselves.
  Zero is the lowest possible score. Values closer to zero indicate a better partition.
![Davies-Bouldin score - 畫圖](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/0cb0cae0-1a29-48a7-a789-a082489e2e73)
### 2.1.4 Elbow Method <a name="2.1.4-elbowmethod"></a>
![Elbow Method](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/47677bfb-3615-4cd9-ac97-4b9d8542e572)

     
     
     
     
     
# 三、六種駕駛行為與九軸特徵關係 <a name="3-六種駕駛行為與九軸特徵關係"></a>


| X角速度 | Y角速度 |Z角速度|
| :-: | :-: | :-: |
| ![Relationship Between X-Axis Angular Velocity and 6 Driving Behaviors（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/fb03f7d3-2bf6-457f-b374-db393bf4eb37)|![Relationship Between Y-Axis Angular Velocity and 6 Driving Behaviors（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/59660a9b-72f8-4d73-9b1e-b62594c965fd)| ![Relationship Between Z-Axis Angular Velocity and 6 Driving Behaviors（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/34b3ac78-c286-49b5-8456-3302c58990f5)|
|X加速度  |Y加速度 | Z加速度 |
| ![Relationship Between X-axis Acceleration and 6 Driving Behaviors（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/f8cb2394-2992-4a6a-a03f-763cd25f82ec)|![Relationship Between Y-axis Acceleration and 6 Driving Behaviors（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/de0439a4-7b78-4253-bc32-97294f7f1a1a)| ![Relationship Between Z-axis Acceleration and 6 Driving Behaviors（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/4fb17a86-0d99-4a35-a7ac-34559bd97b4f)|
| X角度 | Y角度| Z角度 |
| ![Relationship Between X-axis Angle and 6 Driving Behaviors（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/b3fefc1e-246f-4dc0-a245-2e5a9500f0a8)|![Relationship Between Y-axis Angle and 6 Driving Behaviors（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/4ab884e7-6de8-4fae-9d48-6682ebb921e3)| ![Relationship Between Z-axis Angle and 6 Driving Behaviors（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/82d25635-566d-4916-91f6-93d46a8505a2)|



# 四、各行為九軸特徵比較 <a name="4-各行為九軸特徵比較"></a>
## 4.1 不相似動作比較 <a name="4.1-不相似動作比較"></a>
### 4.1.1 右轉vs左轉 <a name="4.1.1-右轉vs左轉"></a>

| X角速度 | Y角速度 |Z角速度|
| :-: | :-: | :-: |
| ![X-axis Angular Velocity Turn right vs Turn left（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/549e3b79-75bc-4e94-ad91-e0a411c5505e)|![Y-axis Angular Velocity Turn right vs Turn left（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/7face7e0-c121-4e80-ac24-7ae97f19a11e)| ![Z-axis Angular Velocity Turn right vs Turn left（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/a31971d3-7780-4877-9cac-99efd3c081da)|
|X加速度  |Y加速度 | Z加速度 |
|![X-axis Acceleration Turn right vs Turn left（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/b85c90fe-29b1-417c-ae61-a9961ff54ee4) |![Y-axis Acceleration Turn right vs Turn left（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/9b49c554-0ed5-494c-a13b-e0028bae5d19)| ![Z-axis Acceleration Turn right vs Turn left（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/8f63fc6e-a588-40d3-afb6-a010a929257f)|
| X角度 | Y角度| Z角度 |
| ![X-axis Angle Turn right vs Turn left（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/4e5aed44-9832-44f9-89d7-92ba22f9cd41)|![Y-axis Angle Turn right vs Turn left（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/3fb4d2c3-456f-4a93-b026-3365c24da1d9)| ![Z-axis Angle Turn right vs Turn left（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/318b05d4-6677-4900-bbe7-f4e56c2ff03d)|



### 4.1.2 右轉vs迴轉 <a name="4.1.2-右轉vs迴轉"></a>

| X角速度 | Y角速度 |Z角速度|
| :-: | :-: | :-: |
|![X-axis Angular Velocity Turn right vs U-turn（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/22b51367-0a1c-4a1a-a9a2-27ebe4d4c15b)|![Y-axis Angular Velocity Turn right vs U-turn（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/dc5269a0-9c01-4f12-8270-54f4e150a7ee)| ![Z-axis Angular Velocity Turn right vs U-turn（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/5f0a66fe-2773-456b-b51e-7e8d8bffbba8)|
|X加速度  |Y加速度 | Z加速度 |
|![X-axis Acceleration Turn right vs U-turn（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/ec46a6bf-9912-41e8-8897-5876e8720cf4)|![Y-axis Acceleration Turn right vs U-turn（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/39935ce3-9e89-48b0-8739-69b852874fbc)|![Z-axis Acceleration Turn right vs U-turn（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/ab915f13-9243-42d9-9dbe-3139d2aef392)|
| X角度 | Y角度| Z角度 |
|![X-axis Angle Turn right vs U-turn（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/798b4b06-ae41-45ba-a833-067f8df43074)|![Y-axis Angle Turn right vs U-turn（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/65f637fa-1731-4052-a452-729a0cbe65ce)| ![Z-axis Angle Turn right vs U-turn（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/4ea19ccb-0930-4e04-82da-cf43f2df685e)|



### 4.1.3 右轉vs待轉 <a name="4.1.3-右轉vs待轉"></a>
| X角速度 | Y角速度 |Z角速度|
| :-: | :-: | :-: |
|![X-axis Angular Velocity Turn right vs Two-stage left turn（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/4b625021-eb3a-4c90-bacb-5dfd54ca3e5c)|![Y-axis Angular Velocity Turn right vs Two-stage left turn（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/a5dbfb0f-702b-4e90-a560-0c4b06e3c18c)| ![Z-axis Angular Velocity Turn right vs Two-stage left turn（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/7e047fcc-282c-479f-97c5-50afe048cc91)|
|X加速度  |Y加速度 | Z加速度 |
|![X-axis Acceleration Turn right vs Two-stage left turn（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/d3b65cbd-2a91-41c9-8046-fbe3b6cd8cdf)|![Y-axis Acceleration Turn right vs Two-stage left turn（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/3cb30910-d6e7-4e25-86f7-228a6c740bf4)|![Z-axis Acceleration Turn right vs Two-stage left turn（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/da52f567-fb70-488f-a800-b17fbf802f25)|
| X角度 | Y角度| Z角度 |
|![X-axis Angle Turn right vs Two-stage left turn（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/aaef7260-e886-404a-b241-d98cf16c0d12)|![Y-axis Angle Turn right vs Two-stage left turn（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/40185652-bcc8-48eb-93ee-c6fbb968eba2)| ![Z-axis Angle Turn right vs Two-stage left turn（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/b15bbbe7-650b-41bd-bdc0-5ff6e76342b1)|








## 4.2 相似動作比較 <a name="4.2-相似動作比較"></a>
### 4.2.1 左轉vs迴轉 <a name="4.2.1-左轉vs迴轉"></a>
| X角速度 | Y角速度 |Z角速度|
| :-: | :-: | :-: |
|![X-axis Angular Velocity Turn left vs U-turn（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/249ab429-4751-4950-88de-8b32892660a4)|![Y-axis Angular Velocity Turn left vs U-turn（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/23aa7bfa-ff8a-4843-9e01-49fce1f55140)|![Z-axis Angular Velocity Turn left vs U-turn（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/5b540d54-9e7c-4f99-a0f6-b127df80ffa2)|
|X加速度  |Y加速度 | Z加速度 |
|![X-axis Acceleration Turn left vs U-turn（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/663e0b73-278f-4b39-a384-3db0f5aae74b)|![Y-axis Acceleration Turn left vs U-turn（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/a75598de-5953-4633-a881-64ca03e9ee78)|![Z-axis Acceleration Turn left vs U-turn（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/7fa65655-4f61-4b11-b144-b63ab4b2b1e7)|
| X角度 | Y角度| Z角度 |
|![X-axis Angle Turn left vs U-turn（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/10d7db58-5365-4382-8443-6e2d462587ed)|![Y-axis Angle Turn left vs U-turn（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/cc9ca078-0415-4e10-8bd5-cdc3f53cf51c)|![Z-axis Angle Turn left vs U-turn（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/30cdf932-9c8a-4ab3-8eac-968f0760230f)|
### 4.2.2 左轉vs待轉 <a name="4.2.2-左轉vs待轉"></a>
| X角速度 | Y角速度 |Z角速度|
| :-: | :-: | :-: |
|![X-axis Angular Velocity Turn left vs Two-stage left turn（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/f43b853d-e6ee-4b7d-aa0f-bc8fe80d9a22)|![Y-axis Angular Velocity Turn left vs Two-stage left turn（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/57068531-42bf-44a7-919d-16e9b31c1a4d)|![Z-axis Angular Velocity Turn left vs Two-stage left turn（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/09c73a36-211f-4dd5-9597-de1f357cae00)|
|X加速度  |Y加速度 | Z加速度 |
|![X-axis Acceleration Turn left vs Two-stage left turn（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/cd2f22d4-2c58-4216-9a00-9ef3cb31cdad)|![Y-axis Acceleration Turn left vs Two-stage left turn（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/4e33109b-94db-4b09-932b-5d0197d11f57)|![Z-axis Acceleration Turn left vs Two-stage left turn（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/1c2d3f96-f88f-4b02-ac46-d1eb45a2c35a)|
| X角度 | Y角度| Z角度 |
|![X-axis Angle Turn left vs Two-stage left turn（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/d4cb1844-9ac8-45f8-9e2f-6599299da933)|![Y-axis Angle Turn left vs Two-stage left turn（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/401894a7-ed31-44fb-97de-1e0025a94069)|![Z-axis Angle Turn left vs Two-stage left turn（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/ac6b1c38-98cb-40bf-b378-75b2c829426c)|
### 4.2.3 直線vs怠速 <a name="4.2.3-直線vs怠速"></a>
| X角速度 | Y角速度 |Z角速度|
| :-: | :-: | :-: |
|![X-axis Angular Velocity Go straight vs Idle（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/a0043f29-687d-45a3-8719-424f107e600e)|![Y-axis Angular Velocity Go straight vs Idle（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/fa58832e-8884-405f-9c7e-73365d7fbe87)|![Z-axis Angular Velocity Go straight vs Idle（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/5738b785-f8b8-4cba-883b-82119293f4c6)|
|X加速度  |Y加速度 | Z加速度 |
|![X-axis Acceleration Go straight vs Idle（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/9e1eb967-ab40-4e1e-9823-07b9a64d93e5)|![Y-axis Acceleration Go straight vs Idle（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/c9891fe2-6b32-458e-8305-464c486ad3ea)|![Z-axis Acceleration Go straight vs Idle（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/d0db754b-cdcd-4c51-81be-a1d16b5a064b)|
| X角度 | Y角度| Z角度 |
|![X-axis Angle Go straight vs Idle（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/2ea3dbc2-149b-4a78-8446-776af70effcb)|![Y-axis Angle Go straight vs Idle（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/4e984626-4db8-4205-8d90-9cdb94fc7b41)|![Z-axis Angle Go straight vs Idle（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/afc750c5-09fa-4ea1-a8cd-e15f0403d461)|




# 五、動作元素個數與VOMM建模預測 <a name="5-動作元素個數與VOMM建模預測"></a> 

**參考演算法 - VOMM (Variable Order Markov Models)** <br>
**該演算法的實現參考了[rpgomez/vomm](https://github.com/rpgomez/vomm)項目。** <br>
**感謝[rpgomez](https://github.com/rpgomez)的貢獻和開源精神！可拜訪該項目的GitHub頁面以獲取更多關於VOMM算法的詳細信息和代碼實現。** <br>

[訓練輸入與測試輸入請參考 VOMM_Input.txt]()


## 5.1 輸入4段序列動作資料進行訓練<a name="5.1-輸入4段序列動作資料進行訓練"></a>


### 5.1.1 動作元素4群探討 <a name="5.1.1-動作元素4群探討"></a>
| Model\Action   |   Go Straight Model |   Idle Model |   Turn Left Model |   Turn Right Model |   Two-Stage Left Model |   U-turn Model |
|:--------------:|:-------------------:|:------------:|:-----------------:|:------------------:|:----------------------:|:--------------:|
| Go Straight    |    **-20.05**           |       -22.21 |            -28.76 |             -22.47 |                 -22.11 |         -29.45 |
| Idle           |              -92.73 |     **-88.52**   |           -105.47 |             -92.05 |                -104    |        -114.46 |
| Turn Left      |              -17.32 |       -17.9  |            **-15.32** |             -18.98 |                 -23.41 |         -24.25 |
| Turn Right     |              -18.14 |       -17.98 |            -16.32 |            **-13.57** |                 -21.24 |         -18.31 |
| Two-Stage Left |              -57.87 |       -49.5  |            -43.74 |             -50.73 |                 **-25.53** |         -30.67 |
| U-turn         |              -57.72 |       -48.73 |            -43.8  |             -47.71 |                 -16.02 |         **-12.63** |
### 5.1.2 動作元素8群探討 <a name="5.1.2-動作元素8群探討"></a>
| Model\Action   |   Go Straight Model |   Idle Model |   Turn Left Model |   Turn Right Model |   Two-Stage Left Model |   U-turn Model |
|:--------------:|:-------------------:|:------------:|:-----------------:|:------------------:|:----------------------:|:--------------:|
| Go Straight    |              **-23.63** |       -28.73 |            -30.61 |             -27.55 |                 -26.98 |         -26.02 |
| Idle           |             -100.9  |      -166.86 |           -119.82 |            -119.71 |                **-97.71** |        -133.69 |
| Turn Left      |              -26.94 |       -28.43 |            -26.13 |             -27.88 |                 -30.17 |         **-25.32** |
| Turn Right     |              -24.96 |       -19.25 |            **-17.92** |             -18.57 |                 -25.26 |         -19.27 |
| Two-Stage Left |              -66.58 |       -63.92 |            -57.76 |             -58.03 |                 **-27.13** |         -63.06 |
| U-turn         |              -37.29 |       -33.88 |            -29.78 |             -38.49 |                 -33.49 |         **-18.01** |
### 5.1.3 動作元素10群探討 <a name="5.1.3-動作元素10群探討"></a>
| Model\Action   |   Go Straight Model |   Idle Model |   Turn Left Model |   Turn Right Model |   Two-Stage Left Model |   U-turn Model |
|:--------------:|:-------------------:|:------------:|:-----------------:|:------------------:|:----------------------:|:--------------:|
| Go Straight    |              **-33.97** |       -46    |            -38.95 |             -40.35 |                 -36.2  |         -49.81 |
| Idle           |             **-134.29** |      -177.38 |           -197.77 |            -203.78 |                -160.65 |        -212.08 |
| Turn Left      |              -43.15 |       **-34.11** |            -36.16 |             -38.73 |                 -44.93 |         -40.56 |
| Turn Right     |              -36.12 |       -33.1  |            **-32.1**  |             -32.62 |                 -38.47 |         -39.41 |
| Two-Stage Left |              -76.11 |       -68.34 |            -73.21 |             -73.05 |                 **-41.88** |         -46.66 |
| U-turn         |              -73.71 |       -60.91 |            -63.99 |             -64.36 |                 **-22.69** |         -24.47 |




## 5.2 輸入8段序列動作資料進行訓練<a name="5.2-訓練輸入該動作8段序列資料"></a>

### 5.2.1 動作元素4群探討 <a name="5.2.1-動作元素4群探討"></a>
| Model\Action   |   Go Straight Model |   Idle Model |   Turn Left Model |   Turn Right Model |   Two-Stage Left Model |   U-turn Model |
|:--------------:|:-------------------:|:------------:|:-----------------:|:------------------:|:----------------------:|:--------------:|
| Go Straight    |              -14.51 |       -13.26 |            -15.5  |             **-12.03** |                 -15.56 |         -15.55 |
| Idle           |              **-83**    |       -91.08 |            -93.24 |             -89.12 |                 -95.15 |        -103.21 |
| Turn Left      |              -19.54 |       -21.81 |            **-19.52** |             -19.85 |                 -27.4  |         -23.19 |
| Turn Right     |              -19.71 |       -21.94 |            -21.86 |             -21.22 |                 **-14.71** |         -20.98 |
| Two-Stage Left |              -25.72 |       -47.97 |            -46.11 |             -46.65 |                 **-24.54** |         -27    |
| U-turn         |              -28.33 |       -56.16 |            -51.74 |             -56.22 |                 -19.85 |         **-17.98** |
### 5.2.2 動作元素8群探討 <a name="5.2.2-動作元素8群探討"></a>
| Model\Action   |   Go Straight Model |   Idle Model |   Turn Left Model |   Turn Right Model |   Two-Stage Left Model |   U-turn Model |
|:--------------:|:-------------------:|:------------:|:-----------------:|:------------------:|:----------------------:|:--------------:|
| Go Straight    |              -23.39 |       **-18.39** |            -23.09 |             -23.58 |                 -22.35 |         -21.97 |
| Idle           |             **-103.33** |      -190.84 |           -173.43 |            -164.64 |                -132.97 |        -169.27 |
| Turn Left      |              -34.65 |       -35.91 |            -36.28 |             **-32.5**  |                 -35.6  |         -48.4  |
| Turn Right     |              -38.55 |       -33.63 |            -35.23 |             **-30.15** |                 -42.85 |         -41.29 |
| Two-Stage Left |              -44.91 |       -63.12 |            -64.84 |             -62.83 |                 **-32.23** |         -37.15 |
| U-turn         |              -36.54 |       -62.09 |            -64.86 |             -65.15 |                 **-21.79** |         -24.41 |
### 5.2.3 動作元素10群探討 <a name="5.2.3-動作元素10群探討"></a>
| Model\Action   |   Go Straight Model |   Idle Model |   Turn Left Model |   Turn Right Model |   Two-Stage Left Model |   U-turn Model |
|:--------------:|:-------------------:|:------------:|:-----------------:|:------------------:|:----------------------:|:--------------:|
| Go Straight    |              -27.75 |       **-18.7**  |            -22.16 |             -21.21 |                 -28.46 |         -26.66 |
| Idle           |             **-124.19** |      -183.94 |           -231.74 |            -195.43 |                -158.03 |        -206.77 |
| Turn Left      |              -43.3  |       -37.53 |            -43.38 |             -42.51 |                 **-36.51** |         -58.97 |
| Turn Right     |              -42.21 |       -41.3  |            **-39.77** |             -40.74 |                 -42.95 |         -45.34 |
| Two-Stage Left |              -53.77 |       -62.82 |            -76.38 |             -68.61 |                 -46.76 |         **-46.35** |
| U-turn         |              -39.83 |       -64.48 |            -65.9  |             -65.79 |                 **-20.94** |         -24.47 |




## 5.3 預測序列資料 <a name="5.3-預測序列資料"></a>

### 5.3.1 動作元素4群預測 <a name="5.3.1-動作元素4群預測"></a>

| Label \Time step   |   6 |   12 |   18 |   24 |   30 | 
|:--------------:|:-------------------:|:------------:|:-----------------:|:------------------:|:------------------:|
| Go Straight    |       21 %        |  **34 %**   |      32 %      |     23 %        |18 %|
| Idle           |       **45 %**       |  37 %    |      33 %      |     30 %        | 28 %|
| Turn Left      |       36 %       |  **40 %**     |      26 %       |       25 %       |28 %|
| Turn Right     |       52 %       |   72 %      |    70 %        |     78 %         |**82 %**|
| Two-Stage Left |      36 %        |   **44%**     |     39%        |      38 %        |37 %|
| U-turn         |     **54 %**         |   32 %     |     29 %         |     22 %         |  20 % |



      
### 5.3.2 自動標記預測 <a name="5.3.2-自動標記預測"></a>



#### 5.3.2.1 觀察序列(怠速-待轉-怠速(無轉換時間)) <a name="5.3.2.1-觀察序列(怠速-待轉-怠速(無轉換時間))"></a>


| Action         | Predict 6      | Predict 12     | Predict 18     | Predict 24     | Predict 30     |
|:---------------|:---------------|:---------------|:---------------|:---------------|:---------------|
| Idle           | Turn Left      | Idle           | Idle           | Idle           | Idle           |
| Idle           | Turn Right     | Idle           | Two-Stage Left | Idle           | Idle           |
| Idle           | Turn Right     | Idle           | Idle           | Idle           | Idle           |
| Idle           | Turn Right     | Idle           | Idle           | Idle           | Idle           |
| Idle           | Turn Right     | Idle           | Idle           | Idle           | Idle           |
| Idle           | Turn Right     | Idle           | Idle           | Idle           | Idle           |
| Idle           | Idle           | Idle           | Idle           | Idle           | Idle           |
| Idle           | Turn Right     | Turn Right     | Idle           | Idle           | Idle           |
| Idle           | Idle           | Idle           | Idle           | Idle           | Idle           |
| Idle           | Turn Left      | Idle           | Idle           | Idle           | Idle           |
| Idle           | Turn Left      | Turn Right     | Idle           | Idle           | Turn Left      |
| Idle           | Turn Left      | U-turn         | Idle           | Idle           | Idle           |
| Idle           | Turn Left      | Turn Left      | Idle           | Idle           | Idle           |
| Idle           | Turn Left      | Turn Left      | Idle           | Idle           | Idle           |
| Idle           | Turn Left      | Idle           | Idle           | Idle           | Idle           |
| Idle           | Idle           | Idle           | Idle           | Idle           | Idle           |
| Idle           | Turn Left      | Idle           | Idle           | Idle           | Idle           |
| Idle           | Two-Stage Left | Idle           | Turn Left      | Idle           | Idle           |
| Idle           | Two-Stage Left | Idle           | Idle           | Idle           | Idle           |
| Idle           | Turn Right     | Turn Left      | Turn Left      | Idle           | Idle           |
| Idle           | Idle           | Turn Left      | Idle           | Idle           | Idle           |
| Idle           | Turn Right     | Turn Left      | Turn Left      | Turn Left      | Idle           |
| Two-Stage Left | Turn Right     | Turn Left      | Turn Left      | Turn Left      | Turn Left      |
| Two-Stage Left | Turn Right     | Turn Left      | Turn Left      | Turn Left      | Turn Left      |
| Two-Stage Left | Two-Stage Left | Two-Stage Left | Turn Left      | Turn Left      | Turn Left      |
| Two-Stage Left | Turn Left      | Turn Right     | Turn Left      | Turn Left      | Turn Left      |
| Two-Stage Left | Turn Right     | Turn Left      | Turn Left      | Turn Left      | Turn Left      |
| Two-Stage Left | Turn Left      | Turn Left      | Turn Left      | Turn Left      | Turn Left      |
| Two-Stage Left | Two-Stage Left | Turn Left      | Turn Left      | Two-Stage Left | U-turn         |
| Two-Stage Left | Turn Left      | Turn Left      | Turn Left      | Turn Left      | Turn Left      |
| Two-Stage Left | Two-Stage Left | Turn Left      | Turn Left      | Turn Left      | Turn Left      |
| Two-Stage Left | Two-Stage Left | Two-Stage Left | Two-Stage Left | Turn Left      | Turn Left      |
| Two-Stage Left | Go Straight    | Two-Stage Left | Turn Left      | Turn Left      | Turn Left      |
| Two-Stage Left | Go Straight    | Turn Left      | Turn Left      | Turn Left      | Two-Stage Left |
| Two-Stage Left | Go Straight    | Two-Stage Left | Two-Stage Left | Turn Left      | Two-Stage Left |
| Two-Stage Left | Turn Right     | Two-Stage Left | Two-Stage Left | Two-Stage Left | Two-Stage Left |
| Two-Stage Left | Two-Stage Left | Two-Stage Left | Two-Stage Left | Two-Stage Left | Two-Stage Left |
| Two-Stage Left | Turn Right     | Two-Stage Left | Two-Stage Left | Two-Stage Left | Two-Stage Left |
| Two-Stage Left | Idle           | Two-Stage Left | Two-Stage Left | Two-Stage Left | Two-Stage Left |
| Two-Stage Left | Two-Stage Left | Two-Stage Left | Two-Stage Left | Two-Stage Left | Two-Stage Left |
| Two-Stage Left | Two-Stage Left | U-turn         | Two-Stage Left | Two-Stage Left | Two-Stage Left |
| Two-Stage Left | Two-Stage Left | Two-Stage Left | Two-Stage Left | Two-Stage Left | Two-Stage Left |
| Two-Stage Left | Two-Stage Left | Two-Stage Left | Two-Stage Left | Two-Stage Left | Two-Stage Left |
| Two-Stage Left | Two-Stage Left | Two-Stage Left | Two-Stage Left | Two-Stage Left | Two-Stage Left |
| Idle           | Two-Stage Left | Two-Stage Left | Two-Stage Left | Two-Stage Left | Two-Stage Left |
| Idle           | Two-Stage Left | Two-Stage Left | Two-Stage Left | Two-Stage Left | Two-Stage Left |
| Idle           | Two-Stage Left | Two-Stage Left | Two-Stage Left | Two-Stage Left | Two-Stage Left |
| Idle           | Two-Stage Left | Two-Stage Left | Two-Stage Left | Two-Stage Left | Two-Stage Left |
| Idle           | Two-Stage Left | Two-Stage Left | Two-Stage Left | Two-Stage Left | Two-Stage Left |
| Idle           | Two-Stage Left | Two-Stage Left | Two-Stage Left | Two-Stage Left | Two-Stage Left |
| Idle           | Turn Left      | Two-Stage Left | Two-Stage Left | Two-Stage Left | Two-Stage Left |
| Idle           | Go Straight    | Two-Stage Left | Two-Stage Left | Two-Stage Left | Two-Stage Left |
| Idle           | Turn Right     | Two-Stage Left | Two-Stage Left | Two-Stage Left | Two-Stage Left |
| Idle           | Turn Right     | Two-Stage Left | Two-Stage Left | Two-Stage Left | Two-Stage Left |
| Idle           | Turn Right     | Two-Stage Left | Two-Stage Left | Two-Stage Left | Two-Stage Left |
| Idle           | Turn Right     | Two-Stage Left | Two-Stage Left | Two-Stage Left | Two-Stage Left |
| Idle           | Idle           | Turn Right     | Two-Stage Left | Two-Stage Left | Two-Stage Left |
| Idle           | Idle           | Turn Right     | Two-Stage Left | Two-Stage Left | Two-Stage Left |
| Idle           | Idle           | Turn Right     | Two-Stage Left | Two-Stage Left | Two-Stage Left |
| Idle           | Idle           | Turn Right     | Two-Stage Left | Two-Stage Left | Two-Stage Left |
| Idle           | Idle           | Turn Right     | Two-Stage Left | Two-Stage Left | Two-Stage Left |
| Idle           | Idle           | Go Straight    | Two-Stage Left | Two-Stage Left | Two-Stage Left |
| Idle           | Idle           | Idle           | Go Straight    | Two-Stage Left | Two-Stage Left |
| Idle           | Idle           | Turn Left      | Turn Right     | Two-Stage Left | Two-Stage Left |
| Idle           | Idle           | Turn Left      | Turn Right     | Two-Stage Left | Two-Stage Left |
| Idle           | Turn Right     | Turn Left      | Turn Right     | U-turn         | Two-Stage Left |


#### 5.3.2.3 觀察序列(迴轉-左轉-怠速(轉換時間)) <a name="5.3.2.2-觀察序列(迴轉-左轉-怠速(轉換時間))"></a>

| Action    | Predict 6      | Predict 12     | Predict 18     | Predict 24     | Predict 30     |
|:----------|:---------------|:---------------|:---------------|:---------------|:---------------|
| Idle      | Two-Stage Left | U-turn         | Turn Left      | Turn Left      | Turn Right     |
| U-turn    | Two-Stage Left | Two-Stage Left | U-turn         | Turn Left      | Turn Right     |
| U-turn    | Two-Stage Left | Two-Stage Left | U-turn         | U-turn         | Turn Right     |
| U-turn    | Two-Stage Left | Two-Stage Left | U-turn         | U-turn         | U-turn         |
| U-turn    | U-turn         | Two-Stage Left | U-turn         | U-turn         | U-turn         |
| U-turn    | U-turn         | U-turn         | U-turn         | U-turn         | U-turn         |
| U-turn    | U-turn         | U-turn         | U-turn         | U-turn         | U-turn         |
| U-turn    | U-turn         | U-turn         | U-turn         | U-turn         | U-turn         |
| U-turn    | U-turn         | U-turn         | U-turn         | U-turn         | U-turn         |
| U-turn    | U-turn         | U-turn         | U-turn         | U-turn         | U-turn         |
| U-turn    | U-turn         | U-turn         | U-turn         | U-turn         | U-turn         |
| U-turn    | U-turn         | U-turn         | U-turn         | U-turn         | U-turn         |
| U-turn    | Two-Stage Left | U-turn         | U-turn         | U-turn         | U-turn         |
| U-turn    | U-turn         | U-turn         | U-turn         | U-turn         | U-turn         |
| U-turn    | U-turn         | U-turn         | U-turn         | U-turn         | U-turn         |
| U-turn    | U-turn         | U-turn         | U-turn         | U-turn         | U-turn         |
| U-turn    | U-turn         | U-turn         | U-turn         | U-turn         | U-turn         |
| nan       | U-turn         | U-turn         | U-turn         | U-turn         | U-turn         |
| nan       | Turn Left      | U-turn         | U-turn         | U-turn         | U-turn         |
| nan       | Two-Stage Left | U-turn         | U-turn         | U-turn         | U-turn         |
| nan       | Turn Left      | U-turn         | U-turn         | U-turn         | U-turn         |
| nan       | Two-Stage Left | U-turn         | U-turn         | U-turn         | U-turn         |
| nan       | Turn Left      | Two-Stage Left | U-turn         | U-turn         | U-turn         |
| nan       | Turn Left      | Two-Stage Left | U-turn         | U-turn         | U-turn         |
| nan       | Turn Right     | Turn Left      | U-turn         | U-turn         | U-turn         |
| nan       | Turn Right     | Two-Stage Left | U-turn         | U-turn         | U-turn         |
| nan       | Turn Right     | Two-Stage Left | Two-Stage Left | U-turn         | U-turn         |
| nan       | Turn Right     | Two-Stage Left | Two-Stage Left | U-turn         | U-turn         |
| nan       | Turn Right     | Turn Right     | Two-Stage Left | U-turn         | U-turn         |
| nan       | Turn Right     | Turn Right     | Two-Stage Left | U-turn         | U-turn         |
| nan       | Turn Right     | Turn Right     | Turn Right     | U-turn         | U-turn         |
| nan       | Turn Right     | Turn Right     | Turn Right     | Two-Stage Left | U-turn         |
| nan       | U-turn         | Turn Right     | Turn Right     | Two-Stage Left | U-turn         |
| nan       | U-turn         | Turn Right     | Turn Right     | Two-Stage Left | U-turn         |
| nan       | Turn Right     | Turn Right     | Turn Right     | Two-Stage Left | U-turn         |
| nan       | Idle           | Turn Right     | Turn Right     | Turn Right     | U-turn         |
| nan       | Idle           | Turn Right     | Turn Right     | Turn Right     | U-turn         |
| nan       | Go Straight    | Turn Right     | Turn Right     | Turn Right     | Two-Stage Left |
| nan       | Turn Right     | Turn Right     | Turn Right     | Turn Right     | Two-Stage Left |
| nan       | Turn Right     | Turn Right     | Turn Right     | Turn Right     | Two-Stage Left |
| nan       | Turn Right     | Turn Right     | Turn Right     | Turn Right     | Two-Stage Left |
| nan       | Turn Right     | Idle           | Turn Right     | Turn Right     | Turn Right     |
| nan       | Turn Left      | Idle           | Turn Right     | Turn Right     | Turn Right     |
| nan       | Idle           | Idle           | Turn Right     | Turn Right     | Turn Right     |
| Turn Left | Idle           | Idle           | Turn Right     | Turn Right     | Turn Right     |
| Turn Left | Go Straight    | Idle           | Turn Right     | Turn Right     | Turn Right     |
| Turn Left | Turn Left      | Idle           | Turn Right     | Turn Right     | Turn Right     |
| Turn Left | Go Straight    | Turn Left      | Idle           | Turn Right     | Turn Right     |
| Turn Left | U-turn         | Turn Left      | Idle           | Turn Right     | Turn Right     |
| Turn Left | Turn Right     | Turn Left      | Idle           | Turn Right     | Turn Right     |
| Turn Left | Two-Stage Left | Turn Left      | Idle           | Turn Right     | Turn Right     |
| Turn Left | Idle           | Go Straight    | Idle           | Turn Right     | Turn Right     |
| Turn Left | Two-Stage Left | Turn Left      | Turn Right     | Turn Right     | Turn Right     |
| Turn Left | Turn Left      | Turn Left      | Turn Left      | Turn Right     | Turn Right     |
| Turn Left | Turn Left      | Two-Stage Left | Turn Left      | Idle           | Turn Right     |
| Turn Left | Turn Left      | Turn Left      | Turn Left      | Turn Left      | Turn Right     |
| Turn Left | Turn Left      | Turn Left      | Turn Left      | Turn Right     | Turn Right     |
| Turn Left | Turn Left      | Turn Left      | Turn Left      | Turn Left      | Turn Right     |
| Turn Left | Turn Right     | Turn Left      | Turn Left      | Turn Right     | Turn Right     |
| nan       | Turn Right     | Turn Left      | Turn Left      | Turn Left      | Turn Right     |
| nan       | Turn Right     | Turn Right     | Turn Left      | Turn Left      | Turn Right     |
| nan       | Turn Right     | Turn Right     | Turn Right     | Turn Right     | Turn Right     |
| nan       | Turn Right     | Turn Right     | Turn Right     | Turn Right     | Turn Right     |
| nan       | Turn Right     | Turn Right     | Turn Right     | Turn Right     | Turn Right     |
| nan       | Turn Right     | Turn Right     | Turn Left      | Turn Left      | Turn Right     |
| nan       | Turn Left      | Turn Right     | Turn Right     | Turn Left      | Turn Left      |
| nan       | Go Straight    | Turn Right     | Turn Right     | Turn Right     | Turn Left      |
| nan       | Go Straight    | Turn Right     | Turn Right     | Turn Right     | Turn Right     |
| nan       | Idle           | Turn Right     | Turn Right     | Turn Right     | Turn Right     |
| nan       | Idle           | Turn Right     | Turn Right     | Turn Right     | Turn Right     |
| nan       | Idle           | Turn Right     | Turn Right     | Turn Right     | Turn Right     |
| nan       | Go Straight    | Turn Right     | Turn Right     | Turn Right     | Turn Right     |
| nan       | Turn Right     | Turn Right     | Turn Right     | Turn Right     | Turn Right     |
| nan       | Turn Right     | Turn Right     | Turn Right     | Turn Right     | Turn Right     |
| nan       | Turn Right     | Idle           | Turn Right     | Turn Right     | Turn Right     |
| nan       | Turn Right     | Idle           | Turn Right     | Turn Right     | Turn Right     |
| nan       | Turn Right     | Turn Right     | Turn Right     | Turn Right     | Turn Right     |
| nan       | Idle           | Turn Right     | Turn Right     | Turn Right     | Turn Right     |
| nan       | Idle           | Turn Right     | Turn Right     | Turn Right     | Turn Right     |
| nan       | Turn Left      | Turn Right     | Turn Right     | Turn Right     | Turn Right     |
| Idle      | Idle           | Turn Right     | Turn Right     | Turn Right     | Turn Right     |
| Idle      | Turn Left      | Turn Right     | Turn Right     | Turn Right     | Turn Right     |
| Idle      | Idle           | Turn Right     | Turn Right     | Turn Right     | Turn Right     |
| Idle      | Turn Left      | Idle           | Turn Right     | Turn Right     | Turn Right     |
| Idle      | Turn Right     | Idle           | Turn Right     | Turn Right     | Turn Right     |
| Idle      | Turn Right     | Idle           | Turn Right     | Turn Right     | Turn Right     |
| Idle      | Idle           | Idle           | Turn Right     | Turn Right     | Turn Right     |
| Idle      | Turn Left      | Turn Left      | Turn Right     | Turn Right     | Turn Right     |
| Idle      | Turn Left      | Idle           | Turn Right     | Turn Right     | Turn Right     |
| Idle      | Turn Right     | Two-Stage Left | Idle           | Turn Right     | Turn Right     |
| Idle      | Two-Stage Left | Turn Right     | Idle           | Turn Right     | Turn Right     |
| Idle      | Turn Left      | Turn Left      | Idle           | Turn Right     | Turn Right     |
| Idle      | Two-Stage Left | Turn Left      | U-turn         | Turn Right     | Turn Right     |
| Idle      | Idle           | Two-Stage Left | Two-Stage Left | Turn Right     | Turn Right     |
| Idle      | Turn Left      | Two-Stage Left | Two-Stage Left | Turn Right     | Turn Right     |
| Idle      | Idle           | Two-Stage Left | Two-Stage Left | Idle           | Idle           |
| Idle      | Idle           | Turn Left      | Turn Left      | Idle           | Turn Right     |
| Idle      | Idle           | Turn Left      | Turn Left      | Idle           | Turn Right     |
| Idle      | Idle           | Idle           | Turn Left      | Idle           | Turn Right     |
| Idle      | Idle           | Idle           | Turn Left      | Turn Left      | Turn Right     |
