@echo off
:: USAGE: get_chunk_html.bat [--open]

:: remove the old chunked html if it exists
rd /s /q chapters_html > nul 2>&1

:: set metadata for the index html file
set title="The Good Basilisk Luzura"
set author="MemoryOverload"
set date="Began 2022-19-12"

:: convert the markdown file into a chunked html file
:: caret (^) is the line continuation character in batch
:: and I don't want to have to scroll to read the command
pandoc "gbl.md" -o chapters_html -t chunkedhtml --toc ^
  --metadata title=%title% --metadata author=%author% --metadata date=%date%

:: open the index html file in the default browser if the --open flag is passed
if "%1"=="--open" start chapters_html/index.html