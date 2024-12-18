import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim


def FEN():
    
    image = cv2.imread(r'C:\Users\Ryan Matthew\Desktop\CV\Project\myproject\myapp\static\images\templates\region_screenshot.png')

    templates = {
        'K': cv2.imread(r'C:\Users\Ryan Matthew\Desktop\CV\Project\myproject\myapp\static\images\templates\K.png'),
        'Q': cv2.imread(r'C:\Users\Ryan Matthew\Desktop\CV\Project\myproject\myapp\static\images\templates\Q.png'),
        'R': cv2.imread(r'C:\Users\Ryan Matthew\Desktop\CV\Project\myproject\myapp\static\images\templates\R.png'),
        'B': cv2.imread(r'C:\Users\Ryan Matthew\Desktop\CV\Project\myproject\myapp\static\images\templates\B.png'),
        'N': cv2.imread(r'C:\Users\Ryan Matthew\Desktop\CV\Project\myproject\myapp\static\images\templates\N.png'),
        'P': cv2.imread(r'C:\Users\Ryan Matthew\Desktop\CV\Project\myproject\myapp\static\images\templates\P.png'),
        'k': cv2.imread(r'C:\Users\Ryan Matthew\Desktop\CV\Project\myproject\myapp\static\images\templates\bk.png'),
        'q': cv2.imread(r'C:\Users\Ryan Matthew\Desktop\CV\Project\myproject\myapp\static\images\templates\bq.png'),
        'r': cv2.imread(r'C:\Users\Ryan Matthew\Desktop\CV\Project\myproject\myapp\static\images\templates\br.png'),
        'b': cv2.imread(r'C:\Users\Ryan Matthew\Desktop\CV\Project\myproject\myapp\static\images\templates\bb.png'),
        'n': cv2.imread(r'C:\Users\Ryan Matthew\Desktop\CV\Project\myproject\myapp\static\images\templates\bn.png'),
        'p': cv2.imread(r'C:\Users\Ryan Matthew\Desktop\CV\Project\myproject\myapp\static\images\templates\bp.png'),
        '0': cv2.imread(r'C:\Users\Ryan Matthew\Desktop\CV\Project\myproject\myapp\static\images\templates\e1.png'),
        '1': cv2.imread(r'C:\Users\Ryan Matthew\Desktop\CV\Project\myproject\myapp\static\images\templates\e2.png'),
    }

    def classify_square(square_image):
        best_match = None
        best_val = -1  
        
        square_image = square_image.astype(np.uint8)  
        
        for piece, template in templates.items():
            if square_image.shape != template.shape:
                template_resized = cv2.resize(template, (square_image.shape[1], square_image.shape[0]))
            else:
                template_resized = template
            
            if len(square_image.shape) == 3:
                square_image_gray = cv2.cvtColor(square_image, cv2.COLOR_BGR2GRAY)
            else:
                square_image_gray = square_image
            
            if len(template_resized.shape) == 3:
                template_gray = cv2.cvtColor(template_resized, cv2.COLOR_BGR2GRAY)
            else:
                template_gray = template_resized

            score, _ = ssim(square_image_gray, template_gray, full=True)

            if score > best_val:
                best_val = score
                best_match = piece
        
        return best_match


    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    fen_position = []
    for row in range(8):
        row_fen = []
        for col in range(8):
            
            sub_image = image_rgb[85*row:85*(row+1), 85*col:85*(col+1)]
            piece = classify_square(sub_image)
            row_fen.append(piece)
        fen_position.append(row_fen)

    def classify_to_fen(classification):
        fen_rows = []
        for row in classification:
            fen_row = ''
            empty_count = 0
            for piece in row:
                if piece == '0' or piece== '1':  
                    empty_count += 1
                else:
                    if empty_count > 0:
                        fen_row += str(empty_count)
                        empty_count = 0
                    fen_row += piece[0] 
            if empty_count > 0:
                fen_row += str(empty_count)
            fen_rows.append(fen_row)
        return '/'.join(fen_rows)

    fen_string = classify_to_fen(fen_position)
    return fen_string
    

if __name__ == "__main__":
    FEN()


