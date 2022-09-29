import select
import sys

from junit_xml import TestCase, TestSuite

from black_junit.__pkginfo__ import __description__


def main() -> None:
    filter_not_modified = " wasn't modified on disk since last run."
    filter_already_formatted = " already well formatted, good job."
    filter_would_reformat = "would reformat "
    if select.select([sys.stdin], [], [], 1) == ([], [], []):
        print(__description__)
        print("Usage:")
        print("  > black . --check --verbose 2>results.txt")
        print("  > black-junit < results.txt > report.xml")
        exit(0)
    lines = [line.rstrip() for line in sys.stdin.readlines()]
    files_fail = [l[len(filter_would_reformat) :] for l in lines if l.startswith(filter_would_reformat)]
    files_good = [l[: -len(filter_already_formatted)] for l in lines if l.endswith(filter_already_formatted)]
    files_good += [l[: -len(filter_not_modified)] for l in lines if l.endswith(filter_not_modified)]
    cases = []
    for filename in files_fail:
        case = TestCase(filename.split("/")[-1], file=filename)
        case.add_failure_info("Not formatted")
        cases.append(case)
    for filename in files_good:
        cases.append(TestCase(filename.split("/")[-1], file=filename))
    results = TestSuite("Format check", test_cases=cases)
    print(TestSuite.to_xml_string([results]))
    exit(1 if len(files_fail) > 0 else 0)
