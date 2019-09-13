09/10/2018

*meztli.vergara@justia.com*

*www.skema.word.com*


# Voice Search - Justia
### By Meztli Vergara

### Es una funci�n que permite a los usuarios buscar cosas por medio de voz en lugar de texto, lo cual hace que la automatizaci�n sea de manera natural.


## Asistente Virtual

-	Google (Android)
-	Siri (Iphone)
-	Emy (Huawei)
-	Alexa (amazon)
-	Bixby (Samsung)
-	Cortana (Windows)


## Como cambia el internet

-	Sem�ntica
-	T�rminos
-	Conversacionales
-	Datos Estructurados


## Datos Estructurados

Ayudan a los navegadores a entender la informaci�n (*Microdata, RDfa, JSon, LD*)


## Tarjetas de Informaci�n

-	Resultado (Geolocalizaciones y/o gr�ficas)
-	Gr�fica de conocimiento
-	Preguntas Relacionadas (T�rminos conversacionales)

*Machine Learning by Google: https://www.youtube.com/watch?v=Hgav0LQAN6A*


## Herramientas para pruebas de datos estructurados

-	Legal Service


## Optimizar Contenido

Formato de preguntas y respuestas 
Google cuenta con el servicio �Mi Negocio� el cual provee una plataforma gratuita a negocios para pr�ximas b�squedas de los usuarios y cuenta con actualizaci�n de este e incluye datos estructurados.
El futuro es: *Google Duplex, Voice Shooping, Smart home*


## Dom�tica: 

-	Utiliza aparatos muy tecnol�gicos para mejorar las tareas 
-	Ingenier�a Social






11/10/2018

*hecdan8@hotmail.com*

# Introducci�n a Docker � Click It
### By H�ctor Aguirre


## Docker es una tecnolog�a de virtualizaci�n con una amplia variedad de lenguajes donde se puede tener de uno a muchos contenedores en ejecuci�n.
Un contenedor es una forma de separar los procesos. Docker cuenta con im�genes que tambi�n se crean de una manera especial las cuales ser�n usadas al lanzar un container.
Una imagen de Docker es un conjunto de capas.


## Como Recursos de Virtualizaci�n:

-	Host
-	Computador

*Se construye todo desde cero.*


## Como Recursos de Containers:

-	Archivos .dll
-	Computador

*Se hace uso de los recursos*


## Comandos m�s comunes

-	Mainteiner
-	From (de quien se hace mantenimiento)
-	Add (crea capas)
-	Env (define construcci�n)
-	Enty point (define entrada de inicio)
-	Cmd (a�ade par�metros al entry point)
-	expose (permite abrir y correr archivos dentro del container)


## �Por qu� usar Docker?

Porque crea ambientes inmutables, adem�s de ser muy portable, nos brinda seguridad al manejar un ambiente aislado. Para hacerlo seguro es necesario que los procesos NO tengan privilegios de root.







09/10/2018 � 11/10/2018

*cm@paybook.com*
*www.paybook.com*


# Aplicaciones y Servicios Basados en Arquitectura Docker � Pay Book
### By Claudio Montoya � Infrastructure Manager


# Docker

## Docker hace uso de c�digo abierto el cual nos permite mostrar aplicaciones, ejecutar funciones y editarlas dentro de contenedores, siendo de gran ayuda para el desarrollo de software, para administrar sistemas de bases de datos, servidores, p�ginas web entre muchos otros.
Dentro de este taller aprendimos a usar contenedores, con im�genes, usamos comandos que son muy similares a los de Linux. Tambi�n utilizamos la m�quina virtual, para poder trabajar con Docker, ya que Docker solo es compatible con Windows enter Price o Windows Pro.
Primero instalamos Virtual box, luego a�adimos el archivo Docker. Una vez lista la maquina iniciamos sesi�n para comenzar a trabajar.


## Comandos
	
-	-- link (va a enlazar el conteiner de una BD al local Host)

-	-d (se ejecuta back door para seguir trabajando)

-	docker exec (ejecuta comandos dentro de un conteiner

-	docker images (muestra las im�genes de docker)

-	docker pull (nombre de imagen: versi�n) � (descarga im�genes) 

-	docker rm (nombre de imagen: versi�n) � (elimina el contenedor)

-	docker rmi (id contenedor) - (elimina im�genes)

-	docker ps -a (muestra los conteiners en ejecuci�n)

-	docker run (id contenedor: versi�n) � (lanza el conteiner)

-	docker stop (id contenedor: versi�n) � (detiene la ejecuci�n del conteiner


## Conclusiones

Hicimos una conexi�n al local host con PHP My Admin, mostramos c�digo y ejecutamos prints de java, C y GO, modificamos puertos y creamos un blog en wordpress.
En lo personal pude observar que con Docker es m�s sencillo desarrollar o dar mantenimiento a un sistema, ya que ahorramos tiempo al no tener que descargar int�rpretes de lenguajes o cualquier otro software, ni instalar paquetes y las librer�as que utilizan estos. 
Hoy en d�a se trabaja con Docker en importantes empresas como Pay Book y Click IT, por ello la importancia de aprender a manejar esta tecnolog�a tan enfocada en el uso de la nube. 


