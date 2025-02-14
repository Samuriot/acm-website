import PyPDF2
from google import genai

def extractingTextFromPDF(pdfFile: str):
    with open(pdfFile, 'rb') as pdf:
        reader = PyPDF2.PdfReader(pdf, strict=False)
        pdfText = []
        
        for page in reader.pages:
            content = page.extract_text()
            pdfText.append(content)
            
        return pdfText

def startOpenAI():
    apiKey = open("apiKey", "r").read()
    client = genai.Client(api_key=apiKey)
    parsedResume = extractingTextFromPDF("jomikaelgruizResume.pdf")
    resumeQuery = []
    resumeQuery.append({"Act as a senior software engineer scouting for both new graduate" +  
                        "and internship positions for your company. Provide feedback on the following " + 
                        "resume provided via text format." + str(parsedResume)})
    
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents = resumeQuery,
    )
    
    answer = response.candidates[0].content.parts[0].text
    print("answer\n", answer)
    
if __name__ == '__main__':
    startOpenAI()