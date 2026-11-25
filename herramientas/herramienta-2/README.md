# Herramienta 2: Generador de Plantillas de Psicoeducación y Tareas Entre Sesiones

## Objetivo Operativo
Permitir al psicólogo generar en segundos fichas de psicoeducación claras, con lenguaje accesible y formatos estructurados de tareas inter-sesión para el consultante. Optimiza el tiempo administrativo garantizando material profesional y libre de etiquetas clínicas estigmatizantes.

## Archivos
- `generador_psicoeducacion.py`: Módulo generador de plantillas temáticas con ejercicios prácticos y tablas de registro.
- `ejemplo_tarea_psicoeducativa.txt`: Ejemplo generado en texto plano listo para enviar o imprimir.

## Plantillas Incluidas
1. **Comprensión del Ciclo de Activación y Evitación**: Psicoeducación sobre cómo se retroalimentan los pensamientos de alarma y sensaciones corporales, con registro de situaciones y respuestas.
2. **Entrenamiento en Pausa Consciente y Respiración**: Explicación del sistema parasimpático y guía paso a paso con bitácora de auto-observación.
3. **Registro de Agradecimientos y Logros**: Trabajo sobre sesgo atencional con formato de registro nocturno.

## Instrucciones Breves de Uso

1. Ejecución directa:
   ```bash
   python generador_psicoeducacion.py
   ```
2. Integración en código:
   ```python
   from generador_psicoeducacion import generar_plantilla_psicoeducativa, guardar_plantilla

   material = generar_plantilla_psicoeducativa(
       tipo_plantilla="pausa_respiracion",
       codigo_consultante="ID-CONS-42",
       indicaciones_personalizadas="Practicar preferiblemente antes de la jornada laboral."
   )
   guardar_plantilla(material, "tarea_respiracion.txt")
   ```
