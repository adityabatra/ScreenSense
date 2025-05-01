from fastapi import FastAPI, Form
from fastapi.responses import StreamingResponse
from capture import capture_screen
from response import get_response

app = FastAPI()

@app.post("/analyze/")
def analyze_screen(question: str = Form(...)):
    print("Taking screenshot")
    screenshot = capture_screen()
    print("Processing screenshot")
    def generate():
        for event in get_response(screenshot, question):
            if event.type == "response.output_text.delta":
                yield event.delta
            elif event.type == "response.completed":
                yield ("\n")
        

    

    return StreamingResponse(generate(), media_type="text/plain")