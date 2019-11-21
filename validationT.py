def userValid(user):
	z=0
	#debe contener un mínimo de 6 caracteres y un máximo de 12.
	cont = len(user)
	if cont < 6:
		print("Usuario debe tener más de 6 caracteres. ")
		z=z+1
	if cont > 12:
		print("Usuario no debe tener más de 12 caracteres. ")
		z=z+1
	#contener solo letras y números". Nombre de usuario válido, retorna
	if user.isspace()==True: # revisa si hay espacios en blanco
		print("Usuario no puede contener espacios. ")
		z=z+1
	if user.isalnum()==False:# alpha numerico
		print("Debe ser alfa númerico, sin caracteres extraños : ")
		z=z+1
	if z==0:
		return(True)
	if z!=0:
		return(False)



