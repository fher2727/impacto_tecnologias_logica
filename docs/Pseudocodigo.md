INICIO

Cargar historial de evaluaciones desde archivo

REPETIR
    Mostrar menú de tecnologías
    Leer opción del usuario

    SI opción = 0 ENTONCES
        Mostrar mensaje de salida
    SINO SI opción = 5 ENTONCES
        Mostrar historial de evaluaciones
    SINO SI opción corresponde a una tecnología ENTONCES
        Solicitar contexto de análisis
        Ajustar impactos según contexto
        Calcular puntaje total
        Clasificar nivel de impacto
        Generar recomendación
        Mostrar reporte de resultados
        Guardar evaluación en historial
    SINO
        Mostrar mensaje de opción no válida
    FIN SI
HASTA QUE opción = 0

FIN

