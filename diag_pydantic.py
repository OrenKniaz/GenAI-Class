import sys, subprocess
from importlib.metadata import version, PackageNotFoundError

def show(pkg):
    try:
        print(pkg, version(pkg))
    except PackageNotFoundError:
        print(pkg, 'NOT INSTALLED')

print('Python:', sys.version.splitlines()[0])
for pkg in ('pydantic','typing-inspection','typing_extensions','annotated-types','openai'):
    show(pkg)

print('\nUpgrading core typing/pydantic support packages...')
subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pydantic', 'typing-inspection', 'typing_extensions', 'annotated-types'])

print('\nPost-upgrade versions:')
for pkg in ('pydantic','typing-inspection','typing_extensions','annotated-types','openai'):
    show(pkg)

print('\nTry importing pydantic and creating a small model:')
try:
    import pydantic as pd
    class M(pd.BaseModel):
        x: int
    print('pydantic import OK, version', pd.__version__)
except Exception as e:
    print('pydantic import/model error:', repr(e))

print('\nTry importing OpenAI client:')
try:
    import openai
    print('openai version', getattr(openai, '__version__', 'unknown'))
    from openai import OpenAI
    client = OpenAI(api_key=None)
    print('OpenAI client creation OK')
except Exception as e:
    print('openai import/client error:', repr(e))

print('\nDone.')
