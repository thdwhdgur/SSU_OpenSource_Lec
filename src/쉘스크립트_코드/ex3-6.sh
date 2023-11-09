#!/bin/bash

echo "폴더의 이름을 입력하세요:"
read folder_name

if [ ! -d "$folder_name" ]; then
    mkdir "$folder_name"
    echo "폴더 '$folder_name'를 생성했습니다."
else
    echo "폴더 '$folder_name'가 이미 존재합니다."
fi

cd "$folder_name"

for i in {1..5}; do
    echo "내용을 채워 넣은 파일 $i" > "file$i.txt"
done

tar -czf files.tar.gz *.txt

mkdir extracted_folder
tar -xzf files.tar.gz -C extracted_folder/

echo "파일을 압축하고 새로운 폴더에 해제했습니다."
