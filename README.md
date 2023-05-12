# 目錄
* [一、資料集介紹 ](#1-資料集介紹)
  * [採集路線](#1-採集路線) 
  * [採集時間](#1-採集時間) 
  * [採集設備](#1-採集設備)  
* [二、Semi-automatic labeling](#2-使用Sklearn上演算法驗證分群效果)
  * [（一）最佳分群數](#2-使用Sklearn上演算法驗證分群效果)  
    * [1. Silhouette Score](#2-silhouettescore) 
    * [2. Calinski-Harabasz Index](#2-calinskiharabaszindex) 
    * [3. Davies-Bouldin Index](#2-daviesbouldinindex) 
    * [4. Elbow Method](#2-elbowmethod) 

* [三、動作觀察](#3-動作觀察)  
  * [（一）動作差異](#3-動作差異) 
  * [（二）Action Element Label Histogram](#3-動作元素) 
  * [（三）動作元素與特徵比較差異](#3-動作元素與特徵比較差異)
    * [1.動作元素5群探討](#3-動作元素5群) 
      * [（1）左轉右轉比較 （不相似）](#3-動作元素5群-1) 
      * [（2）右轉與迴轉比較 （不相似）](#3-動作元素5群-2) 
      * [（3）右轉與待轉比較 （不相似）](#3-動作元素5群-3)  
      * [（4）左轉與迴轉 （相似）](#3-動作元素5群-4)  
      * [（5）左轉與待轉 （相似）](#3-動作元素5群-5)  
      * [（6）怠速與直行 （相似）](#3-動作元素5群-6) 
    * [2.動作元素4群探討](#3-動作元素4群) 
      * [（1）左轉右轉比較 （不相似）](#3-動作元素4群-1) 
      * [（2）右轉與迴轉比較 （不相似）](#3-動作元素4群-2) 
      * [（3）右轉與待轉比較 （不相似）](#3-動作元素4群-3)  
      * [（4）左轉與迴轉 （相似）](#3-動作元素4群-4)  
      * [（5）左轉與待轉 （相似）](#3-動作元素4群-5)  
      * [（6）怠速與直行 （相似）](#3-動作元素4群-6)     
    * [3.動作元素3群探討](#3-動作元素3群) 
      * [（1）左轉右轉比較 （不相似）](#3-動作元素3群-1) 
      * [（2）右轉與迴轉比較 （不相似）](#3-動作元素3群-2) 
      * [（3）右轉與待轉比較 （不相似）](#3-動作元素3群-3)  
      * [（4）左轉與迴轉 （相似）](#3-動作元素3群-4)  
      * [（5）左轉與待轉 （相似）](#3-動作元素3群-5)  
      * [（6）怠速與直行 （相似）](#3-動作元素3群-6)
* [四、Prefix Tree](#4-PrefixTree-1)   
  * [（一）依不同Acton建立分別的 Prefix Tree model （5 Action Element）](#4-PrefixTree-2) 
    * [（1）怠速](#4-PrefixTree-3) 
    * [（3）直線](#4-PrefixTree-4)  
    * [（4）左轉](#4-PrefixTree-5)  
    * [（5）右轉](#4-PrefixTree-6)  
    * [（6）待轉](#4-PrefixTree-7)   
    * [（7）迴轉](#4-PrefixTree-8) 
    * [模型預測](#4-PrefixTree-9) 
  * [（二）依不同Acton建立分別的 Prefix Tree model （4 Action Element）](#4-PrefixTree-10) 
    * [（1）怠速](#4-PrefixTree-11) 
    * [（3）直線](#4-PrefixTree-12)  
    * [（4）左轉](4-PrefixTree-13)  
    * [（5）右轉](4-PrefixTree-14)  
    * [（6）待轉](4-PrefixTree-15)   
    * [（7）迴轉](4-PrefixTree-16)  
    * [模型預測](#4-PrefixTree-17) 
  * [（三）依不同Acton建立分別的 Prefix Tree model （3 Action Element）](#4-PrefixTree-18) 
    * [（1）怠速](#4-PrefixTree-19) 
    * [（3）直線](#4-PrefixTree-20)  
    * [（4）左轉](#4-PrefixTree-21)  
    * [（5）右轉](#4-PrefixTree-22)  
    * [（6）待轉](#4-PrefixTree-23)   
    * [（7）迴轉](#4-PrefixTree-24)  
    * [模型預測](#4-PrefixTree-25) 
* [五、Probabilistic Suffix Tree](#5-pst-1)   
  * [（一）依不同Acton建立分別的 Probabilistic Suffix Tree model （5 Action Element）](#5-pst-2) 
  * [（二）依不同Acton建立分別的 Probabilistic Suffix Tree model （4 Action Element）](#5-pst-3) 
  * [（三）依不同Acton建立分別的 Probabilistic Suffix Tree model （3 Action Element）](#5-pst-4) 


 
 
# 一、資料集介紹 <a name="1-資料集介紹"></a>
本資料集為2023年4月17日下午14時16分開始採集，採集時間為26分鐘，共計27578筆資料(此資料集以做過正規化)。

## （一） 採集路線 <a name="1-採集路線"></a>
採集路線的GPS詳細資訊可見檔案20230417_GPS.csv，該檔案包含經度、緯度、海拔、時間戳以及速度等資訊。

## （二） 採集時間 <a name="1-採集時間"></a>
採集時間為14:16非尖峰時刻，如圖所示。
![](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/blob/main/Data_Set/20230417_DataSet/Off-peak%20time%20on%20the%20afternoon%20of%20April%2017th.jpg?raw=true)

## （三） 採集設備 <a name="1-採集設備"></a>
本次採集使用的設備為平板，其放置位置如圖所示。
![](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/blob/main/Data_Set/20230417_DataSet/Place_The_Luggage_In_The_Trunk.jpg?raw=true)


# 二、Semi-automatic labeling <a name="2-使用Sklearn上演算法驗證分群效果"></a>

## （一）最佳分群數 <a name="2-使用Sklearn上演算法驗證分群效果"></a>

### 1.Silhouette Score <a name="#2-silhouettescore"></a>
  The best value is 1 and the worst value is -1. Values near 0 indicate overlapping clusters. Negative values generally indicate that a sample has been assigned to the wrong cluster, as a different cluster is more similar.
![image](https://user-images.githubusercontent.com/127264553/235826819-4a162bec-3183-4fb6-8381-8890afefc241.png)

### 2.Calinski-Harabasz Index <a name="#2-calinskiharabaszIndex"></a>
  The score is higher when clusters are dense and well separated, which relates to a standard concept of a cluster.
![image](https://user-images.githubusercontent.com/127264553/235826833-6c1c3234-8d51-418c-827c-611fded8eae7.png)

             
### 3.Davies-Bouldin Index <a name="#2-daviesbouldinindex"></a>
  This index signifies the average ‘similarity’ between clusters, where the similarity is a measure that compares the distance between clusters with the size of the clusters themselves.
  Zero is the lowest possible score. Values closer to zero indicate a better partition.
  
![image](https://user-images.githubusercontent.com/127264553/235826844-2298b55e-b61b-4d90-9f60-c7b6af7fdd97.png)
### 4.Elbow Method <a name="#2-elbowmethod"></a>
![image](https://user-images.githubusercontent.com/127264553/235826864-ed077679-9f80-4766-a49f-9904e24aea21.png)
     
# 三、動作觀察 <a name="3-動作觀察"></a>
## （一）動作差異 （轉分類問題）<a name="3-動作差異"></a>
![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/82d7ba1c-6c1b-4465-aa03-634021954ed8)


## （二）Action Element Label Histogram <a name="3-動作元素"></a>

| 左轉 | 右轉 | 直行 |
| :-: | :-: | :-: |
| ![image](https://user-images.githubusercontent.com/127264553/235834067-3c2c302e-3dcd-454d-92b3-d8deef671a61.png)| ![image](https://user-images.githubusercontent.com/127264553/235834078-1f159ad5-1f4e-4ef1-9c90-cb68d92ae7e5.png)| ![image](https://user-images.githubusercontent.com/127264553/235834094-640278a5-4040-45b3-a26d-8b4148244f64.png)|
| 迴轉 | 待轉 | 怠速 |
| ![image](https://user-images.githubusercontent.com/127264553/235834113-bf58e625-f0d2-465b-9468-60b4e3afe0ac.png)| ![image](https://user-images.githubusercontent.com/127264553/235834130-528e5926-da3f-4786-a2d3-7fbdeba0382f.png)| ![image](https://user-images.githubusercontent.com/127264553/235834145-55750817-c4da-43db-ac9b-21a6956bdb08.png)|


## （三）動作元素與特徵比較差異 <a name="3-動作元素與特徵比較差異"></a>
### 1. 動作元素5群探討 <a name="3-動作元素5群"></a>


 下圖X軸皆為 time step 、Y軸皆為： Value、九宮格分別對應9種特徵視覺化

#### （1）右轉左轉比較 （不相似）<a name="3-動作元素5群-1"></a>


| Z軸角速度 | X軸角速度 | Y軸角速度 |
| :-: | :-: | :-: |
| ![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/0eea92ba-106d-40df-9418-f5465b6b7d09) | ![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/c35d82a0-057e-4d74-8338-fc0e4ae94089) |![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/def4ed46-5952-4f56-be54-26555a739d0a)|
| Z軸加速度 | X軸加速度 | Y軸加速度 |
| ![image](https://user-images.githubusercontent.com/127264553/235827255-987f0275-f681-4a76-91a5-72ded41d874b.png)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/5e45ab68-dbb7-441b-ac01-26f5dcd3dbd6)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/34fbac7a-a56f-43ac-a5db-8ebad589f2e4) |
| Z軸角度 | X軸角度 | Y軸角度 |
|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/6392932d-9a57-477e-b1d7-2182e638d88e)| ![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/968f258b-309e-4540-95aa-32c809e1f54c) |![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/198193be-a009-4ddb-ba11-022c88cc7aec) |


#### （2）右轉與迴轉比較 （不相似）<a name="3-動作元素5群-2"></a>




| Z軸角速度 | X軸角速度 | Y軸角速度 |
| :-: | :-: | :-: |
|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/ee46ad2d-6f7b-4ac7-9205-2f60934c59f8)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/6fa2c79f-9ad8-4e5c-9145-081911fa6a8b)| ![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/756a1d80-f0a8-4590-97e0-0d7ef0714cf4)|
| Z軸加速度 | X軸加速度 | Y軸加速度 |
|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/95c18f18-f870-4902-ba9c-5a36f1ef3f42)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/87655dd1-4571-4f3a-8c48-91f4d3bd9cd7)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/aa1ffbe7-ad24-4fe1-8f8b-1b0bd22d2120)|
| Z軸角度 | X軸角度 | Y軸角度 |
|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/e9ead072-93ac-441a-b6cb-e222cccfe8fc)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/978555a0-3d5d-479a-9323-0ce574f8d182)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/3e7f2d01-3ddf-44b2-993e-c6587c876b27)|


#### （3）右轉與待轉比較 （不相似）<a name="3-動作元素5群-3"></a>



| Z軸角速度 | X軸角速度 | Y軸角速度 |
| :-: | :-: | :-: |
|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/2f89087d-c9e6-45b3-9d54-e6b20fd2d2d1)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/8678c573-5509-4f20-ab94-3e7c0e658a65)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/83edd9df-cd74-463f-963f-02ddaaeb9757)|
| Z軸加速度 | X軸加速度 | Y軸加速度 |
|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/4bb3ddc7-4bcc-447c-9146-fabfc2daa334)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/9999fcf2-bc09-49cb-9f27-a4fa81d94df1)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/75e4dc50-acee-4068-8086-5edfde57ad04)|
| Z軸角度 | X軸角度 | Y軸角度 |
|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/768b73bd-0218-48ea-a0fd-67c3da9b6e64)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/35bb5ca7-a583-422b-aa55-c1d74a216dfc)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/bc609360-3429-48af-b918-960c166af74d)|








#### （4）左轉與迴轉 （相似）<a name="3-動作元素5群-4"></a>


| Z軸角速度 | X軸角速度 | Y軸角速度 |
| :-: | :-: | :-: |
|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/0a3cb9c2-1a18-441d-8cfe-e58347ada9a0)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/238ee62c-905c-4b2d-a115-952fb729462c)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/0b8c3c68-39c2-4b21-b5b1-939964d6d99c)|
| Z軸加速度 | X軸加速度 | Y軸加速度 |
|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/45338673-9b2f-4b2e-88fc-436de9d9d6a5)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/c5531973-700c-41a6-9bcd-4964324a9c48)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/6d8e7475-1987-4425-a88b-44f87080c8ca)|
| Z軸角度 | X軸角度 | Y軸角度 |
|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/168faa12-668a-4423-9fe1-4e4708514ae5)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/b916d2d9-0763-49fc-8c59-0273665002b1)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/837318c2-3c8d-4237-9a45-ad0ee88fedcc)|





#### （5）左轉與待轉 （相似）<a name="3-動作元素5群-5"></a>
| Z軸角速度 | X軸角速度 | Y軸角速度 |
| :-: | :-: | :-: |
|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/c87febaf-a0ac-48b1-9a87-18807d8df8f2)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/df51838a-560a-42e3-bcd2-13918e463962)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/c0238ed4-8a17-414a-bec9-2f4580561270)|
| Z軸加速度 | X軸加速度 | Y軸加速度 |
|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/f1a2e627-cfae-47e9-ba14-fe969e8ed5a2)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/e906f019-296a-409b-9eee-0f5953649663)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/6cc8859c-1a15-40c7-9c51-6e3bc8173a94)|
| Z軸角度 | X軸角度 | Y軸角度 |
|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/1789fdaa-fb58-4da7-8129-6329b7e36100)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/3f169d40-b59f-4ad3-829a-87dcffc17516)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/0eb215e4-cdb5-4b56-8a86-47637055df80)|






#### （6）怠速與直行 （相似）<a name="3-動作元素5群-6"></a>


| Z軸角速度 | X軸角速度 | Y軸角速度 |
| :-: | :-: | :-: |
|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/bffb046a-41a2-48f4-951a-171e171624b1)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/55e5a136-8329-4925-a97a-4c0a41b50c30)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/44d7f400-c034-424b-b256-6f7736c2ce38)|
| Z軸加速度 | X軸加速度 | Y軸加速度 |
|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/19f1a66a-f20d-4966-898b-309a005fd8ce)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/ad495cb0-1bff-4d2d-8194-f5d9e1a915ea)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/afe0f391-aeed-4bc0-b62d-e88ac76f204a)|
| Z軸角度 | X軸角度 | Y軸角度 |
|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/96db561d-f6ba-46b0-b3cc-a941e80f40ee)| ![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/61ddc3c8-0213-4ffc-8406-c6b621c43a8b)| ![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/c263f365-04b5-4583-9dfa-75477b67f289)|






















### 2. 動作元素4群探討 <a name="3-動作元素4群"></a>


 下圖X軸皆為 time step 、Y軸皆為： Value、九宮格分別對應9種特徵視覺化

#### （1）左轉右轉比較 （不相似）<a name="3-動作元素4群-1"></a>


| Z軸角速度 | X軸角速度 | Y軸角速度 |
| :-: | :-: | :-: |
|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/03fa75a7-1911-4dfd-88a1-88db0c12251d)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/4a195976-4a7a-4b31-833c-e5db022ababf)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/4bb7b327-efc1-4e97-8a3c-7e701bb00bac)|
| Z軸加速度 | X軸加速度 | Y軸加速度 |
|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/96f190bd-9671-4d2e-a0ac-7ad2c096d123)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/e861469c-7570-460f-aec9-6e8973940844)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/8b57d114-1c45-430d-a581-b289167f0b0a)|
| Z軸角度 | X軸角度 | Y軸角度 |
|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/d8546863-65c5-4039-8512-71c5e1d020fd)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/fd9d309d-f4e9-44e5-953b-7b9e8ffa8c1a)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/71e26b06-5132-4733-aa01-00be7caab25c)|


#### （2）右轉與迴轉比較 （不相似）<a name="3-動作元素4群-2"></a>




| Z軸角速度 | X軸角速度 | Y軸角速度 |
| :-: | :-: | :-: |
|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/897644fa-e3fb-4150-aad5-60b8f360a120)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/c825a1f7-e9ce-4ca2-8793-7dece0081606)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/febaac24-2822-45c8-8bdb-1ff6421b43b3)|
| Z軸加速度 | X軸加速度 | Y軸加速度 |
|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/8a5b0504-7949-4bd8-805e-41c61f5e829d)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/918373a8-400e-4bfb-91ee-b29db31676da)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/9ed1bf01-9f43-4d3c-a1fd-d341b18cc894)|
| Z軸角度 | X軸角度 | Y軸角度 |
|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/798fc6c9-1796-40b4-922f-fe6f010f85a5)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/ba40bab0-2539-4779-9579-0ed0bb5b44df)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/8046f25c-a35e-4e63-acb0-06b264b3c4b4)|







#### （3）右轉與待轉比較 （不相似）<a name="3-動作元素4群-3"></a>



| Z軸角速度 | X軸角速度 | Y軸角速度 |
| :-: | :-: | :-: |
|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/6a88f372-c642-44aa-b8c1-51d1e1237142)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/ed59907e-cd15-4b60-8476-30b79947bc41)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/49ee75b3-a26e-43db-b50e-9931f4994c85)|
| Z軸加速度 | X軸加速度 | Y軸加速度 |
|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/0bffaab5-9407-4ec8-9a52-8be7b226b122)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/c5e9c317-34cd-4414-8482-51400a194eb0)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/5ce3a558-d40c-4b91-89cb-3f7786d2dc92)|
| Z軸角度 | X軸角度 | Y軸角度 |
|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/7a59061a-2620-4524-8468-73ae39b9aa27)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/b4f71a82-ad36-4c15-af7f-66a653901f0d)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/c8a46580-b92a-4b7c-9218-03506f8ec663)|




#### （4）左轉與迴轉 （相似）<a name="3-動作元素4群-4"></a>


| Z軸角速度 | X軸角速度 | Y軸角速度 |
| :-: | :-: | :-: |
|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/2d0a62a3-b3bc-402e-83a4-ca858724a030)| ![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/992d0f0f-dcca-4f4d-b2d1-be145cb3b89f)| ![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/64cda5de-9a7e-4b9a-a08c-fd67c5bf8156)|
| Z軸加速度 | X軸加速度 | Y軸加速度 |
|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/a416987c-e38b-4fc9-a71a-6425e8567d64)| ![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/97e8c78b-3b1c-437a-9834-b7d69e219e6d)| ![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/2d5c38f3-5a98-450e-abf3-e49cbc4509d2)|
| Z軸角度 | X軸角度 | Y軸角度 |
|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/8edc25e6-8ed1-490f-916d-65d43b287934)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/ffeb7c60-0d44-44a2-bdfc-e8aceafcff60)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/db51e376-1740-4549-a717-be4a09343dc1)|





#### （5）左轉與待轉 （相似）<a name="3-動作元素4群-5"></a>
| Z軸角速度 | X軸角速度 | Y軸角速度 |
| :-: | :-: | :-: |
|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/06dbb8e2-a1b9-4029-88a4-02a9570e4ceb)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/7a9d630b-f0d0-4193-9ad0-b1c435112a16)| ![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/9bf94f0a-4d05-433c-86aa-91807410c6e2)|
| Z軸加速度 | X軸加速度 | Y軸加速度 |
|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/cf451022-1060-4fe5-8850-f422232891e7)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/bf11c37e-4e97-4f9c-98b2-9873b5aa8d84)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/55dcddb8-eb83-4092-b31c-0c34c81445f2)|
| Z軸角度 | X軸角度 | Y軸角度 |
|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/f08e13c3-c14d-423c-8cb6-7bd5d0e91f41)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/74c8663d-551d-4d6a-b18a-68da84c30bfb)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/44822071-ad92-441a-b6c2-d14708152d86)|






#### （6）怠速與直行 （相似）<a name="3-動作元素4群-6"></a>


| Z軸角速度 | X軸角速度 | Y軸角速度 |
| :-: | :-: | :-: |
|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/9260eeb5-bed6-4af9-9a7a-cc0bf7c7bd6a)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/1451db89-e591-40b1-ab23-b1a518f6c6a6)| ![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/36f9653b-fe1c-46b4-b5e2-d87da89cd3bd)|
| Z軸加速度 | X軸加速度 | Y軸加速度 |
|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/702270fe-95dc-43db-b404-b9111ba0eb07)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/95a10aab-afd3-4e82-9a9a-ba5c174fe02d)| ![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/4fff44cf-b668-4b00-8494-c116ac7d26eb)|
| Z軸角度 | X軸角度 | Y軸角度 |
|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/f863961e-62c7-40fe-91d4-80c8ede12f62)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/bc14148d-5be5-4f72-9a11-c3819bd5f56e)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/5eb81494-6a96-427b-8b80-7b583815599b)|









### 3. 動作元素3群探討 <a name="3-動作元素3群"></a>


 下圖X軸皆為 time step 、Y軸皆為： Value、九宮格分別對應9種特徵視覺化

#### （1）左轉右轉比較 （不相似）<a name="3-動作元素3群-1"></a>


| Z軸角速度 | X軸角速度 | Y軸角速度 |
| :-: | :-: | :-: |
| ![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/24c83326-f738-4ece-922a-f42b891e520e)| ![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/753043d0-2b2c-4a2d-8b9b-7172621f18df)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/0a8f596e-5387-474e-9293-764ea2f03872)|
| Z軸加速度 | X軸加速度 | Y軸加速度 |
|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/7d18e96a-1b84-41a0-b7b0-0767cca6c814)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/a27e98e6-375a-4242-a99a-9f9b8717d551)| ![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/0f7f2359-9c12-400d-812a-f34fb4d7f9a7)|
| Z軸角度 | X軸角度 | Y軸角度 |
|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/4d5e43d6-548f-44a3-9181-b483ab113f0c)| ![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/701df363-a5d2-4fbe-aea5-64beedc86adb)| ![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/9a81ec11-c4f7-477c-9914-8e8c584c0a2e)|


#### （2）右轉與迴轉比較 （不相似）<a name="3-動作元素3群-2"></a>




| Z軸角速度 | X軸角速度 | Y軸角速度 |
| :-: | :-: | :-: |
|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/f143e2d0-13cd-4c4e-96a3-8075f8170e5c)| ![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/e91b334a-3270-478a-9142-c250cc59d860)| ![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/f991c8cc-0954-454c-8ba4-885d6de1cf11)|
| Z軸加速度 | X軸加速度 | Y軸加速度 |
|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/d393351c-7af9-43ed-ae22-5687fc8a7418)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/21bc3eee-c72a-4c8c-a313-cfda2d502c6d)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/9f293a18-1210-4a00-8cd1-e70016a8e84e)|
| Z軸角度 | X軸角度 | Y軸角度 |
|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/c8763a36-3b58-4ae6-8226-da5f9a25cc19)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/0983cf22-1b7a-4e44-a26e-5ae96958ba6c)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/e45e367e-8b90-4a50-8f32-265ac4f5d769)|







#### （3）右轉與待轉比較 （不相似）<a name="3-動作元素3群-3"></a>



| Z軸角速度 | X軸角速度 | Y軸角速度 |
| :-: | :-: | :-: |
| ![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/6f19f4da-78b4-47bb-95cd-034f000a00ca)| ![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/9f5c9206-ca13-4788-9632-9731ec779e5d)| ![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/ee9efcc2-6d32-4ac0-a212-237bffe62d17)|
| Z軸加速度 | X軸加速度 | Y軸加速度 |
| ![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/6445f50c-67fc-426a-be7e-a679b04ffa97)| ![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/814da358-8f25-466e-a72a-91d477580453)| ![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/b614d36d-e59d-4816-8538-0f2d7e4becc5)|
| Z軸角度 | X軸角度 | Y軸角度 |
|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/3506ae07-5c04-4655-ab71-e121dc95b841)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/d2470141-29cd-4374-a90b-c5b85eac3f86)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/ae890c91-caea-4734-8da5-e2cead2bd339)|





#### （4）左轉與迴轉 （相似）<a name="3-動作元素3群-4"></a>


| Z軸角速度 | X軸角速度 | Y軸角速度 |
| :-: | :-: | :-: |
|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/e452f469-fbb9-4847-a0bd-0aae78758421)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/3ed4620d-232d-49c4-b775-a972e33913b0)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/823da188-0045-4202-bfa6-941d20c6922d)|
| Z軸加速度 | X軸加速度 | Y軸加速度 |
|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/ac1812cc-3038-46e9-8b20-7df5d5c54ee9)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/5be34930-e156-4245-a888-14ba97a2437f)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/3ff9f116-6110-489f-830c-19edbcc69a79)|
| Z軸角度 | X軸角度 | Y軸角度 |
|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/975ca18d-1ebb-420c-8a2a-bece35417440)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/afa96ab5-929a-46fe-a8c2-c72333af8367)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/ff3b3daf-335a-4611-97e4-328d092660d0)|



#### （5）左轉與待轉 （相似）<a name="3-動作元素3群-5"></a>
| Z軸角速度 | X軸角速度 | Y軸角速度 |
| :-: | :-: | :-: |
|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/bb900272-0b26-4cad-8a1b-3b562b2ee614)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/ffc8bc3d-8799-4e20-8d0c-12852cd1d116)| ![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/c46361fc-54b2-46e8-b3e8-527c91d49726)|
| Z軸加速度 | X軸加速度 | Y軸加速度 |
|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/fbd87ec7-da4d-406a-94b6-0ea1fc8a1d54)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/5e21e828-d524-42a2-880b-f9f89c79dcc6)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/51251af7-db0f-41d4-ba45-a568437297b8)|
| Z軸角度 | X軸角度 | Y軸角度 |
|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/9374f2c5-0d42-4f55-a12e-160d1748a5aa)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/482d1042-9386-43e0-958d-fe8387dd0394)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/afaf868c-536b-47a8-b34a-5bfee221fef2)|






#### （6）怠速與直行 （相似）<a name="3-動作元素3群-6"></a>




| Z軸角速度 | X軸角速度 | Y軸角速度 |
| :-: | :-: | :-: |
|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/blob/main/Discuss/Chart/3%20Cluster/best/similar/Idle%20vs%20Go%20straight/Z-axis%20Angular%20Velocity%20Idle%20vs%20Go%20straight%EF%BC%88best%EF%BC%89.png?raw=true)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/blob/main/Discuss/Chart/3%20Cluster/best/similar/Idle%20vs%20Go%20straight/X-axis%20Angular%20Velocity%20Idle%20vs%20Go%20straight%EF%BC%88best%EF%BC%89.png?raw=true)| ![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/blob/main/Discuss/Chart/3%20Cluster/best/similar/Idle%20vs%20Go%20straight/Y-axis%20Angular%20Velocity%20Idle%20vs%20Go%20straight%EF%BC%88best%EF%BC%89.png?raw=true)|
| Z軸加速度 | X軸加速度 | Y軸加速度 |
|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/blob/main/Discuss/Chart/3%20Cluster/best/similar/Idle%20vs%20Go%20straight/Z-axis%20Acceleration%20Idle%20vs%20Go%20straight%EF%BC%88best%EF%BC%89.png?raw=true)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/blob/main/Discuss/Chart/3%20Cluster/best/similar/Idle%20vs%20Go%20straight/X-axis%20Acceleration%20Idle%20vs%20Go%20straight%EF%BC%88best%EF%BC%89.png?raw=true)| ![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/blob/main/Discuss/Chart/3%20Cluster/best/similar/Idle%20vs%20Go%20straight/Y-axis%20Acceleration%20Idle%20vs%20Go%20straight%EF%BC%88best%EF%BC%89.png?raw=true)|
| Z軸角度 | X軸角度 | Y軸角度 |
| ![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/blob/main/Discuss/Chart/3%20Cluster/best/similar/Idle%20vs%20Go%20straight/Z-axis%20Angle%20Idle%20vs%20Go%20straight%EF%BC%88best%EF%BC%89.png?raw=true)|![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/blob/main/Discuss/Chart/3%20Cluster/best/similar/Idle%20vs%20Go%20straight/X-axis%20Angle%20Idle%20vs%20Go%20straight%EF%BC%88best%EF%BC%89.png?raw=true)| ![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/blob/main/Discuss/Chart/3%20Cluster/best/similar/Idle%20vs%20Go%20straight/Y-axis%20Angle%20Idle%20vs%20Go%20straight%EF%BC%88best%EF%BC%89.png?raw=true)|




# 四、Prefix Tree <a name="4-PrefixTree-1"></a>
## （一）依不同Acton建立分別的 Prefix Tree model （5 Action Element）<a name="4-PrefixTree-2"></a>

### 1.怠速 <a name="4-PrefixTree-3"></a> 
#### 
![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/e3a0c080-f279-4b8f-88ff-3e6c34c591fa)


### 2.直線 <a name="4-PrefixTree-4"></a>
#### 
![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/dee382e5-59b5-4d85-9422-f2d1f70e2f7b)

### 3.轉左 <a name="4-PrefixTree-5"></a>
#### 
![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/47b4e1f5-c742-4ebb-bfd0-a6e2f609f2e8)

### 4.右轉 <a name="4-PrefixTree-6"></a>
#### 
![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/cc96cf99-5e55-4e89-ad31-4f585746a03d)

### 5.待轉 <a name="4-PrefixTree-7"></a>
#### 
![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/83d64ace-d0d5-4a54-8a31-539dd0db6b3d)

### 6.迴轉 <a name="4-PrefixTree-8"></a>
####
![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/53a2bafe-82ad-4b56-827e-24abdeb00e2b)


### 模型預測（5 Action Element） <a name="4-PrefixTree-9"></a>

| Model \ Action | Go Straight | Idle | Turn Left | Turn Right | Two-Stage Left | U-turn |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| Go Straight Model | 0.0058 % | 0.00077 % | 0.0084 % | 0.002 % | 0.0032 % | 0.0032 % |
| Idle Model | 0.0128 % | 0.31334 % | 0.0048 % | 0.018 % | 0.1309 % | 0.0001 % |
| Turn Left Model | 0.026 % | 0.1314 % | 0.0181 % | 0.0144 % | 0.0285 % | 0.0031 % |
| Turn Right Model | 0.0174 % | 0.04935 % | 0.0184 % | 0.0167 % | 0.0399 % | 0.0033 % |
| Two-Stage Left Model | 0.0207 % | 0.00115 % | 0.0051 % | 0.0077 % | 0.0062 % | 0.006 % |
| U-turn Model | 0.0203 % | 0.07834 % | 0.0197 % | 0.0164 % | 0.0215 % | 0.0034 % |

## （二）依不同Acton建立分別的 Prefix Tree model （4 Action Element）<a name="4-PrefixTree-10"></a>



### 1.怠速 <a name="4-PrefixTree-11"></a> 
#### 

![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/e94efc5b-5f68-43fc-b2f6-0f6f48d94a9f)


### 2.直線 <a name="4-PrefixTree-12"></a>
#### 
![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/6f3f3a7f-e039-4fcf-81ab-4914ff1f1838)


### 3.轉左 <a name="4-PrefixTree-13"></a>
#### 
![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/ff2d2f35-a209-411e-93e0-27cac9d64282)


### 4.右轉 <a name="4-PrefixTree-14"></a>
#### 
![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/b5f971f1-71cd-4aac-9adf-7463c1f7584e)


### 5.待轉 <a name="4-PrefixTree-15"></a>
#### 
![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/2d95c62c-ae3e-452b-9513-9573990e93d0)


### 6.迴轉 <a name="4-PrefixTree-16"></a>
####

![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/78cfe25c-5912-4609-8aed-e57cc69295ab)


### 模型預測（4 Action Element） <a name="4-PrefixTree-17"></a>

| Model \ Action | Go Straight | Idle | Turn Left | Turn Right | Two-Stage Left | U-turn |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| Go Straight Model | 0.0238 % |0.0807 % | 0.0567 %|0.095 % | 0.0317 %|0.0713 % |
| Idle Model | 0.00633 % | 0.09349 %| 0.09158 %| 0.11812 %| 0.00958 %| 0.18603 %|
| Turn Left Model | 0.0167 % | 0.1705 %| 0.0815 %|0.0821 % | 0.0302 %| 0.0549 %|
| Turn Right Model | 0.015 % | 0.1246 %| 0.0817 %|0.0904 % | 0.0246 %|0.0748 % |
| Two-Stage Left Model| 0.0076 % | 0.0735 %| 0.0503 %| 0.0595 %| 0.022 %|0.0666 % |
| U-turn Model |  0.0097 %|0.0002 % | 0.0155 %|0.0065 % |0.0064 % | 0.0063 %|












## （三）依不同Acton建立分別的 Prefix Tree model （3 Action Element）<a name="4-PrefixTree-18"></a>


### 1.怠速 <a name="4-PrefixTree-19"></a> 
#### 

![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/67f9162a-62df-4013-8ae9-1819dfe3d8b7)


### 2.直線 <a name="4-PrefixTree-20"></a>
#### 
![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/bad7d75d-8a43-412b-9a40-20571efdd0c9)


### 3.轉左 <a name="4-PrefixTree-21"></a>
#### 
![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/a03d2734-9486-41bb-ba43-bbd8d8e42329)


### 4.右轉 <a name="4-PrefixTree-22"></a>
#### 
![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/bbc7f5b6-8266-4e4d-9367-4a41196bde86)


### 5.待轉 <a name="4-PrefixTree-23"></a>
#### 
![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/85cb8029-d10a-4249-88b3-684b6fc9a67f)



### 6.迴轉 <a name="4-PrefixTree-24"></a>
####

![image](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/ae3ce0d2-71f9-4a7a-8f1e-f5d30edbbaf6)



### 模型預測（3 Action Element） <a name="4-PrefixTree-25"></a>

| Model \ Action | Go Straight | Idle | Turn Left | Turn Right | Two-Stage Left | U-turn |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| Go Straight Model | 0.0238 % |0.0457 %| 0.057 %| 0.0897 %| 0.0324 %|0.0716 %|
| Idle Model   |0.00622 %| 0.16509 %|0.0962 % |0.12087 % |0.00941 %|0.18948 %|
| Turn Left Model  |0.0167 %| 0.0484 %|0.0841 %|0.0858 % |0.0302 %|0.0582 %|
| Turn Right Model  |0.015 %| 0.0664 %| 0.0817 %| 0.0922 %|0.0246 %|0.0765 %|
| Two-Stage Left Model  |0.0076 %| 0.0927 %| 0.0906 %| 0.1035 %|0.022 %|0.1078 %|
| U-turn Model   |0.0227 %|0.0554 % |0.0677 % | 0.0798 %|0.0421 %| 0.0614 %|



# 五、Probabilistic Suffix Tree <a name="#5-pst-1"></a>
d=90, alphabet_size=5
## [（一）依不同Acton建立分別的 Probabilistic Suffix Tree model （5 Action Element）]<a name="#5-pst-2"></a>

| Model\Action | Go Straight | Idle | Turn Left | Turn Right | Two-Stage Left | U-turn |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| Go Straight Model | -90.19 | -511.87|-120.64 | -120.87 |  155.39| -130.27|
| Idle Model |-84.88 | -631.23|-156.77| -141.64| -307.47 | -371.02 |
| Turn Left Model | -84.88 | -631.23| -156.77| -141.64 | -307.47 | -371.02 |
| Turn Right Model | -84.88 | -631.23|-156.77| -141.64| -307.47 | -371.02 |
| Two-Stage Left Model | -84.88 | -631.23|-156.77| -141.64| -307.47 | -371.02 |
| U-turn Model  |-84.88 | -631.23|-156.77| -141.64| -307.47 | -371.02 |


## [（二）依不同Acton建立分別的 Probabilistic Suffix Tree model （4 Action Element）]<a name="#5-pst-3"></a>


| Model\Action | Go Straight | Idle | Turn Left | Turn Right | Two-Stage Left | U-turn |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| Go Straight Model | -72.25|  -469.78| -119.28 | -106.15 |-282.17 |-406.99|
| Idle Model | -74.74|-410.82 |-109.43| -103.99 | -124.64 |-124.60 |
| Turn Left Model | -69.59| 449.37|113.76 | 106.46 | -213.53 |-268.58 |
| Turn Right Model | -72.39|-443.73 |-114.42 | -99.64 | -275.45 | -412.38|
| Two-Stage Left Model | -82.78| -481.12| -120.81| -103.03 | -120.74 | -87.68|
| U-turn Model  |-76.66 |-511.34 | -135.90| -119.69 | -155.03 | -101.65|



## [（三）依不同Acton建立分別的 Probabilistic Suffix Tree model （3 Action Element）]<a name="#5-pst-4"></a>



| Model\Action | Go Straight | Idle | Turn Left | Turn Right | Two-Stage Left | U-turn |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| Go Straight Model | -73.64  | -1842.07|-188.71 |-107.77|-160.50 |-131.73|
| Idle Model|   | -74.00| -979.37|-109.57|-105.48|-132.35 |-112.80|
| Turn Left Model | -69.30  | -1907.64| -122.93|-103.77|-154.81|-124.14 |
| Turn Right Model |-72.39   | -1718.56|-114.17 |-100.37|-152.09|-124.02 |
| Two-Stage Left Model | -80.58  | -2393.92|-150.26 |-132.62|-205.17| -153.95|
| U-turn Model  | -88.51  | -2259.09| -142.53|-129.49|-178.3| -143.16|


