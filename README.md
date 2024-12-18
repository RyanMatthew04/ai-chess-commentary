# AI Chess Commentary Project

This project combines computer vision, chess analysis, and AI commentary to create a live commentary system for chess games. The system leverages `SSIM` (Structural Similarity Index) to identify chess pieces on a live board, converts the board state into FEN notation, and uses Gemini 1.5 Pro via an API to generate commentary for the current chess position. The entire process is embedded in a Django-based full-stack web application with live updates.

## Features

- **Live Chess Board Analysis**: Uses computer vision techniques (SSIM) to locate chess pieces on a real-time chessboard by capturing screenshots.
- **Template Matching**: Each piece is matched with a predefined set of templates for accurate detection.
- **FEN Conversion**: Converts the identified chess pieces into FEN (Forsyth-Edwards Notation), which represents the current state of the chessboard.
- **AI Commentary**: Sends the FEN to Gemini 1.5 Pro using an API, which returns a detailed commentary of the position.
- **Django Web Application**: Built using Django to provide a full-stack experience with live updates via a feature called Streaming HTTP Response.
- **User Interface**: The app includes a start and stop button for controlling the process, along with a text box to display the commentary dynamically as the game progresses.

## How It Works

1. **Capture Chessboard Screenshot**: The application periodically takes screenshots of the live chessboard to capture the current state of the game.
2. **Piece Detection**: The screenshots are processed using SSIM to compare the captured board with templates of each chess piece. The best-matched piece is identified and assigned to the corresponding square on the board.
3. **FEN Conversion**: Once the pieces are identified, the board is converted into a FEN string, which is a standard format to represent a chess position.
4. **API Call to Gemini 1.5 Pro**: The generated FEN string is sent to Gemini 1.5 Pro, which analyzes the position and generates commentary.
5. **Live Commentary Display**: Using Django's Streaming HTTP Response feature, the commentary is updated in real-time on the web app interface, allowing users to see live commentary as the game progresses.
