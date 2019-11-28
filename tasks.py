from invoke import task, run

#elimina los archivos generados al pasar los test
@task 
def clean(ctx):
    print('Cleaning...')
    run ("rm -d -r .pytest_cache")
    run ("rm -d -r ./tests/__pycache__")
    run ("rm -d -r notifier/__pycache__")
    run ("rm .coverage")
    print ('Done!')

#instala las dependencias
@task
def install(ctx):
    print('Instalando...')
    run ('pip install -r requirements.txt')
    print ('Done!')

#ejecuta los test unitarios
@task
def test(ctx):
    run ('python3 -m pytest')

#ejecuta los test de cobertura
@task 
def coverage(ctx):
    run ('python3 -m pytest  --cov-report term --cov=notifier tests/')