from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler

from services.health_check.application.config import Config
from services.health_check.application.api_client import check_popular_repo_app_health


scheduler = BlockingScheduler()
scheduler.add_job(
    check_popular_repo_app_health,
    trigger="interval",
    minutes=Config.HEALTH_CHECK_INTERVAL,
    next_run_time=datetime.now(),
)

if __name__ == "__main__":
    scheduler.start()
