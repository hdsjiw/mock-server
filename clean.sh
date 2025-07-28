# 캐시 파일 지우는 자동화 파일
# 1. 실행 권한 부여 chmod +x clean.sh
# 2. 실행 ./clean.sh

#!/bin/bash

echo "🧹 Cleaning up __pycache__ and *.pyc files..."

# Delete all __pycache__ folders
find . -type d -name "__pycache__" -exec rm -rf {} +

# Delete all .pyc files
find . -type f -name "*.pyc" -exec rm -f {} +

echo "✅ Cleanup complete."