	
#19/11/2022:
#ABOUT THE PROJECT:

	As this was an university assessment, I had to develop it entirely in Spanish.

	This is the first project I've ever coded, it was an university assessment in which we had to choose one .csv file from
	kaggle (https://www.kaggle.com/), clean and process it to extract useful insights from that data.

	For my project I chose one which depicted various metrics on the development of the covid pandemic by country in the year 2020, 
	a quite fitting dataset given this project was developed during 2020. Please do not consider these data as fact as I did not find 
	anything that could verify the validity of it.

	- Functions are declared in 'funciones.py' file.
	- Above each function there is a small description on what each function do.
	- Function calls are made on 'tests.py', at the bottom of the file you can toggle the comments to execute the function(s) you want to.
	- You can change parameter values on some test functions to show data from different dates/countries you like.
	- All outputs can be seen on the console.

	REQUIREMENTS:
	- Python version 3.8 or more.
	- matplotlib library installed in your system. -> Run 'pip install matplotlib' on your cmd to install it.

#WHAT I LEARNED:

	This project taught me many things as:

		- Data structures such as: int, floats, boolean and dates, arrayLists and diccionaries ('maps' as known in other languages)
		- Basic logic with booleans: if, else, else if (elif)
		- Preprocessing and cleaning of data extracted from large csv files (excel),
		- Read csv files with python
		- Lambda functions
		- Python syntax
		- Named tuples
		- Think about useful insights that could be extracted from a dataset and then implement them with code.

		-Overall, this 'initation' project helped me think of insights that could be interpreted from raw data and implement ways 
		to extract them like a programmer would. 
		It also helped me practise my coding skills and build my knowledge of programming from the ground up.

Looking back I can tell it is a very basic and simple project, however it didn't seem like it when I developed it for sure!

I hope you like the project! :)


	#Proyecto primer cuatrimestre Python 3.8

	################################################################################
	####################     UPDATE LOGS     #######################################
	################################################################################

	#21/10/2020:
		- Hoy he creado el readme del proyecto.

	#18/11/2020:
		- Retocado el csv eliminando varias columnas que estaban vacias y otras que proporcionaban datos que no eran utiles para
		- mi proyecto como diabetes_prevalence y iso_code (columna innecesaria ya que solo me hara falta el nombre de los paises). Otras
		- columnas que he quitado ha sido por ejemplo female/ male smokers. Ya que no me interesa estudiar una posible relacion entre fumadores/ covid y 
		- prefiero centrarme en aspectos sanitarios como hospital_beds_per_thousand o la relacion de edad con la columna aged_70_older o la respuesta al 	- virus 
		- en funcion del gdp del pais etc...

	#30/11/2020
		- He retocado un poco más la base de datos y le quite unas pocas columnas mas ya que eran demasiadas filas y ahora tengo un número más manejable
		- de ellas. Además eran filas que creo que no iba a utilizar de todas formas como son los new_cases_per_million. De todas formas, si en algún
		- momento las necesito volveré y retocaré el excel de nuevo. Creado el leer_datos (lectura del fichero) pero me da error al pasar de string a 
		- float, no creo que importe ya que no llegare a hacer calculos con ellas pero bueno. He mandado un correo para ver si se soluciona el problema.

	#01/12/2020
		- Creadas las funciones calcula_paises, filtra_por_continente y total_muertes_por_pais_y_fecha. Estoy contento ya que funcionan :D. Ahora lo 
		- subire a github y hasta el miercoles. 
		- Por cierto: el debug funciona de locos muy util para corregir errores y ver fallos en el codigo.

	#05/12/2020 
		- Hoy he rellenado los espacios en blanco de mi hoja de datos con 0 para que no me de errores y he arreglado algunas columnas que estaban mal
		- y ahora si me deja transformarlas a float. Voy a hacer una funcion que calcule el maximo de muertes totales por continente.

	#20/12/2020
		- Hoy he creado varias funciones a implementar según el word de guía del proyecto como; calcula_poblacion_mundial, agrupar_por_continente, 	
		- evolucion_de_muertes_por_pais etc... Me faltan ya 2 funciones por implementar para completar la 5a entrega. Por otra parte, la funcion de 	
		- grafica no funciona ya que no me detecta el import de matplotlib.

	#28/12/2020
		- Hoy he organizado las funciones por entregas, documentado entradas y salidas, implementado varias funciones de la 5a entrega junto sus test
		- Me falta por implementar 1 funcion y ya estaria terminado.
		- El casting a date type ya lo habia hecho en la anterior entrega.
		- He borrado unas pocas filas del dataset ya que solo contenian 0 y he borrado la columna total_deaths_per_million ya que daba error al castearlo.

	#09/01/2021
		- Hoy he arreglado los fallos con numpy/matplotlib. La solucion es mas sencilla que desintalar todo miniconda. 
		- Simplemente hay que desinstalar con conda uninstall y luego instalarlo con pip`.
		- Ejemplo: conda uninstall matplotlib / pip install matplotlib
		- Dicho esto, he ordenado las funciones como pediste por entrega (esta vez bien) y terminado de comprobar la funcion con grafica una vez arreglado el problema.
		- Tambien he terminado la ultima funcion que me faltaba.
		- NOTA: El database definitivo se llama coviddata3.csv los demas los puedes ignorar.	
	#12/01/2021
		- Arreglada la funcion 7. Implementada funcion 14.
