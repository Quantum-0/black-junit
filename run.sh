black . --check --verbose 2>results.txt
python3 -m black_junit < results.txt > report.xml
rm results.txt