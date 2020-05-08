import hangman
import reversegam
import hangman
import PySimpleGUI as sg 

def almacenar (juego_elegido):
	try:
		a = open ('juegos.txt','a')
		a.write ('Juego elegido: '+juego_elegido+'\n')
	except:
		a = open ('juegos.txt','w')
		a.write ('Juego elegido: '+juego_elegido+'\n')	
	finally:
		a.close()

def ver_juegos_elegidos():
	try:
		a = open ('juegos.txt')
		print(a.read())
	except:
		print ('Error! Ningún juego ha sido jugado aún')	
	finally:
		a.close()

sg.theme ('Dark Purple6')

ven = [
    [sg.Text('Elegí qué juego jugar',size=(40,1),justification='center',font=('Arial',15),text_color='white',key='instrucciones')],
    [sg.Button('Ahorcado',size=(15,1))],
    [sg.Button('Ta-Te-Ti',size=(15,1))],
    [sg.Button('Otello',size=(15,1))],
    [sg.Button('Lista de Juegos Jugados',size=(15,2))],
    [sg.Button('Salir')]
]
ventana = sg.Window('Jueguitos', layout=ven)

while True:
    event, values = ventana.read()
    if event in (None, 'Salir'):	# Salir, cierra ventana
        break
    elif event == 'Ahorcado':
        hangman.main()      
        almacenar ('Ahorcado')
    elif event == 'Ta-Te-Ti':
        tictactoeModificado.main()
        almacenar('Ta-Te-Ti')
    elif event == 'Otello':
        reversegam.main()
        almacenar('Reverse')
    elif event == 'Lista de Juegos Jugados':
        ver_juegos_elegidos()
    
ventana.close()