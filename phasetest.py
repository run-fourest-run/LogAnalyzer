import re



file = r'C:\Users\afournier\PycharmProjects\LogAnalyzer\Logs\test.txt'
version_pattern = re.compile(r'version\s[0-9]\.[0-9][0-9]\.[0-9]')
phase_pattern = re.compile(r'Manta\sFlow\s(\w+)\s(\w+)')

ANALYSIS_PHASE_NAME_PATTERN = re.compile('Analyzer')
EXRACTOR_PHASE_NAME_PATTERN = re.compile('Extractor')


with open(file) as f:
    lines = f.readlines()
    phase_object = next(filter(None,(re.search(phase_pattern,x) for x in lines)))
    phase_string = phase_object.group()


    phase_extraction = re.search(EXRACTOR_PHASE_NAME_PATTERN,phase_string)
    phase_analysis = re.search(ANALYSIS_PHASE_NAME_PATTERN,phase_string)
    phase = ''
    if phase_extraction is not None:
        phase = 'extraction'
    elif phase_analysis is not None:
        phase = 'analysis'
    elif phase_analysis is None & phase_extraction is None:
        phase = 'unknown'

    print(phase)