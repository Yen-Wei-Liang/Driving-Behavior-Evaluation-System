# 目錄
* [第一章 簡介](#1)
* [第二章 相關工作](#2)
  * [2.1 機車駕駛行為與事故風險分析](#21)
  * [2.2 分群K-means演算法的原理與應用](#22)
    * [2.2.1 K-means分群](#221)
    * [2.2.2 Silhouette Score](#222) 
    * [2.2.3 Calinski-Harabasz Index](#223) 
    * [2.2.4 Davies-Bouldin Index](#224) 
    * [2.2.5 Elbow Method](#225)
  * [2.3 PST與VOMM時間序列預測演算法的應用](#23)
    * [2.3.1 機率後綴樹](#231) 
    * [2.3.2 可變階馬爾可夫模型](#232)
* [第三章 方法](#3)
  * [3.1 資料集建置](#31)
    * [3.1.1 目標與說明](#311)
    * [3.1.2 資料收集方法](#312)
    * [3.1.3 資料集蒐整流程](#313)
    * [3.1.4 資料屬性和特徵](#314)
    * [3.1.5 資料集的規模和範圍](#315)
    * [3.1.5.1 訓練資料集](#3151)
    * [3.1.5.2 驗證資料集](#3152)
    * [3.1.6 資料集的獨特性和價值](#316)
    * [3.1.7 資料集標記方法](#317)
    * [3.1.8 資料集的可用性和分享](#318)
  * [3.2 半自動標記演算法](#32)
  * [3.3 VOMM的實作與參數設定](#33)
* [第四章 實驗結果](#4)
  * [4.1 實驗設計](#41)
  * [4.2 探討最佳分群數](#42)
    * [4.2.1動作元素4群探討](#421)
    * [4.2.2動作元素8群探討](#422)
    * [4.2.3動作元素10群探討](#423)
  * [4.3 傳統方法](#43)
    * [4.3.1 六種駕駛行為與九軸特徵關係](#431)
    * [4.3.2 轉至分類問題](#432)
  * [4.4 序列與分群動作元素可視化](#44)
    * [4.4.1 右轉 vs 左轉](#441)
    * [4.4.2 右轉 vs 迴轉](#442)
    * [4.4.3 右轉 vs 待轉](#443)
    * [4.4.4 左轉 vs 迴轉](#444)
    * [4.4.5 左轉 vs 待轉](#445)
    * [4.4.6 直線 vs 怠速](#446)
  * [4.5 PST與VOMM的時間序列預測結果評估](#45)
    * [4.5.1 過濾動作演算法](#451)
  * [4.6 實驗結果討論與解釋](#46) 
* [第五章 結論](#5) 



# RideTrack：通過自動標記和實時檢測分析駕駛行為
# RideTrack: Analyzing Motorcycle Behavior through Automated Labeling and Real-time Detection

# 第一章 簡介 <a id="1"></a>

**根據交通部至民國112年的統計數據，我國擁有22,926,176輛動力交通工具，其中機車佔比高達62.9%。這突顯了機車是我國交通環境中最主要且普及的交通工具。然而，去年全年機車事故占交通事故總數的78%，這個比例明顯地超過了預期水準。為提升機車騎士的安全性，本研究專注於機車駕駛行為分析，並提出一種方法來識別不同駕駛行為，包括直行、迴轉、右轉、左轉和兩階段左轉等。**

**該方法基於定期採集的慣性測量單元（IMU）資訊和機車ECU傳感數據，構建了序列資料庫。並透過分群演算法提出了一種自動標記方法，用於標記每個時刻的行為，將資料序列轉換為標籤序列。進一步，我們利用這些標籤序列建立了個體行為的PST模型，並利用該模型進行即時行為檢測，以進行駕駛行為分析。**

**本研究的貢獻在於提供了一種有效的方法來分析和識別機車駕駛行為。通過收集和分析傳感器數據，能夠自動標記駕駛行為並建立相應的行為模型。這有助於深入了解駕駛行為的特徵和模式，並為改善交通安全提供基礎。此外，本研究還展示了如何利用數據分析（如PST/VoM模型）來實現駕駛行為預測，從而能夠及時檢測和回饋駕駛行為的異常或危險情況。**

**這項研究為摩托車騎士的安全駕駛提供了重要的工具和方法，同時也為智慧交通系統和交通安全政策的制定者提供了寶貴的參考。通過深入瞭解駕駛行為，我們能制定更有效的安全措施，提供更好的道路設計和交通規則執行，以減少機車事故的發生，保護機車騎士的生命和財產安全。**


# 第二章 相關工作 <a id="2"></a>
## 2.1 機車駕駛行為與事故風險分析 <a id="21"></a>

**機車駕駛在我國交通環境中佔有重要地位，然而，與機車相關的交通事故風險仍然具有挑戰性。本節旨在探討機車駕駛行為與交通事故風險的關聯，透過官方統計數據結果顯示，機車駕駛行為在交通事故風險中起著關鍵作用。
不同的駕駛行為，都會對交通安全產生不同程度的影響。**

**此外，駕駛行為中的一些因素被證實與交通事故風險密切相關。例如，駕駛者的注意力、反應能力和意識水準在駕駛安全中扮演著重要角色。對於機車駕駛者而言，能夠及時察覺並適應道路環境的變化至關重要。
另交通環境和道路設施的特徵也會影響機車駕駛的安全性。例如，道路狹窄、交通流量高和缺乏交通標誌的地區可能增加事故發生的機率。**

**為提升機車騎士的安全性，對於駕駛行為的分析和識別至關重要。這可以通過使用先進的技術和系統，如監控攝像頭、車輛感應器和人工智能分析來實現。這些技術能夠即時監測駕駛行為，並提供相關的安全建議和警示。
總結而言，瞭解機車駕駛行為與交通事故風險之間的關聯對於制定有效的交通安全措施至關重要。透過對機車駕駛行為的分析和技術的應用，我們能夠提供駕駛者更全面的安全指導和措施，以減少交通事故的發生。
如樣本來自特定地區，仍需要進一步研究來更全面地瞭解交通事故風險與高齡駕駛者之間的關係。然而，這項研究為我們提供了一個重要的起點，以促進交通安全和駕駛者福祉的努力。**





## 2.2 分群K-means演算法的原理與應用 <a id="22"></a>
### 2.2.1 K-means分群 <a id="221"></a>
**K-means是一種常見的無監督學習演算法，用於將資料集分為K個不同的群組。以下是K-means演算法的步驟：**
**步驟一：初始化**
**隨機選擇K個初始中心點。**
**步驟二：分配**
**將每個數據點分配到與其最近的中心點所屬的群集。**
**步驟三：更新**
**對於每個群集，計算所有資料點的平均值，以獲取新的中心點。**
**步驟四：重複**
**重複步驟二和步驟三，直到中心點不再改變或達到預定的停止條件。**

$$
\sum_{i=0}^{n}\min_{\mu_j \in C}(||x_i - \mu_j||^2)
$$

### 2.2.2 Silhouette Score <a id="222"></a>
**Silhouette Score用於衡量K-means分群的效果，值越高表示分群結果越好。以下是計算Silhouette Score的步驟和公式：**
**步驟一：計算每個數據點的輪廓係數**
**對於每個數據點i，計算其與同群集中所有其他數據點的平均距離a<sub>i</sub>，以及與最近其他群集的所有數據點的平均距離b<sub>i</sub>。**
**步驟二：計算輪廓係數**
**對於每個數據點i，計算輪廓係數**





<br>**步驟三：計算整體輪廓係數**
**計算所有數據點的平均輪廓係數S**

$$
s_i = \frac{{b_i - a_i}}{{\max\{a_i, b_i\}}}
$$



<br>**輪廓係數的值範圍在[-1, 1]之間，接近1表示分群效果好，接近-1表示分群效果差。**

### 2.2.3 Calinski-Harabasz Index <a id="223"></a>

**Calinski-Harabasz Index也是一個用於評估分群結果的指標，值越高表示分群結果越好。以下是計算Calinski-Harabasz Index的步驟和公式：**

**步驟一：計算群集內的平方和**
**Calinski-Harabasz Index的步驟和公式：**

**步驟一：計算群集內的平方和（within-cluster sum of squares, WCSS）。
對於每個群集k，計算所有數據點到其所屬中心點的距離平方和WCSS<sub>k</sub>**






<br>**其中x<sub>i</sub>表示群集 k 中的數據點，center<sub>k</sub> 表示群集 k 的中心點。**

**步驟二：計算群集之間的平方和（between-cluster sum of squares, BCSS）。
計算所有群集的中心點center的平均距離平方和BCSS。**

$$
\text{{WCSS}_{k_i}) = \sum_{i=1}^{n} \left( \text{distance} \left( x_i, \text{center}_k \right)^2 \right)
$$


<br>**其中count<sub>k</sub>表示群集k中的數據點數量，center表示所有數據點的中心點，center<sub>k</sub>表示群集k的中心點。**

**步驟三：計算Calinski-Harabasz Index。**


$$
\text{CH Index} = \frac{\frac{\text{BCSS}}{(K-1)}}{\frac{\text{WCSS}}{(N-K)}}
$$


<br>**其中K表示分群數量，N表示總數據點數量。
Calinski-Harabasz Index的值越大，表示分群效果越好。**


### 2.2.4 Davies-Bouldin Index <a id="224"></a>


**Davies-Bouldin Index是另一個用於評估分群結果的指標，值越小表示分群結果越好。以下是計算Davies-Bouldin Index的步驟和公式：**
**步驟一：計算群集內的平均距離（average intra-cluster distance）。**

**對於每個群集k，計算該群集內所有數據點之間的平均距離。**

$$
\text{intra\_cluster\_distance\_K} = \frac{1}{{\text{count}_{k}}} \sum_{i=1}^{k} \left( \text{distance}(x_{i}, x_{j}) \right)
$$


<br>**其中x<sub>i</sub>和x<sub>j</sub>表示群集k中的數據點，count<sub>k</sub>表示群集k的數據點數量。**
**步驟二：計算群集之間的距離（inter-cluster distance）。**

**計算每對群集之間的距離，可以使用不同的距離度量方法，如歐氏距離、曼哈頓距離等。**

$$
\text{inter\_cluster\_distance}(k_1, k_2) = \text{distance}(\text{center}_{k_1}, \text{center}_{k_2})
$$



<br>**其中center<sub>k1</sub>和center<sub>k2</sub>表示群集k<sub>1</sub>和k<sub>2</sub>的中心點。**
**步驟三：計算Davies-Bouldin Index。**

'$$
\text{DB\_Index} = \frac{1}{k} \sum_{k=1}^{k} \left(\frac{\max \left(\text{intra\_cluster\_distance}(k\_1) + \text{intra\_cluster\_distance}(k\_2)\right)}{\text{inter\_cluster\_distance}(k\_1, k\_2)}\right)
$$'


<br>**其中K表示分群數量。
Davies-Bouldin Index的值越小，表示分群效果越好。**



### 2.2.5 Elbow Method <a id="225"></a>

**Elbow Method是一種簡單直觀的方法來尋找最佳的分群數量。該方法基於WCSS（within-cluster sum of squares）的變化率來進行評估。以下是Elbow Method的步驟：**
**步驟一：執行K-means分群算法**

**對於不同的K值（分群數量），執行K-means分群算法。
步驟二：計算WCSS**

**對於每個K值，計算對應的WCSS。
步驟三：繪製WCSS隨K值的變化圖**

**將K值作為橫軸，對應的WCSS作為縱軸，繪製WCSS隨K值的變化圖。
步驟四：尋找"彎曲點"**

**觀察WCSS隨K值變化的圖形，尋找一個"彎曲點"。
"彎曲點"是指當K值增加時，WCSS的下降速度明顯減緩的點。
步驟五：確定最佳分群數量**

**最佳分群數量通常在"彎曲點"之前，即K值選擇該"彎曲點"對應的數量。
Elbow Method通過觀察WCSS的變化趨勢，選擇WCSS下降速度明顯減緩的點作為最佳的分群數量。**


## 2.3 PST與VOMM時間序列預測演算法的應用 <a id="23"></a>

### 2.3.1 機率後綴樹 <a id="231"></a>

**PST（Probability Suffix Tree，PST）是一種統計模型，用於建立和表示一個文本序列中的機率模型。以下是PST的步驟和公式：**

**步驟一：建立後綴樹
從給定的文本序列中，建立一個後綴樹。後綴樹是一種特殊的字典樹，用於存儲所有後綴（suffix）的資訊。**

**步驟二：計算機率
對於每個後綴節點，計算其後綴的機率。這可以使用最大概似法（Maximum Likelihood Estimation）或其他統計方法來計算。**

**步驟三：建立機率模型
使用後綴樹和後綴的機率，建立一個機率模型。機率模型描述了每個後綴的機率分佈，可以用於預測和生成文本序列。**

**公式：**

**後綴的機率估計可以使用最大概似法來計算。對於一個後綴節點n，其後綴的機率可以表示為：**


$$
P(\text{suffix}_{n}) = \frac{\text{count}(\text{suffix}_{n})}{\text{count}(n)}
$$



<br>**其中，count(suffix<sub>n</sub> )是後綴n出現的次數，count(n)是後綴節點n的出現次數。
機率後綴樹可以用於語言建模、文本生成、預測等自然語言處理任務，以及其他需要建立機率模型的應用場景。**





### 2.3.2 可變階馬爾可夫模型 <a id="232"></a>

**可變階馬爾可夫模型（Variable-order Markov models，VOMM）是一種統計模型，用於建立和表示文本序列中的機率模型。以下是VOMM的步驟和公式：**

**步驟一：確定階數
確定模型的階數（order）。階數代表模型考慮的前幾個觀測值來預測下一個觀測值的條件機率。**

**步驟二：計算條件機率
對於每個觀測序列中的位置，計算根據當前階數的條件機率。**

**步驟三：建立機率模型
使用觀測序列和條件機率，建立一個機率模型。機率模型描述了觀測值的機率分佈，可以用於預測和生成文本序列。**

**公式：
條件機率可以使用最大概似法或其他統計方法來計算。對於一個特定階數k和前 k 個觀測值 x<sub>1</sub>,x<sub>2</sub>,…,x<sub>k</sub>，條件機率可以表示為：**


$$
P(x_{k+1} | x_1, x_2, \ldots, x_k) = \frac{\text{count}(x_1, x_2, \ldots, x_k, x_{k+1})}{\text{count}(x_1, x_2, \ldots, x_k)}
$$




<br>**其中，count(x<sub>1</sub>,x<sub>2</sub>,…,x<sub>k</sub>,x<sub>(k+1)</sub>)是在觀測序列中出現 x<sub>1</sub>,x<sub>2</sub>,…,x<sub>k</sub>,x<sub>(k+1)</sub>的次數，count(x<sub>1</sub>,x<sub>2</sub>,…,x<sub>k</sub> )是在觀測序列中出現 x<sub>1</sub>,x<sub>2</sub>,…,x<sub>k</sub>的次數。**

**可變階馬爾可夫模型可以應用於語言建模、預測、文本生成等自然語言處理任務，並且在需要考慮不同階數上下文的場景中非常有用。**



















# 第三章 方法 <a id="3"></a>
## 3.1 資料集建置 <a id="31"></a>
**本研究建立了兩個不同的資料集，用於模型的訓練和驗證。首先，我們收集了一個位於學區附近、車流量較少的環境中的資料集，作為訓練資料集。這是因為在機車駕駛的大部分時間中，駕駛者主要進行直行和怠速（等紅燈）的動作。為了避免預測時盲猜情況，我們設計了六種常見的駕駛行為，包括直行、左轉、右轉、迴轉、待轉和怠速。同時，我們在資料集的採集路線中減少了直線和怠速狀態的數量，也因安全因素考量，故找學區車流量較少的地方進行蒐整資料集。**


**另外，我們還收集了在夜市（車流量和人流量較多）環境中的資料集，作為驗證集使用，需要注意的是，在資料集中的迴轉和待轉狀態是根據我國法規特意採集的。如果研究對象是左駕國家，可以考慮移除這兩個狀態。**

### 3.1.1 目標與說明 <a id="311"></a>
**我們的主要目標是利用蒐集的資料集來改善機車駕駛行為的預測能力。為了保護使用者隱私，我們選擇不使用影像資訊，而是將機車的ECU和IMU資料作為主要的特徵資訊。我們希望透過這些資料的分析和預測，能夠提供更準確和有效的機車駕駛行為評估方法，並促進機車行駛安全和交通管理的發展。**
### 3.1.2 資料收集方法 <a id="312"></a>
**為了蒐集資料集，我們使用了Android平板來收集IMU資料。具體而言，我們將Android平板放置於機車後車箱中（車身中央），以獲取機車行駛時的加速度、角速度等數據。這樣的位置選擇可以減少來自不同位置的噪音干擾，同時我們使用Gopro攝影機來記錄整個採樣過程。這一方面可以方便後續對資料進行標記和驗證預測效果的準確度，另一方面也有助於對齊ECU和IMU資料。**

**此外，為了提高資料集的可行性，我們還記錄了GPS訊號和行駛路線的資訊如圖2、3。這些資料將有助於進一步分析機車駕駛行為與地理位置之間的關聯性，並為相關研究提供更多有價值的資源。**

**學區所對應資料集:0417_GPS.csv**
**夜市所對應資料集:0530_GPS.csv**

![Place_The_Luggage_In_The_Trunk](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/5102ba59-28f1-4ef3-a53b-0d9a0746e240)


**圖 1 ECU接收器與IMU感測器放置位子**



![學區取樣地圖-1](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/70cf1b6b-34b2-405d-ae9f-1482a667ce50)

# 圖 2 學區資料採集路線(左)，六類動作採集位置(右)，怠速則為機車停紅燈時


![忠孝夜市採集-2](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/270a88b0-5c7e-422c-99bb-4685119d9d21)


# 圖 3 夜市資料採集路線(左)，六類動作採集位置(右)，怠速則為機車停紅燈時


### 3.1.3 資料集蒐整流程 <a id="313"></a>

**準備Android平板和Gopro攝影機，確保它們正常運作並具備足夠的電量。
將Android平板放置於機車後車箱中心位置，以確保資料的準確性和一致性。**

**啟動Android平板上的IMU資料記錄程式，開始收集加速度、角速度等數據。
同時使用Gopro攝影機記錄整個採樣過程，以便後續資料標記和驗證。
在收集過程中同步記錄GPS訊號和行駛路線的資訊。完成資料收集後，對資料進行儲存和整理，確保資料的可讀性和可用性。
這樣的資料收集方法能夠提供充分且多樣化的機車駕駛行為資料，有助於進一步的分析和研究。**


![流程圖](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/cf53dc96-9baf-4711-ba0d-f378be8ac3d9)

**圖2 資料集蒐整流程**


### 3.1.4 資料屬性和特徵 <a id="314"></a>
**本資料集包含了多個變量和特徵，提供了詳細的機車駕駛行為資訊。具體而言，資料集中包含了當前時間、XYZ角速度、XYZ加速度、XYZ角度、TPS開度、引擎轉速等共計61項特徵。IMU資料已經經過校正並進行了min-max正規化，將數值映射至[0,1]之間，以確保資料的一致性和可用性。**

### 3.1.5 資料集的規模和範圍 <a id="315"></a>
#### 3.1.5.1 訓練資料集 <a id="3151"></a>
**訓練資料集的採集時間為2023年4月17日下午14時16分開始，總共採集了26分鐘，共計27578筆資料。資料集中包含了每個時間點的樣本數據，以及該時間範圍內的GPS詳細資訊（如經度、緯度、海拔、時間戳和速度等）。此外，資料集的採集時間選擇在非尖峰時刻的14:16，以確保資料的可靠性和一致性。**



![採集資料集當下車流_2](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/08035579-a54b-4d4f-a095-f96afb620a29)
**圖3 車流量較少資料集的實體環境**




#### 3.1.5.2 驗證資料集 <a id="3152"></a>
**驗證資料集的採集時間為2023年5月30日下午18時00分開始，總共採集了28分鐘，共計28009筆資料。資料集中包含了每個時間點的樣本數據，以及該時間範圍內的GPS詳細資訊（如經度、緯度、海拔、時間戳和速度等）。此外，資料集的採集時間選擇在尖峰時刻的18:00，以確保資料的可靠性和一致性。**



![採集資料集夜市](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/561c62bd-fff1-459a-b1f9-b7dfea10d156)

**圖4 車流量較多資料集的實體環境**

### 3.1.6 資料集的獨特性和價值 <a id="316"></a>

**這份資料集的獨特之處在於結合了機車的ECU和IMU資料，並提高了採集頻率。相較於現有的資料集，我們的資料集不僅提供了更豐富的特徵資訊，還包含了複雜環境下的駕駛情境。這樣的資料集填補了當前研究領域中在機車駕駛行為預測方面的缺口，並為相關研究提供了更具價值的資源和新的研究方向。**



### 3.1.7 資料集標記方法 <a id="317"></a>

**我們使用剪輯軟體Adobe Premiere將GoPro錄製的影片導入。由於剪輯軟體設定為24幀數（25進制），ECU採集的最小時間單位為0.01秒（1.00進制），因此，每一幀對應於ECU採集時間間隔為0.25秒。在剪輯軟體中，我們使用了標記功能。我們將標記的時間表示為分鐘:秒數:幀數，並與影片中ECU開始採集的時間標記進行相減，從而得到時間差(分鐘:秒數:幀數)。然後，我們將中間的差距轉換為秒數（從ECU開始採集到當前狀態經過的時間），從而準確判斷我在影片標記中的實際時間。在與資料集對應的幀數時進行標記，以盡量減小誤差。**

**這樣的標記方法能夠準確地將影片中的標記時間與資料集中的時間對應起來，並最大程度地減小誤差。**

![Adobe](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/80562d5b-1134-4c35-9491-d6fa249eb19a)
**圖 5 剪輯軟體Adobe Premiere 紅色框為剪輯軟體中時間，橘色框為影片中動作標記**


### 3.1.8 資料集的可用性和分享 <a id="318"></a>
**我們準備將這份資料集公開分享給其他研究人員，以促進相關領域的研究和發展。我們將提供資料集的存取方式和共享方式，以確保其他研究人員能夠方便地獲取和使用這份資料集。這將有助於促進知識交流和合作，並推動機車駕駛行為預測研究的進展。**



## 3.2 半自動標記演算法 <a id="32"></a>
**為了提高標記效率和準確性，我們提出了一種基於分群序列的半自動標記方法，以克服目前人工標記方式的耗時和效率低下的問題，並解決不同人員標記之間存在的差異性，從而間接提升標記結果的準確性。本方法結合了分群分析和機器學習技術的優勢。**

**首先，我們使用了Silhouette Score、Calinski-Harabasz Index、Davies-Bouldin Index、Elbow Method等算法，通過評估不同分群數量（即動作元素數量）的性能指標，以找尋最佳分群數量。這樣可以確保我們在後續分群過程中選擇了最適合的動作元素數量，從而提高駕駛行為特徵的提取效果。**

**接著，我們使用K-means分群算法對資料進行分群。通過將資料劃分為不同的群集，我們能夠捕捉到不同駕駛行為的特徵，並將其應用於後續的分類任務。這樣的分群方式不僅提高了效率，還能夠減少人工標記的主觀性和差異性。**

**在分群後，我們利用這些動作元素序列來訓練Vomm模型，我們建立一個能夠自動識別駕駛行為的模型，通過訓練好的模型進行預測，我們可以得到一個自動化的標記結果。**

**我們與人工標記結果進行比較，平均重疊率達到了約80%。相較於傳統的閾值設定和分類方法，本方法在標記效率和準確性方面都取得了顯著的提升。這一技術的引入不僅可以節省大量的標記時間和成本，還能夠確保標記結果的一致性和準確性，從而為相關研究和應用提供了更可靠的基礎。**

**這種基於分群序列的半自動標記方法為駕駛行為分析和研究領域帶來了重要的貢獻，並在標記效率和準確性方面取得了顯著的突破。**
## 3.3 VOMM的實作與參數設定 <a id="33"></a>
**在本研究中，我們選擇了VOMM（Variable Order Markov Model）演算法來建立序列模型。VOMM演算法是一種用於序列資料建模的方法，能夠根據給定的序列資料來學習模型的參數並進行預測。**

**在實作VOMM演算法時，我們需要設定幾個參數來進行模型的建構與訓練。其中，最重要的是上下文序列的長度(d)和符號的分群數(alphabet size)。**

**上下文序列的長度(d)指定了模型所考慮的最大上下文序列的長度。在我們的研究中，我們設定了一個上限值，只考慮長度小於等於d的上下文序列。這是為了在模型構建的過程中限制上下文的長度，以便在實際應用中獲得更好的預測性能。**

**符號的分群數(alphabet size)代表了可能觀察到的不同符號的數量。在VOMM演算法中，這個參數通常對應著模型的狀態數或分群數。透過設定適當的分群數，我們可以更好地捕捉序列資料中的隱藏結構和模式。**

**根據我們的實驗結果，在考慮的上下文序列長度(d)大於30時，我們觀察到增加上下文序列長度對預測機率的影響不大。因此，我們選擇在實作中設定上下文序列的長度(d)小於或等於30，以保證模型在預測性能和計算效率之間達到良好的平衡。**






















# 第四章 實驗結果 <a id="4"></a>
## 4.1 實驗設計 <a id="41"></a>
**本研究旨在提高駕駛行為標記的效率和準確性，並比較我們提出半自動標記演算法與閾值規則和傳統分類方法的性能。我們在研究中選擇了具有較低噪音品質的資料集作為訓練集，以更好地學習駕駛的多種行為。隨後，我們將訓練好的模型應用於車流量較高的測試集進行實際測試。**

**在實驗中，我們首先探索了利用慣性測量單元（Inertial Measurement Unit, IMU）資訊進行預處理的方法。然而，我們發現使用規則閾值方法進行預測存在彈性不足的問題。為了改進這一問題，我們引入了半自動標記演算法作為改進方案。**

**半自動標記演算法的流程如下：首先，我們使用Silhouette Score、Calinski-Harabasz Index、Davies-Bouldin Index和Elbow Method等算法來尋找最佳的分群數量（即動作元素數量）。這一步驟確保我們選擇了最適合的分群數量，以提高駕駛行為特徵的提取效果。**

**接下來，我們使用K-means分群算法對資料進行分群，以捕捉不同駕駛行為的特徵。這樣的分群方式不僅提高了效率，還減少了人工標記的主觀性和差異性。**

**在分群後，我們利用事先人工標記的駕駛行為，選取這些行為的動作元素序列來訓練Vomm模型，該模型能夠自動識別駕駛行為。透過訓練好的模型進行預測，我們獲得了自動化的標記結果。**

**為了比較半自動標記方法與閾值規則和傳統分類方法的性能，我們進行了相應的評估。根據實驗結果，我們觀察到半自動標記方法相較於傳統分類方法和閾值規則方法，在駕駛行為準確度和標記效率方面取得了優異的結果。**

**具體而言，我們的半自動標記方法在平均重疊率方面達到了約77%，而傳統分類方法和閾值規則方法分別為約50%和約7%。這顯示出半自動標記方法在駕駛行為準確度方面相對較高。**


| Time step | Accuracy| Go Straight | Idle | Turn Left | Turn Right | Two-Stage Left | U-turn |
|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|
| length_6   |75.665399 | 15.306122   | 96.130167 | 5.882353 | 11.25    | 40.776699     | 33.695652 |
| length_12  |67.237009 | 11.224490   | 82.937555 | 10.294118 | 15.00   | 39.805825     | 51.086957 |
| length_18  |62.167300 | 3.061224    | 77.396658 | 10.294118 | 11.25   | 39.805825     | 44.565217 |
| length_24  |57.351077 | 1.020408    | 73.175022 | 11.764706 | 8.75    | 26.213592     | 32.608696 |
| length_30  |56.210393 | 1.020408    | 70.272647 | 10.294118 | 12.50   | 31.067961     | 41.304348 |
| Filter_6   | 77.883397| 5.102041    | 98.944591 | 0.000000 | 15.00    | 46.601942     | 42.391304 |
| Filter_12  |75.602028 | 2.040816    | 94.986807 | 2.941176 | 16.25    | 45.631068     | 53.260870 |
| Filter_18  |66.793409 | 0.000000    | 84.872471 | 0.000000 | 15.00    | 32.038835     | 47.826087 |
| Filter_24  |59.125475 | 0.000000    | 76.693052 | 0.000000 | 1.25     | 27.184466     | 34.782609 |
| Filter_30  |59.505703 | 0.000000    | 74.054529 | 11.764706 | 0.00    | 40.776699     | 51.086957 |

**表1 使用我們提出演算法自動標記訓練Vomm預測**


| Model                                    | Accuracy | F1_Score | Recall              | Go Straight | Idle       | Turn Left | Turn Right | Two-Stage Left | U-turn |
|:--------:|:--------:|:--------:|:--------:|:--------:|:--------:|:--------:|:--------:|:--------:|:--------:|
| 支持向量機(Support Vector Machines)               | 0.50     | 0.333333 | 0.50   | 1.020408    | 100.000000 | 0.000000  | 0.00       | 16.504854      | 0.0    |
| 最近的鄰居(Nearest Neighbors)                        | 0.25     | 0.125000 | 0.25   | 8.163265    | 100.000000 | 0.000000  | 0.00       | 0.000000       | 0.0    |
| 決策樹(Decision Trees)                           | 0.25     | 0.166667 | 0.25   |12.244898   | 87.686895  | 2.941176  | 15.00      | 5.825243       | 0.0    |
| 隨機森林(Forests of randomized trees)              | 0.75     | 0.750000 | 0.75   |25.510204   | 80.386983  | 0.000000  | 8.75       | 9.708738       | 0.0    |
| 神經網路(Neural Network models)                    | 0.50     | 0.458333 | 0.50   |2.040816    | 99.824099  | 0.000000  | 0.00       | 3.883495       | 0.0    |
| 高斯過程(GaussianProcess)                           | 0.25     | 0.100000 | 0.25   |3.061224    | 99.824099  | 0.000000  | 0.00       | 0.0|0.0|

**表2 使用傳統分類演算法預測**

|  Time step | Accuracy | Go Straight | Idle     | Turn Left | Turn Right | Two-Stage Left | U-turn |
|:----------:|:-----------:|:-----------:|:-----------:|:-----------:|:-----------:|:-------------:|:-------------:|
| length_6    | 7.351077        | 100.0       | 1.583113 | 0.0       | 0.0        | 0.0            | 0.0    |
| Filter_6    | 6.210393        | 100.0       | 0.0      | 0.0       | 0.0        | 0.0            | 0.0    |
| length_12   | 6.210393        | 100.0       | 0.0      | 0.0       | 0.0        | 0.0            | 0.0    |
| Filter_12   | 6.210393        | 100.0       | 0.0      | 0.0       | 0.0        | 0.0            | 0.0    |
| length_18   | 6.210393        | 100.0       | 0.0      | 0.0       | 0.0        | 0.0            | 0.0    |
| Filter_18   | 6.210393        | 100.0       | 0.0      | 0.0       | 0.0        | 0.0            | 0.0    |
| length_24   | 6.210393        | 100.0       | 0.0      | 0.0       | 0.0        | 0.0            | 0.0    |
| Filter_24   | 6.210393        | 100.0       | 0.0      | 0.0       | 0.0        | 0.0            | 0.0    |
| length_30   | 6.210393        | 100.0       | 0.0      | 0.0       | 0.0        | 0.0            | 0.0    |
| Filter_30   | 6.210393        | 100.0       | 0.0      | 0.0       | 0.0        | 0.0            | 0.0    |

**表3 使用傳統閥值分四群訓練Vomm預測**

|Time step  | Accuracy | Go Straight | Idle    | Turn Left | Turn Right | Two-Stage Left | U-turn |
|:----------:|:-----------:|:-----------:|:-----------:|:-----------:|:-----------:|:-------------:|:-------------:|
| length_6    | 7.160963        | 95.918367   | 1.583113 | 0.0       | 0.0        | 0.0            | 1.086957 |
| Filter_6    | 6.083650        | 97.959184   | 0.0      | 0.0       | 0.0        | 0.0            | 0.0      |
| length_12   | 6.210393        | 100.0       | 0.0      | 0.0       | 0.0        | 0.0            | 0.0      |
| Filter_12   | 6.210393        | 100.0       | 0.0      | 0.0       | 0.0        | 0.0            | 0.0      |
| length_18   | 6.210393        | 100.0       | 0.0      | 0.0       | 0.0        | 0.0            | 0.0      |
| Filter_18   | 6.210393        | 100.0       | 0.0      | 0.0       | 0.0        | 0.0            | 0.0      |
| length_24   | 6.210393        | 100.0       | 0.0      | 0.0       | 0.0        | 0.0            | 0.0      |
| Filter_24   | 6.210393        | 100.0       | 0.0      | 0.0       | 0.0        | 0.0            | 0.0      |
| length_30   | 6.210393        | 100.0       | 0.0      | 0.0       | 0.0        | 0.0            | 0.0      |
| Filter_30   | 6.210393        | 100.0       | 0.0      | 0.0       | 0.0        | 0.0            | 0.0      |

**表4 使用傳統閥值分九群訓練Vomm預測**







| Time Step   | Accuracy   | Idle     | U-turn   | Turn Right | Turn Left | Go Straight | Two-Stage Left | 
|:----------:|:-----------:|:-----------:|:-----------:|:-----------:|:-----------:|:-------------:|:-------------:|
| Action      | Action      | 100.000  | 100.000  | 100.00     | 100.000   | 100.000      | 100.000        |
| length_6    | 77.820    | 95.954   | 28.260   | 42.50      | 25.000    | 3.061        | 55.339         | 
| Filter_6    | **81.368**    | 95.866   | 48.913   | 66.25      | 23.529    | 0.000        | 77.669         | 
| length_12   |  75.792   | 93.316   | 13.043   | 41.25      | 33.824    | 3.061        | 62.136         |  
| Filter_12   |77.693   | 93.316   | 22.826   | 45.00      | 38.235    | 0.000        | 79.612         |  
| length_18   | 74.715    | 91.645   | 1.087    | 40.00      | 41.176    | 3.061        | 70.874         |      
| Filter_18   | 76.362    | 91.821   | 1.087    | 53.75      | 51.471    | 0.000        | 79.612         |       
| length_24   | 74.208    | 91.381   | 0.000    | 47.50      | 41.176    | 4.081        | 60.194         |    
| Filter_24   | 74.271    | 91.381   | 0.000    | 45.00      | 50.000    | 0.000        | 61.165         |      
| length_30   | 71.039   | 88.391   | 0.000    | 45.00      | 27.941    | 3.061        | 56.311         |     
| Filter_30   |  70.722   | 88.391   | 0.000    | 45.00      | 25.000    | 0.000        | 56.311         |    


**表5 使用我們提出演算法自動標記(含部分ECU特徵)訓練Vomm預測**





**此外，我們觀察到半自動標記方法在各類駕駛行為的預測中表現良好。特別是對於耗時較長的駕駛行為（例如Two-Stage Left、U-turn），在參考的過去時間步越長時，其預測準確率越高。然而，對於較短耗時的駕駛行為（例如Turn Left、Turn Right），因為它為Two-Stage Left、U-turn的前置動作，故參考的過去時間步長度的增加對於預測，較短耗時的駕駛行為（例如Turn Left、Turn Right）準確率才會略有下降的現象，但並不影響整體的準確度。**

**綜上所述，半自動標記方法在駕駛行為標記的效率和準確性方面具有顯著的優勢。這一方法為駕駛行為分析和研究領域提供了一個可靠且高效的標記解決方案。這將有助於提高相關研究和應用的準確性和可靠性。**

## 4.2 探討最佳分群數 <a id="42"></a>

![Silhouette score - 畫圈](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/45898ad4-f5b6-44e8-994b-ec99d3666f54)
**圖 6 Silhouette Score**




![Davies-Bouldin score - 畫圖](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/8e494db8-66a7-44f5-b55e-8fec1c72c510)
**圖 7 Davies-Bouldin Index**



![Calinski-Harabasz Index - 畫圈](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/b076c61e-ba5a-4d67-bffc-ca85b51a208e)
**圖 8 Calinski-Harabasz Index**




![Elbow Method](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/b79f4630-4401-404a-8d72-6d86fc18dd35)
**圖 9 Elbow Method**





**在本研究中，我們使用了Silhouette Score、Calinski-Harabasz Index、Davies-Bouldin Index和Elbow Method等四種演算法，以探討最適合的分群數。我們嘗試了分群數為2、4、5、8和10，並觀察了這些數值下的結果。根據觀察，我們認為分群數為2的情況應該被排除，因為群數太少會使得各個動作之間的差異較難辨識和分類。分群數為5與4相似度較高，但在我們的實驗中未加入該數值，我們計劃在未來的研究中進一步探討這個數值的效果。因此，我們選擇了分群數為4、8和10進行觀察，以檢驗增加群數是否能提高準確度。**

**我們根據實驗中的結果，在使用6種駕駛行為動作作為輸入訓練VOMM模型時，每種動作各取4次序列並使用其他非該動作的序列進行驗證。根據觀察，分成4群的準確度效果最佳。**


### 4.2.1動作元素4群探討 <a name="421"></a>
| Model\Action   |   Go Straight Model |   Idle Model |   Turn Left Model |   Turn Right Model |   Two-Stage Left Model |   U-turn Model |
|:--------------:|:-------------------:|:------------:|:-----------------:|:------------------:|:----------------------:|:--------------:|
| Go Straight    |    **-20.05**           |       -22.21 |            -28.76 |             -22.47 |                 -22.11 |         -29.45 |
| Idle           |              -92.73 |     **-88.52**   |           -105.47 |             -92.05 |                -104    |        -114.46 |
| Turn Left      |              -17.32 |       -17.9  |            **-15.32** |             -18.98 |                 -23.41 |         -24.25 |
| Turn Right     |              -18.14 |       -17.98 |            -16.32 |            **-13.57** |                 -21.24 |         -18.31 |
| Two-Stage Left |              -57.87 |       -49.5  |            -43.74 |             -50.73 |                 **-25.53** |         -30.67 |
| U-turn         |              -57.72 |       -48.73 |            -43.8  |             -47.71 |                 -16.02 |         **-12.63** |
### 4.2.2 動作元素8群探討 <a name="422"></a>
| Model\Action   |   Go Straight Model |   Idle Model |   Turn Left Model |   Turn Right Model |   Two-Stage Left Model |   U-turn Model |
|:--------------:|:-------------------:|:------------:|:-----------------:|:------------------:|:----------------------:|:--------------:|
| Go Straight    |              **-23.63** |       -28.73 |            -30.61 |             -27.55 |                 -26.98 |         -26.02 |
| Idle           |             -100.9  |      -166.86 |           -119.82 |            -119.71 |                **-97.71** |        -133.69 |
| Turn Left      |              -26.94 |       -28.43 |            -26.13 |             -27.88 |                 -30.17 |         **-25.32** |
| Turn Right     |              -24.96 |       -19.25 |            **-17.92** |             -18.57 |                 -25.26 |         -19.27 |
| Two-Stage Left |              -66.58 |       -63.92 |            -57.76 |             -58.03 |                 **-27.13** |         -63.06 |
| U-turn         |              -37.29 |       -33.88 |            -29.78 |             -38.49 |                 -33.49 |         **-18.01** |
### 4.2.3 動作元素10群探討 <a name="423"></a>
| Model\Action   |   Go Straight Model |   Idle Model |   Turn Left Model |   Turn Right Model |   Two-Stage Left Model |   U-turn Model |
|:--------------:|:-------------------:|:------------:|:-----------------:|:------------------:|:----------------------:|:--------------:|
| Go Straight    |              **-33.97** |       -46    |            -38.95 |             -40.35 |                 -36.2  |         -49.81 |
| Idle           |             **-134.29** |      -177.38 |           -197.77 |            -203.78 |                -160.65 |        -212.08 |
| Turn Left      |              -43.15 |       **-34.11** |            -36.16 |             -38.73 |                 -44.93 |         -40.56 |
| Turn Right     |              -36.12 |       -33.1  |            **-32.1**  |             -32.62 |                 -38.47 |         -39.41 |
| Two-Stage Left |              -76.11 |       -68.34 |            -73.21 |             -73.05 |                 **-41.88** |         -46.66 |
| U-turn         |              -73.71 |       -60.91 |            -63.99 |             -64.36 |                 **-22.69** |         -24.47 |



**需要注意的是，我們所使用的分群數和實驗結果可能因資料集和特定情況而有所差異。因此，在選擇最佳分群數時，建議根據具體的實驗設計和資料分析來進行評估和選擇。**




## 4.3 傳統方法 <a id="43"></a>
### 4.3.1 六種駕駛行為與九軸特徵關係 <a id="431"></a>






![Relationship Between X-Axis Angular Velocity and 6 Driving Behaviors（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/961b6dc5-6b5e-49c6-adec-d0fda74a073a)

**圖 10 X軸角速度與六種駕駛行為關係圖**


![Relationship Between Y-Axis Angular Velocity and 6 Driving Behaviors（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/484510f3-1e6b-4682-a08b-77eeca7c3e15)

**圖 11 Y軸角速度與六種駕駛行為關係圖**

![Relationship Between Z-Axis Angular Velocity and 6 Driving Behaviors（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/37474790-6468-41c2-a1e0-c84fb88599ee)

**圖 12 Z軸角速度與六種駕駛行為關係圖**

![Relationship Between X-axis Acceleration and 6 Driving Behaviors（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/40e717c1-12b8-4997-a38f-dfe0fd051f10)

**圖 13 X軸加速度與六種駕駛行為關係圖**

![Relationship Between Y-axis Acceleration and 6 Driving Behaviors（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/e0634c30-4758-4d81-a622-e81b09f9537d)

**圖 14 Y軸加速度與六種駕駛行為關係圖**

![Relationship Between Z-axis Acceleration and 6 Driving Behaviors（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/ab8d0f2e-4ffd-41b1-987f-5c15ac01d759)

**圖 15 Z軸加速度與六種駕駛行為關係圖**
![Relationship Between X-axis Angle and 6 Driving Behaviors（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/b759bccf-23da-414a-8cff-9b8218c6e41d)

**圖 16 X角度與六種駕駛行為關係圖**
![Relationship Between Y-axis Angle and 6 Driving Behaviors（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/f57e513f-83db-43bf-9b75-cf143c9d9484)

**圖 17 Y角度與六種駕駛行為關係圖**

![Relationship Between Z-axis Angle and 6 Driving Behaviors（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/6913ecca-e4ba-4d17-888f-159a6e9775bb)

**圖 18 Z角度與六種駕駛行為關係圖**



### 4.3.2 轉至分類問題 <a id="432"></a>
**將從IMU收集的資料進行正規化或移動平均(Moving averge)處理後，可以輕鬆利用閾值規則的方法來識別車身目前的左偏或右偏情況。然而，對於非常相似的動作，無法準確進行預測。例如，左轉、待轉和迴轉都包含大量車身左偏的情況，因此無法準確預測，其他分類模型也無法準確預測出相似動作。**






![偏左偏右](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/24aec2f7-8b48-4bfb-8ff2-be5eea1ac9b7)

**圖 19 以Z軸角速度來判斷車身偏左或偏右**


## 4.4 序列與分群動作元素可視化 <a id="44"></a>
**我們將駕駛行為分為六組，分別是右轉 vs 左轉、右轉 vs 待轉、右轉 vs 迴轉、左轉 vs 待轉、左轉 vs 迴轉，以及直線 vs 待速。我們觀察了這六組駕駛行為序列和分群動作元素之間的關係。**

**在進行觀察時，我們發現最容易區分各類動作的是Z軸角速度。**
### 4.4.1 右轉 vs 左轉 <a id="441"></a>

| 角速度 | 加速度 |角度|
| :-: | :-: | :-: |
|![X-axis Angular Velocity Turn right vs Turn left（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/2af29677-2ba8-4674-a178-12040c100c27)|![X-axis Acceleration Turn right vs Turn left（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/2e9e6eaf-b2da-4808-8edf-ecd9032edfea)|![X-axis Angle Turn right vs Turn left（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/3f3db7ab-979f-4e67-a329-db137cf5b930)|

**圖 20右轉與左轉X軸的關係圖**

| 角速度 | 加速度 |角度|
| :-: | :-: | :-: |
|![Y-axis Angular Velocity Turn right vs Turn left（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/1fd7d9b8-16ce-483a-a732-bbd437b664f3)|![Y-axis Acceleration Turn right vs Turn left（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/e92f75d1-968d-4203-8cba-159cfd9888cb)|![Y-axis Angle Turn right vs Turn left（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/b00e2f2e-d3da-4344-93df-a0e4db0b4e73)|



**圖 21右轉與左轉Y軸的關係圖**


| 角速度 | 加速度 |角度|
| :-: | :-: | :-: |
|![Z-axis Angular Velocity Turn right vs Turn left（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/552f1626-7381-4f50-83fb-c9dc08766749)|![Z-axis Acceleration Turn right vs Turn left（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/9de5a1c5-5aca-4e4c-bf3a-44d5696ed9ba)|![Z-axis Angle Turn right vs Turn left（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/1cdb902d-505f-4d4f-86ab-d4d3fe8a98c3)|

**圖 22右轉與左轉Z軸的關係圖**




### 4.4.2 右轉 vs 迴轉 <a id="442"></a>

| 角速度 | 加速度 |角度|
| :-: | :-: | :-: |
|![X-axis Angular Velocity Turn right vs U-turn（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/e856eac3-ac97-405b-9d23-3fe69ecacf09)|![X-axis Acceleration Turn right vs U-turn（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/2a47bbfc-271c-471d-9cb0-36334bf041ec)|![X-axis Angle Turn right vs U-turn（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/ff6a85ef-199a-4940-b2bf-190b68e754b3)|


**圖 23 右轉與迴轉X軸的關係圖**


| 角速度 | 加速度 |角度|
| :-: | :-: | :-: |
|![Y-axis Angular Velocity Turn right vs U-turn（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/c264d41b-1fb7-4be3-acd3-9c9ef8e79eaf)|![Y-axis Acceleration Turn right vs U-turn（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/0af00585-783b-40a0-898c-56d73d314bf0)|![Y-axis Angle Turn right vs U-turn（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/a2bd1c90-ecde-4afd-8088-d63decba28d0)|

**圖 24 右轉與迴轉Y軸的關係圖**
| 角速度 | 加速度 |角度|
| :-: | :-: | :-: |
|![Z-axis Angular Velocity Turn right vs U-turn（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/93f6479f-dc3c-45ba-b949-f900df885ad7)|![Z-axis Acceleration Turn right vs U-turn（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/6c1cb19c-a899-45d4-854d-51dfdf75806b)|![Z-axis Angle Turn right vs U-turn（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/dd4a7a13-52c6-4ef9-b8bf-fb372404aa16)|


**圖 25 右轉與迴轉Z軸的關係圖**




### 4.4.3 右轉 vs 待轉 <a id="443"></a>


| 角速度 | 加速度 |角度|
| :-: | :-: | :-: |
|![X-axis Angular Velocity Turn right vs Two-stage left turn（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/0548301e-d02c-4f4d-bca5-d044fd1d1db5)|![X-axis Acceleration Turn right vs Two-stage left turn（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/61123e56-ddfb-4f1c-a9ba-fa1e7aa44313)|![X-axis Angle Turn right vs Two-stage left turn（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/015103f3-353b-4d44-8ddd-fc5727bc059c)|

**圖 26 右轉與待轉X軸的關係圖**

| 角速度 | 加速度 |角度|
| :-: | :-: | :-: |
|![Y-axis Angular Velocity Turn right vs Two-stage left turn（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/b30ae0d8-30b1-4723-92e2-2c52f1c6d237)|![Y-axis Acceleration Turn right vs Two-stage left turn（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/e735d332-a6be-42e1-9788-4f07b61c71c5)|![Y-axis Angle Turn right vs Two-stage left turn（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/6fedc48b-1a4f-414d-b5b9-46bd38630ba8)|

**圖 27 右轉與待轉Y軸的關係圖**



| 角速度 | 加速度 |角度|
| :-: | :-: | :-: |
|![Z-axis Angular Velocity Turn right vs Two-stage left turn（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/ed47e143-5b84-459b-85ed-c8ec0e0f40ec)|![Z-axis Acceleration Turn right vs Two-stage left turn（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/ec1ae560-cdd2-4153-946a-ef282c01e0b0)|![Z-axis Angle Turn right vs Two-stage left turn（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/8c7de990-d76e-47cb-bcf2-0300d9650131)|

**圖 28 右轉與待轉Z軸的關係圖**



### 4.4.4 左轉 vs 迴轉 <a id="444"></a>

| 角速度 | 加速度 |角度|
| :-: | :-: | :-: |
|![X-axis Angular Velocity Turn left vs U-turn（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/3da88cba-7939-4034-bd10-4fad7cdbdc8a)|![X-axis Acceleration Turn left vs U-turn（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/08e5db21-4656-4ea4-84f4-4f2ab6fdecae)|![X-axis Angle Turn left vs U-turn（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/7cf9c854-e48b-4bad-ad02-0e7f2150440d)|


**圖 29 左轉與迴轉X軸的關係圖**

| 角速度 | 加速度 |角度|
| :-: | :-: | :-: |
|![Y-axis Angular Velocity Turn left vs U-turn（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/56084f57-bf7b-44e3-8395-0344cc2cb486)|![Y-axis Acceleration Turn left vs U-turn（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/9b70be2c-7bee-4240-a4c0-b114378f6697)|![Y-axis Angle Turn left vs U-turn（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/80a8dafd-f0d7-4498-8d0c-bb2c94918af4)|



**圖 30 左轉與迴轉Y軸的關係圖**


| 角速度 | 加速度 |角度|
| :-: | :-: | :-: |
|![Z-axis Angular Velocity Turn left vs U-turn（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/534549e1-0abe-4324-b0ab-78522e232001)|![Z-axis Acceleration Turn left vs U-turn（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/fe09e18d-7193-4a44-a34d-3d8fbb0dcd42)|![Z-axis Angle Turn left vs U-turn（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/0eb14ea0-9066-40b9-8ad7-b73d2798b42d)|



**圖 31 左轉與迴轉Z軸的關係圖**







### 4.4.5 左轉 vs 待轉 <a id="445"></a>


| 角速度 | 加速度 |角度|
| :-: | :-: | :-: |
|![X-axis Angular Velocity Turn left vs Two-stage left turn（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/b02fcb09-5d54-4796-8ab4-ac262832aefb)|![X-axis Acceleration Turn left vs Two-stage left turn（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/2f930a3e-74ae-428b-8f3b-7a9e9f77f734)|![X-axis Angle Turn left vs Two-stage left turn（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/d7019406-cf7e-480d-8814-a65acc3a1e6c)|
**圖 32左轉與待轉X軸的關係圖**


| 角速度 | 加速度 |角度|
| :-: | :-: | :-: |
|![Y-axis Angular Velocity Turn left vs Two-stage left turn（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/cb8fd109-da3a-4cb3-aea0-5e03d2d71816)|![Y-axis Acceleration Turn left vs Two-stage left turn（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/07b7e9fe-373c-43da-ba98-44730a7dee22)|![Y-axis Angle Turn left vs Two-stage left turn（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/97b44297-e90c-404e-8e49-feb120e479bd)|


**圖 33左轉與待轉Y軸的關係圖**




| 角速度 | 加速度 |角度|
| :-: | :-: | :-: |
|![Z-axis Angular Velocity Turn left vs Two-stage left turn（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/8a415a69-c66b-48ad-8440-3a41ed691783)|![Z-axis Acceleration Turn left vs Two-stage left turn（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/23ad8ea5-ac76-4bf7-8899-7f4fcf9c8948)|![Z-axis Angle Turn left vs Two-stage left turn（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/8067cfd8-461f-4449-a735-a001be3cc84c)|

**圖 34左轉與待轉Z軸的關係圖**





### 4.4.6 直線 vs 怠速 <a id="446"></a>


| 角速度 | 加速度 |角度|
| :-: | :-: | :-: |
|![X-axis Angular Velocity Go straight vs Idle（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/247ee7e1-e729-40b4-b68b-22a7cfb5b596)|![X-axis Acceleration Go straight vs Idle（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/f3c4d862-2171-4220-bcea-b4657058abe1)|![X-axis Anfle Go straight vs Idle（unite）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/5f760daa-6c6f-48bf-a685-65c0ac7419da)|


**圖 35 直線與怠速X軸的關係圖**


| 角速度 | 加速度 |角度|
| :-: | :-: | :-: |
|![Y-axis Angular Velocity Go straight vs Idle（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/4bc597ee-e93e-40ff-aaf4-fb69a5256e4a)|![Y-axis Acceleration Go straight vs Idle（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/51964731-1414-48d2-a087-5f6aaef12cf9)|![Y-axis Anfle Go straight vs Idle（unite）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/4923c6a9-6472-4264-b0cc-6544da820da2)|


**圖 36 直線與怠速Y軸的關係圖**

| 角速度 | 加速度 |角度|
| :-: | :-: | :-: |
|![Z-axis Angular Velocity Go straight vs Idle（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/2ad44464-6391-4990-9c5c-436b69d0e209)|![Z-axis Acceleration Go straight vs Idle（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/a61fb1f3-dc64-4f08-b03e-003a814ad3a4)|![Z-axis Angle Go straight vs Idle（best）](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/d0e9f717-f0f2-4991-928e-e74f4b67a991)|

**圖 37 直線與怠速Z軸的關係圖**


## 4.5 PST與VOMM的時間序列預測結果評估 <a id="45"></a>
**在這一部分中，我們利用訓練好的六種駕駛行為模型，將資料集中的每筆資料輸入到這六個模型中。我們選擇預測機率最高的模型作為當下的駕駛行為動作，然後將預測結果與資料集中事先標記好的資料進行比對，以評估模型的準確度。**

**此外，我們也實驗了預測模型所需參考的過去時間長度，以達到最佳的準確度。由於平均一個駕駛動作約莫能在5秒內完成，我們以每秒取樣30次的頻率進行考量。因此，我們分別考慮了30、60、90、...、150個時間步來預測當前的駕駛行為，其準確度結果如表(1)所示。**


  
|      檔案名稱      |    資料集描述     |  總資料筆數  |  取樣頻率  |  動作元素分群  |  標記狀況  |
|:------------------:|:-----------------|:-------------:|:-----------:|:--------------:|:----------:|
|   Train_Data     | 時間：2023年4月17日14時16分開始<br>地點：學校附近<br>車人流量：少 |   27577筆   |  30Hz |      4群      |  12983筆 |
|    Test_Data     | 時間：2023年4月17日14時16分開始<br>地點：學校附近<br>車人流量：少 |   27577筆   |  30Hz |      4群      |  5774筆  |
  
**準確率計算是基於將預測結果與人工標記的資料進行比較，以確定成功率。**

**表 1 參考時間步與預測準確度關係**

|取樣頻率|　6　|取樣頻率　|　10　| 取樣頻率　|　30　|
| :-: | :-:  | :-: | :-: |  :-: | :-: | 

| 時間步 | 準確度 | 時間步 | 準確度 | 時間步 | 準確度 |
| :-: | :-:  | :-: | :-: |  :-: | :-: | 
|6   |**77.162630**|10   |72.689512|30   |**72.878421**|
|12   |70.069204|20   |**72.793354**|60  |71.735365|
|18   |66.262976|30  |61.526480|90  |69.674402|
|24   |62.456747|40 |60.280374|120 |64.807759|
|30   |61.159170|50  |56.490135|150  |60.980256|










**為了追求更高的準確度，我們發現預測錯誤的部分幾乎都出現在動作與動作之間的過渡期或是一連串預測中參雜少量預測錯誤。這是非常直觀的，因為動作之間的過渡期含有許多雜訊，增加了預測的困難度。為了解決這個問題，我們簡單設計一個過濾雜訊演算法，並重新進行預測。**









![圖片6](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/7131ed94-7970-4043-8a56-4f904263e264)


**圖 38 時間序列動作圖**

### 4.5.1 過濾動作演算法 <a id="451"></a>

**過濾動作演算法是一個用於過濾動作的函式，它接受兩個參數：DataSet（資料集）和frequency（頻率）。
<br>以下是該演算法的運作流程：
<br>1.初始化一個空的 filtered_data 列表，用於儲存過濾後的資料。
<br>2.初始化 previous_action 變數為 None，用於追蹤前一個動作。
<br>3.使用 enumerate 函式遍歷資料集中的每個動作，獲取索引 i 和動作值 action。
<br>4.如果當前動作與前一個動作不相同，進入過濾判斷的流程
<br>5.從資料集中取出一個長度為 2*frequency 的window（即 2 秒的資料），並將其儲存為 window 變數。
<br>6.如果window中的眾數與當前動作相同，表示當前動作與前一個動作不符是因為動作轉換屬於正常現象，因此直接跳過該動作。
<br>7.否則，進入下一個判斷步驟。
<br>8.檢查當前一個點過去與未來的window（範圍為 i-frequency 到 i+frequency）的眾數是否與當前動作相同。
<br>9.如果兩者眾數不相同，表示window中和前一個點window中都沒有正確的眾數存在。根據第一種情況，將當前動作更改為window中的眾數。
<br>10.如果兩者眾數相同，表示前一個點的資訊是正確的。根據第二種情況，將當前動作更改為前一個點的動作值。
<br>11.將更新後的動作值加入到 filtered_data 列表中。
<br>12.更新 previous_action 為當前動作。
<br>13.迭代結束後，返回 filtered_data 列表作為過濾後的資料集。**

**這個演算法通過比較動作的眾數來過濾可能的錯誤或雜訊。如果一個動作在window中的眾數與該動作本身相同，則該動作被視為正確的。如果window中的眾數與當前動作不同，則通過比較前一個點的window眾數與當前動作來判斷是否保留當前動作或更改為前一個點的動作。這樣的過濾方法可以幫助消除一些噪聲或錯誤的動作，從而提高資料集的品質，結果顯示其準確度提升，如表(2)所示。**

|取樣頻率　|　6　|取樣頻率　|　10　| 取樣頻率|　30　|
| :-: | :-:  | :-: | :-: |  :-: | :-: | 

| 時間步 | 準確度 | 時間步 | 準確度 | 時間步 | 準確度 |
| :-: | :-:  | :-: | :-: |  :-: | :-: | 
|6  |**79.325260**|10  |**77.414330**|30  |**78.714929**|
|12  |76.557093|20 |72.793354|60  |74.350537|
|18   |71.799308|30   |63.499481|90  |69.674402|
|24   |64.532872|40   |61.370717|120  |69.899550|
|30   |61.159170|50  |56.697819|150 |62.088673|



**從實驗結果觀察得知，使用過濾動作演算法能夠提高準確度，但仍然無法達到完美的預測。**




**以上所述的修正策略旨在提升模型的準確度，以更好地應用於駕駛行為預測**

## 4.6 實驗結果討論與解釋 <a id="46"></a>
**在本節中，我們將討論和解釋我們使用VOMM模型和相應的演算法所得到的實驗結果。這些結果顯示了該模型在駕駛行為預測方面的優越性，並提供了一些關於模型性能和應用的洞察和解釋。**

**首先，我們的實驗結果表明，使用VOMM模型進行駕駛行為預測可以取得令人滿意的結果。相比於傳統的規則閾值方式，VOMM模型具有更高的彈性和適應性，能夠捕捉到更多的行為模式和變化。這使得我們的模型能夠更準確地預測駕駛行為，提供更精確的行為分類和判斷。**

**同時，我們的模型僅使用IMU資料，而不使用影像資訊。這不僅有助於保護使用者的隱私，還大大提高了預測的計算效率，實現了即時（Realtime）預測。這對於在實際應用中獲得快速和準確的結果非常重要，並有助於減少任務的計算負擔。**

**此外，我們的實驗結果還提供了一些關於模型參數設定和性能評估的洞察。透過系統地調整VOMM模型中的上下文序列長度和分群數，我們發現當上下文序列長度(d)小於或等於30時，模型的預測性能達到了較好的平衡。這意味著在實際應用中，我們可以設定一個相對較小的上下文序列長度，同時保持良好的預測能力，從而節省計算資源並提高效率。**

**綜上所述，我們的實驗結果顯示了使用VOMM模型進行駕駛行為預測的優勢。這一方法在彈性、隱私保護和計算效率方面都具有優勢，並為駕駛行為分析和安全**








<br>
<br>
<br>
<br>
<br>

### Deep ConvLSTM with self-attention for human activity decoding using wearables.
https://github.com/isukrit/encodingHumanActivity/tree/master

|EPOCH|準確度	|Recall	|F1 Score|
| :-: | :-: | :-: | :-: | 
|1|0.812312047	|0.398903237	|0.176339798|
|2|0.811781355	|0.399257032	|0.166666667|
|3|0.812312047	|0.398195648	|0.170760696|
|4|0.815142402	|0.392711834	|0.183297015|
|5|0.811781355	|0.399257032	|0.166666667|
|6|0.814257916	|0.394303909	|0.189491538|
|7|0.815673094	|0.391473554	|0.185|
|8|0.811958252	|0.398903237	|0.1675|
|9|0.812312047	|0.398195648	|0.176339798|
|10|0.811781355	|0.399257032	|0.166666667|





# 第五章 結論 <a id="5"></a>
**在本研究中，我們探索了駕駛行為預測的方法和技術，旨在提高交通安全和駕駛體驗。我們介紹了兩種不同的資料集，也介紹兩種方法VOMM與規則閥值方法，並對它們進行了詳細的實作和參數設定。**

**首先，我們利用K-means演算法將駕駛行為資料進行分群，並引入了VOMM演算法，我們進一步探討了VOMM模型的實作和參數設定，並發現在適當的上下文序列長度和分群數設定下，VOMM模型能夠提供準確的駕駛行為預測。**

**最後，我們對我們的研究進行了總結和討論。我們的實驗結果表明，使用VOMM模型進行駕駛行為預測可以獲得優越的結果，相比於傳統的規則閾值方式，VOMM模型具有更高的準確性和彈性。同時，我們的模型只使用了IMU資料，而不依賴於影像資訊，這有助於保護使用者的隱私並提高預測的計算效率。**

**總而言之，本研究的目標是探索並提出有效的方法和技術來預測駕駛行為。我們的實驗結果和討論表明， VOMM模型在駕駛行為預測方面都具有潛力和優勢。這些研究成果為交通安全領域提供了有價值的洞察和解決方案，並為未來進一步的研究和應用奠定了基礎。我們相信這些方法和技術將對交通系統的智能化和駕駛體驗的改進做出重要貢獻。**
