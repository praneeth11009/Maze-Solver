#!/bin/bash
if [ "$#" -eq 2 ]; then
	python3 decoder.py $1 $2 1
fi

if [ "$#" -eq 3 ]; then 
	python3 decoder.py $1 $2 $3
fi 