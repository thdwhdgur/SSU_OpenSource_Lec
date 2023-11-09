#!/bin/bash

echo "숫자를 입력하세요:"
read num

if [[ $num =~ ^[0-9]+$ ]]; then
	for ((i=1; i<=$num; i++)) do
		echo "hello world"
	done
else
	echo "올바른 숫자를 입력하세요."
fi
