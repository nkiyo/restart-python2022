$files = @("hoge.py", "hoge2.py")

foreach($f in $files) {
  Write-Host "processing $($f) ..."
  py -m black $f
  py -m mypy --ignore-missing-import $f
  py -m flake8 $f
  Write-Host "$($f) done"
}
