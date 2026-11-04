# Malta Predictiva

## Descripción

Prototipo de inteligencia artificial desarrollado para anticipar
indicadores de calidad de la malta a partir de variables del proceso
de secado en la planta Cebadas y Maltas (CYM).

El sistema permite introducir condiciones operativas y obtener
predicciones mediante una interfaz web conectada a una API FastAPI.

## Objetivo

Explorar la viabilidad de utilizar modelos de aprendizaje automático
como herramienta de apoyo para anticipar resultados de calidad.

## Datos utilizados

Se integraron registros históricos de producción (PTS) y resultados
de calidad (MQI), relacionados mediante el identificador de lote.

- Registros integrados: 453
- Registros completos: 449
- Entrenamiento: 314
- Validación: 67
- Prueba: 68

La división se realizó cronológicamente para evitar utilizar
información futura durante el entrenamiento.

## Variables de entrada

1. Variedad de cebada
2. Tamaño de batch
3. Tiempo de calentamiento
4. Tiempo de curado
5. Temperatura de inicio
6. Temperatura de curado
7. Temperatura previa al punto de quiebre

## Indicadores de salida

- Extracto
- Color
- Kolbach
- FAN
- Beta glucanos
- Poder diastásico
- PUGs
- WUGs
- Friabilidad
- Pasamalla

## Modelos

Se evaluaron tres alternativas:

- Modelo base mediante medianas por variedad
- Random Forest
- Extra Trees

La selección de cada indicador se realizó utilizando el conjunto
de validación. Posteriormente se evaluó el desempeño con un
conjunto de prueba independiente.

Los resultados se encuentran en modelos/metricas_finales.csv.

## Arquitectura

Usuario
    |
Interfaz web (HTML)
    |
API FastAPI
    |
Validación de entradas
    |
Modelos predictivos
    |
Respuesta JSON con diez indicadores

La aplicación se distribuye mediante Docker.

## Validaciones

La API comprueba los tipos de datos, campos obligatorios y rangos
operativos. Los rangos se calcularon utilizando los mínimos y
máximos del entrenamiento, ampliados con una tolerancia del 10%.

Los límites son criterios experimentales del prototipo y no
sustituyen las especificaciones oficiales del proceso.

## Pruebas

Se realizaron pruebas de funcionamiento en Docker y ocho casos
de validación de entradas.

Resultados de la versión 1.1:

- Una entrada normal: HTTP 200
- Siete entradas inválidas o fuera de rango: HTTP 422
- Ocho pruebas con el comportamiento esperado

## Ejecución

Consultar MANUAL_DESPLIEGUE.md.

## Limitaciones

El proyecto es una prueba de concepto. Los resultados no deben
utilizarse para modificar automáticamente parámetros de producción.

Las pruebas de API comprueban el funcionamiento técnico, pero no
garantizan la precisión de los modelos ante nuevos lotes.

Los datos históricos y los modelos entrenados con información
industrial deben gestionarse de acuerdo con las autorizaciones
de la organización.
