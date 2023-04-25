#  Go Straight
### Go_Straight_PST = PST()
### Go_Straight_PST.fit("00000201100001010002412024020220012220240201110000244224", 3)
### Go_Straight_PST.show()

![](https://github.com/Yen-Wei-Liang/Driving-Behavior-Evaluation-System/blob/main/Discuss/20230423/20230425/Go_Straight_PST.png?raw=true)

graph PST {
node0[label = Root];

node1[label = 4];
"node0" -- "node1"[label = 6, prob = 1.0];

node2[label = 1];
"node0" -- "node2"[label = 9, prob = 0.6];

node3[label = 2];
"node0" -- "node3"[label = 15, prob = 0.5];

node4[label = 0];
"node0" -- "node4"[label = 26, prob = 0.46];


-------------------level 1-------------------------

node5[label = 2];
"node1" -- "node5"[label = 1, prob = 0.02];

node6[label = 4];
"node1" -- "node6"[label = 1, prob = 0.02];

node7[label = 0];
"node1" -- "node7"[label = 2, prob = 0.03];

node8[label = 1];
"node1" -- "node8"[label = 1, prob = 0.02];

node9[label = 2];
"node2" -- "node9"[label = 2, prob = 0.03];

node10[label = 0];
"node2" -- "node10"[label = 4, prob = 0.06];

node11[label = 1];
"node2" -- "node11"[label = 3, prob = 0.04];

node12[label = 2];
"node3" -- "node12"[label = 4, prob = 0.05];

node13[label = 4];
"node3" -- "node13"[label = 5, prob = 0.06];

node14[label = 0];
"node3" -- "node14"[label = 6, prob = 0.07];

node15[label = 1];
"node4" -- "node15"[label = 5, prob = 0.06];

node16[label = 2];
"node4" -- "node16"[label = 8, prob = 0.08];

node17[label = 0];
"node4" -- "node17"[label = 13, prob = 0.12];


-------------------level 2-------------------------


node18[label = 2];
"node5" -- "node18"[label = 1, prob = 0.01];

node19[label = 2];
"node6" -- "node19"[label = 1, prob = 0.01];

node20[label = 2];
"node7" -- "node20"[label = 2, prob = 0.02];

node21[label = 2];
"node8" -- "node21"[label = 1, prob = 0.01];

node22[label = 2];
"node9" -- "node22"[label = 1, prob = 0.01];

node23[label = 0];
"node9" -- "node23"[label = 1, prob = 0.01];

node24[label = 1];
"node10" -- "node24"[label = 1, prob = 0.01];

node25[label = 0];
"node10" -- "node25"[label = 3, prob = 0.02];

node26[label = 1];
"node11" -- "node26"[label = 1, prob = 0.01];

node27[label = 0];
"node11" -- "node27"[label = 2, prob = 0.02];

node28[label = 4];
"node12" -- "node28"[label = 1, prob = 0.01];

node29[label = 2];
"node12" -- "node29"[label = 1, prob = 0.01];

node30[label = 0];
"node12" -- "node30"[label = 2, prob = 0.02];

node31[label = 4];
"node13" -- "node31"[label = 1, prob = 0.01];

node32[label = 0];
"node13" -- "node32"[label = 2, prob = 0.02];

node33[label = 1];
"node13" -- "node33"[label = 1, prob = 0.01];

node34[label = 0];
"node14" -- "node34"[label = 1, prob = 0.01];

node35[label = 2];
"node14" -- "node35"[label = 3, prob = 0.02];

node36[label = 1];
"node14" -- "node36"[label = 2, prob = 0.01];

node37[label = 2];
"node15" -- "node37"[label = 1, prob = 0.01];

node38[label = 0];
"node15" -- "node38"[label = 2, prob = 0.01];

node39[label = 1];
"node15" -- "node39"[label = 2, prob = 0.01];

node40[label = 2];
"node16" -- "node40"[label = 1, prob = 0.01];

node41[label = 4];
"node16" -- "node41"[label = 4, prob = 0.03];

node42[label = 0];
"node16" -- "node42"[label = 3, prob = 0.02];

node43[label = 1];
"node17" -- "node43"[label = 2, prob = 0.01];

node44[label = 2];
"node17" -- "node44"[label = 3, prob = 0.02];

node45[label = 0];
"node17" -- "node45"[label = 8, prob = 0.05];
}


-------------------level 3-------------------------
