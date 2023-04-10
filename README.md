# Driving-Behavior-Evaluation-System


## I. Description:
##### Intelligent Motorcycle Driving Behavior Online Diagnosis, Detection, and Evaluation System.

## II. Dataset Construction:

### A. Axis Data Collection:

#### ．Equipment used: ASUS ZenPad 3s 10 LTE

<div style="display:flex">
    <img src="https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/blob/main/Axis_App/%E5%AF%A6%E9%9A%9B%E5%9F%B7%E8%A1%8C%E7%95%AB%E9%9D%A2Screen1.jpg?raw=true" style="width:45%">
    <img src="https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/blob/main/Axis_App/%E5%AF%A6%E9%9A%9B%E5%9F%B7%E8%A1%8C%E7%95%AB%E9%9D%A2Screen2.jpg?raw=true" style="width:45%">
</div>


#### ．Software used: MIT App Inventor
![MIT App Inventor](https://user-images.githubusercontent.com/127264553/230847516-f5b062d1-43f3-4634-8423-a5a9dbfd3ac7.png)
<div style="display:flex">
    <img src="https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/blob/main/Axis_App/Screen1.png?raw=true" style="width:45%">
    <img src="https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/blob/main/Axis_App/Screen2.png?raw=true" style="width:45%">
</div>

#### ．Physical testing:

##### (To be updated)

### B. ECU Data Collection:

#### ．Hardware introduction:

### C. Data merging:
##### The absolute time characteristics of the data acquisition are used to align and merge the data. Since Axis samples 30 times per second and ECU collects 2 to 4 times per second (K-Line), the ECU data is duplicated and displayed repeatedly to align with Axis time.


## III. Semi-automatic labeling

##### K-means clustering is used to observe data characteristics, and the Elbow Method, Silhouette Score, and Gap Statistic are used to test the effectiveness of appropriate clustering. Adobe Premiere video editing software is used with a 24-frame-per-second interval and a minimum ECU interval of 0.01 seconds, with a 0.04-second interval paired with video frames and manually labeled driving behaviors with a GoPro camera (to reduce actual errors). The clustering results are compared to the manually labeled corresponding relationships, and the entire DataSet is labeled using the trained model.


## IV. Analyzing Sequential Data

### Transformer Model
