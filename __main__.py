from twitchstream.outputvideo import TwitchBufferedOutputStream
from twitchstream.chat import TwitchChatStream

import Commands
from Colours import COLOURS_DICT, is_hex_colour_code, convert_hex_colour_code
from game import Game
import streaminfo
import time

def parse_message(message):
		message_strings = message['message'].split()

		command = message_strings[0]
		
		legit_command = False
		if command in Commands.MOVEMENT:
			legit_command = True
			
			if len(message_strings) > 1:
				try:
					amount = min(int(message_strings[1]), 5)
				except:
					amount = 1
			else:
				amount = 1
					
			if command == Commands.UP:
				game.move_up(amount)

			elif command == Commands.DOWN:
				game.move_down(amount)

			elif command == Commands.LEFT:
				game.move_left(amount)

			elif command == Commands.RIGHT:
				game.move_right(amount)

		elif command in Commands.BRUSH:
			legit_command = True
			
			if command == Commands.LIFT or command == Commands.RAISE:
				game.painting = False

			elif command == Commands.LOWER:
				game.painting = True

			elif command == Commands.SIZE:
				if len(message_strings) > 1:
					game.change_size(int(message_strings[1]))

		elif command in COLOURS_DICT.keys():
			legit_command = True
			game.change_colour(COLOURS_DICT[command])

		elif is_hex_colour_code(command):
			legit_command = True
			game.change_colour(convert_hex_colour_code(command))
			
			
		elif command in Commands.DEBUGGING_COMMANDS:
			legit_command = True
			print ('ADMIN COMMAND')
			if command == Commands.RESET:
				game.reset()

		if legit_command:
			game.paint()
			
			print("user: '%s' - command: %s" % (
				message['username'],
				command
			))


if __name__ == "__main__":
	game = Game()
	game.reset()
	
	# load two streams, one for video one for chat
	with TwitchBufferedOutputStream(
			twitch_stream_key=streaminfo.STREAMKEY,
			width=640,
			height=480,
			fps=30.,
			enable_audio=False,
			verbose=False) as videostream, \
			TwitchChatStream(
				username=streaminfo.USERNAME,
				oauth=streaminfo.OAUTH,
				verbose=False) as chatstream:

		chatstream.send_chat_message('connecting to chat...')
		print ('connected to chat...')

		# main loop
		while True:
			# Every loop, call to receive messages.
			# This is important, when it is not called,
			# Twitch will automatically log you out.
			# This call is non-blocking.
			chat_messages = chatstream.twitch_receive_messages()

			# process messages
			if chat_messages:
				for chat_message in chat_messages:
					parse_message(chat_message)

			# if there are not enough frames left, add more
			if videostream.get_video_frame_buffer_state() < 30:
				try:
					videostream.send_video_frame(game.frame)
				except:
					print 'uh oh'
			else:
				time.sleep(0.001) # relax for a bit, we sent all the frames we could
