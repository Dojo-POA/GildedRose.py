rm -f actual_output.txt && python texttest_fixture.py 10 > actual_output.txt && colordiff original_output.txt actual_output.txt
