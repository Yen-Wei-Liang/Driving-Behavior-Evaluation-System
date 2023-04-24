## Actions: idling, going straight, turning right, turning left, two-stage left turning, turning, two sequence data for each action

Action.csv : 12 sequence action data

Case_1.csv : Normalization + Kmean (divided into 5 groups)

Case_2.csv : Normalization + PCA (9 elements) + Kmean (divided into 5 groups)

Case_3.csv: Normalization + PCA (4 elements) + Kmean (divided into 5 groups)

## Case1 : Normalization + Kmean

|Action|Base Action|Number|Rate|
|:-:|:-:|:-:|:-:|
|Go straight 1|0|12|23.08|
|Go straight 1|1|0|0|
|Go straight 1|2|18|34.62|
|Go straight 1|3|10|19.23|
|Go straight 1|4|12|23.08|
|Go straight 2|0|26|46.43|
|Go straight 2|1|0|0|
|Go straight 2|2|15|26.79|
|Go straight 2|3|9|16.07|
|Go straight 2|4|6|10.71|
|Idle 1|0|52|89.66|
|Idle 1|1|0|0|
|Idle 1|2|6|10.34|
|Idle 1|3|0|0|
|Idle 1|4|0|0|
|Idle 2|0|37|52.86|
|Idle 2|1|0|0|
|Idle 2|2|18|25.71|
|Idle 2|3|11|15.71|
|Idle 2|4|4|5.71|
|Trun left 1|0|22|29.33|
|Trun left 1|1|0|0|
|Trun left 1|2|25|33.33|
|Trun left 1|3|11|14.67|
|Trun left 1|4|17|22.67|
|Turn left 2|0|16|20.51|
|Turn left 2|1|0|0|
|Turn left 2|2|29|37.18|
|Turn left 2|3|6|7.69|
|Turn left 2|4|27|34.62|
|Turn right 1|0|31|42.47|
|Turn right 1|1|0|0|
|Turn right 1|2|18|24.66|
|Turn right 1|3|8|10.96|
|Turn right 1|4|16|21.92|
|Turn right 2|0|25|37.31|
|Turn right 2|1|0|0|
|Turn right 2|2|21|31.34|
|Turn right 2|3|7|10.45|
|Turn right 2|4|14|20.9|
|Two-stage left turn 1|0|54|54.55|
|Two-stage left turn 1|1|38|38.38|
|Two-stage left turn 1|2|3|3.03|
|Two-stage left turn 1|3|3|3.03|
|Two-stage left turn 1|4|1|1.01|
|Two-stage left turn 2|0|51|58.62|
|Two-stage left turn 2|1|30|34.48|
|Two-stage left turn 2|2|1|1.15|
|Two-stage left turn 2|3|4|4.6|
|Two-stage left turn 2|4|1|1.15|
|U-trun 1|0|4|5.63|
|U-trun 1|1|53|74.65|
|U-trun 1|2|6|8.45|
|U-trun 1|3|4|5.63|
|U-trun 1|4|4|5.63|
|U-turn 2|0|3|3.7|
|U-turn 2|1|59|72.84|
|U-turn 2|2|10|12.35|
|U-turn 2|3|7|8.64|
|U-turn 2|4|2|2.47|

## Case1 : Centers

||X-axis Angular Velocity|Y-axis Angular Velocity|Z-axis Angular Velocity|X-axis Acceleration|Y-axis Acceleration|Z-axis Acceleration|X-axis Angle|Y-axis Angle|Z-axis Angle|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|Group 0|0.709223555|0.733413843|0.206165427|0.355683052|0.534956072|0.604279648|0.420169569|0.741768367|0.131780889|
|Group 1|0.431342918|0.411600086|0.688949873|0.445824701|0.515307789|0.605584159|0.411932711|0.677216222|0.138203881|
|Group 2|0.713007164|0.705948145|0.217150747|0.509190213|0.334886101|0.616319834|0.233106304|0.527913106|0.156434844|
|Group 3|0.714613983|0.722941127|0.232255527|0.647268411|0.63057995|0.574324285|0.541521476|0.119462382|0.183838694|
|Group 4|0.697118085|0.692942373|0.206140252|0.390488134|0.730843458|0.508902158|0.657228458|0.89580011|0.30755167|




## Case 2 : Normalization + PCA(9) + Kmean

|Action|Base Action|Number|Rate|
|:-:|:-:|:-:|:-:|
|Go straight 1|0|12|23.08|
|Go straight 1|1|0|0|
|Go straight 1|2|12|23.08|
|Go straight 1|3|10|19.23|
|Go straight 1|4|18|34.62|
|Go straight 2|0|26|46.43|
|Go straight 2|1|0|0|
|Go straight 2|2|6|10.71|
|Go straight 2|3|9|16.07|
|Go straight 2|4|15|26.79|
|Idle 1|0|49|84.48|
|Idle 1|1|0|0|
|Idle 1|2|0|0|
|Idle 1|3|0|0|
|Idle 1|4|9|15.52|
|Idle 2|0|37|52.86|
|Idle 2|1|0|0|
|Idle 2|2|4|5.71|
|Idle 2|3|11|15.71|
|Idle 2|4|18|25.71|
|Trun left 1|0|21|28|
|Trun left 1|1|0|0|
|Trun left 1|2|17|22.67|
|Trun left 1|3|11|14.67|
|Trun left 1|4|26|34.67|
|Turn left 2|0|16|20.51|
|Turn left 2|1|0|0|
|Turn left 2|2|27|34.62|
|Turn left 2|3|6|7.69|
|Turn left 2|4|29|37.18|
|Turn right 1|0|29|39.73|
|Turn right 1|1|0|0|
|Turn right 1|2|15|20.55|
|Turn right 1|3|8|10.96|
|Turn right 1|4|21|28.77|
|Turn right 2|0|24|35.82|
|Turn right 2|1|0|0|
|Turn right 2|2|14|20.9|
|Turn right 2|3|7|10.45|
|Turn right 2|4|22|32.84|
|Two-stage left turn 1|0|54|54.55|
|Two-stage left turn 1|1|38|38.38|
|Two-stage left turn 1|2|1|1.01|
|Two-stage left turn 1|3|3|3.03|
|Two-stage left turn 1|4|3|3.03|
|Two-stage left turn 2|0|51|58.62|
|Two-stage left turn 2|1|30|34.48|
|Two-stage left turn 2|2|1|1.15|
|Two-stage left turn 2|3|4|4.6|
|Two-stage left turn 2|4|1|1.15|
|U-trun 1|0|4|5.63|
|U-trun 1|1|53|74.65|
|U-trun 1|2|4|5.63|
|U-trun 1|3|4|5.63|
|U-trun 1|4|6|8.45|
|U-turn 2|0|3|3.7|
|U-turn 2|1|60|74.07|
|U-turn 2|2|2|2.47|
|U-turn 2|3|7|8.64|
|U-turn 2|4|9|11.11|


## Case2 : Centers

||Component 1|Component 2|Component 3|Component 4|Component 5|Component 6|Component 7|Component 8|Component 9|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|Group 0|-0.14136422|0.098940355|-0.075854349|-0.023293167|-0.025273801|0.002695079|-0.008050485|-0.017050601|-0.005195443|
|Group 1|0.501098191|0.025172289|0.003413016|-0.006213414|-0.010176565|-0.006264785|-0.007058141|-0.001821962|0.000895609|
|Group 2|-0.139746109|0.387128209|0.164105228|0.026858622|0.078411574|0.0045789|0.023836205|0.034673309|0.010552249|
|Group 3|-0.135939645|-0.396702566|0.4243703|0.001222564|-0.092316215|0.019260072|-0.008250624|-0.003269974|0.001313017|
|Group 4|-0.109293876|-0.253947686|-0.151083055|0.033073205|0.053051539|-0.009927131|0.011903404|0.014567899|0.00191913|



## Case 3 : Normalization + PCA(4) + Kmean



|Action|Base Action|Number|Rate|
|:-:|:-:|:-:|:-:|
|Go straight 1|0|15|28.85|
|Go straight 1|1|2|3.85|
|Go straight 1|2|11|21.15|
|Go straight 1|3|11|21.15|
|Go straight 1|4|13|25|
|Go straight 2|0|10|17.86|
|Go straight 2|1|4|7.14|
|Go straight 2|2|18|32.14|
|Go straight 2|3|11|19.64|
|Go straight 2|4|13|23.21|
|Idle 1|0|34|58.62|
|Idle 1|1|0|0|
|Idle 1|2|18|31.03|
|Idle 1|3|1|1.72|
|Idle 1|4|5|8.62|
|Idle 2|0|16|22.86|
|Idle 2|1|0|0|
|Idle 2|2|28|40|
|Idle 2|3|16|22.86|
|Idle 2|4|10|14.29|
|Trun left 1|0|23|30.67|
|Trun left 1|1|3|4|
|Trun left 1|2|8|10.67|
|Trun left 1|3|28|37.33|
|Trun left 1|4|13|17.33|
|Turn left 2|0|24|30.77|
|Turn left 2|1|4|5.13|
|Turn left 2|2|7|8.97|
|Turn left 2|3|21|26.92|
|Turn left 2|4|22|28.21|
|Turn right 1|0|12|16.44|
|Turn right 1|1|1|1.37|
|Turn right 1|2|10|13.7|
|Turn right 1|3|25|34.25|
|Turn right 1|4|25|34.25|
|Turn right 2|0|8|11.94|
|Turn right 2|1|1|1.49|
|Turn right 2|2|9|13.43|
|Turn right 2|3|31|46.27|
|Turn right 2|4|18|26.87|
|Two-stage left turn 1|0|38|38.38|
|Two-stage left turn 1|1|0|0|
|Two-stage left turn 1|2|43|43.43|
|Two-stage left turn 1|3|11|11.11|
|Two-stage left turn 1|4|7|7.07|
|Two-stage left turn 2|0|36|41.38|
|Two-stage left turn 2|1|0|0|
|Two-stage left turn 2|2|26|29.89|
|Two-stage left turn 2|3|20|22.99|
|Two-stage left turn 2|4|5|5.75|
|U-trun 1|0|17|23.94|
|U-trun 1|1|0|0|
|U-trun 1|2|23|32.39|
|U-trun 1|3|12|16.9|
|U-trun 1|4|19|26.76|
|U-turn 2|0|16|19.75|
|U-turn 2|1|4|4.94|
|U-turn 2|2|19|23.46|
|U-turn 2|3|21|25.93|
|U-turn 2|4|21|25.93|


## Case3 : Centers

||Component 5|Component 6|Component 7|Component 9|
|:-:|:-:|:-:|:-:|:-:|
|Group 0|0.029911107|0.068532348|-0.034005581|-0.001832198|
|Group 1|0.286265631|0.317287546|0.038190456|-0.021470701|
|Group 2|-0.02846863|-0.085903692|-0.056282232|-0.005875602|
|Group 3|-0.121307965|0.048443323|0.047412944|0.001963997|
|Group 4|0.108820132|-0.083452731|0.060011519|0.010223869|



## Data Normalization Visualize

### Left or Right
![Left or Right](https://raw.githubusercontent.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/main/Discuss/20230423/Normalization%20%2B%20Z%E8%A7%92%E9%80%9F%E5%BA%A6_%E5%81%8F%E5%B7%A6%E5%81%8F%E5%8F%B3%E8%A1%8C%E7%82%BA.png)


### Driving Behavior
![Driving Behavior](https://raw.githubusercontent.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/main/Discuss/20230423/Normalization%20%2B%20Z%E8%A7%92%E9%80%9F%E5%BA%A6_%E5%88%A4%E6%96%B7%E8%A1%8C%E7%82%BA.png)





