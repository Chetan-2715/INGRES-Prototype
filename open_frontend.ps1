# Open the INGRES ChatBot frontend in the default browser
$frontendPath = Join-Path $PSScriptRoot "frontend\index.html"
Start-Process $frontendPath
Write-Host "✅ INGRES ChatBot interface opened in your browser!" -ForegroundColor Green
Write-Host "📍 If it doesn't open automatically, navigate to:" -ForegroundColor Yellow
Write-Host "   $frontendPath" -ForegroundColor Cyan
