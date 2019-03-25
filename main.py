from serial.can.can_main import run_can_main
from serial.nav.nav_main import run_nav_main
from services.eld_service import run_eld_services
import threading
# Start threads for devices


if __name__ == '__main__':
    service_thread = threading.Thread(name='eld_services', target=run_eld_services)
    service_thread.start()
    service_thread = threading.Thread(name='nav_main', target=run_nav_main)
    service_thread.start()
    run_can_main()


