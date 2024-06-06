import iocsearcher
from iocsearcher.searcher import Searcher

class IOCTool:
    # Class used tools are implemented using iocsearcher tool documentation: https://github.com/malicialab/iocsearcher
    def __init__(self):
        self.iocs = []
    def dict_format(self, input_string):
        # Remove '{', '}'
        input_string = input_string.strip('{}')
        # Split the string into key-value pairs separated by comma and whitespace
        pairs = input_string.split(', ')
        # Split each pair into key and value
        formatted_dict = {pair.split()[0]: pair.split()[1] for pair in pairs}
        return  formatted_dict
    def extract_iocs(self, text):
        # Instantiate Searcher IOCSearcher
        searcher = Searcher()

        # Search for IOCs in the text
        results = searcher.search_data(text)

        # Format extracted IOCs
        for row in results:
            row_dict = self.dict_format(str(row))
            # And append to IOCs list
            for key, val in row_dict.items():
                self.iocs.append((val, key.upper(), self.calculate_confidence(val)))

    def calculate_confidence(self, ioc):
        # Confidence calculation
        return 1.0

    def get_iocs(self):
        return self.iocs