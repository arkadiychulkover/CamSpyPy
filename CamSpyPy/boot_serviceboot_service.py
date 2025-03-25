from jnius import autoclass
from plyer import notification

Context = autoclass('android.content.Context')
Intent = autoclass('android.content.Intent')
PythonService = autoclass('org.kivy.android.PythonService')

def start_service(context, intent):
    service_intent = Intent(context, PythonService)
    context.startService(service_intent)

notification.notify(title="Сервис", message="Boot Completed Triggered!", timeout=5)
