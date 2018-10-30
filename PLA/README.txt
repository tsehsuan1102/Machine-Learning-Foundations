######################################
B06902032 
Perceptron Learning Algorithm
Machine Learning Foundation 2018
######################################

使用的語言為python
(我把data set取為train.dat)
先讀入data

然後將data每一行包成一個五維的tuple(第一維為0)
裝進lst這個list裡面

然後為了方便之後作圖，我將結果寫進output.csv裡

每一次開始PLA之前，會先random shuffle一次，再開始PLA

而PLA的做法就如同上課提到的方法一樣，先檢查w和Xi的內積方向，如果和Yi一樣就代表正確，如果不同便開始修正，w加上一個YiXi，同時更新step次數

重複這個動作1126次，並計算平均修改次數
