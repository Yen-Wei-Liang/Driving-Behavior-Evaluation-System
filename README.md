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
 
