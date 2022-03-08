
def display_board(board):
	print("          "+ '|'+'==========='+ '|')
	print("          "+ '|'+" " + board[7]+" " + '|' +" " +  board[8]+" " + '|' +" " +  board[9]+" "+ '|')
	print("          "+ '|'+ '-----------'+ '|')
	print("          "+ '|'+" " +  board[4]+" " + '|' +" " +  board[5]+" " + '|' +" " +  board[6]+" "+ '|')
	print("          "+ '|'+ '-----------'+ '|')
	print("          "+ '|'+" " +  board[1]+" " + '|' +" " +  board[2]+" " + '|' +" " +  board[3]+" "+ '|')
	print("          "+ '|'+'==========='+ '|')


def player_choice():
	player_flag = False
	while player_flag == False:
		player_one = input("Choose (X/O or x/o):" )
		player_one = player_one.capitalize()
		if (player_one not in ['X','O']):
			print("only enter (X/O or x/o)")
		else:
			player_flag = True

	return player_one


def display_player(choice):
	if choice == 'X':
	    player_two = 'O'
	else:
		player_two = 'X'

	print("Player 1 is " + choice)
	print("Player 2 is " + player_two)

	return player_two


def player_move(p_one,p_two,invalid_inputs):
	valid_inputs = ['1','2','3','4','5','6','7','8','9']
	if p_one == True:
		player = 1
		p_one = False
	if p_two == True:
		player = 2
		p_two = False
	print(invalid_inputs)
	while True:
		move = input(f'player {player}\'s turn: ')
		if move not in valid_inputs:
			print("It  is not a  valid input.")
		elif move in invalid_inputs:
			print("You have already used this option.")
		else:
			invalid_inputs.append(move)
			break



	return move




def winning_pattern(game_board):
	winner = "null"
	gameon = True
	if game_board[1] == game_board[2] == game_board[3]:
		if  game_board[1] == 'X' or  game_board[1] == 'O':
			winner = game_board[1]
			
	elif game_board[4] == game_board[5] == game_board[6]:
		if game_board[4] == 'X' or game_board[4]== 'O':
			winner = game_board[4]
			
	elif game_board[7] == game_board[8] == game_board[9]:
		if game_board[7] == 'X' or game_board[7] == 'O':
			winner = game_board[7]
			
	elif game_board[7] == game_board[4] == game_board[1]:
		if game_board[7] == 'X' or game_board[7] == 'O':
			winner = game_board[7]
			
	elif game_board[8] == game_board[5] == game_board[2]:
		if game_board[8] == 'X' or game_board[8] == 'O':
			winner = game_board[8]
			
	elif game_board[9] == game_board[6] == game_board[3]:
		if game_board[9] == 'X' or game_board[9] == 'O':
			winner = game_board[9]
			
	elif game_board[7] == game_board[5] == game_board[3]:
		if game_board[7] == 'X' or game_board[7] == 'O':
			winner = game_board[7]
			
	elif game_board[1] == game_board[5] == game_board[9]:
		if  game_board[1] == 'X' or  game_board[1] == 'O':
			winner = game_board[1]

	elif '.' not in game_board:
		if winner != 'null':
			pass
		else:
			winner = 'Draw'
		
	return winner
	

def game_won(won,choice,game_board,player_two):
	game_won = False
	while game_won == False:
		game_won = True
		if won == 'X' or won == 'O':
			game_won = False
			if won == choice:
				print("player one wins")
				keep_playing()
			elif won == player_two:
				print("player two win")
				keep_playing()
		elif won == 'Draw':
			print("Its a  Draw!!")
			keep_playing()
	return won

def keep_playing():
	while True:
	    replay = input("Do you want to keep  playing (y/n): ")
	    if replay == 'y':
	    	game_start()
	    elif replay == 'n':
	    	exit()
	    else:
	    	print("I dont understand.")


def game_start():
	game_board = ["#",'.','.','.','.','.','.','.','.','.'] 
	invalid_inputs = []
	gameon = True
	player_one = player_choice()
	player_two = display_player(player_one)
	display_board(game_board)
	
	
	while gameon:
		p_one = True
		p_two = False
		move = int(player_move(p_one,p_two,invalid_inputs))
		game_board[move] = player_one
		display_board(game_board)
		winn = winning_pattern(game_board)
		game_won(winn,player_one,game_board,player_two)

		p_two = True
		move = int(player_move(p_one,p_two,invalid_inputs))
		game_board[move] = player_two
		display_board(game_board)
		winn = winning_pattern(game_board)
		game_won(winn,player_one,game_board,player_two)
	return game_board


game_board = game_start()











