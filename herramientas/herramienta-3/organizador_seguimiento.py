"""
Herramienta 3: Organizador de notas temáticas y seguimiento de objetivos de trabajo terapéutico.
Mantiene el foco en metas acordadas colaborativamente, protegiendo la confidencialidad mediante anonimización de registros.
"""

import json
from datetime import datetime
from pathlib import Path

class OrganizadorNotasSeguimiento:
    def __init__(self, ruta_archivo: str = None):
        if ruta_archivo is None:
            self.ruta_archivo = Path(__file__).parent / "registro_casos.json"
        else:
            self.ruta_archivo = Path(ruta_archivo)
        self.datos = self._cargar_datos()

    def _cargar_datos(self) -> dict:
        if self.ruta_archivo.exists():
            try:
                return json.loads(self.ruta_archivo.read_text(encoding="utf-8"))
            except Exception:
                return {"casos": {}}
        return {"casos": {}}

    def _guardar_datos(self):
        self.ruta_archivo.write_text(json.dumps(self.datos, indent=2, ensure_ascii=False), encoding="utf-8")

    def registrar_caso(self, codigo_consultante: str, motivo_general: str, objetivos_iniciales: list) -> dict:
        """Crea o inicializa el seguimiento de un consultante anonimizado."""
        if codigo_consultante not in self.datos["casos"]:
            self.datos["casos"][codigo_consultante] = {
                "codigo": codigo_consultante,
                "fecha_inicio": datetime.now().strftime("%Y-%m-%d"),
                "motivo_general": motivo_general,
                "objetivos": [
                    {"id": i + 1, "descripcion": obj, "estado": "En progreso", "fecha_creacion": datetime.now().strftime("%Y-%m-%d")}
                    for i, obj in enumerate(objetivos_iniciales)
                ],
                "sesiones": []
            }
            self._guardar_datos()
            print(f"[OK] Caso {codigo_consultante} registrado correctamente.")
        return self.datos["casos"][codigo_consultante]

    def agregar_nota_sesion(self, codigo_consultante: str, num_sesion: int, temas_trabajados: list, avances_observados: str, compromisos_proxima_sesion: str):
        """Agrega una nota temática de sesión estructurada sin información confidencial no autorizada."""
        if codigo_consultante not in self.datos["casos"]:
            raise KeyError(f"El código {codigo_consultante} no existe. Regístralo primero con registrar_caso().")

        nueva_sesion = {
            "numero_sesion": num_sesion,
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "temas_clave": temas_trabajados,
            "avances_observados": avances_observados,
            "compromisos_acordados": compromisos_proxima_sesion
        }
        self.datos["casos"][codigo_consultante]["sesiones"].append(nueva_sesion)
        self._guardar_datos()
        print(f"[OK] Sesión #{num_sesion} registrada para el consultante {codigo_consultante}.")

    def actualizar_estado_objetivo(self, codigo_consultante: str, id_objetivo: int, nuevo_estado: str):
        """Actualiza el progreso de una meta acordada ('Pendiente', 'En progreso', 'Alcanzado')."""
        caso = self.datos["casos"].get(codigo_consultante)
        if not caso:
            raise KeyError(f"Código {codigo_consultante} no encontrado.")

        for obj in caso["objetivos"]:
            if obj["id"] == id_objetivo:
                obj["estado"] = nuevo_estado
                self._guardar_datos()
                print(f"[OK] Objetivo {id_objetivo} actualizado a '{nuevo_estado}'.")
                return
        print(f"[!] No se encontró el objetivo #{id_objetivo}.")

    def generar_resumen_preparatorio(self, codigo_consultante: str) -> str:
        """Genera un resumen rápido para que el psicólogo repase antes de entrar a sesión."""
        caso = self.datos["casos"].get(codigo_consultante)
        if not caso:
            return f"No existen registros previos para el código {codigo_consultante}."

        lineas = []
        lineas.append("=" * 68)
        lineas.append(f"FICHA OPERATIVA DE PREPARACIÓN DE SESIÓN")
        lineas.append(f"Consultante: {caso['codigo']} | Motivo: {caso['motivo_general']}")
        lineas.append("=" * 68)

        lineas.append("\n🎯 OBJETIVOS DE TRABAJO ACTIVOS:")
        for obj in caso["objetivos"]:
            estado_icono = "✅" if obj["estado"] == "Alcanzado" else "⏳"
            lineas.append(f"  {estado_icono} [Obj #{obj['id']}] ({obj['estado']}): {obj['descripcion']}")

        sesiones = caso.get("sesiones", [])
        lineas.append(f"\n📋 HISTORIAL DE SESIONES REGISTRADAS: {len(sesiones)}")
        if sesiones:
            ultima = sesiones[-1]
            lineas.append(f"  Última Sesión (Sesión #{ultima['numero_sesion']} el {ultima['fecha']}):")
            lineas.append(f"  - Temas abordados: {', '.join(ultima['temas_clave'])}")
            lineas.append(f"  - Avances: {ultima['avances_observados']}")
            lineas.append(f"  - Tareas o compromisos acordados: {ultima['compromisos_acordados']}")
        else:
            lineas.append("  (Aún no hay sesiones previas registradas)")

        lineas.append("\n" + "=" * 68)
        return "\n".join(lineas)

if __name__ == "__main__":
    print("--- Demostración de Herramienta 3 ---")
    organizador = OrganizadorNotasSeguimiento()

    # Caso de prueba
    id_prueba = "CONS-2026-DEMO"
    organizador.registrar_caso(
        codigo_consultante=id_prueba,
        motivo_general="Gestión de sobrecarga laboral y establecimiento de límites asertivos",
        objetivos_iniciales=[
            "Identificar disparadores de reactividad ante demandas urgentes en el trabajo",
            "Practicar dos respuestas asertivas por semana ante solicitudes extraordinarias",
            "Consolidar rutina de desconexión digital después de las 6:30 p.m."
        ]
    )

    organizador.agregar_nota_sesion(
        codigo_consultante=id_prueba,
        num_sesion=1,
        temas_trabajados=["Revisión de agenda semanal", "Concepto de asertividad vs. complacencia"],
        avances_observados="Mayor claridad conceptual al diferenciar una urgencia real de una percibida.",
        compromisos_proxima_sesion="Llevar registro de las veces en que postergó una negativa por incomodidad."
    )

    organizador.actualizar_estado_objetivo(id_prueba, id_objetivo=1, nuevo_estado="Alcanzado")

    resumen = organizador.generar_resumen_preparatorio(id_prueba)
    print(resumen)
