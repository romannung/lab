import logging
import sentry_sdk

logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

sentry_sdk.init(
   dsn="https://d84816fa1e98d1d28a75d82abba00db4@o4509388742131712.ingest.de.sentry.io/4509388747243600",
   send_default_pii=True,
   traces_sample_rate=1.0
)

logging.info("Додаток запущено")
raise Exception("Тестова помилка для Sentry")

