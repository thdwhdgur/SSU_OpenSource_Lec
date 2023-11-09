#!/bin/bash

echo "리눅스가 재미있나요? (yes / no)"
read response

case "$response" in
    [Yy]|[Yy][Ee][Ss])
        echo "예, 리눅스는 정말 재미있습니다!"
        ;;
    [Nn]|[Nn][Oo])
        echo "아니요, 리눅스는 재미있지 않습니다."
        ;;
    *)
        echo "올바른 입력이 아닙니다. (yes 또는 no로 대답해주세요.)"
        ;;
esac
