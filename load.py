import google.generativeai as genai
def output(text):
    response = model.generate_content("Summarize this and also don't make this too short "+text)
    return response
GOOGLE_API_KEY="AIzaSyCgX2dUhfUNGZ1aSrjUIlXNfor1ylBdw7I"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')