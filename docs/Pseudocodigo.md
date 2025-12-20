INICIO

  DEFINIR RUTA_HISTORIAL = "data/historial.json"

  DEFINIR TECNOLOGIAS (diccionario) con:
    1: IA
    2: Automatización
    3: IoT
    4: KamsayMed (caso de estudio)
  CADA opción contiene:
    - nombre
    - impactos_base {social, economico, etico}
    - riesgos (lista)

  PROCEDIMIENTO AsegurarDirectorioData()
    SI no existe carpeta "data" ENTONCES
      CREAR carpeta "data"
    FIN SI
  FIN PROCEDIMIENTO

  FUNCION CargarHistorial() DEVUELVE lista
    AsegurarDirectorioData()
    SI no existe RUTA_HISTORIAL ENTONCES
      DEVOLVER lista vacía
    SINO
      INTENTAR leer JSON desde RUTA_HISTORIAL
      SI lectura exitosa ENTONCES
        DEVOLVER lista leída
      SINO
        DEVOLVER lista vacía
      FIN SI
    FIN SI
  FIN FUNCION

  PROCEDIMIENTO GuardarHistorial(historial)
    AsegurarDirectorioData()
    GUARDAR historial como JSON en RUTA_HISTORIAL
  FIN PROCEDIMIENTO

  FUNCION PedirEntero(mensaje, minimo, maximo) DEVUELVE entero
    REPETIR
      MOSTRAR mensaje
      LEER entrada
      SI entrada no es número ENTONCES
        MOSTRAR "Entrada inválida"
      SINO
        valor = convertir entrada a entero
        SI valor < minimo O valor > maximo ENTONCES
          MOSTRAR "Fuera de rango"
        SINO
          DEVOLVER valor
        FIN SI
      FIN SI
    HASTA ingresar un valor válido
  FIN FUNCION

  PROCEDIMIENTO MostrarMenu()
    MOSTRAR "1. Inteligencia Artificial"
    MOSTRAR "2. Automatización"
    MOSTRAR "3. Internet de las Cosas (IoT)"
    MOSTRAR "4. KamsayMed (caso de estudio)"
    MOSTRAR "5. Ver historial"
    MOSTRAR "0. Salir"
  FIN PROCEDIMIENTO

  FUNCION AjustarPorContexto(impactos_base, contexto) DEVUELVE impactos
    COPIAR impactos_base en impactos

    SI contexto = 1 (Urbano) ENTONCES
      impactos.economico = impactos.economico + 5
    SINO SI contexto = 2 (Rural) ENTONCES
      impactos.social = impactos.social + 8
      impactos.economico = impactos.economico - 5
    SINO SI contexto = 3 (Educación) ENTONCES
      impactos.social = impactos.social + 6
      impactos.etico = impactos.etico + 3
    SINO SI contexto = 4 (Salud) ENTONCES
      impactos.social = impactos.social + 7
      impactos.etico = impactos.etico + 5
    FIN SI

    PARA cada area en impactos HACER
      SI impactos[area] > 100 ENTONCES impactos[area] = 100
      SI impactos[area] < 0 ENTONCES impactos[area] = 0
    FIN PARA

    DEVOLVER impactos
  FIN FUNCION

  FUNCION ClasificarNivel(score_total) DEVUELVE texto
    SI score_total >= 85 ENTONCES DEVOLVER "ALTO"
    SINO SI score_total >= 60 ENTONCES DEVOLVER "MEDIO"
    SINO DEVOLVER "BAJO"
    FIN SI
  FIN FUNCION

  FUNCION EvaluarTecnologia(opcion) DEVUELVE registro
    tech = TECNOLOGIAS[opcion]

    MOSTRAR "Selecciona contexto: 1 Urbano, 2 Rural, 3 Educación, 4 Salud"
    contexto = PedirEntero("Contexto (1-4):", 1, 4)

    impactos = AjustarPorContexto(tech.impactos_base, contexto)

    score_total = PROMEDIO(impactos.social, impactos.economico, impactos.etico)
    REDONDEAR score_total

    nivel = ClasificarNivel(score_total)

    SI nivel = "ALTO" ENTONCES recomendacion = "Implementar con enfoque ético y controles"
    SINO SI nivel = "MEDIO" ENTONCES recomendacion = "Mitigar riesgos y educar al usuario"
    SINO recomendacion = "Evaluar viabilidad y aceptación social"
    FIN SI

    CREAR registro con:
      fecha, tecnologia, contexto(texto), impactos, score_total, nivel, riesgos, recomendacion

    DEVOLVER registro
  FIN FUNCION

  PROCEDIMIENTO MostrarReporte(registro)
    MOSTRAR datos del registro (fecha, tecnologia, contexto, impactos, score_total, nivel)
    MOSTRAR recomendacion
    MOSTRAR lista de riesgos
  FIN PROCEDIMIENTO

  PROCEDIMIENTO VerHistorial(historial)
    SI historial está vacío ENTONCES
      MOSTRAR "No hay historial"
    SINO
      MOSTRAR últimas 10 evaluaciones
    FIN SI
  FIN PROCEDIMIENTO

  // PROGRAMA PRINCIPAL
  historial = CargarHistorial()
  opcion = -1

  MIENTRAS opcion != 0 HACER
    MostrarMenu()
    opcion = PedirEntero("Selecciona una opción:", 0, 5)

    SI opcion = 0 ENTONCES
      MOSTRAR "Programa finalizado"
    SINO SI opcion = 5 ENTONCES
      VerHistorial(historial)
    SINO SI opcion entre 1 y 4 ENTONCES
      registro = EvaluarTecnologia(opcion)
      MostrarReporte(registro)
      AGREGAR registro a historial
      GuardarHistorial(historial)
    SINO
      MOSTRAR "Opción no válida"
    FIN SI
  FIN MIENTRAS

FIN
