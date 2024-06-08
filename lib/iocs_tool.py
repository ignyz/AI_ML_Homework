import iocsearcher
from iocsearcher.searcher import Searcher
from pydantic import BaseModel
from iocsearcher.document import open_document

class IOCTool:
    # Class used tools are implemented using iocsearcher tool documentation: https://github.com/malicialab/iocsearcher
    def __init__(self):
        self.iocs = []

    def dict_format(self, input_string):
        # IOC results formatting method
        # used only for managing sets of data
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
            # And append to IOCs list
            self.iocs.append((row[0], row[1], row[2]))
        return self.iocs
    def extract_doc_iocs(self, file):
        doc = open_document("file.pdf")
        text, _ = doc.get_text() if doc is not None else ""

        searcher = Searcher()
        searcher.search_data(text)
    def get_iocs(self):
        return self.iocs