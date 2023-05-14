# LINFO 1001 - Project 3 
### Abstract
 The project
consists of a creation, with the help of a device that can be attached to the wrists of
the elderlies, to help them as best as possible in their daily lives. Our group received
a Raspberry Pi with added sensors that can help create more multi and innovative
functions in order to help complete this project. We decided to name our project the
"ElderOxilium" (the Elder Helper).
## Program details
### Ressources
The Raspberry Pi is able to detect components in its environnement through its implented
sensors. It is capable of detecting the level of humidity, the temperature, the acceleration
rate and its spatial position. In addition, a joystick and LEDs are also attached onto the
Raspberry Pi.
To help us in our task, the site Trinket.io provided us with the SenseHat simulator so
that functions could be tested without the need of the physical device. It also provided
us a library, The SenseHat, with already pre-made functions to use. The Raspberry Pi
is controlled by implementing code in the Python language. We have also been given an
encryption code from Moodle in order to secure any information saved.
### Main functions at the client request
As demanded by the belgium ministry of public health, our team was demanded to create
two main functions to help the elderly live an easier life.

- First, the shopping list function allows the user to add products they want with
a specified quantity (either in grams, liters, or units). Once the list is saved, the user
is able to manupilate it and remove said items or even just change the quantity of
a specific one. A few grocery items will already pre-exist in a list (present in the
code) containing the basic items most people would use. However, when the user
wants to add a non existing item to the shopping list, it will automatically create
that item into the list so that it is saved. This is in order to give the possibility for
an AI inspired function that could ask the user if they would like to use previous
or frequently used items, (this, unfortunately, hasn’t been implemented yet). But
something that is already implemented is that the program is able to reiterate the
shopping list that has already been created, so that items can be ticked off when
doing groceries.

- Second, the bank code function stores the user’s bank code into the RaspberryPi
through an encryption, meaning that the secret code that is saved is not the raw
version inputed by the user. The encryption is done based on their personal and
saved password. If a password has not yet been included, the program will ask
the user to create one so that the encryption works properly. After both secret
code and password have been done, the user is able to view their code at any time.
However, they will only be able to do so if they input the same password they had
previously saved. If a steal of the secret code file ever does occur, there would be
very low possibilities that the person could find the correct decrypted version. The
user would also be able to change their secret code at any time.
### Added functionalities
We also developped five added functionalities to further improve the ElderOxilium:
- A start function that ’wakes’ the device from its sleep. Inspired from Iphones,
when the device is rotated back and forth once or the joystick is pressed, the device
turns on and is immediadetly ready for use.
-  A display all modes functions in order to allow the user to see all the possible
modes the program has installed, as well as being able to choose which function of
the program they wish to use. This was because we imagined that it would be quite
difficult as well as irritating to be able to only navigate using voice commands, and
only memory of what functions are available (considering our clients are people with
trouble remembering). Hence, we chose to use images with a 8x8 bit format to fit
the LEDs. Those images represent each mode and can be navigated back and forth
using the joystick.
- An event function which can remind the user of a beforhand saved event. Its name
can be chosen between various presets such as "bleu", "vert", "rouge", "jaune",
"médicaments", "rendez-vous 1" or "rendez-vous 2". These names were not selected
randomly: the colors were chosen for a mnemonic purpose as colors or images can help
with remembering things or even help understand them more easily. Doing so could
incite the user to hopefully create a pattern using this feature and help remember
things more easily. As for "rendez-vous 1" and "rendez-vous 2", we wanted to give the
possibility of having more than one meeting reminder. And finally, "médicaments"
was specifically chosen to remind an elderly to take their medication as forgetting at
their current condition could be life changing. This function could therefore be very
vital and useful for the client.
- A deafen function that allows the user to deafen all sound the device makes. This
was done to be quiet and prevent from disturbing others in certain places such as
cinemas, libraries, etc
- A dimming function dims the LED brightness as looking at a bright screen in the
dark can possibly cause health issues as well as irritation. Giving this possibility
reduces the places in which the user would not want to have their device with them.
## User guide
Theoretically, the ElderOxilium is quite easy to use. First the user has to turn the device
on, which then, two possibilities are given to start the program : rotate the device at an
angle of 180° and turn it back or simply press the joystick. A friendly transition will then
be displayed on the 8x8 bit screen.
It is now time to choose what the user wants to accomplish using the ElderOxilium. For
this step, they can easily select a pixelized image representing a mode with the joystick.
When pressing left or right, the presented mode changes, and when pressing in the middle,
the displayed function starts. Then, if the joystick is pressed down, this function will be
stopped and the program will be back into the main menu where the user can choose other
modes. To further help the user, all of the modes’ names are spoken out by a synthetic
voice. But please keep in mind that all of the inputs need to be implemented using a
keyboard and a computer screen.
- If the shopping list function is chosen, the program will ask the user what they would
like to do. The request is made by a sythetic voice coming out of speakers (the text
to speech function) After, which the user would have to input whatever is asked by
the program based on wether they would like to add, remove or hear their list.
- If the bank code function is chosen. The program will first check wether a password
has already been set. If not, the program will ask to create one which, once has been
inputed, will be hashed and saved. After a password is set, the program will ask to
input their secret bank code that will then be encrypted and saved into a file. Once
both passwords and code have been saved, restarting the function will ask for the
password you had previously saved and will only display the code when the correct
password is inputed. In a case where the user has forgotten their password, they are
firstly able to exit and change their bank code and password from scratch.
- Pressing on the deafen function will toggle between a muted or unmuted version of
the program, each represented with an image to know which is on.
- If dimming function is chosen, a toggle of dim and bright LED lights will visibly be
seen.
- Pressing event function, the program will ask vocally the user to input a (preset)
name, date and hour for the event to be reminded. When the time comes, the
program will speak out the chosen name of the event at the exact minute the user
wanted it to.
## Limitations
Even though the hardware provided gives a wide range of possible creativities, it also has
its limitations. Some of them being the sensors not being very precise causing things like
the rotation of the wrist for the start function to not work perfectly, the microphone picking
up background noise and ruining the voice input or even the lagging speed at which the
program executes and jumps from one function to another.
A group fault also occured where everyone worked on their own functions without
implementing the voice commands nor test them out and were solely started based off the
simulator. This caused confusion and errors when the voice command had to be added as
there was a lack of experience and time to do that transition.
## Conclusion
Although the final project isn’t as effective as we would have liked it to be (mainly the
speech to intent, when the device acts based on what the user vocally says, did not go
as planned and still doesn’t work), we have to keep in mind that this is the beta version
of the program and can therefore be considered a prototype. Note that the functions do
work and are effective on their own but only require an implementation of speech to intent.
The code handed out is also very flexible in a sense that if worked on again by the same
or different group, it could easily be understood and manupilated based on their ideas or
change of plans. The code is also commented in order to help with the understanding. All
this was still done even with the program not being effective as the group kept in mind
that it still has a possibility to become very effective in the future and help thousands of
lives.
