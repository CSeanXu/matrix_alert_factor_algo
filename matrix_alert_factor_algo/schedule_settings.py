from apscheduler.executors.pool import ThreadPoolExecutor

MARKET_CRAWLER_SCHEDULER_EXECUTORS = {
    "default": ThreadPoolExecutor(10)
}

MARKET_CRAWLER_SCHEDULER_SETTINGS = {
    "trigger": "interval",
    "minutes": 10,
}
