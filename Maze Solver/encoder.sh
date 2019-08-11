#!/bin/bash
if [ "$#" -eq 1 ]; then
	python3 encoder.py $1 1
fi

if [ "$#" -eq 2 ]; then 
	python3 encoder.py $1 $2
fi 