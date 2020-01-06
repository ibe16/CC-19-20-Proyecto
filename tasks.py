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
    run ('python3 -m pytest --cov-report term --cov=notifier tests/')

# -b para indicar la ip y el puerto por el que acceder al servicio
# --workers es el número de procesos de se despliegan
# --daemon ejecuta la orden en segundo plano
# -p guarda el pid del proceso
# "notifier:create_app()" arranca el servicio. Se pasa una función porque se ha usado el patrón factoría
# La documentación de gunicorn recomienda establecer el número de workers así (2 x $num_cores) + 1
@task
def start(ctx, ip="0.0.0.0", puerto="5000"):
    run('gunicorn -b '+ip+':'+puerto+' --workers=5 -p notifier.pid "notifier:create_app()"')

# para el proceso de gunicorn
@task
def stop(ctx):
    run ('kill -9 $(cat notifier.pid)')
    run ('rm notifier.pid')