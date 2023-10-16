from celery import Celery
def make_celery(app):
    celery = Celery("Application Jobs",broker='redis://localhost:6379/0',backend='redis://localhost:6379/0')
                
    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)
    celery.Task=ContextTask
    return celery