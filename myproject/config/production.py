from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'\xf4\x8d\x17\xe9\xb6yxZ\xa4g|\xeb\x08\xe8\x8e\x11'