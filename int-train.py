# client interview practice questions:

"""
?What will you do when the incoming client data is not even formatted properly?
Answer:
If incoming client data is unformatted or inconsistent, I handle it in a structured way:

First, I define a contract/schema for what the backend expects (JSON schema / Pydantic model).

Then I implement a pre-processing layer which cleans the raw input:
    remove invalid characters
    normalize dates, numbers, units
    handle missing/null values

I also add a data validation layer using tools like:
    Pydantic validation
    JSON schema validation
    custom validation rules

If the data is too corrupted, I don’t reject everything immediately. Instead:
    I move invalid records into a quarantine bucket (dead-letter queue / error table)
    and continue processing valid data.     
This ensures the pipeline remains stable while maintaining traceability of bad input.


?If the only input you receive from clients is PDF files, how will you process and extract structured data from them?
Answer:
If input is only PDFs, I design a pipeline depending on the PDF type:

Case 1: Text-based PDFs
    Use libraries like pdfplumber / PyMuPDF
    Extract text, then parse using regex + NLP patterns
    Convert into structured JSON

Case 2: Scanned PDFs (Images)
    Use OCR tools like Tesseract OCR or cloud services like AWS Textract / Google Vision OCR
    Extract raw text, then apply parsing rules
    Post Processing

Standardize extracted fields (dates, units, naming)
    Validate extracted output with schema
    Store the structured result in DB
Also, I ensure the system has confidence scoring and manual review fallback if extraction quality is low.


?Where will you use GenAI in this data standardization and extraction pipeline?
Answer:
I will use GenAI only in places where rule-based logic becomes too complex.

Typical use cases:  
    Field mapping:   -            detecting that “Pipe Length”, “Pipeline Distance”, “Total Length” refer to same KPI.
    PDF extraction enhancement:   extracting structured entities from messy OCR text.
    Schema inference:             understanding what columns represent if headers are unclear.
    Semantic normalization:       converting unstructured descriptions into standard structured output.
                                  GenAI works best as an assistant layer, not as the final source of truth.

                                  

?4) How will you ensure that GenAI does not generate incorrect mappings or KPIs?
Answer:
GenAI hallucination is a real risk, so I apply multiple safeguards:
    Use GenAI only for suggestions, not final decisions.
    Enforce strict output schema validation (Pydantic / JSON schema).
    Add confidence thresholding: low confidence responses go to manual review.
    Maintain a golden mapping dictionary (approved KPI mappings).
    Implement human-in-the-loop approval for new mappings.
    Add automated tests using known client samples to verify mappings.
    Track GenAI outputs with audit logs for traceability.
    This ensures AI is used as a productivity booster, not a source of incorrect business metrics.

    
"""



