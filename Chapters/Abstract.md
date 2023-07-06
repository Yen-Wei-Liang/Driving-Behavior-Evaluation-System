### [回目錄](../ReadMe.md)
# Abstract 

<br>

**According to statistics from the Ministry of Transportation, motorcycle accidents account for 78% of the total traffic accidents. In order to enhance the safety of motorcycle riders, we propose a proactive motorcycle driver behavior tracking method called RideTrack. RideTrack enables online tracking of motorcycle driving behavior, including straight-line riding, right turns, left turns, U-turns, and waiting for turns.**
**The establishment of the RideTrack model is based on regularly collected IMU (Inertial Measurement Unit) and motorcycle ECU (Engine Control Unit) sensor data. We first construct a dataset of sensor data sequences and utilize our proposed automatic labeling method to convert the sensor data sequence dataset into a labeled sequence dataset. Then, we use these labeled sequences to construct a Variable Length Markov Model (VLMM) model. Finally, RideTrack utilizes this model for real-time behavior detection and tracking to analyze driving behavior.**