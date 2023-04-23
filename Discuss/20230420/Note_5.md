## Actions: idling, going straight, turning right, turning left, two-stage left turning, turning, two sequence data for each action

Action.csv : 12 sequence action data

Case_1.csv : Normalization + Kmean (divided into 5 groups)

Case_2.csv : Normalization + PCA (9 elements) + Kmean (divided into 5 groups)

Case_3.csv: Normalization + PCA (4 elements) + Kmean (divided into 5 groups)

## Case1 : Normalization + Kmean

|Action|Base Action|Number|
|:-:|:-:|:-:|
|Idle 1 ||58|
||Base Action 0 | 52 |
||Base Action 1 | 6 |
|Idle 2 ||70|
||Base Action 0 | 37 |
||Base Action 1 | 18 |
||Basse Action 3 | 11 |
||Base Action 4 | 4 |
|Go straight 1 || 52 |
||Base Action 0 | 11 |
||Base Action 1 | 18 |
||Base Action 3 | 10 |
||Base Action 4 | 13 |
|Go straight 2 || 56 |
||Base Action 0 | 26 |
||Base Action 1 | 15 |
||Base Action 3 | 9 |
||Base Action 4 | 6 |
|Turn left 1 || 75  |
||Base Action 0 | 22 |
||Base Action 1 | 25 |
||Base Action 3 | 11 |
||Base Action 4 | 17 |
|Turn left 2|| 78 |
||Base Action 0 | 15 |
||Base Action 1 | 29 |
||Base Action 3 | 6 |
||Base Action 4 | 28 |
|Turn right 1 ||73|
||Base Action 0 | 31 |
||Base Action 1 | 18 |
||Base Action 3 | 8 |
||Base Action 4 | 16 |
|Turn right 2 || 67 |
||Base Action 0 | 64 |
||Base Action 1 | 21 |
||Base Action 3 | 7 |
||Base Action 4 | 15 |
|Two-stage left turn 1 || 99 |
||Base Action 0 | 54 |
||Base Action 1 | 3 |
||Base Action 2 | 38 |
||Base Action 3 | 3 |
||Base Action 4 | 1 |
|Two-stage left turn 2 || 87 |
||Base Action 0 | 51 |
||Base Action 1 | 1 |
||Base Action 2 | 30 |
||Base Action 3 | 4 |
||Base Action 4 | 1 |
|U-turn 1 || 71 |
||Base Action 0 | 4 |
||Base Action 1 | 6 |
||Base Action 2 | 52 |
||Base Action 3 | 5 |
||Base Action 4 | 4 |
|U-turn 2 || 81 |
||Base Action 0 | 3 |
||Base Action 1 | 10 |
||Base Action 2 | 59 |
||Base Action 3 | 7 |
||Base Actoin 4 | 2 |


## Case 2 : Normalization + PCA(9) + Kmean

| Action | Base Action | Total |
|:--:|:--:|:--:|
|Idle 1 || 58 |
||Base Action 0 | 8 |
||Base Action 2 | 50 |
|Idle 2 || 37 |
||Base Action 0 | 18 |
||Base Action 1 | 4 |
||Base Action 2 | 37 |
||Base Action 3 | 11 |
|Go straight 1 || 52 |
||Base Action 0 | 18 |
||Base Action 1 | 12 |
||Base Acrion 2 | 12 |
||Base Action 3 | 10 |
|Go straight 2 || 56 |
||Base Action 0 | 15 |
||Base Action 1 | 6 |
||Base Action 2 | 26 |
||Base Action 3 | 9 |
|Trun left 1 || 75 |
||Base Action 0 | 26 |
||Base Action 1 | 17 |
||Base Action 2 | 21 |
||Base Action 3 | 11 |
|Turn left 2 || 78 |
||Base Action 0 | 29 |
||Base Action 1 | 27 |
||Base Action 2 | 16 |
||Base Action 3 | 6 |
|Turn right 1 || 73 |
||Base Action 0 | 21 |
||Base Action 1 | 16 |
||Base Action 2 | 28 |
||Base Action 3 | 8 |
|Trun right 2 || 67 |
||Base Action 0 | 22 |
||Base Action 1 | 14 |
||Base Action 2 | 24 |
||Base Action 3 | 7 |
|Two-stage left turn 1 || 99 |
||Base Action 0| 3 |
||Base Action 1| 1 |
||Base Action 2| 54 |
||Base Action 3| 3 |
||Base Action 4| 38 |
|Two-stage left turn 2 || 87 |
||Base Action 0| 1 |
||Base Action 1| 1 |
||Base Action 2| 51 |
||Base Action 3| 4 |
||Base Action 4| 30 |
|U-turn 1 || 71 |
||Base Action 0 | 6 |
||Base Action 1 | 4 |
||Base Action 2 | 4 |
||Base Action 3 | 4 |
||Base Action 4 | 53 |
|U-turn 2 || 81 |
||Base Action 0 | 9 |
||Base Action 1 | 2 |
||Base Action 2 | 3 |
||Base Action 3 | 7 |
||Base Action 4 | 60 |


## Case 3 : Normalization + PCA(4) + Kmean

|Action|Base Action|Total|
|:--:|:--:|:--:|
|Idle 1 || 58 |
||Base Action 1 | 31 |
||Base Action 2 | 1 |
||Base Action 3 | 22 |
||Base Action 4 | 4 |
|Idle 2 || 70 |
||Base Action 1 | 14 |
||Base Action 2 | 16 |
||Base Action 3| 29 |
||Base Action 4 | 11 |
|Go straight 1 || 52 |
||Base Action 0 | 2 |
||Base Action 1 | 15 |
||Base Action 2 | 11 |
||Base Action 3 | 11 |
||Base Action 4 | 13 |
|Go straight 2 || 56 |
||Base Action 0 | 4 |
||Base Action 1 | 10 |
||Base Action 2 | 11 |
||Base Action 3 | 18 |
||Base Action 4 | 13 |
|Trun left 1 || 75 |
||Base Action 0 | 3 |
||Base Action 1 | 24 |
||Base Action 2 | 27 |
||Base Action 3 | 8 |
||Base Action 4 | 13 |
|Trun left 2 || 78 |
||Base Action 0 | 4 |
||Base Action 1 | 25 |
||Base Action 2 | 19 |
||Base Action 3 | 8 |
||Base Action 4 | 22 |
|Trun right 1 || 73 |
||Base Action 0 | 1 |
||Base Action 1 | 12 |
||Base Action 2 | 25 |
||Base Action 3 | 10 |
||Base Action 4 | 25 |
|Trun right 2 || 67 |
||Base Action 0 | 1 |
||Base Action 1 | 8 |
||Base Action 2 | 32 |
||Base Action 3 | 9 |
||Base Action 4 | 17 |
|Two-stage left turn 1 || 99 |
||Base Action 1 | 38 |
||Base Action 2 | 10 |
||Base Action 3 | 44 |
||Base Action 4 | 7 |
|Two-stage left turn 2 || 87 |
||Base Action 1 | 37 |
||Base Action 2 | 19 |
||Base Action 3 | 26 |
||Base Action 4 | 5 |
|U-turn 1 || 71 |
||Base Action 1 | 16 |
||Base Action 2 | 12 |
||Base Action 3 | 24 |
||Base Action 4 | 19 |
|U-turn 2 || 81 |
||Base Action 0 | 4 |
||Base Action 1 | 16 |
||Base Action 2 | 22 |
||Base Action 3 | 18 |
||Base Action 4 | 21 |



































