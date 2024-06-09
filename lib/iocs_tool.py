import requests

import iocsearcher
from iocsearcher.searcher import Searcher
from pydantic import BaseModel
from iocsearcher.document import open_document


class IOCTool:
    # Class used tools are implemented using iocsearcher tool documentation: https://github.com/malicialab/iocsearcher
    def __init__(self):
        self.iocs = []

    def calculate_confidentiality_score(self, ioc_type, ioc):
        # Placeholder for confidentiality score calculation
        score = 0

        if ioc_type in ['ip4', 'ip6', 'ip4Net']:
            # IP addresses may be more sensitive if they belong to internal networks
            if ioc.startswith('192.168.') or ioc.startswith('10.') or ioc.startswith('172.16.'):
                score += 3
            else:
                score += 1

        elif ioc_type == 'fqdn':
            # Domain names related to known malicious activities might be more sensitive
            if 'malware' in ioc or 'phishing' in ioc:
                score += 5
            else:
                score += 1

        elif ioc_type == 'url':
            # URLs pointing to suspicious or malicious websites may have higher sensitivity
            if 'malicious' in ioc or 'phishing' in ioc:
                score += 5
            else:
                score += 1

        elif ioc_type in ['md5', 'sha1', 'sha256']:
            # File hashes indicating known malware may pose a higher risk
            # Make API request
            score = self.malware_call(ioc, score)

        elif ioc_type == 'email':
            # Email addresses associated with known phishing campaigns or threat actors might be more sensitive
            if ioc.endswith('@malicious.com') or ioc.endswith('@phishing.com'):
                score += 5
            else:
                score += 1

        return score

    def malware_call(self, ioc, score):
        data = {
            "query": "get_info",
            "hash": ioc,
            # "apikey": '4615ebf4ffbee0a4fd953d941c38f6b0'
        }
        response = requests.post("https://mb-api.abuse.ch/api/v1/", data=data)
        # Check if request was successful
        if response.status_code == 200:
            # Parse response JSON
            data = response.json()

            # Check if file exists in Malware Bazaar's database
            if data["query_status"] == "ok":
                result = str(data["data"])
                try:
                    if "malicious" in result.lower():
                        score += 10
                    else:
                        print("File is not found in Malware Bazaar's database.")
                except Exception as e:
                    print(str(e))

            else:
                print("Query status is not ok:", data["query_status"])
        else:
            print("Error:", response.status_code)
        return score

    def dict_format(self, input_string):
        # IOC results formatting method
        # used only for managing sets of data
        # Remove '{', '}'
        input_string = input_string.strip('{}')
        # Split the string into key-value pairs separated by comma and whitespace
        pairs = input_string.split(', ')
        # Split each pair into key and value
        formatted_dict = {pair.split()[0]: pair.split()[1] for pair in pairs}
        return formatted_dict

    def extract_iocs(self, text):
        # Instantiate Searcher IOCSearcher
        searcher = Searcher()

        # Search for IOCs in the text
        results = searcher.search_data(text)

        # Format extracted IOCs
        for row in results:
            # And append to IOCs list
            confidenciality_score = self.calculate_confidentiality_score(row[0], row[1])
            self.iocs.append((row[0], row[1], confidenciality_score))
        return self.iocs

    def extract_doc_iocs(self, file):
        doc = open_document(file)
        text, _ = doc.get_text() if doc is not None else ""
        searcher = Searcher()
        searcher.search_data(text)

    def get_iocs(self):
        return self.iocs
