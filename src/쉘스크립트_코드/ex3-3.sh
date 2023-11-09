#!/bin/bash

echo "몸무게(kg)를 입력하세요:"
read weight

echo "키(m)를 입력하세요:"
read height

# BMI 계산
bmi=$(echo "scale=2; $weight / ($height * $height)" | bc)

# BMI를 출력하고 비만 여부 판단
echo "당신의 BMI: $bmi"

if (( $(echo "$bmi < 18.5" | bc -l) )); then
    echo "저체중입니다."
elif (( $(echo "$bmi >= 18.5 && $bmi < 23" | bc -l) )); then
    echo "정상체중입니다."
else
    echo "과체중입니다."
fi
