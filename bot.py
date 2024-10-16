import re
import requests
import os
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Application, MessageHandler, ConversationHandler, filters


ASK_DNI, ASK_LOCATION = range(2)


async def start(update: Update, context) -> int:
    await update.message.reply_text('Hola! Por favor, envíame tu DNI (debe tener 8 dígitos).')
    return ASK_DNI


async def ask_dni(update: Update, context) -> int:
    dni = re.findall(r'\d+', update.message.text)
    if dni:
        dni = ''.join(dni)
        if len(dni) == 8:
            context.user_data['dni'] = dni
            await update.message.reply_text(f"Gracias! El DNI capturado es: {dni}. Ahora, por favor envíame tu ubicación.")
            location_button = KeyboardButton(
                text="Enviar ubicación", request_location=True)
            custom_keyboard = [[location_button]]
            reply_markup = ReplyKeyboardMarkup(custom_keyboard)
            await update.message.reply_text('Haz clic en el botón para compartir tu ubicación.', reply_markup=reply_markup)
            return ASK_LOCATION
        else:
            await update.message.reply_text("El DNI debe tener exactamente 8 dígitos. Por favor, intenta nuevamente.")
            return ASK_DNI
    else:
        await update.message.reply_text("No se encontró un DNI válido. Por favor, envíame un número de DNI válido.")
        return ASK_DNI


async def ask_location(update: Update, context) -> int:
    user_location = update.message.location
    if user_location:
        latitude = user_location.latitude
        longitude = user_location.longitude
        dni = context.user_data.get('dni', 'No proporcionado')
        endpoint = "https://dvahr80gmj.execute-api.us-east-1.amazonaws.com/cloud-chicho-lambda"
        data = {
            "dni": dni,
            "latitude": latitude,
            "longitude": longitude
        }
        response = requests.post(endpoint, json=data)
        print(response.json())
        await update.message.reply_text(f"Recibí tu ubicación: Latitud: {latitude}, Longitud: {longitude}. \nDNI: {dni}\nGracias por brindarnos sus datos.")
    else:
        await update.message.reply_text("No se pudo obtener tu ubicación.")

    return ConversationHandler.END


async def cancel(update: Update, context) -> int:
    await update.message.reply_text('Operación cancelada.')
    return ConversationHandler.END


def main() -> None:
    token = os.getenv('BOT_TOKEN', 'test_123')
    print(f"Token: {token}")
    application = Application.builder().token(
        token
    ).build()

    conv_handler = ConversationHandler(
        entry_points=[MessageHandler(filters.TEXT & (
            filters.Regex('^(Hola|Ayuda|ayuda|hola|auxilio|Auxilio)$')), start)],
        states={
            ASK_DNI: [MessageHandler(filters.TEXT & ~filters.COMMAND, ask_dni)],
            ASK_LOCATION: [MessageHandler(filters.LOCATION, ask_location)]
        },
        fallbacks=[MessageHandler(filters.Regex('^(cancelar)$'), cancel)],
    )
    application.add_handler(conv_handler)
    application.run_polling()


if __name__ == '__main__':
    main()
