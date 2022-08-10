import sys
from junit_xml import TestSuite, TestCase


def main():
    filter_not_modified = ' wasn\'t modified on disk since last run.'
    filter_already_formated = ' already well formatted, good job.'
    filter_would_reformat = 'would reformat '
    lines = [l.rstrip() for l in sys.stdin.readlines()]
    files_fail = [l[len(filter_would_reformat):] for l in lines if l.startswith(filter_would_reformat)]
    files_good = [l[:-len(filter_already_formated)] for l in lines if l.endswith(filter_already_formated)]
    files_good += [l[:-len(filter_not_modified)] for l in lines if l.endswith(filter_not_modified)]
    cases = []
    for fname in files_fail:
        case = TestCase(fname.split('/')[-1], file=fname)
        case.add_failure_info('Not formatted')
        cases.append(case)
    for fname in files_good:
        cases.append(TestCase(fname.split('/')[-1], file=fname))
    results = TestSuite('Format check', test_cases=cases)
    print(TestSuite.to_xml_string([results]))


if __name__ == "__main__":
    main()
