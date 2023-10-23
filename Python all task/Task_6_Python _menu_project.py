import pyttsx3
import os
import speech_recognition as sr 
import pyaudio

mic = pyttsx3.init()
voices = mic.getProperty('voices')

mic.setProperty('voice', voices[0].id)
mic.runAndWait()
print("")
print("")

print(" =============================================== CHATBOT!! ================================================")
mic.say('CHATBOT!!')

print("")
print(" My name is Chatty, the Chatbot, I can open below apps :-")

print("\n\t 1.GOOGLE CHROME \t 2.VLC PLAYER	 \n\t 3.MICROSOFT EDGE \t 4.NOTEPAD \n\t 5.MICROSOFT PAINT \n\n\t\t	 0. FOR EXIT")


print("\n ============================================ Welcome To My Tools ============================================")
pyttsx3.speak("Welcome to my tools")
print("")
print("")

while True:
	# take input
	pyttsx3.speak("Type 'SPEAK' to give command through voice or 'WRITE' to write your command :")
	inp_type = input("type 'SPEAK' to give command through voice or 'WRITE' to write your command :" ).upper()
	command =""
	if inp_type == 'WRITE':
		print(" CHAT WITH ME WITH YOUR REQUIREMENTS : ")
		command = input()
		command = command.upper()
		print(command)
	elif inp_type == 'SPEAK':
		rec = sr.Recognizer()
		with sr.Microphone() as mic:
			print("speak:")
			audio = rec.listen(mic, timeout=2, phrase_time_limit=4)
			try:
				command = rec.recognize_google(audio)
				print("You said : "+command)
				command = command.upper()
			except Exception as err:
				print("Error:", err, end='\n\n')
	else:
		print("Invalid input")
		pyttsx3.speak("Invalid input")
		continue

	if ("DONT" in command) or ("DON'T" in command) or ("do not" in command):
		pyttsx3.speak("Type Again")
		print(".")
		print(".")
		continue

	elif ("GOOGLE" in command) or ("SEARCH" in command) or ("WEB BROWSER" in command) or ("CHROME" in command) or ("BROWSER" in command) or ("1" in command):
		pyttsx3.speak("Opening")
		pyttsx3.speak("GOOGLE CHROME")
		print(".")
		print(".")
		os.system("start chrome")

	elif  ("MSEDGE" in command) or ("EDGE" in command) or ("3" in command):
		pyttsx3.speak("Opening")
		pyttsx3.speak("MICROSOFT EDGE")
		print(".")
		print(".")
		os.system("start msedge")

	elif ("NOTE" in command) or ("NOTES" in command) or ("NOTEPAD" in command) or ("EDITOR" in command) or ("4" in command):
		pyttsx3.speak("Opening")
		pyttsx3.speak("NOTEPAD")
		print(".")
		print(".")
		os.system("Notepad")

	elif ("VLCPLAYER" in command) or ("PLAYER" in command) or ("VIDEO PLAYER" in command) or ("2" in command):
		pyttsx3.speak("Opening")
		pyttsx3.speak("VLC PLAYER")
		print(".")
		print(".")
		os.system("start VLC")

	elif ("PAINT" in command) or ("DRAW" in command) or ("MSPAINT" in command) or ("5" in command):
		pyttsx3.speak("Opening")
		pyttsx3.speak("MICROSOFT PAINT")
		print(".")
		print(".")
		os.system("mspaint")

	elif ("EXIT" in command) or ("QUIT" in command) or ("CLOSE" in command) or ("0" in command):
		pyttsx3.speak("Exiting")
		break

	else:
		pyttsx3.speak(command)
		print("Is Invalid,Please Try Again")
		pyttsx3.speak("is Invalid,Please try again")
		print(".")
		print(".")
