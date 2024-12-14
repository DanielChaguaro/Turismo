# Turismo
Este proyecto es una aplicación web desarrollada en Flask en estructura MVC que permite gestionar actividades, preferencias de usuarios y generar reportes por temporada. Incluye funcionalidades para registrar usuarios, administrar actividades y destinos, así como generar estadísticas basadas en preferencias y reservas.

Estructura

  	/app
  
    	/controllers                Carpetas de la lógicas del proyecto
      
    		activ_controller.py       Lógica CRUD de las actividades
      
	  		auth_controller.py        Lógica de iniciar sesion del usuario
	      
	  		core_controller.py        Generación de reportes
	      
	  		des_controller.py         Lógica CRUD de los destinos
	      
	  		res_controller.py         Lógica CRUD de las reservas
	      
	  		user_controller.py        Lógica CRUD de los usuarios
	    
	  	/models                     Carpeta de los modelos
	      
	  		Actividad.py              Define el modelo de Actividad
	      
	  		Comentario.py             Define los comentarios asociados a actividades
	      
	  		db.py                     Configuracion e inicialización a la base de datos
	      
	  		Destino.py                Modelo de destinos relacionados con las actividades
	      
	  		Reserva.py                Modelo para gestionar reservas de usuarios.
	      
	  		Usuario.py                Modelo para usuarios de la aplicación.
	    
	  	/templates                  Contiene las plantillas HTML que definen las vistas de la aplicación.
	      
	  		/temactiv                 
	        
	  			editar_actividad.html   Vista para editar y crear los detalles de una actividad específica.
	        
	  			listar_actividades.html Vista que muestra una lista de todas las actividades disponibles.
	      
	  		/temdest                  Carpeta con las vista para listar, crear y editar los destinos 
	      
	  		/tempreserva              Carpeta con las vista para listar, crear y editar las reservas
	      
	  		/tempuser                 Carpeta con las vista para listar, crear y editar los usuarios
	      
	    		base.html                 Vista del dashboard
	      
	    		login.html                Vista del login
	      
	    		recomendaciones_basicas.html   Vista del CORE
	      
	    		reportes.html             Vista de los reportes
	    
	  	__init__.py                 Creación y configuración de la aplicación web
	    
	  	routes.py                   Contiene todas las rutas 
	  
	  main.py                       Punto de entrada para ejecutar una aplicación Flask 
	 
Requisitos Previos

  
	Python 3.8+
  
	SQL Server (para la base de datos).
  
Instalación de dependencias:
	
	pip install
	Flask                 Framework principal para el backend
	Flask-SQLAlchemy      ORM para manejar la base de datos
	pyodbc                Driver para conectarte a SQL Server
  
Creación de la Base de datos:
  
	Ejecutar en SQLServer el archivo SQLQuery1.sql

Configuración de la Base de Datos:
  
  En el archivo /app/models/db.py

	DATABASE_URL=mssql+pyodbc://<user>:<password>@<server>/<database>

Iniciar la aplicación:

	python main.py

