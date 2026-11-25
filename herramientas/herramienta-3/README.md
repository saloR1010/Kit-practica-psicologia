# Herramienta 3: Organizador de Notas Temáticas y Seguimiento de Objetivos

## Objetivo Operativo
Proveer al psicólogo un sistema ligero y privado para almacenar notas temáticas, metas terapéuticas acordadas y generar resúmenes preparatorios antes de cada consulta, asegurando que cada sesión comience con una visión nítida de los compromisos previos.

## Archivos
- `organizador_seguimiento.py`: Clase administradora de casos, sesiones, metas y reportes preparatorios.
- `registro_casos.json`: Base de datos local ligera (formato JSON) donde se almacenan los registros anonimizados.

## Funcionalidades Principales
1. **Registro Anonimizado de Consultantes**: Creación de expedientes mediante códigos sin almacenar identificadores civiles sensibles.
2. **Seguimiento Dinámico de Metas**: Control de estado (`Pendiente`, `En progreso`, `Alcanzado`).
3. **Notas de Sesión Estructuradas**: Registro de temas clave, avances observados y tareas inter-sesión.
4. **Ficha Preparatoria Pre-Consulta**: Resumen ejecutivo con 1 solo clic para repasar antes de que inicie la cita.

## Instrucciones Breves de Uso

1. Ejecución de prueba:
   ```bash
   python organizador_seguimiento.py
   ```
2. Uso en módulos de Python:
   ```python
   from organizador_seguimiento import OrganizadorNotasSeguimiento

   org = OrganizadorNotasSeguimiento()
   org.registrar_caso("ID-PAC-05", "Manejo del estrés", ["Regular horarios de sueño"])
   org.agregar_nota_sesion("ID-PAC-05", num_sesion=1, temas_trabajados=["Higiene del sueño"], avances_observados="Registró sus horarios", compromisos_proxima_sesion="Cena 2h antes de dormir")
   print(org.generar_resumen_preparatorio("ID-PAC-05"))
   ```
