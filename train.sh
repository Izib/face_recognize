rm images/* -rf
python capture.py ./images/$1.jpg
ls images > list.txt
python train_cap.py test
