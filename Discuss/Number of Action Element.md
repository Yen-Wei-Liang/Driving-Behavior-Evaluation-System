


[模型訓練輸入值與測試輸入值參考](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/blob/main/Discuss/Chart/input.txt)


### （*****）依Action Element數量為5建立的 Probabilistic Suffix Tree model<a name="5-pst-10"></a>

| Model\Action | Go Straight | Idle | Turn Left | Turn Right | Two-Stage Left | U-turn |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| Go Straight Model | -15.50|-95.75| -28.14|-22.37| -42.94 |-48.48  | 
| Idle Model|-13.71 |-80.81 |-22.24| -16.22 | -38.66 |-61.27 |
| Turn Left Model | -12.27| -97.31|-24.13| -23.13 |-39.16  |-46.75 |
| Turn Right Model |-12.27 | -97.31|-24.13| -23.13 | -39.16 |-46.75 |
| Two-Stage Left Model |-15.69 | -99.91|-23.81| -25.28 | -27.58 | -23.80|
| U-turn Model | -19.33| -125.78|-33.04| -25.37 | -36.12 |-20.83 |










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


