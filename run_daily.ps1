Set-Location "C:\Users\user\Documents\gpu-price-tracker"
.\.venv\Scripts\python.exe src\gpu_price_tracker\scraper.py

if($LASTEXITCODE -ne 0){
    exit 1
}

git add data/raw
git diff --staged --quiet

if($LASTEXITCODE -ne 0){
    git commit -m "Add daily price data"
    git push
}