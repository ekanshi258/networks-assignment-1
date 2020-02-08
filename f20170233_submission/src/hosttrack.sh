#!/usr/bin/python3
x=3600
w=$2
z=$((x/w))
y=0
while [ $y -le 21600 ]
do
    python3 hosttrack.py $1
    y=$((y+z))
    sleep $z
done
