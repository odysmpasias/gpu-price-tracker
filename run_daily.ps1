Set-Location "C:\Users\user\Documents\gpu-price-tracker"
Start-Transcript -Path "logs\run_daily.log" -Append
.\.venv\Scripts\python.exe src\gpu_price_tracker\scraper.py 2>&1 | Out-Host

if($LASTEXITCODE -ne 0){
    exit 1
    Stop-Transcript
}

git add data/raw
git diff --staged --quiet

if($LASTEXITCODE -ne 0){
    git commit -m "Add daily price data"
    git push
}
Stop-Transcript