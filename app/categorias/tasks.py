from celery.decorators import task

@task
def test_celeybeat_task():
    time.sleep(1)
    print('Hello Im a periodic tasks executing every 10 secs')