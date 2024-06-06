from lib.iocs_tool import IOCTool

# Example usage
if __name__ == "__main__":
    extractor = IOCTool()
    text = "IPs  192.168.1.1, domain duckduckgo.com, URL  http://google.com, hash  a2asd58a4sd654as8d4a6b8c3d4e5, email adress ignas@gmail.com"
    extractor.extract_iocs(text)
    iocs = extractor.get_iocs()
    for ioc in iocs:
        print("IOC: {}, Type: {}, Confidence: {}".format(ioc[0], ioc[1], ioc[2]))


