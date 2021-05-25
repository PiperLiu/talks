# 接收参数（演讲名称）
param($a)
if ([String]::IsNullOrEmpty($a)) {
    $a = Get-Date -Format 'yyyyMMdd'
}

# build slidev
Set-Location .\slidev
npm run build -- --base="/talks/talks/$a/"  # talks for github

# move to setup log
Copy-Item ./dist ../talks/$a -Recurse

# backup slidev.md
Copy-Item ./slides.md ../slidev_backup/$a.md

Set-Location ..
