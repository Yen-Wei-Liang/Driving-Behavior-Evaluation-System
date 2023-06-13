# 目錄
* [第一章 簡介](#1)
* [第二章 相關工作](#2)
  * [2.1 交通事故風險與高齡駕駛者相關研究報導](#21)
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
  * [3.2 分群K-means演算法的實作與參數設定](#32)
  * [3.3 VOMM的實作與參數設定](#33)
* [第四章 實驗結果](#4)
  * [4.1 實驗設計](#41)
  * [4.2 探討最佳分群數](#42)
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














# 第一章 簡介 <a id="1"></a>
**隨著人口結構的變化，高齡人口比例在我國以及全球內持續增加，這對社會和交通安全帶來了重大挑戰。根據最新統計資料，我國自101年至111年間的十年間，高齡人口比例從11.53%上升至17.56%。預計到114年時，高齡人口比例將達到20%。這個持續增長的趨勢需要我們關注和解決，以應對相應的挑戰。**

**首先，全球和國內高齡人口比例增加是一個普遍現象，這是由於醫療技術的進步和生活品質的提高，人們的壽命得以延長。然而，這種人口結構的變化對交通系統產生了直接的影響，因為高齡人口在駕駛行為和道路安全方面面臨著特定的挑戰。**

**特別是高齡駕駛者在交通事故中面臨著更高的風險。隨著年齡的增長，身體和認知能力逐漸下降，這可能影響到他們的駕駛技能和反應能力。因此，高齡駕駛者在遇到危險情況時可能更容易受到影響，並導致交通事故的發生。這對社會安全和個人安全都帶來了嚴重影響，需要我們採取措施來提高交通安全並減少高齡駕駛者在道路上的風險。**

**在交通安全領域，駕駛行為辨識一直是一個重要的研究話題。IEEE（電機與電子工程師學會）提供了多種方法和技術，駕駛行為辨識是一個重要的研究領域，尤其對於應對高齡駕駛者的挑戰而言更為關鍵。傳統的基於規則閥值的方法在彈性和泛化能力方面可能存在不足，因此需要更先進的方法來應對這一挑戰。**

**近年來，機器學習和人工智能技術在駕駛行為辨識方面取得了重大進展。通過使用大量的資料和深度學習算法，可以從駕駛者的行為模式中學習和提取特徵，從而實現更準確的行為辨識。例如，可以使用影像資訊或傳感器資料來收集駕駛者的行為資訊，如加速度、角速度、角度、目前車前畫面或者是目前駕駛畫面等。然後，這些資料都可以輸入至深度學習模型。**

**另外，還可以使用傳感器技術，如眼動傳感器、心率監測器等，來獲取更多有關駕駛者狀態和行為的信息。這些資料可以用於訓練模型，以識別疲勞、分心、酒駕或其他不正常行為。**

**除了單獨的駕駛行為辨識，還可以使用這些技術來開發駕駛輔助系統，例如疲勞駕駛檢測系統、預警系統或自動緊急制動系統等，以提高駕駛安全性。
需要指出的是，這些技術在實際應用中仍面臨一些挑戰，例如影像資訊隱私保護、影像運算量過大、系統可靠性和硬體設施成本與使用者接受度等。因此，研究人員和相關機構需要繼續努力，以克服這些問題並確保這些技術的有效應用。**

**用於分析和識別駕駛者的行為模式。然而，傳統的基於規則的方法存在彈性和泛化能力不足的問題。因此，我們需要更先進的方法來應對高齡駕駛者的行為辨識挑戰。**

**綜上所述在本研究中，我們提出了一個評估系統的概念，旨在實時評估高齡駕駛者的適應性和安全性。首先必須要克服規則閥值方法所缺乏的彈性與泛化性，我們先將駕駛行為分解為多個動作元素，並利用動作元素的組合來來建立行為辨識模型（如VOMM或PST），以準確預測高齡駕駛者的駕駛行為。通過評估駕駛行為的準確性，我們可以提供政府和相關單位一個有效的工具，用於評估高齡駕駛者是否適合持有駕照。**

**這樣的評估系統有助於提升交通安全並減少高齡駕駛者在道路上的風險。它為政府和相關單位提供了一個有效的工具，用於評估駕駛者的適應性和安全性。透過這種方式，我們可以更好地保護高齡駕駛者和其他路上使用者的安全，並建立更加安全和可持續的交通環境。**

**為了達到這個目標，本研究將使用機車上的ECU紀錄和IMU上的資料，並進行預處理以確保資料的可靠性和有效性。我們將採用分群K-means演算法將資料分群，以獲取駕駛行為的特徵，並利用Silhouette Score、Calinski-Harabasz Index、Davies-Bouldin Index、Elbow Method，等演算法找尋最佳分群數(最佳動作元素數量)然後，我們將應用傳統演算法PST和VOMM，利用這些動作元素的時間序列進行駕駛行為的預測。**

**最後，我們將根據預測結果和評估駕駛行為的準確性，提供建議和參考給政府和相關單位，作為是否發放駕照給高齡駕駛者的重要依據。這將有助於建立一個更公平、更可靠的駕駛者評估制度，提高交通安全性，並確保高齡駕駛者的安全。**




















# 第二章 相關工作 <a id="2"></a>

## 2.1 交通事故風險與高齡駕駛者相關研究報導 <a id="21"></a>
**隨著人口老齡化趨勢的加劇，高齡駕駛者的交通事故風險日益受到關注。
該研究旨在了解高齡駕駛者在交通事故風險方面的表現，統計駕駛行為、身體健康狀況、認知功能和社會支持等方面的資料。**

**研究結果顯示，幾個關鍵因素與高齡駕駛者的交通事故風險密切相關。首先，身體健康狀況被確定為一個重要的預測因素。身體機能的衰退，如視力和聽力下降，以及身體活動能力的減弱，可能使高齡駕駛者在駕駛時面臨更大的挑戰和風險。**

**此外，認知功能的變化也是交通事故風險的一個關鍵因素。隨著年齡增長，認知功能可能會受到衰退的影響，包括記憶力、注意力和反應能力等方面。這些變化可能會影響高齡駕駛者對道路環境的感知和駕駛能力，增加交通事故的風險。**


**此外，社會支持也被證明在交通事故風險方面起著重要作用。高齡駕駛者若能獲得家人、朋友或社區的支持和幫助，他們更有可能維持良好的駕駛能力和安全意識。這種社會支持可以包括提供代步服務、陪同駕駛或與其他駕駛者分享交通負擔等方式，以減輕高齡駕駛者的壓力和風險。**

**研究的結果強調了針對高齡駕駛者的交通安全措施的重要性。基於這些發現，相關機構和社區可以採取一系列的措施來減少高齡駕駛者的交通事故風險。這些措施可以包括定期身體健康檢查，提供駕駛能力評估和培訓，以及提供交通代步選項和社會支持網路等。**

**同時，教育和宣傳活動也是至關重要的，旨在提高高齡駕駛者對自身身體和認知變化的認識，並促使他們主動關注交通安全問題。這可以透過舉辦工作坊、分發宣傳資料和在社區中舉辦討論會等方式來實現。**

**總結而言，瞭解高齡駕駛者的交通事故風險以及影響因素是制定相應政策和措施的關鍵。通過重視高齡駕駛者的身體健康、認知功能和社會支持，我們可以更好地保障他們的交通安全，同時確保他們能夠保持獨立和參與社區活動。**

**如樣本來自特定地區，仍需要進一步研究來更全面地瞭解交通事故風險與高齡駕駛者之間的關係。然而，這項研究為我們提供了一個重要的起點，以促進交通安全和駕駛者福祉的努力。**

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

**此外，為了提高資料集的可行性，我們還記錄了GPS訊號和行駛路線的資訊。這些資料將有助於進一步分析機車駕駛行為與地理位置之間的關聯性，並為相關研究提供更多有價值的資源。**

![Place_The_Luggage_In_The_Trunk](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/assets/127264553/5102ba59-28f1-4ef3-a53b-0d9a0746e240)


**圖 1 ECU接收器與IMU感測器放置位子**



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
## 3.2 分群K-means演算法的實作與參數設定 <a id="32"></a>
**在應用K-means演算法之前，我們對資料進行正規化或標準化處理，以確保各個特徵具有相同的尺度。這有助於避免某些特徵對分群結果產生過大的影響，我們了解到K-means演算法在不同的初始值下可能會有些微差異，儘管這些差異可能不大。為了避免這些差異對實驗結果產生影響，我們進行了十次K-means演算法的運行，並從這十次運行的結果中選取眾數來確定最終的分群結果。這樣做可以增加結果的穩定性和可靠性。**
## 3.3 VOMM的實作與參數設定 <a id="33"></a>
**在本研究中，我們選擇了VOMM（Variable Order Markov Model）演算法來建立序列模型。VOMM演算法是一種用於序列資料建模的方法，能夠根據給定的序列資料來學習模型的參數並進行預測。**

**在實作VOMM演算法時，我們需要設定幾個參數來進行模型的建構與訓練。其中，最重要的是上下文序列的長度(d)和符號的分群數(alphabet size)。**

**上下文序列的長度(d)指定了模型所考慮的最大上下文序列的長度。在我們的研究中，我們設定了一個上限值，只考慮長度小於等於d的上下文序列。這是為了在模型構建的過程中限制上下文的長度，以便在實際應用中獲得更好的預測性能。**

**符號的分群數(alphabet size)代表了可能觀察到的不同符號的數量。在VOMM演算法中，這個參數通常對應著模型的狀態數或分群數。透過設定適當的分群數，我們可以更好地捕捉序列資料中的隱藏結構和模式。**

**根據我們的實驗結果，在考慮的上下文序列長度(d)大於30時，我們觀察到增加上下文序列長度對預測機率的影響不大。因此，我們選擇在實作中設定上下文序列的長度(d)小於或等於30，以保證模型在預測性能和計算效率之間達到良好的平衡。**






















# 第四章 實驗結果 <a id="4"></a>
## 4.1 實驗設計 <a id="41"></a>
**本研究選擇了具有較低噪音品質的資料集（即車流量較小的情況）作為訓練集，以期更好地學習駕駛的多種行為。接著，利用已經訓練完成的模型對車流量較高的測試集進行實際測試。**

**在實驗中，我們首先探索了利用慣性測量單元（Inertial Measurement Unit, IMU）資訊進行預處理的方法。我們將駕駛行為的問題轉化為分類問題，並使用規則閥值方法進行預測。然而，我們驗證了該方法存在彈性不足的問題。**

**隨後，我們進行了實驗測試以確定最佳的分群數量。使用了Silhouette Score、Calinski-Harabasz Index、Davies-Bouldin Index和Elbow Method等四種演算法，首先縮小了最佳分群數量的範圍。然後，我們使用不同的分群數量建立模型，並進行簡單的預測判斷以評估準確度是否提高。**

**此外，由於某些駕駛行為難以判斷，例如直線行駛轉換為右轉動作，因為高頻率取樣的情況下，中間過渡階段的數據也會增加。因此，我們額外訓練了一個過渡階段的模型，並探討增加過渡階段模型預測能否提升整體準確度。**

**最後，我們使用模型對資料集進行預測，並與之前人工標記的部分進行比對，以確定準確度。**
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

**我們根據表1中的結果，在使用6種駕駛行為動作作為輸入訓練VOMM模型時，每種動作各取4次序列並使用其他非該動作的序列進行驗證。根據觀察，分成4群的準確度效果最佳。**

表1 

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
**將從IMU收集的資料進行正規化或移動平均(Moving averge)處理後，可以輕鬆利用閾值規則的方法來識別車身目前的左偏或右偏情況。然而，對於非常相似的動作，無法準確進行預測。例如，左轉、待轉和迴轉都包含大量車身左偏的情況，因此無法準確預測，其他分類模型做預測如表1。**

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

| 時間步 | 準確度 |
| :-: | :-: | 
|30  (1 Sec) |**72.878421**|
|60  (2 Sec) |71.735365|
|90  (3 Sec) |69.674402|
|120 (4 Sec) |64.807759|
|150 (5 Sec) |60.980256|










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



| 時間步 | 準確度 |
| :-: | :-: | 
|30  (1 Sec) |**78.714929**|
|60  (2 Sec) |74.350537|
|90  (3 Sec) |69.674402|
|120 (4 Sec) |69.899550|
|150 (5 Sec) |62.088673|



**從實驗結果觀察得知，使用過濾動作演算法能夠提高準確度，但仍然無法達到完美的預測。**




**以上所述的修正策略旨在提升模型的準確度，以更好地應用於駕駛行為預測**

## 4.6 實驗結果討論與解釋 <a id="46"></a>
**在本節中，我們將討論和解釋我們使用VOMM模型和相應的演算法所得到的實驗結果。這些結果顯示了該模型在駕駛行為預測方面的優越性，並提供了一些關於模型性能和應用的洞察和解釋。**

**首先，我們的實驗結果表明，使用VOMM模型進行駕駛行為預測可以取得令人滿意的結果。相比於傳統的規則閾值方式，VOMM模型具有更高的彈性和適應性，能夠捕捉到更多的行為模式和變化。這使得我們的模型能夠更準確地預測駕駛行為，提供更精確的行為分類和判斷。**

**同時，我們的模型僅使用IMU資料，而不使用影像資訊。這不僅有助於保護使用者的隱私，還大大提高了預測的計算效率，實現了即時（Realtime）預測。這對於在實際應用中獲得快速和準確的結果非常重要，並有助於減少任務的計算負擔。**

**此外，我們的實驗結果還提供了一些關於模型參數設定和性能評估的洞察。透過系統地調整VOMM模型中的上下文序列長度和分群數，我們發現當上下文序列長度(d)小於或等於30時，模型的預測性能達到了較好的平衡。這意味著在實際應用中，我們可以設定一個相對較小的上下文序列長度，同時保持良好的預測能力，從而節省計算資源並提高效率。**

**綜上所述，我們的實驗結果顯示了使用VOMM模型進行駕駛行為預測的優勢。這一方法在彈性、隱私保護和計算效率方面都具有優勢，並為駕駛行為分析和安全**



















# 第五章 結論 <a id="5"></a>
**在本研究中，我們探索了駕駛行為預測的方法和技術，旨在提高交通安全和駕駛體驗。我們介紹了兩種不同的資料集，也介紹兩種方法VOMM與規則閥值方法，並對它們進行了詳細的實作和參數設定。**

**首先，我們利用K-means演算法將駕駛行為資料進行分群，並引入了VOMM演算法，我們進一步探討了VOMM模型的實作和參數設定，並發現在適當的上下文序列長度和分群數設定下，VOMM模型能夠提供準確的駕駛行為預測。**

**最後，我們對我們的研究進行了總結和討論。我們的實驗結果表明，使用VOMM模型進行駕駛行為預測可以獲得優越的結果，相比於傳統的規則閾值方式，VOMM模型具有更高的準確性和彈性。同時，我們的模型只使用了IMU資料，而不依賴於影像資訊，這有助於保護使用者的隱私並提高預測的計算效率。**

**總而言之，本研究的目標是探索並提出有效的方法和技術來預測駕駛行為。我們的實驗結果和討論表明， VOMM模型在駕駛行為預測方面都具有潛力和優勢。這些研究成果為交通安全領域提供了有價值的洞察和解決方案，並為未來進一步的研究和應用奠定了基礎。我們相信這些方法和技術將對交通系統的智能化和駕駛體驗的改進做出重要貢獻。**
