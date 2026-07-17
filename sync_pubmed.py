from Bio import Entrez
import os
import time

# --- 設定項目 ---
EMAIL = "your-email@example.com"  # NCBIへの連絡用メールアドレス（必須）
AUTHOR_NAME = "Sakashita Misaki[Author]" # 検索クエリ
MY_NAME_BOLD = "Misaki Sakashita" # 太字にする名前
OUTPUT_DIR = "_publications"

Entrez.email = EMAIL

def fetch_pubmed_publications(query):
    # 1. PMID（論文ID）の検索
    handle = Entrez.esearch(db="pubmed", term=query, retmax=50)
    record = Entrez.read(handle)
    handle.close()
    return record["IdList"]

def get_work_details(pmid):
    # 2. 個別の論文詳細を取得
    handle = Entrez.esummary(db="pubmed", id=pmid)
    record = Entrez.read(handle)
    handle.close()
    return record[0]

def generate_markdown(detail):
    title = detail.get('Title', 'No Title').strip(".")
    pub_date = detail.get('PubDate', '1900')
    pub_year = pub_date.split()[0] # "2025 Jan 1" -> "2025"
    journal = detail.get('Source', 'Unknown Journal')
    doi = detail.get('DOI', '')
    
    # 3. 著者リストの抽出（Pubmedは明確にAuthorのみを返します）
    authors = detail.get('AuthorList', [])
    formatted_authors = []
    for auth in authors:
        # "Sakashita M" などの形式を "Misaki Sakashita" に近づける調整
        # Pubmedの形式に合わせるか、姓名を入れ替えるかは好みで調整
        if "Sakashita" in auth:
            formatted_authors.append(f"<b>{auth}</b>")
        else:
            formatted_authors.append(auth)
            
    authors_str = ", ".join(formatted_authors)
    
    # ファイル名の生成
    safe_title = title[:30].replace(' ', '-').replace('/', '-').lower()
    filename = f"{pub_year}-{safe_title}.md"
    
    content = f"""---
title: "{title}"
collection: publications
permalink: /publication/{pub_year}-{safe_title}
date: {pub_year}-01-01
venue: "{journal}"
citation: "{authors_str}. ({pub_year}). {title}. <i>{journal}</i>."
---

Pubmed ID: {detail['Id']}
[Link to publication](https://doi.org/{doi})
"""
    return filename, content

# --- メイン処理 ---
print(f"Searching Pubmed for: {AUTHOR_NAME}...")
pmids = fetch_pubmed_publications(AUTHOR_NAME)

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

for pmid in pmids:
    try:
        print(f"Fetching details for PMID: {pmid}...")
        detail = get_work_details(pmid)
        fname, md_content = generate_markdown(detail)
        
        with open(os.path.join(OUTPUT_DIR, fname), "w", encoding="utf-8") as f:
            f.write(md_content)
        
        time.sleep(0.3) # NCBIサーバーへの負荷軽減
    except Exception as e:
        print(f"Error processing PMID {pmid}: {e}")

print(f"\nCompleted! Generated {len(pmids)} files in {OUTPUT_DIR}.")