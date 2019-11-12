from invoke import task, run

@task 
def clean(ctx):
    print('Cleaning...')
    run ("rm -d -r .pytest_cache")
    run ("rm -d -r ./tests/__pycache__")
    run ("rm -d -r notifier/__pycache__")
    print ('Done!')

@task
def install(ctx):
    print('Instalando...')
    run ('pip install -r requirements.txt')
    print ('Done!')

@task
def test(ctx):
    run ('pytest')

@task 
def coverage(ctx):
    run ('py.test  --cov-report term --cov=tests/')