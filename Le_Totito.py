A="A"
B="B"
C="C"
D="D"
E="E"
F="F"
G="G"
H="H"
I="I"
x=False
d=0
print(" Bienvenido al menu de totito. \n Escoger la casilla que se quiere llenar.\n J1=X J2=O")
while x==False 	or d<=9:
	d=d+1
	if A=="X" and B=="X" and C=="X":
		x=True
		ganador="Jugador 1"
	if D=="X" and E=="X" and F=="X":
		x=True
		ganador="Jugador 1"
	if G=="X" and H=="X" and I=="X":
		x=True
		ganador="Jugador 1"
	if A=="X" and D=="X" and G=="X":
		x=True
		ganador="Jugador 1"
	if B=="X" and E=="X" and H=="X":
		x=True
		ganador="Jugador 1"
	if C=="X" and F=="X" and I=="X":
		x=True
		ganador="Jugador 1"
	if A=="X" and E=="X" and I=="X":
		x=True
		ganador="Jugador 1"
	if G=="X" and E=="X" and C=="X":
		x=True
		ganador="Jugador 1"
	if A=="O" and B=="O" and C=="O":
		x=True
		ganador="Jugador 2"
	if D=="O" and E=="O" and F=="O":
		x=True
		ganador="Jugador 2"
	if G=="O" and H=="O" and I=="O":
		x=True
		ganador="Jugador 2"
	if A=="O" and D=="O" and G=="O":
		x=True
		ganador="Jugador 2"
	if B=="O" and E=="O" and H=="O":
		x=True
		ganador="Jugador 2"
	if C=="O" and F=="O" and I=="O":
		x=True
		ganador="Jugador 2"
	if A=="O" and E=="O" and I=="O":
		x=True
		ganador="Jugador 2"
	if G=="O" and E=="O" and C=="O":
		x=True
		ganador="Jugador 2"
	if x==False:
		print (A+" "+B+" "+C+"\n"+D+" "+E+" "+F+"\n"+G+" "+H+" "+I)
		opc1=input("Turno del Jugador 1, seleccione una opción: ")
		if opc1==A and A!="O":
			A="X"
		if opc1==B and B!="O":
			B="X"
		if opc1==C and C!="O":
			C="X"
		if opc1==D and D!="O":
			D="X"
		if opc1==E and E!="O":
			E="X"
		if opc1==F and F!="O":
			F="X"
		if opc1==G and G!="O":
			G="X"
		if opc1==H and H!="O":
			H="X"
		if opc1==I and I!="O":
			I="X"
		print (A+" "+B+" "+C+"\n"+D+" "+E+" "+F+"\n"+G+" "+H+" "+I)
		opc2=input("Turno del Jugador 2, seleccione una opción: ")
		if opc2==A and A!="X":
			A="O"
		if opc2==B and B!="X":
			B="O"
		if opc2==C and C!="X":
			C="O"
		if opc2==D and D!="X":
			D="O"
		if opc2==E and E!="X":
			E="O"
		if opc2==F and F!="X":
			F="O"
		if opc2==G and G!="X":
			G="O"
		if opc2==H and H!="X":
			H="O"
		if opc2==I and I!="X":
			I="O"
if d==9:
	ganador="empate"
print (A+" "+B+" "+C+"\n"+D+" "+E+" "+F+"\n"+G+" "+H+" "+I)
print("Ganador: "+ ganador)