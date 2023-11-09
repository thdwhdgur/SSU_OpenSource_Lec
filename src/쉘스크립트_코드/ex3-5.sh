#!/bin/bash

execute_command() {
    local command="$1"
    local options="$2"

    echo "프로그램을 시작합니다."
    echo "함수 내부로 진입했습니다."
    echo "실행할 명령어: $command $options"
    $command $options
    echo "프로그램을 종료합니다."
}

echo "리눅스 명령어를 입력하세요 (e.g., ls):"
read user_command

echo "명령어의 옵션을 입력하세요 (e.g., -l):"
read user_options

execute_command "$user_command" "$user_options"

