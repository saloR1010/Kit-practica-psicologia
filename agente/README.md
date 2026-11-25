# Asistente Operativo del Psicólogo (Bot de Telegram)

## Objetivo
Asistente enfocado en la preparación previa a la jornada de trabajo, organización de recordatorios administrativos y consulta rápida de objetivos terapéuticos bajo códigos de consultante anonimizados, sin emitir juicios ni diagnósticos clínicos automatizados.

## Comandos Disponibles
- `/start` - Bienvenida e inducción de comandos.
- `/jornada` - Resumen inicial para comenzar la jornada laboral.
- `/tareas` - Lista de pendientes administrativos y operativos.
- `/recordar <texto>` - Registrar un nuevo recordatorio en la lista.
- `/check <id>` - Marcar una tarea pendiente como finalizada.
- `/preparar <codigo>` - Generar la ficha ejecutiva de objetivos antes de atender a un consultante (conecta con Herramienta 3).
- `/ayuda` - Explicación de los límites éticos y confidencialidad.

## Configuración y Ejecución

1. Asegúrate de tener configurado tu token en el archivo `.env`:
   ```env
   TELEGRAM_BOT_TOKEN=tu_token_aqui
   ```
2. Inicia el bot:
   ```bash
   python bot_telegram.py
   ```
