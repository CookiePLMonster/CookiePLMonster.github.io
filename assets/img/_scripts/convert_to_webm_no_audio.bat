@echo off
set /p CQ="Enter CQ value (blank for default 40): "
if "%CQ%"=="" set CQ=40

for %%F in (%*) do (
	"C:\Program Files\HandBrake\HandBrakeCLI.exe" --preset-import-file C:\Users\Adrian\AppData\Roaming\HandBrake\presets.json --preset "Blog" -q %CQ% -a none -s none -i "%%~F" -o "%~dp0%%~nF.webm"
)