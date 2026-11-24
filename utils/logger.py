import pathlib
from datetime import datetime
import logging

# El logger sirve para registrar información sobre la ejecución del código, como errores, advertencias, información de depuración, etc.

log_dir = pathlib.Path("logs") # se define la carpeta donde se guardarán los logs
log_dir.mkdir(exist_ok=True) # se crea la carpeta si no existe

# ahora almacenamos la fecha y hora para poder crear un nombre de archivo único para cada ejecución del código
timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M-%S") # se obtiene la fecha y hora actual en formato DD-MM-YYYY_HH-MM-SS

logging.basicConfig(
    filename=log_dir / f"log_{timestamp}.log", # se define el nombre del archivo de log con la fecha y hora actual
    level=logging.INFO, # indica a partir de qué nivel de severidad se registrarán los mensajes (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s", # se define el formato del mensaje de log (fecha y hora, nivel de severidad, mensaje)
    force=True # fuerza la configuración del logger aunque ya haya sido configurado previamente
)

logger = logging.getLogger("test_sauce_demo")