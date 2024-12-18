import chess

def check_castling(prev_fen, curr_fen):
    board_prev = chess.Board(prev_fen)
    board_curr = chess.Board(curr_fen)

    castling_moves = []

    if board_prev.piece_at(chess.E1) and not board_curr.piece_at(chess.E1):
        if board_curr.piece_at(chess.G1):
            castling_moves.append("white castled king side")
        elif board_curr.piece_at(chess.C1): 
            castling_moves.append("white castled queen side")
    
    if board_prev.piece_at(chess.E8) and not board_curr.piece_at(chess.E8):
        if board_curr.piece_at(chess.G8):  
            castling_moves.append("black castled king side")
        elif board_curr.piece_at(chess.C8):  
            castling_moves.append("black castled queen side")
    
    if castling_moves:
        return ', '.join(castling_moves)
    
    return None

def find_move(previous_fen, current_fen):

    castling_result = check_castling(previous_fen, current_fen)
    if castling_result:
        return castling_result
    
    board_prev = chess.Board(previous_fen)
    piece_map = {'p': 'pawn', 'n': 'knight', 'b': 'bishop', 'r': 'rook', 'q': 'queen', 'k': 'king'}

    move = None
    for legal_move in board_prev.legal_moves:
        board_prev.push(legal_move)
        if board_prev.fen().split()[0] == current_fen.split()[0]:
            move = legal_move
            board_prev.pop()
            break
        board_prev.pop()
    
    if move:
        if len(move.uci()) == 5:
            next_square = move.uci()[-3:-1]
        else:
            next_square = move.uci()[-2:]

        prev_square = move.uci()[:2]
        piece = piece_map[f"{board_prev.piece_at(chess.parse_square(prev_square)).symbol().lower()}"]
        board_piece = board_prev.piece_at(chess.parse_square(prev_square))
        color = "white" if board_piece.color else "black"
        return f"{color} played {piece} to {next_square}"
    else:
        return None


