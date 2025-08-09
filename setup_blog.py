import os
import glob
import re
from datetime import datetime

def add_front_matter_to_md_files(directory):
    """마크다운 파일들에 Front Matter를 추가하는 함수"""
    
    # 디렉토리 내의 모든 .md 파일 찾기 (index.md 제외)
    md_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md') and file != 'index.md':
                md_files.append(os.path.join(root, file))
    
    for file_path in md_files:
        print(f"Processing: {file_path}")
        
        # 파일 읽기
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 이미 Front Matter가 있는지 확인
        if content.startswith('---'):
            print(f"  - Front Matter already exists, skipping...")
            continue
        
        # 파일명에서 제목 추출
        file_name = os.path.basename(file_path)
        title = file_name.replace('.md', '')
        
        # 폴더명에서 카테고리 추출
        folder_name = os.path.basename(os.path.dirname(file_path))
        
        # 파일의 수정 시간 가져오기
        mod_time = datetime.fromtimestamp(os.path.getmtime(file_path))
        date_str = mod_time.strftime('%Y-%m-%d')
        
        # Front Matter 생성
        front_matter = f"""---
layout: default
title: "{title}"
date: {date_str}
category: "{folder_name}"
description: ""
---

"""
        
        # 새로운 내용 작성
        new_content = front_matter + content
        
        # 파일에 쓰기
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"  - Added Front Matter successfully")

def create_folder_index_files(directory):
    """각 폴더에 index.md 파일을 생성하는 함수"""
    
    folders = []
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path) and not item.startswith('.') and not item.startswith('_'):
            folders.append((item, item_path))
    
    for folder_name, folder_path in folders:
        index_path = os.path.join(folder_path, 'index.md')
        
        if os.path.exists(index_path):
            print(f"Index file already exists: {index_path}")
            continue
        
        # 폴더 내 .md 파일 개수 세기
        md_count = len([f for f in os.listdir(folder_path) if f.endswith('.md')])
        
        # index.md 내용 생성
        index_content = f"""---
layout: folder
title: "{folder_name}"
description: "{folder_name} 카테고리의 글 모음 ({md_count}개 포스트)"
folder_path: "/{folder_name}/"
---

{folder_name} 카테고리의 글들을 모아둔 공간입니다.
"""
        
        # index.md 파일 생성
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(index_content)
        
        print(f"Created index file: {index_path}")

if __name__ == "__main__":
    blog_directory = "."  # 현재 디렉토리 (블로그 루트)
    
    print("=== Adding Front Matter to Markdown Files ===")
    add_front_matter_to_md_files(blog_directory)
    
    print("\n=== Creating Folder Index Files ===")
    create_folder_index_files(blog_directory)
    
    print("\n=== Process Complete ===")
