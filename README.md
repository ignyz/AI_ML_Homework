# AI_ML_Homework - IoCs Extraction Tool

This tool is designed to extract IoCs from various text sources, identifying IP addresses, domain names, URLs, file hashes, and email addresses, and outputting the IoC type - score.

## Features

- [x] Extraction of IoCs from diverse text sources (`pdf, csv, xls, docx, txt, csv, html`).
- [x] Identification of IoC types: IP addresses, domain names, URLs, file hashes, and email addresses.
- [x] Output generation with IoC, type, and confidentiality score.
- [ ] [Optional] User interface with input and output windows.

## Full Task:
Create a tool that can extract Indicators of Compromise (IoCs) from various text sources, such as emails, security reports, and threat intelligence feeds. The extracted IoCs should include IP addresses, domain names, URLs, file hashes, and email addresses. Output at least should have IoC, type of IoC and confidentiality score.
End result depends on your knowledge and varies from a blueprint to a full-stack application with input and output windows. It could be a presentation, pdf, application, etc. We understand that it is a short time period to build something robust. We are focusing on the quality of documentation and presentation (live demo).


## Requirements

- Python 3.8 or higher

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/ignyz/AI_ML_Homework
    cd <repository_directory>
    ```

2. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Starting the API Server

Run the following command to start the FastAPI server:

```bash
uvicorn main:app --host 127.0.0.1 --port 8000
```
### API testing enviroment:
To test API functions you can either use Postman or FastAPI `/docs`

```bash 
http://127.0.0.1:8000/docs
```
### Endpoints
1. Extract IOCs from Text
   - Endpoint: `/extract_iocs_from_text/`
   - Method: POST
   - Request Body:
     - `text`: Text content from which IOCs will be extracted.
   - Response: List of extracted IOCs with their types and confidentiality scores.
2. Extract IOCs from Document
   - Endpoint: `/extract_doc_iocs/`
   - Method: POST
   - Request Body:
     - `file`: Document file from which IOCs will be extracted.
   - Response: List of extracted IOCs with their types and confidentiality scores.
### Output 
**IOCs**
   - `ioc`: The Indicator of Compromise.
   - `type`: The type of IOC.
   - `confidentiality_score`: The confidentiality score associated with the IOC.
### Error Handling
   - If any error occurs during the extraction process, an empty list will be returned as the response.

## Credits

This tool was developed with help of sources below and by Ignas Narušis.

### Source list
- https://github.com/InQuest/iocextract
- https://github.com/malicialab/iocsearcher
