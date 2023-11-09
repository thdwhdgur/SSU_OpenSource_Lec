#!/bin/bash

while true; do
    echo "1. 정보 추가"
    echo "2. 처음부터 다시 작성"
    echo "3. 정보 검색"
    echo "4. 종료"
    read choice

    case $choice in
        1)
            echo "이름과 전화번호 또는 생일을 입력하세요:"
            read info
            echo "$info" >> DB.txt
            echo "정보가 추가되었습니다."
            ;;
        2)
            > DB.txt
            echo "DB.txt 파일이 초기화되었습니다."
            ;;
        3)
            echo "검색할 팀원의 이름을 입력하세요:"
            read search_name

            # DB.txt 파일에서 이름으로 검색하여 정보 출력
            found=false
            while IFS= read -r line; do
                name=$(echo "$line" | cut -d' ' -f1)
                info=$(echo "$line" | cut -d' ' -f2-)
                if [[ "$name" == "$search_name" ]]; then
                    echo "팀원: $name, 정보: $info"
                    found=true
                    break
                fi
            done < DB.txt

            if [ "$found" = false ]; then
                echo "검색한 팀원의 정보를 찾을 수 없습니다."
            fi
            ;;
        4)
            echo "프로그램을 종료합니다."
            exit
            ;;
        *)
            echo "올바른 선택이 아닙니다. 다시 시도하세요."
            ;;
    esac
done
