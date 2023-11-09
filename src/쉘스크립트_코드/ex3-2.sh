#!/bin/bash

echo "첫 번째 숫자를 입력하세요:"
read num1

echo "두 번째 숫자를 입력하세요:"
read num2

echo "연산자를 입력하세요 (+ 또는 -):"
read operator

# 입력된 값이 올바른지 확인하는 조건문
if [[ $num1 =~ ^[0-9]+$ && $num2 =~ ^[0-9]+$ && ( "$operator" == "+" || "$operator" == "-" ) ]]; then
    if [ "$operator" == "+" ]; then
        result=$((num1 + num2))
        echo "결과: $result"
    elif [ "$operator" == "-" ]; then
        result=$((num1 - num2))
        echo "결과: $result"
    fi
else
    echo "올바른 숫자와 연산자를 입력하세요."
fi

