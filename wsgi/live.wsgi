import os
import sys
import site
import dotenv

from django.core.wsgi import get_wsgi_application

# The home directory of the user
USERHOME_DIR = '/home/django'

dotenv.read_dotenv(os.path.join(USERHOME_DIR, '.env'))

# Django directory, where manage.py resides
DPROJECT_DIR = os.path.join(USERHOME_DIR, 'project/projectile')
os.environ['DJANGO_SETTINGS_MODULE'] = 'projectile.settings_live'
sys.path.append(DPROJECT_DIR)

# Site-packages under virtualenv directory
SITEPACK_DIR = os.path.join(USERHOME_DIR, 'env/lib/python3.6/site-packages')
site.addsitedir(SITEPACK_DIR)

application = get_wsgi_application()