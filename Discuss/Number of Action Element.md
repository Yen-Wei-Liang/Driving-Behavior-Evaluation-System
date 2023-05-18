


[模型訓練輸入值與測試輸入值參考](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/blob/main/Discuss/Chart/input.txt)

## 使用資料集(一秒採樣5次)
### （*****）依Action Element數量為5建立的 Probabilistic Suffix Tree model<a name="5-pst-10"></a>

| Model\Action | Go Straight | Idle | Turn Left | Turn Right | Two-Stage Left | U-turn |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| Go Straight Model | -15.50|-95.75| -28.14|-22.37| -42.94 |-48.48  | 
| Idle Model|-13.71 |-80.81 |-22.24| -16.22 | -38.66 |-61.27 |
| Turn Left Model | -12.27| -97.31|-24.13| -23.13 |-39.16  |-46.75 |
| Turn Right Model |-12.27 | -97.31|-24.13| -23.13 | -39.16 |-46.75 |
| Two-Stage Left Model |-15.69 | -99.91|-23.81| -25.28 | -27.58 | -23.80|
| U-turn Model | -19.33| -125.78|-33.04| -25.37 | -36.12 |-20.83 |



## 使用資料集(一秒採樣6次)
### 先取樣再分群依Action Element數量為5
| Model\Action   |   Go Straight Model |   Idle Model |   Turn Left Model |   Turn Right Model |   Two-Stage Left Model |   U-turn Model |
|:--------------:|:-------------------:|:------------:|:-----------------:|:------------------:|:----------------------:|:--------------:|
| Go Straight    |              -18.78 |       -19.6  |            -19.36 |             -16.18 |                 -19.2  |         -17.68 |
| Idle           |             -100    |      -126.84 |           -119.46 |            -127.62 |                -112.25 |        -132.72 |
| Turn Left      |              -27.38 |       -24.3  |            -24.61 |             -19.94 |                 -31.3  |         -26.41 |
| Turn Right     |              -27.38 |       -24.3  |            -24.61 |             -19.94 |                 -31.3  |         -26.41 |
| Two-Stage Left |              -32.76 |       -56.42 |            -54.01 |             -56.41 |                 -28.2  |         -30.94 |
| U-turn         |              -29.98 |       -54.63 |            -57.56 |             -56.27 |                 -19.97 |         -24.15 |


### 先分群Action Element數量為5 在取樣
| Model\Action   |   Go Straight Model |   Idle Model |   Turn Left Model |   Turn Right Model |   Two-Stage Left Model |   U-turn Model |
|:--------------:|:-------------------:|:------------:|:-----------------:|:------------------:|:----------------------:|:--------------:|
| Go Straight    |             -107.79 |      -102.53 |           -123.54 |            -101.56 |                -110.5  |         -98.55 |
| Idle           |             -820.69 |      -635.95 |           -756.46 |            -655.72 |                -812.5  |        -720.2  |
| Turn Left      |             -208.58 |      -168.87 |           -185.16 |            -178.31 |                -183.12 |        -183.2  |
| Turn Right     |             -168.76 |      -158.03 |           -168.59 |            -153.88 |                -167.31 |        -144.45 |
| Two-Stage Left |             -252.69 |      -201.55 |           -240.35 |            -218.51 |                -243.64 |        -245.45 |
| U-turn         |             -155.82 |      -143.88 |           -171.78 |            -185.21 |                -178.88 |        -174.63 |

### 先取樣再分群依Action Element數量為8


| Model\Action   |   Go Straight Model |   Idle Model |   Turn Left Model |   Turn Right Model |   Two-Stage Left Model |   U-turn Model |
|:--------------:|:-------------------:|:------------:|:-----------------:|:------------------:|:----------------------:|:--------------:|
| Go Straight    |              -24.81 |       -23.78 |            -19.45 |             -19.56 |                 -26.73 |         -24.23 |
| Idle           |             -126.14 |      -150.24 |           -184.89 |            -155.21 |                -135.01 |        -189.17 |
| Turn Left      |              -36.71 |       -36.34 |            -37.86 |             -31.53 |                 -42.03 |         -50.27 |
| Turn Right     |              -34.01 |       -33.53 |            -38.76 |             -30.34 |                 -38.16 |         -36.58 |
| Two-Stage Left |              -42.2  |       -58.92 |            -65.35 |             -59.51 |                 -38.21 |         -54.22 |
| U-turn         |              -37.31 |       -60.41 |            -63.24 |             -63.08 |                 -21.84 |         -26.22 |


# 取樣每秒3次

### 依Action Element數量為5

| Model\Action   |   Go Straight Model |   Idle Model |   Turn Left Model |   Turn Right Model |   Two-Stage Left Model |   U-turn Model |
|:--------------:|:-------------------:|:------------:|:-----------------:|:------------------:|:----------------------:|:--------------:|
| Go Straight    |              -10.05 |        -9.31 |             -7.37 |              -6.73 |                 -10.14 |         -12.41 |
| Idle           |              -55.18 |       -49.93 |            -51.9  |             -51.87 |                 -57.99 |         -86.53 |
| Turn Left      |              -13.86 |       -10.16 |            -11.4  |              -7.49 |                 -11.89 |         -14.99 |
| Turn Right     |              -13.86 |       -10.16 |            -11.4  |              -7.49 |                 -11.89 |         -14.99 |
| Two-Stage Left |              -25.59 |       -23.45 |            -24.89 |             -25.09 |                 -16.23 |         -21.56 |
| U-turn         |              -30.09 |       -22.43 |            -22.39 |             -21.93 |                 -11.18 |          -8.93 |


### 依Action Element數量為8

| Model\Action   |   Go Straight Model |   Idle Model |   Turn Left Model |   Turn Right Model |   Two-Stage Left Model |   U-turn Model |
|:--------------:|:-------------------:|:------------:|:-----------------:|:------------------:|:----------------------:|:--------------:|
| Go Straight    |              -11.82 |        -9.21 |            -10.46 |             -10.59 |                 -11.75 |         -13.77 |
| Idle           |              -57.91 |       -75.66 |            -71.88 |             -72.17 |                 -73.22 |        -103.65 |
| Turn Left      |              -25.15 |       -18.56 |            -16.44 |             -16.47 |                 -19.06 |         -20.77 |
| Turn Right     |              -15.41 |       -14.5  |            -16.82 |             -11.55 |                 -15.92 |         -19.43 |
| Two-Stage Left |              -30.12 |       -32.74 |            -26.36 |             -27    |                 -18.77 |         -25.59 |
| U-turn         |              -36.93 |       -27.88 |            -28.68 |             -25.67 |                 -12.54 |         -11.4  |


### 依Action Element數量為9



| Model\Action   |   Go Straight Model |   Idle Model |   Turn Left Model |   Turn Right Model |   Two-Stage Left Model |   U-turn Model |
|:--------------:|:-------------------:|:------------:|:-----------------:|:------------------:|:----------------------:|:--------------:|
| Go Straight    |              -14.52 |        -9.41 |            -10.75 |              -9.22 |                 -12.88 |         -12.65 |
| Idle           |              -70.07 |       -77.46 |            -83.66 |             -85.14 |                 -73.45 |        -100.13 |
| Turn Left      |              -28.11 |       -21.11 |            -17.09 |             -18.24 |                 -19.33 |         -22.62 |
| Turn Right     |              -17.32 |       -15.72 |            -16.34 |             -11.35 |                 -16.49 |         -19.41 |
| Two-Stage Left |              -35.19 |       -32.39 |            -31.51 |             -28.35 |                 -20.07 |         -28.75 |
| U-turn         |              -38.92 |       -27.94 |            -28.68 |             -26.15 |                 -12.38 |         -12.42 |

### 依Action Element數量為10

| Model\Action   |   Go Straight Model |   Idle Model |   Turn Left Model |   Turn Right Model |   Two-Stage Left Model |   U-turn Model |
|:--------------:|:-------------------:|:------------:|:-----------------:|:------------------:|:----------------------:|:--------------:|
| Go Straight    |              -10.91 |        -9.89 |            -11.14 |             -13.83 |                 -12.09 |         -13.24 |
| Idle           |             -130.12 |      -120.02 |            -87.9  |             -90.6  |                -135.92 |        -130.61 |
| Turn Left      |              -17.57 |       -16.91 |            -20.74 |             -22.7  |                 -17.33 |         -21.16 |
| Turn Right     |              -12.66 |       -17.55 |            -16.7  |             -16.28 |                 -15.76 |         -19.58 |
| Two-Stage Left |              -38.99 |       -31.97 |            -33.47 |             -30.2  |                 -26.28 |         -30.17 |
| U-turn         |              -37.85 |       -15.72 |            -16.72 |             -16.45 |                 -19.71 |         -18.94 |





### 分八群    ..............訓練4  測試輸入2個序列


| Model\Action   |   Go Straight Model |   Idle Model |   Turn Left Model |   Turn Right Model |   Two-Stage Left Model |   U-turn Model |
|:--------------:|:-------------------:|:------------:|:-----------------:|:------------------:|:----------------------:|:--------------:|
| Go Straight    |              -30.08 |       -32.24 |            -38.97 |             -29.86 |                 -32.3  |         -44.46 |
| Idle           |             -144.72 |      -178.21 |           -207.47 |            -170.3  |                -150.66 |        -234.62 |
| Turn Left      |              -30.19 |       -30.21 |            -32.67 |             -28.63 |                 -35.4  |         -37.7  |
| Turn Right     |              -31.02 |       -28.88 |            -29.79 |             -31.65 |                 -29.55 |         -38.24 |
| Two-Stage Left |              -53.14 |       -62.48 |            -72.12 |             -64.01 |                 -39.23 |         -54.07 |
| U-turn         |              -33.68 |       -25.28 |            -26.63 |             -23.67 |                 -11.99 |         -11.4  |







### 分八群    ..............訓練4  測試輸入2個序列





| Model\Action   |   Go Straight Model |   Idle Model |   Turn Left Model |   Turn Right Model |   Two-Stage Left Model |   U-turn Model |
|:--------------:|:-------------------:|:------------:|:-----------------:|:------------------:|:----------------------:|:--------------:|
| Go Straight    |              -23.11 |       -15.79 |            -27.18 |             -27.35 |                 -27.85 |         -34.29 |
| Idle           |             -101.99 |      -178.37 |           -168.58 |            -147.45 |                -142.58 |        -218.07 |
| Turn Left      |              -43.84 |       -34.67 |            -32.64 |             -31.93 |                 -36.33 |         -40.68 |
| Turn Right     |              -27.19 |       -28.76 |            -26.54 |             -23.45 |                 -31.16 |         -33.34 |
| Two-Stage Left |              -54.17 |       -56.52 |            -52.49 |             -50.32 |                 -41.08 |         -48.48 |
| U-turn         |              -36.93 |       -27.88 |            -28.68 |             -25.67 |                 -12.54 |         -11.4  |






## 使用資料集(一秒採樣30次)
### （一）依不同Action Element數量 model 成功預測紀錄<a name="5-pst-9"></a>


| Model\Action | Go Straight | Idle | Turn Left | Turn Right | Two-Stage Left | U-turn |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| 3 Action Element | X | O | X| O|O|X|
| 4 Action Element | X | O|X |X|O|X|
| 5 Action Element | O |O |X |X|O|O|
| 6 Action Element |X | O | X| X|X|O|
| 7 Action Element |X |O  | X| X|O|O|

### （二）依Action Element數量為3建立的 Probabilistic Suffix Tree model<a name="5-pst-3"></a>



| Model\Action | Go Straight | Idle | Turn Left | Turn Right | Two-Stage Left | U-turn |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| Go Straight Model | -62.74| -133.77 |-106.10 | -92.16 |-137.98 |-109.52|
| Idle Model |-66.97 | -75.77 | -100.55| -89.29 |-124.76 |-94.52|
| Turn Left Model | -59.11| -130.01 |-99.65 | -78.78 |-129.81 |-103.75|
| Turn Right Model |-64.05 | -132.22 |-94.48 | -82.40 |-130.12 |-104.26|
| Two-Stage Left Model |-59.50 | -122.29 |-98.05 | -79.30 |-121.22 |-107.94|
| U-turn Model |-57.84 | -133.95 | -97.32| -90.83 |-123.65 |-104.29|



### （三）依Action Element數量為4建立的 Probabilistic Suffix Tree model<a name="5-pst-4"></a>


| Model\Action | Go Straight | Idle | Turn Left | Turn Right | Two-Stage Left | U-turn |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| Go Straight Model |-72.24 | -469.78 | -119.27 | -106.15 | -128.43|-399.24|
| Idle Model |-74.74 | -410.81 | -109.42 | -103.99 |-122.94 |-120.63|
| Turn Left Model | -68.89| -447.09 | -112.32 | -105.74 | -211.04|-262.01|
| Turn Right Model | -72.38| -443.72 | -114.42 | -99.63 | -274.71|-404.63|
| Two-Stage Left Model | -76.81| -476.10 | -118.96 | -98.76 |- 119.89|-86.93|
| U-turn Model  | -74.35| -470.22 | -123.69|-111.21 | -139.58 | -93.70|




### （四）依Action Element數量為5建立的 Probabilistic Suffix Tree model<a name="5-pst-5"></a>

| Model\Action | Go Straight | Idle | Turn Left | Turn Right | Two-Stage Left | U-turn |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| Go Straight Model |-84.87 |-631.23 |-156.77 | -141.64 | -307.47 |-371.02 |
| Idle Model |-90.19 |-511.87 |-120.63 | -120.87 | -155.38 | -130.26|
| Turn Left Model | -87.09| -593.48| -154.95| -129.28 |-314.68  |-372.49 |
| Turn Right Model | -93.23|-594.41 |-148.46 | -124.96 | -312.54 | -371.83|
| Two-Stage Left Model | -86.15| -555.75| -124.14| -114.91 |-149.07  |-130.09 |
| U-turn Model | -96.00| -625.50| -168.38| -127.63 |-195.94  | -118.97|


### （五）依Action Element數量為6建立的 Probabilistic Suffix Tree model<a name="5-pst-6"></a>



| Model\Action | Go Straight | Idle | Turn Left | Turn Right | Two-Stage Left | U-turn |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| Go Straight Model | -102.23| -636.02 |-165.63 |-150.30 |-323.41 |-366.17|
| Idle Model| -112.14| -533.41 | -136.61| -141.45|-162.37 |-165.23|
| Turn Left Model| -100.77| -695.52 | -176.30| -146.77|-336.25 |-373.58|
| Turn Right Model |-105.28 |-680.83  |-152.45 |-150.00 |-318.50 |-367.04|
| Two-Stage Left Model |-100.82 | -586.15 | -147.01| -141.74|-168.38 |-139.13|
| U-turn Model| -100.04| -765.01 | -200.08| -166.23| -232.76|-121.90|


### （五）依Action Element數量為7建立的 Probabilistic Suffix Tree model<a name="5-pst-7"></a>


| Model\Action | Go Straight | Idle | Turn Left | Turn Right | Two-Stage Left | U-turn |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| Go Straight Model |-105.45 | -737.68 |-176.86 | -161.66|-342.78|-384.07|
| Idle Model|  -120.36 | -565.65| -151.93|-161.47|-176.26|-167.28|
| Turn Left Model|-103.28 | -751.49 |-183.53 | -168.88|-343.32|-379.71|
| Turn Right Model | -108.95| -741.25 | -196.71|-167.32 |-338.96|-383.35|
| Two-Stage Left Model | -108.76| -645.94 | -161.05| -150.45|-160.30|-133.47|
| U-turn Model | -123.47 | -740.18| -195.66|-195.58|-223.13|-119.36|


