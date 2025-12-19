"""
Proyecto Integrador – Lógica de Programación
Tema: El impacto de las nuevas tecnologías en la sociedad: visualización del futuro

Autor: Fernando Vinicio Santos
Año: 2025
"""

from datetime import datetime
import json
import os

HISTORY_PATH = os.path.join("data", "historial.json")

# --- Estructura de datos: tecnologías y configuración base ---
TECHS = {
    1: {
        "nombre": "Inteligencia Artificial (IA)",
        "impactos_base": {"social": 85, "economico": 80, "etico": 70},
        "riesgos": ["Sesgos algorítmicos", "Privacidad de datos", "Dependencia tecnológica"],
    },
    2: {
        "nombre": "Automatización",
        "impactos_base": {"social": 65, "economico": 85, "etico": 60},
        "riesgos": ["Desplazamiento laboral", "Brecha de habilidades", "Concentración de poder"],
    },
    3: {
        "nombre": "Internet de las Cosas (IoT)",
        "impactos_base": {"social": 70, "economico": 75, "etico": 65},
        "riesgos": ["Ciberseguridad", "Privacidad", "Dependencia de conectividad"],
    },
    4: {
        "nombre": "KamsayMed™ (Salud preventiva – caso de estudio)",
        "impactos_base": {"social": 90, "economico": 70, "etico": 80},
        "riesgos": ["Uso incorrecto sin orientación", "Dependencia de internet", "Manejo de datos sensibles"],
    },
}


# ---------------------- Utilidades ----------------------
def asegurar_directorio_data():
    """Crea la carpeta /data si no existe."""
    if not os.path.exists("data"):
        os.makedirs("data")


def cargar_historial():
    """Lee historial desde JSON si existe, si no retorna lista vacía."""
    asegurar_directorio_data()
    if not os.path.exists(HISTORY_PATH):
        return []
    try:
        with open(HISTORY_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return []


def guardar_historial(historial):
    """Guarda historial en JSON."""
    asegurar_directorio_data()
    with open(HISTORY_PATH, "w", encoding="utf-8") as f:
        json.dump(historial, f, ensure_ascii=False, indent=2)


def pedir_entero(mensaje, minimo=None, maximo=None):
    """Valida entrada numérica con límites opcionales."""
    while True:
        try:
            valor = int(input(mensaje).strip())
            if minimo is not None and valor < minimo:
                print(f"⚠️ Debe ser >= {minimo}. Intenta de nuevo.")
                continue
            if maximo is not None and valor > maximo:
                print(f"⚠️ Debe ser <= {maximo}. Intenta de nuevo.")
                continue
            return valor
        except ValueError:
            print("⚠️ Entrada inválida. Ingresa un número.")


def barra(valor, maximo=100, ancho=20):
    """Dibuja una barra simple en consola."""
    bloques = int((valor / maximo) * ancho)
    return "█" * bloques + "░" * (ancho - bloques)


# ---------------------- Lógica del programa ----------------------
def mostrar_menu():
    print("\n" + "=" * 60)
    print("   IMPACTO DE LAS NUEVAS TECNOLOGÍAS EN LA SOCIEDAD")
    print("=" * 60)
    for k in sorted(TECHS.keys()):
        print(f"{k}. {TECHS[k]['nombre']}")
    print("5. Ver historial")
    print("0. Salir")


def ajustar_por_contexto(impactos_base, contexto):
    """
    Ajusta impactos según contexto (condicionales).
    Contextos:
      1 = Urbano
      2 = Rural
      3 = Educación
      4 = Salud
    """
    impactos = impactos_base.copy()

    if contexto == 1:  # Urbano
        impactos["economico"] += 5
    elif contexto == 2:  # Rural
        impactos["social"] += 8
        impactos["economico"] -= 5
    elif contexto == 3:  # Educación
        impactos["social"] += 6
        impactos["etico"] += 3
    elif contexto == 4:  # Salud
        impactos["social"] += 7
        impactos["etico"] += 5

    # Limitar a 0..100
    for k in impactos:
        impactos[k] = max(0, min(100, impactos[k]))
    return impactos


def clasificar_nivel(score):
    """Clasifica score total (condicionales)."""
    if score >= 85:
        return "ALTO"
    elif score >= 60:
        return "MEDIO"
    else:
        return "BAJO"


def evaluar_tecnologia(opcion):
    """Evalúa una tecnología seleccionada y devuelve un registro."""
    tech = TECHS[opcion]

    print("\nSelecciona el contexto de análisis:")
    print("1. Urbano")
    print("2. Rural")
    print("3. Educación")
    print("4. Salud")
    contexto = pedir_entero("Contexto (1-4): ", 1, 4)

    impactos = ajustar_por_contexto(tech["impactos_base"], contexto)
    score_total = round((impactos["social"] + impactos["economico"] + impactos["etico"]) / 3)
    nivel = clasificar_nivel(score_total)

    # Recomendación simple basada en nivel (condicionales)
    if nivel == "ALTO":
        recomendacion = "Alta proyección: implementar con enfoque ético y controles claros."
    elif nivel == "MEDIO":
        recomendacion = "Proyección moderada: implementar con educación y mitigación de riesgos."
    else:
        recomendacion = "Proyección limitada: evaluar viabilidad, riesgos y aceptación social."

    registro = {
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "tecnologia": tech["nombre"],
        "contexto": {1: "Urbano", 2: "Rural", 3: "Educación", 4: "Salud"}[contexto],
        "impactos": impactos,
        "score_total": score_total,
        "nivel": nivel,
        "riesgos": tech["riesgos"],
        "recomendacion": recomendacion,
    }
    return registro


def mostrar_reporte(registro):
    """Imprime un reporte claro en consola."""
    print("\n" + "-" * 60)
    print(f"REPORTE DE IMPACTO – {registro['tecnologia']}")
    print("-" * 60)
    print(f"Fecha: {registro['fecha']}")
    print(f"Contexto: {registro['contexto']}")
    print("\nImpactos (0–100):")
    for area in ["social", "economico", "etico"]:
        val = registro["impactos"][area]
        print(f" - {area.capitalize():10s}: {val:3d} |{barra(val)}|")

    print(f"\nScore total: {registro['score_total']}  → Nivel: {registro['nivel']}")
    print(f"Recomendación: {registro['recomendacion']}")

    print("\nRiesgos principales:")
    for r in registro["riesgos"]:
        print(f" - {r}")
    print("-" * 60)


def ver_historial(historial):
    """Muestra historial guardado (bucle)."""
    if not historial:
        print("\n📭 No hay historial registrado todavía.")
        return

    print("\n" + "=" * 60)
    print("HISTORIAL DE EVALUACIONES")
    print("=" * 60)

    # Mostrar últimas 10
    ultimos = historial[-10:]
    for i, item in enumerate(ultimos, start=1):
        print(f"{i}. [{item['fecha']}] {item['tecnologia']} | {item['contexto']} | {item['nivel']} ({item['score_total']})")

    print("\nTip: mientras más ejecuciones tengas, más evidencia para el docente.")


def main():
    historial = cargar_historial()

    opcion = -1
    while opcion != 0:
        mostrar_menu()
        opcion = pedir_entero("Selecciona una opción: ", 0, 5)

        if opcion in TECHS:
            registro = evaluar_tecnologia(opcion)
            mostrar_reporte(registro)

            historial.append(registro)
            guardar_historial(historial)

        elif opcion == 5:
            ver_historial(historial)

        elif opcion == 0:
            print("\n✅ Programa finalizado. Gracias por usar el simulador.")
        else:
            print("⚠️ Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    main()

