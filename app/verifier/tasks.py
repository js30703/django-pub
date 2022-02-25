from celery import shared_task

from app.logger.models import TaskLog


@shared_task
def task_test(pk):
    log = TaskLog(title=f'테스크 로그 {pk}', body='테스크 로그 정상')

    try:
        log.status = 'S'
    except Exception:
        log.status = 'F'
    log.save()
