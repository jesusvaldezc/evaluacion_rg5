# Evaluacion

### Introduccion
Este programa te permite convertir archivos CSV a JSON, solo necesitas agregar tus archivos csv a la carpeta data, no es necesario cambiar el nombre del archivo en el script.

### Requisitos
- Python 
-Docker

###Instrucciones
- Clonar este repo
- Crear imagen en docker
```

 docker build -t "evaluacion" .

```

-Correr Imagen en modo developer (Salir con [CTRL + C])

```
docker run -it -p 5050:5050 --rm --name "evaluacion-volatil" evaluacion

```

## Si deseas correr el script de manera dinamica debes de correr el siguiente codigo
```

docker run --name my-running-app -d -p 5050:5050 -v /rockstar/evaluacion/:/usr/src/app evaluacion

```
Este codigo te permite mantener el servicio corriendo y ademas te permite mostrar los cambios de manera dinamica al poder editar la tabla CSV en los datos y darle refresh a la pagina web sin tener que construir la imagen en cada cambio


