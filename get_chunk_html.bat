@echo off
:: This script is used to convert a markdown file into a chunked html file

:: remove the old chunked html
rd /s /q gbl_chunked > nul 2>&1 || echo No old chunked html to remove

:: convert the markdown file into a chunked html file
pandoc "c:\Users\kandr\Desktop\Fic\GBL\gbl.md" -o gbl_chunked -t chunkedhtml -s --toc --metadata title="Good Basilisk Luzura" --metadata date="Began 2021-12-19" --metadata author="MemoryOverload"

:: enter into chunked html
cd gbl_chunked

:: and open the index page
.\index.html