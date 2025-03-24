from jnius import autoclass
from android.broadcast import BroadcastReceiver

Context = autoclass('android.content.Context')
Intent = autoclass('android.content.Intent')

def start_service(context, intent):
    service = Intent(context, Context.getSystemService(Context.JOB_SCHEDULER_SERVICE))
    context.startService(service)

boot_receiver = BroadcastReceiver(start_service, actions=['android.intent.action.BOOT_COMPLETED'])
boot_receiver.start()

