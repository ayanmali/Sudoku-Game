import sudokusolver as ss
import pygame as pg

WIDTH, HEIGHT = 600, 600
WIN = pg.display.set_mode(size = (WIDTH, HEIGHT))
TILE_WIDTH = 50
pg.display.set_caption("Sudoku")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
SELECTION_RECT = pg.Rect(50, 50, TILE_WIDTH, TILE_WIDTH)

FPS = 60

board = [

[5, 3, 0, 0, 7, 0, 0, 0, 0],
[6, 0, 0, 1, 9, 5, 0, 0, 0],
[0, 9, 8, 0, 0, 0, 0, 6, 0],
[8, 0, 0, 0, 6, 0, 0, 0, 3],
[4, 0, 0, 8, 0, 3, 0, 0, 1],
[7, 0, 0, 0, 2, 0, 0, 0, 6],
[0, 6, 0, 0, 0, 0, 2, 8, 0],
[0, 0, 0, 4, 1, 9, 0, 0, 5],
[0, 0, 0, 0, 8, 0, 0, 7, 9]

]

solvedBoard = ss.solvedBoard
#tileSelected = False

pg.font.init()
textfont = pg.font.SysFont("Arial", 40)
textfontsmall = pg.font.SysFont("Arial", 20)

class Tile:
    isSelected = False
    found = False
    num = 0
    row = 0
    col = 0

    def __init__(self, pos):
        self.pos = pos

    def select(self):
        isSelected = True
        pg.draw.rect(WIN, RED, (self.pos, (TILE_WIDTH, TILE_WIDTH)), 3)

    def deselect(self):
        isSelected = False

    def makeGuess(self, guess):
        #print(self.row, self.col)

        # if guess is correct
        if guess == solvedBoard[self.row][self.col]:
            print("correct")
            board[self.row][self.col] = guess
            self.found = True
            return True
        print("incorrect")
        return False
        # if guess is incorrect
        #else:
            #print("incorrect")
            #numMistakes += 1
    
def setup():
    WIN.fill(WHITE)
    #pg.draw.line(WIN, BLACK, (75, 75), (75, 450))
    incr = 0

    for i in range(10):
        if i % 3 == 0:
            pg.draw.line(WIN, BLACK, (75+incr, 75), (75+incr, 525), width = 5)
            pg.draw.line(WIN, BLACK, (75, 75+incr), (525, 75+incr), width = 5)
            incr += 50
            continue

        pg.draw.line(WIN, BLACK, (75+incr, 75), (75+incr, 525))
        pg.draw.line(WIN, BLACK, (75, 75+incr), (525, 75+incr))
        incr += 50

    #textTBD = textfont.render("5", 1, RED)
    #WIN.blit(textTBD, (75, 75))

    #first = Tile((75+50*4, 75))
    #first.select()
    #first.deselect()

    #pg.display.update()

def setupTiles():
    tiles = [[], [], [], [], [], [], [], [], []]

    for i in range(9):
        for j in range(9):
            tiles[i].append(Tile((75+(TILE_WIDTH*j), 75+(TILE_WIDTH*i))))
            tiles[i][j].row = i
            tiles[i][j].col = j

    return tiles

def placeNumbers(board, tiles):
    numSolved = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            tiles[i][j].num = board[i][j]
            if board[i][j] != 0:
                text = textfont.render(str(board[i][j]), 1, BLACK)
                WIN.blit(text, (tiles[i][j].pos[0] + 16, tiles[i][j].pos[1] + 2))
                tiles[i][j].found = True
                numSolved += 1

    if numSolved == 81:
        return "fully solved"

def solveAll(tiles):
    pass


def main():
    #global tileSelected
    over = False
    tileSelected = False
    numMistakes = 0
    clock = pg.time.Clock()
    run = True
    pressed = []
    guess = 0

    tiles = setupTiles()
    selectedTile = None

    setup()
    placeNumbers(board, tiles)

    while run:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            
            if event.type == pg.MOUSEBUTTONUP and not over:
                if event.button == 1 and tileSelected == False and placeNumbers(board, tiles) != "fully solved" and numMistakes < 3:
                    setup()
                    placeNumbers(board, tiles)
                    for r in tiles:
                        for t in r:
                            if t.pos[0] <= pg.mouse.get_pos()[0] <= t.pos[0] + TILE_WIDTH-2 and t.pos[1] <= pg.mouse.get_pos()[1] <= t.pos[1] + TILE_WIDTH-2:
                    #pg.draw.rect(WIN, RED, SELECTION_RECT, 3)
                                row = tiles.index(r)
                                col = r.index(t)
                                print(f'row is {row} and column is {col}')
                                selectedTile = t
                                selectedTile.select()
                                guess = 0
                                #takeNumber(t)
                                #tileSelected = True
                    continue    

                #if event.button == 1 and tileSelected == True:
                    #print("wfq")
                    #setup()
                    #placeNumbers(board, tiles)
                    # re-place all the numbers on the board, including those initially set and those that have already been discovered
                    #tileSelected = False

                #if numMistakes >= 3:
                    #setup()
                    #placeNumbers(board, tiles)
                    #numMistakes = 0
                    #print("you made 3 mistakes, game over")

                #if placeNumbers(board, tiles) == "fully solved":
                    #setup()
                    #placeNumbers(board, tiles)
                    #print("you win")

            if event.type == pg.KEYDOWN and not over:
                #guess = 0
                
                keys = {pg.K_1 : 1,    # variable R is used to assign the pygame keypress K_r
                pg.K_2 : 2,
                pg.K_3 : 3,
                pg.K_4 : 4,
                pg.K_5 : 5,
                pg.K_6 : 6,
                pg.K_7 : 7,
                pg.K_8 : 8,
                pg.K_9: 9}
                
                #key = pg.K_r
                
                key_input = pg.key.get_pressed()
                for key in keys:
                    if key_input[key] and selectedTile != None and not selectedTile.found:
                        #print(keys[key])
                        guess = keys[key]
                        pg.draw.rect(WIN, WHITE, (selectedTile.pos[0]+5, selectedTile.pos[1]+5, TILE_WIDTH-10, TILE_WIDTH-10))
                        text = textfontsmall.render(str(guess), 1, BLUE) # ***
                        WIN.blit(text, (selectedTile.pos[0] + 8, selectedTile.pos[1] + 2)) # ***

                        #selectedTile.makeGuess(keys[key])
                
                #if event:
                    # pass in the guess
                    #takeNumber()

                if selectedTile != None and not selectedTile.found and guess != 0:
                    if event.key == pg.K_RETURN:
                        pg.draw.rect(WIN, WHITE, (selectedTile.pos[0]+5, selectedTile.pos[1]+5, TILE_WIDTH-10, TILE_WIDTH-10))
                        if not selectedTile.makeGuess(guess):
                            numMistakes += 1
                        else:
                            text = textfont.render(str(guess), 1, BLACK) # ***
                            WIN.blit(text, (selectedTile.pos[0] + 16, selectedTile.pos[1] + 2)) # ***
                                                
                        guess = 0

                    elif event.key == pg.K_BACKSPACE:
                        guess = 0
                        pg.draw.rect(WIN, WHITE, (selectedTile.pos[0]+5, selectedTile.pos[1]+5, TILE_WIDTH-10, TILE_WIDTH-10))


        #xPos = pg.mouse.get_pos()[0]
        #yPos = pg.mouse.get_pos()[1]
        #print(numMistakes)
        if numMistakes >= 3:
            setup()
            placeNumbers(board, tiles)
            over = True
            gameend = textfont.render("You Lose!", 1, BLACK) # ***
            WIN.blit(gameend, (WIDTH//2-70, 540)) # ***


        #if placeNumbers(board, tiles) == "fully solved":
            #setup()
            #placeNumbers(board, tiles)
            #over = True
            #print("you win")

        solved = True
        for r in tiles:
            for t in r:
                if not t.found:
                    solved = False
                    break
        
        if solved:
            setup()
            placeNumbers(board, tiles)
            over = True
            gameend = textfont.render("You Win!", 1, BLACK) # ***
            WIN.blit(gameend, (WIDTH//2-70, 540)) # ***

        pg.display.update()

    pg.quit()

if __name__ == "__main__":
    main()