class Animal:
    def speak(self, sound=None, times=None):
        if sound is not None and times is not None:
            print((sound + " ") * times)
        elif sound is not None:
            print(sound)
        else:
            print("Animal makes a sound")

# Create object
a = Animal()

a.speak()                 # No arguments
a.speak("Roar")           # One argument
a.speak("Woof", 3)        # Two arguments