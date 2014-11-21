#!/usr/bin/env python

'''for challenge http://www.reddit.com/r/dailyprogrammer/comments/2mlfxp/20141117_challenge_189_easy_hangman/ '''

import string
import random

def main():
	select_difficulty()
	pick_word()
	global chances_remaining
	chances_remaining = 5
	while chances_remaining >= 0:
		picked_letter = select_letter()
		check_letter(picked_letter)
		player_guessing = True

		if chances_remaining:
			player_guessing = raw_input('Would you like to try and guess the word?: y/N? ').upper() == 'Y'
		if player_guessing:
			player_guess = raw_input('Please type your guess: ').upper().strip()
			correct_guess = guess_word(player_guess)
			if correct_guess:
				break 
	print 'The correct word was %s.' % selected_word

def select_difficulty():
	global difficulty
	difficulty_selection = raw_input('Hello, welcome to Hangman in Python! " Please select difficulty, Easy-Hard (1-3): ')
	while int(difficulty_selection) not in range(1,4):
		difficulty_selection = raw_input('Hello, welcome to Hangman in Python! " Please select difficulty, Easy-Hard (1-3): ')
	difficulty = int(difficulty_selection)

def pick_word():
	f = open('wordlist.txt', 'r')
	words = f.read().splitlines() 
	f.close()

	words = [word.replace("'", "").upper() for word in words]  
	easy_words = [word for word in words if len(word) <= 5]
	medium_words = [word for word in words if len(word) >= 5 and len(word) <= 7]
	hard_words = [word for word in words if len(word) >= 8]

	global selected_word
	global hidden_word

	if difficulty == 1:
		selected_word = random.choice(easy_words)
	elif difficulty == 2:
		selected_word = random.choice(medium_words)
	elif difficulty == 3:
		selected_word = random.choice(hard_words)
	global hidden_word
	hidden_word = '-' * len(selected_word)

def select_letter():
	global hidden_word
	print 'Your word currently looks like this: %s ' % hidden_word
	player_pick = raw_input("Please select a letter: ")
	player_pick = player_pick.upper()
	return player_pick


def check_letter(player_pick):
	global hidden_word
	global chances_remaining

	if player_pick in selected_word:		
		print 'You guessed %s, which is used in this word' % player_pick
		indices = [i for i, x in enumerate(selected_word) if x == player_pick]
		word_list = list(hidden_word)
		for x in indices:
			word_list[x] = player_pick
		hidden_word = ''.join(word_list)
	else:
		print 'You guessed %s, which is not used in this word. You have %s chances remaining.' % (player_pick, str(chances_remaining))
		chances_remaining = chances_remaining - 1
	print hidden_word

def guess_word(player_guess):
	global chances_remaining
	if player_guess == selected_word:
		print "Congratulations you guessed correctly!"
		return True
	elif player_guess != selected_word:
		chances_remaining = chances_remaining - 1
		print 'Incorrect! You have %s guesses remaining.' % str(chances_remaining)	
		return False






if __name__ == '__main__':
	main()

alphabet = list(string.ascii_uppercase)
letters_guessed = []
words_letter = []
difficulty = None
selected_word = None
hidden_word = None
player_pick = None
chances_remaining = None