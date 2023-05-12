from sense_hat import SenseHat
from time import sleep

s = SenseHat()
s.low_light = True

sense = SenseHat()

orientation = sense.get_orientation_degrees()    ## Récupère l'orientation du Raspberry 
deg = "p: {pitch}, r: {roll}, y: {yaw}".format(**orientation)
#event = sense.stick.wait_for_event()  ## Détecte un évênement sur le joystick

def start():   ## Fonction pour démarrer le Raspberry Pi
  sense.rotation = 270    ## Pour afficher le message à l'endroit
  sense.show_message("Welcome to your Raspberry Pi!", text_colour=[255, 0, 0], back_colour=[0, 255, 0], scroll_speed=0.08)
  sense.show_message("Choose a function:", text_colour=[255, 0, 0], back_colour=[0, 0, 255], scroll_speed=0.08)
    
bool = True
while bool : 
  orientation = sense.get_orientation_degrees()    ## Récupère l'orientation du Raspberry 
  pitch = float("{pitch}".format(**orientation))   ## Assigne la valeur du pitch récuperée à "pitch"
  print(pitch) ## Pour vérifier le pitch    
  if pitch > 100  or pitch < 75 :    ## Raspberry s'allume si on pivote assez le Raspberry 
     start()
  
  else:                             ## Raspberry s'allume si on bouge le joystick 

    if sense.stick.get_events() != []: ##detecte un evenement sur le joystick             
      start()        
      bool = False