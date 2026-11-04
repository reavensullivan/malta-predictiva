# Manual de despliegue - Malta Predictiva

## 1. Requisitos

- Windows con Docker Desktop y motor Docker funcionando
- Docker Engine compatible con contenedores Linux
- Archivos de la aplicación y modelos autorizados
- Puerto local 8001 disponible

No se requiere instalar Anaconda ni las dependencias de Python
en el equipo anfitrión para ejecutar la aplicación con Docker.

## 2. Archivos necesarios

- Dockerfile
- requirements.txt
- api.py
- web/index.html
- modelos/configuracion.json
- modelos/referencia_base.json
- modelos/limites_operativos.json
- Archivos .joblib requeridos por los modelos seleccionados

## 3. Construcción

Abrir una terminal en la carpeta principal del proyecto y ejecutar:

```powershell
docker build -t malta-predictiva:1.1 .
```

Esperar a que finalice la construcción sin errores.

## 4. Ejecución

```powershell
docker run -d --name malta-predictiva-app -p 127.0.0.1:8001:8000 malta-predictiva:1.1
```

## 5. Acceso a la aplicación

Interfaz web:

http://127.0.0.1:8001/app

Documentación interactiva de la API:

http://127.0.0.1:8001/docs

## 6. Comprobación

Abrir la dirección principal:

http://127.0.0.1:8001/

La API debe responder correctamente.

Desde la interfaz web, introducir valores dentro de los límites
operativos establecidos y ejecutar una predicción.

## 7. Detener el contenedor

```powershell
docker stop malta-predictiva-app
```

## 8. Volver a iniciarlo

```powershell
docker start malta-predictiva-app
```

## 9. Consultar registros

```powershell
docker logs malta-predictiva-app
```

## 10. Actualizar la aplicación

Después de modificar api.py, los modelos o las configuraciones:

```powershell
docker rm -f malta-predictiva-app
docker build -t malta-predictiva:1.1 .
docker run -d --name malta-predictiva-app -p 127.0.0.1:8001:8000 malta-predictiva:1.1
```

## 11. Consideraciones

Los modelos deben estar disponibles durante la construcción.

No publicar información industrial sin autorización.

Los límites operativos implementados corresponden a un criterio
experimental basado en el histórico de entrenamiento.

Las predicciones son orientativas y requieren validación adicional
antes de su utilización en producción.
