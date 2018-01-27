'''
De Luna, Kobe Jee B.
G-3L
Project for CMSC 11
Specification: Medium - Connect X

References: 
board: inventwithpython.com/extra/fourinarow_text.py
os.path.exists: stackoverflow.com/questions/82831/how-to-check-whether-a-file-exists-using-python

'''

import sys #imported sys module to exit the program
import os #imported os module to clear the screen and check whether a file exists

def menu(): #base of the program
	global moveList,countx #to be able to access the value of the possible values that the user can input outside the function
	moveList = [1,2,3,4,5,6,7,8] #list that provides the possible values of moves
	os.system("clear") #clears the screen
	print() #prints new line for better readability
	print(" " * 19 + "Welcome to Connect-Four!" + "\n") 
	print("\t\t" + "#" * 30 + "\n" + "\t\t#         MAIN MENU          #\n " + "\t\t#" + (" ") * 28 + "#" + "\n\t\t#" + (" ") * 2 + "[1] Play New Game" + (" ") * 9 + "#\n" + "\t\t#" + (" ") * 2 + "[2] Load Previous Game" + (" ") * 4 + "#\n" + "\t\t#" + (" ") * 2 + "[3] View Instructions" + (" ") * 5 + "#\n" + "\t\t#" + (" ") * 2 + "[4] Exit" + (" ") * 18  + "#" + "\n" +(" ") * 4 + "\t\t" + "#" + (" ") * 2 + "[5] Load Last Match" + (" ") * 7 + "#" +(" ") * 20 + "\n\t \t#" + (" ") * 28 + "#" + "\n" + "\t\t" + "#" * 30 + "\n") #prints the main menu 
	return chooseOption() #goes to the def function

def chooseOption(): #the user chooses from the main menu options
	choice = input("What do you want to do? ") #asks input from the user 	
	if choice == "1": #NewGame
		return chooseBoardSize()
	elif choice == "2": #load the last state of the game
		loadPreviousGame()
	elif choice == "3": #view instructions and rules of the game
		viewInstructions()
	elif choice == "4": #exit the program
		sys.exit() 
	elif choice == "5":
		loadlastmatch()
	else:
		menu() #if the user's input is not in the possible options, it will print the main menu and let the user to choose again
def chooseBoardSize(): #asks the user what are the dimensions of the board they want to play
	global countx, counto	
	countx = 0	
	counto = 0
	os.system("clear") #clears the screen
	global boardWidth, boardHeight, winNumberDisc #makes these variables accessible; important in drawing the boardsize
	isChoiceInvalid = False
	while isChoiceInvalid == False: #let the user to choose again if the input is invalid
		print("\nPress Q to exit or Enter to go back to menu.")
		print("\n\tChoose the dimensions of your board")
		print("\t\t[a] 7 x 6")
		print("\t\t[b] 8 x 7\n")
		sizeChoice = input("Enter your choice here: ") #makes the user input lowercase
		sizeChoice = sizeChoice.lower()
		if sizeChoice == "a":
			boardWidth = 7
			boardHeight = 6
			winNumberDisc = 4
			moveList.pop(7) #removes the option "8" to the possibles moves
			break #breaks the loop if the user input is valid
		elif sizeChoice == "b":
			boardWidth = 8
			boardHeight = 7
			winNumberDisc = 5
			break #breaks the loop if the user input is valid
		elif sizeChoice == "q" or sizeChoice == "quit" or sizeChoice == "exit":
			sys.exit() #if the user wants to exit the program
		elif sizeChoice == "":
			return menu() #if the user wants to go back to menu
	return chooseTile()

def chooseTile(): #asks the user to choose from the default X,O tiles who will be the first turn
	os.system("clear")
	global firstPlayerTile, secondPlayerTile, currentPlayerTurn
	isInvalidTile = True #while the user input is invalid
	while isInvalidTile:
		print("\nPress Q to exit or Enter to go back to menu.")
		print("\n\tWhat tile do you want to use?")
		print("\t\t[X] or [O]\n")
		firstPlayerTile = input("Enter your choice here: ")
		firstPlayerTile = firstPlayerTile.upper() #makes the user input uppercase
		if firstPlayerTile == "X":
			secondPlayerTile = "O"
			isInvalidTile = False #the same function as break
		elif firstPlayerTile == "O":
			secondPlayerTile = "X"
			isInvalidTile = False #breaks the loop
		elif firstPlayerTile == "Q" or firstPlayerTile == "QUIT" or firstPlayerTile == "EXIT":
			sys.exit()
		elif firstPlayerTile == "":
			return menu()
		else:
			print("Error: Please enter valid tile (X or O)") #error message when the user input is invalid
	currentPlayerTurn = firstPlayerTile 
	return createNewBoard()

def alternation(): #for the switching of turns of the two tiles
	global currentPlayerTurn
	if currentPlayerTurn == "X": 
		currentPlayerTurn = "O"
	else:
		currentPlayerTurn = "X"
	return(print(currentPlayerTurn))
def createNewBoard(): #creates a nested list for the board
	board = []
	for x in range(boardWidth):
		board.append([" "] * boardHeight)
	return drawBoard(board)

def drawBoard(board): #draws the board
	os.system("clear")
	print(("+---+") + ("---+" * (boardWidth - 1)))	
	for y in range(boardHeight):
		print("|" + ("   |" * (boardWidth)))
		print("|", end="")
		for x in range(boardWidth):
			print(" %s |" % board[x][y], end="") #designates a "null" element to the board
		print()
		print("|   " * (boardWidth + 1))
		print("+---+" + ("---+" * (boardWidth - 1)))
	print("====" * (boardWidth) + "=")
	print("| " + "1",end="")
	for i in range(boardWidth-1):
		print(" |" ,i+2, end="")
	print(" |")
	print("====" * (boardWidth) + "=")
	if checkWin(board) != None: #if there is already a winner, it returns the winner (X or O)
		return (currentPlayerTurn)
	elif checkWin(board) == None and isBoardFull(board) == True: #if there is still no winner but the board is already full
		print("There is no winner. TIE!")
		print("Number of Moves: ", "X =" ,countx, "|| O =",counto)
		goBack = input("Do you want to play again? (y/n): ")
		goBack = goBack.lower()
		if goBack == "y":
			return chooseBoardSize()
		elif goBack == "n":
			return menu()
		elif goBack == "q":
			sys.exit()
		else: 
			return drawBoard(board)
	return enterMove(board,currentPlayerTurn)

def enterMove (board,currentPlayerTurn):
	inValidMove = True
	global countx, counto
	while inValidMove:
		print("Current Player Turn:", currentPlayerTurn, "\nNumber of Moves: ", "X =" ,countx, "|| O =",counto)
		move = input("Enter your move here: ")
		if move == "quit" or move == "q" or move == "exit":
			sys.exit()
		elif move == "":
			return menu()
		try:
			move = int(move)
		except ValueError: #if a string will be typecasted to integer
			print("Error: Please enter valid move (1-7). Try again...")
			continue
		if move not in moveList:
			print("Error: Please enter valid move (1-7). Try again...")			
			continue
		else:
			for i in range(-1,-(boardWidth),-1):
				if board[move-1][i] == " ": #starts from negative to access the bottom first
					if currentPlayerTurn == "X":
						countx += 1
					elif currentPlayerTurn == "O":
						counto += 1
					board[move-1][i] = currentPlayerTurn #changes the empty element to the currentplayerturn's tile
					writeHandler = open("movesfile.txt","w") 
					for x in range(boardWidth):
						for y in range(boardHeight):
							writeHandler.write(board[x][y] + ",") #it writes the current value of each element of the board to a file
					writeHandler.write(str(boardWidth)) #it will also write the values of boardWidth, boardHeight, currentPlayerTurn and the required number of discs to win to the file; it typecasts from int to str
					writeHandler.write(str(boardHeight))
					writeHandler.write(currentPlayerTurn)
					writeHandler.write(str(winNumberDisc))
					writeHandler.write(","+str(countx)+","+str(counto)+",")	
					writeHandler.close()	
					if checkWin(board) == currentPlayerTurn: #means the currentplayer won the game 
						writeHandle = open("lastmatch.txt","w")
						drawBoard(board)
						for x in range(boardWidth):
							for y in range(boardHeight):
								writeHandle.write(board[x][y] + ",") #it writes the current value of each element of the board to a file
						writeHandle.write(str(boardWidth)) #it will also write the values of boardWidth, boardHeight, currentPlayerTurn and the required number of discs to win to the file; it typecasts from int to str
						writeHandle.write(str(boardHeight))
						writeHandle.write(currentPlayerTurn)
						writeHandle.write(str(winNumberDisc))
						writeHandle.write(","+str(countx)+","+str(counto)+",")	
						writeHandle.close()	
						print(currentPlayerTurn, "wins")
						print("Number of Moves: ", "X =" ,countx, "|| O =",counto)
						print("\nPress Q to exit.\n")
						option = input("Do you want to play again? (y/n):") #asks the user if they want to play again
						option = option.lower()
						if option == "y": #if yes, the player will be redirected to the choosetile menu
							return chooseBoardSize()
						elif option == "n": #if no, the player will be redirected to menu
							return menu()
						elif option == "q" or "quit" or "exit": #if the player wants to exit the program
							sys.exit()
						else: 
							return menu()
					alternation() #it reverses the 	O and X every turn
					return(drawBoard(board)) #it terminates this function by updating the board

def checkWin(newBoard): 
	for x in range(boardWidth): #vertical
		currentDisc = 0	 #initiation
		for y in range(boardHeight):
			if newBoard[x][y] == currentPlayerTurn:
				currentDisc += 1 #update
				if currentDisc == winNumberDisc: #currentPlayerTurn is the winner
					return(currentPlayerTurn)
			elif newBoard[x][y] != currentPlayerTurn or newBoard[x][y] == " ": #if it encountered different tile from the currentplayerturn, it will set back the value of the currentdisc to 0
				currentDisc = 0
	for x in range(boardHeight): #horizontal; basically the same function as above
		currentDisc = 0 
		for y in range(boardWidth):
			if newBoard[y][x] == currentPlayerTurn:
				currentDisc += 1
				if currentDisc == winNumberDisc:
					return(currentPlayerTurn)	
			elif newBoard[y][x] != currentPlayerTurn or newBoard[y][x] == " ":
				currentDisc = 0
	#diagonal\ for 8x7 board
	if boardWidth == 8:
		for x in range(boardWidth-4):
			for y in range(4,boardHeight):
				if newBoard[x][y] == currentPlayerTurn and newBoard[x+1][y-1] == currentPlayerTurn and newBoard[x+2][y-2] == currentPlayerTurn and newBoard[x+3][y-3] == currentPlayerTurn and newBoard[x+4][y-4] == currentPlayerTurn:
					return(currentPlayerTurn)
		for x in range(boardWidth-4): #diagonal for 8x7 board/
			for y in range(boardHeight-4):
				if newBoard[x][y] == currentPlayerTurn and newBoard[x+1][y+1] == currentPlayerTurn and newBoard[x+2][y+2] == currentPlayerTurn and newBoard[x+3][y+3] == currentPlayerTurn and newBoard[x+4][y+4] == currentPlayerTurn:
					return(currentPlayerTurn)
	elif boardWidth == 7: #diagonal \ for 7x6 board
		for x in range(boardWidth-3):
			for y in range(3,boardHeight):
				if newBoard[x][y] == currentPlayerTurn and newBoard[x+1][y-1] == currentPlayerTurn and newBoard[x+2][y-2] == currentPlayerTurn and newBoard[x+3][y-3] == currentPlayerTurn:
					return(currentPlayerTurn)
		for x in range(boardWidth-3): #diagonal / for 7x6 board
			for y in range(boardHeight-3):
				if newBoard[x][y] == currentPlayerTurn and newBoard[x+1][y+1] == currentPlayerTurn and newBoard[x+2][y+2] == currentPlayerTurn and newBoard[x+3][y+3] == currentPlayerTurn:
					return(currentPlayerTurn)

def loadPreviousGame():
	global boardWidth, boardHeight, currentPlayerTurn, winNumberDisc, countx, counto
	if os.path.exists("movesfile.txt") == False: #to check if there's already an existing file, if it is the user's ever first game, it will result to false
		os.system("clear")
		print("\n\t\tNothing is saved in the database!")
		decision = input("\t\t  Press enter to go back to menu\n")
		if decision == "":
			return menu()
		else:
			loadPreviousGame()
	else:
		dimensions = [] #for boardheight, boardwidth, winning number of disc, and currentplayerturn
		output = []
		dict1 = {}
		readHandler = open("movesfile.txt","r")
		for line in readHandler:
			data = line
			datalist = data.split(",") #split the [[moves],[boardhwidth, boardheight, currentPlayerturn, winnumberdisc], [countx][counto][countx]
		dimensions.append(datalist[-4])
		dict1["counto"] = datalist[-2]
		dict1["countx"] = datalist[-3]
		dict1["boardWidth"] = dimensions[0][0]
		dict1["boardHeight"] = dimensions[0][1]
		n = int(dimensions[0][1])
		dict1["currentPlayerTurn"] = dimensions[0][2]
		dict1["winNumberDisc"] = dimensions[0][3]
		for x in range((len(datalist))//n): #to get values 0:7, 7:14, 14:21 21:28 28:35 35:42 or 42:49
			output.append(datalist[x*n:x*n+n])
		dict1["moves"] = output
		countx = int(dict1["countx"]) #turns the strings to integers
		counto = int(dict1["counto"])
		boardWidth = int(dict1["boardWidth"])
		boardHeight = int(dict1["boardHeight"])
		currentPlayerTurn = dict1["currentPlayerTurn"]
		winNumberDisc = int(dict1["winNumberDisc"])
		readHandler.close()
		if checkWin(dict1["moves"]) == currentPlayerTurn:
			iCantThinkofaVariableName = True
			while iCantThinkofaVariableName:
				decision = input("Do you want to continue load the previous game?(y/n) ")
				if decision.lower() == "y":
					drawBoard(dict1["moves"])
					print(currentPlayerTurn, "won this game!")
					print("Number of Moves: ", "X =" ,countx, "|| O =",counto)
					print("Press Q to quit and Enter to go back to menu.\n")
					inputInvalid = True
					while inputInvalid:
						decision = input("Press enter to go back to menu. ")
						if decision == "":
							return menu()
						elif decision == "q":
							sys.exit()
						else:
							continue
				elif decision.lower() == "n":
					return menu()
				
		alternation() #alternate the turn
		return (drawBoard(dict1["moves"]))

def viewInstructions(): #displays the instructions and rules of the game
	os.system("clear")

	print("=" * 52)
	print("\n\t    The rules are simple: \n\tTry to build a row of four checkers \n while keeping your opponent from doing the same.\n Sounds easy, but it's not! The vertical strategy \n creates a unique challenge: you must think in a\n  whole new way to block your opponent's moves!\n")
	print("=" * 52)	
	print("\t\tHOW TO PLAY")
	print("=" * 52)
	print("\n1. Decide who plays first. Players will alternate\n   turns after playing a checker.\n\n\t\tNOTE: The player starting the first \n\t\tgame will play second in the next \n\t\tgame.\n")
	print("2. On your turn, drop one of your checkers down ANY\n   of the slots in the top of the grid.\n")
	print("3. Play alternates until one player gets FOUR \n   (in a 7x6 board) or FIVE (in an 8x7 board) \n   checkers of his or her color in a row. The four \n   in a row can be horizontal, vertical or diagonal.\n")
	print("=" * 52)
	print("\t\tHOW TO WIN")
	print("=" * 52)
	print("\n   If you're the first player to get four of your \ncheckers in a row (in a 7x6 board) or five of your \ncheckers in a row(in an 8x7 board), you win the game!\n")
	print("=" * 52)
	print("(https://www.fgbradleys.com/rules/Connect%20Four.pdf)")
	print("\nPress enter to go back to menu.")
	goBack = input("")
	if goBack == "":
		return menu()
	else:
		viewInstructions()

def isBoardFull(board):
	for x in range(boardWidth):
		for y in range(boardHeight):
			if board[x][y] == " ": #if it encountered at least one empty element, it will terminate the function by returning false -- meaning that the board is not yet full
				return False
	return True

def loadlastmatch():
	global boardWidth, countx, counto, boardHeight, currentPlayerTurn, winNumberDisc
	dimensions = []
	dict1 = {}
	output = []
	readHandle = open("lastmatch.txt","r")
	for line in readHandle: 
		data = line
		datalist = data.split(",")
		dimensions.append(datalist[-4])
		dict1["counto"] = datalist[-2]
		dict1["countx"] = datalist[-3]
		dict1["boardWidth"] = dimensions[0][0]
		dict1["boardHeight"] = dimensions[0][1]
		n = int(dimensions[0][1])
		dict1["currentPlayerTurn"] = dimensions[0][2]
		dict1["winNumberDisc"] = dimensions[0][3]
		for x in range((len(datalist))//n): #to get values 0:7, 7:14, 14:21 21:28 28:35 35:42 or 42:49
			output.append(datalist[x*n:x*n+n])
		dict1["moves"] = output
		countx = int(dict1["countx"]) #turns the strings to integers
		counto = int(dict1["counto"])
		boardWidth = int(dict1["boardWidth"])
		boardHeight = int(dict1["boardHeight"])
		currentPlayerTurn = dict1["currentPlayerTurn"]
		winNumberDisc = int(dict1["winNumberDisc"])
		readHandle.close()
		if checkWin(dict1["moves"]) == currentPlayerTurn:
			iCantThinkofaVariableName = True
			while iCantThinkofaVariableName:
				decision = input("Do you want to continue load the last match?(y/n) ")
				if decision.lower() == "y":
					drawBoard(dict1["moves"])
					print(currentPlayerTurn, "won this game!")
					print("Number of Moves: ", "X =" ,countx, "|| O =",counto)
					print("Press Q to quit and Enter to go back to menu.\n")
					inputInvalid = True
					while inputInvalid:
						decision = input("Press enter to go back to menu. ")
						if decision == "":
							return menu()
						elif decision == "q":
							sys.exit()
						else:
							continue
				elif decision.lower() == "n":
					return menu()
				
		alternation() #alternate the turn
		return (drawBoard(dict1["moves"]))
		

___init___ = menu() #starts the program

