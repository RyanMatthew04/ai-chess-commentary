
from django.shortcuts import render
import pyautogui
from .fen import FEN
from .move import find_move
import google.generativeai as genai
from django.http import StreamingHttpResponse
import time

genai.configure(api_key="Enter Key")

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 1000,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
  ]
)

def index_view(request):
    
    context={'message': None}
   
    return render(request, 'index.html',context)



def start_commentary_view(request):
    def commentary_stream():
        region = (1115, 242, 680, 680)
        prev = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w"

        while True:
            
            screenshot = pyautogui.screenshot(region=region)
            screenshot.save(r'C:\Users\Ryan Matthew\Desktop\CV\Project\myproject\myapp\static\images\templates\region_screenshot.png')

            fen_string = FEN()
            if 'w' in prev:
                fen_string = fen_string + ' b'
            else:
                fen_string = fen_string + ' w'

            if fen_string.split()[0] != prev.split()[0]:
                move= find_move(prev,fen_string)
                if move is not None:
                    response = chat_session.send_message(f"Given the following positions:\nPrevious Position: {prev}\nCurrent Position: {fen_string}\n{move}. Explain in brief the reasoning for this move?")
                    prev=fen_string
                    message = response.text
                    print(message)
                    yield f"data: {message}\n\n"  
            
            time.sleep(1)  

    return StreamingHttpResponse(commentary_stream(), content_type='text/event-stream')


def stop_commentary_view(request):
    context={'message': None}
 
    return render(request, 'index.html',context)


