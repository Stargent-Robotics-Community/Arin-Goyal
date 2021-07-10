import pyttsx3 as pt
import speech_recognition as sr
import pyaudio

bot = pt.init()

voices = bot.getProperty("voices")

bot.setProperty('voice', voices[0].id)

intro = "Hello , my name is CH bot and I am here to help you"
bot.say(intro)
bot.runAndWait()
r = sr.Recognizer()
def func():
    with sr.Microphone() as Source:
        print("Say something... :")

        audio = r.listen(Source)
        ans = r.recognize_google(audio)
        print(ans)
        try:
            if ans == "hello":
                print("bot: hello master")
                bot.say("hello master, how can I help you ?")
                bot.runAndWait()


            elif ans == "introduce yourself":
                print("bot: MY name is CH bot. I have been created by Arin Goyal and I am here to help you.\n")
                bot.say("MY name is CH bot. I have been created by Arin Goyal and I am here to help you")
                bot.runAndWait()
                return func()

            elif ans == "what can you do for me":
                print("bot: you can ask me for anything. Try saying \"Tell me a joke\"")
                bot.say("you can ask me for anything. Try saying \"Tell me a joke\"")
                bot.runAndWait()
                return func()

            elif ans == "tell me a joke":
                print("bot : Why do we tell actors to “break a leg”? Because every play has a cast 😅😂.")
                bot.say("Why do we tell actors to “break a leg”? Because every play has a cast")
                bot.runAndWait()
                return func()

            elif ans == "thanks for helping me":
                print("bot: It's my pleasure")
                bot.say("It's my pleasure")
                bot.runAndWait()
                return



        except:
            bot.say("sorry, Try again")
            print(": sorry try again")
            return func()
func()
