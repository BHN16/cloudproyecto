
# Proyecto Final Telegram Cloud computing (CS3P02) 

#### Integrantes:

- Dario Toribio

- Luis Ponce

---

## Descripción

Este proyecto consiste en un bot de Telegram diseñado para recopilar el DNI y la ubicación del usuario de manera sencilla e interactiva. Los datos obtenidos se envían a un endpoint específico para su procesamiento. El bot está desarrollado utilizando la biblioteca `python-telegram-bot` para la integración con Telegram y `requests` para realizar solicitudes HTTP hacia un servicio externo.

## Requisitos

Antes de ejecutar el proyecto, asegúrate de cumplir con los siguientes requisitos:

- **Python 3.7 o superior**: Verifica que tengas instalada una versión compatible de Python.
- **Librerías necesarias**: Asegúrate de instalar las siguientes dependencias:
   - `python-telegram-bot`
   - `requests`

Puedes instalarlas ejecutando el siguiente comando:

```bash
pip install python-telegram-bot requests
```

## Configuración

### 1. Obtener el token del bot de Telegram

Para iniciar, necesitas obtener el token de tu bot en Telegram. Sigue estos pasos:

- Accede a [BotFather](https://t.me/BotFather) en Telegram.
- Crea un nuevo bot siguiendo las instrucciones proporcionadas y copia el token generado.

### 2. Configurar las variables de entorno

El token obtenido debe configurarse como una variable de entorno para que el bot pueda funcionar correctamente. Puedes hacerlo de la siguiente manera:

- Crea un archivo `.env` en el directorio del proyecto o establece la variable directamente en tu sistema.
- Agrega el siguiente contenido al archivo `.env` o ejecuta este comando en tu terminal.

```bash
export BOT_TOKEN=tu_token_aqui

```

### 3. Configurar el endpoint para el procesamiento de datos

El bot envía los datos recopilados a un endpoint para su procesamiento. Asegúrate de que el endpoint esté activo y sea capaz de recibir solicitudes POST con formato JSON.

El endpoint configurado por defecto es el siguiente:

```plaintext
https://dvahr80gmj.execute-api.us-east-1.amazonaws.com/cloud-chicho-lambda

```

Si utilizas un endpoint diferente, asegúrate de actualizar el código del bot con la nueva URL.


## Uso

### 1. Ejecutar el script

Para iniciar el bot, abre tu terminal en el directorio donde se encuentra el archivo del proyecto y ejecuta el siguiente comando:

```bash
python nombre_del_archivo.py
```

### 2. Interacción con el bot

- Inicia la conversación escribiendo `Hola` o una palabra similar en el chat del bot.
- Cuando el bot lo solicite, ingresa un DNI válido de 8 dígitos.
- Comparte tu ubicación utilizando el botón que el bot te proporcionará.

### 3. Cancelar la operación

- En cualquier momento, puedes detener el flujo de la conversación escribiendo `cancelar`.

## Flujo del bot

### 1. Inicio  
   - El bot inicia la interacción solicitando al usuario que ingrese su DNI.

### 2. Validación del DNI  
   - El bot verifica si el DNI ingresado es válido (debe contener exactamente 8 dígitos).  
   - Si el DNI no es válido, solicita al usuario que lo ingrese nuevamente.

### 3. Solicitud de ubicación  
   - Una vez validado el DNI, el bot solicita al usuario que comparta su ubicación mediante un botón interactivo.

### 4. Envío de datos  
   - El bot recopila los datos ingresados (DNI y ubicación) y los envía al endpoint configurado para su procesamiento.

### 5. Finalización  
   - Finalmente, el bot agradece al usuario por su colaboración y concluye la conversación.


```plaintext
Inicio
  |
  v
Solicitar DNI
  |
  v
¿DNI válido (8 dígitos)?
  |--------------------|
  No                  Sí
  |                    |
  v                    v
Solicitar DNI       Solicitar ubicación
                     |
                     v
           Compartir ubicación
                     |
                     v
             Enviar datos al endpoint
                     |
                     v
              Agradecer y finalizar
```

## Manejo de errores

- **Validación del DNI**: 
Si el usuario ingresa un DNI no válido (que no cumple con los 8 dígitos requeridos), el bot pedirá al usuario que ingrese nuevamente un DNI correcto.
- **Ubicación no recibida**: 
Si la ubicación no se comparte correctamente, el bot notificará al usuario e intentará solicitar la ubicación nuevamente.

## Personalización

- **Modificar el endpoint**: 
Puedes actualizar el endpoint donde se envían los datos cambiando el valor en la función `ask_location`.
- **Editar mensajes**: 
Los textos enviados al usuario son personalizables y pueden ser modificados directamente en las funciones del bot para adaptarse a tus necesidades.

## Contribuciones

Si deseas colaborar en este proyecto, puedes hacerlo abriendo un issue o enviando un pull request en el repositorio correspondiente. Las sugerencias y mejoras siempre son bienvenidas.

## Licencia

Este proyecto está licenciado bajo los términos de la licencia MIT, lo que significa que puedes usar, modificar y distribuir el código libremente, respetando los términos de la licencia.
