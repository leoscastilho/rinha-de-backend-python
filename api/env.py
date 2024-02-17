import os


def get_env(var, default=None):
    return os.environ[var] or default


config = {
    'database_url': get_env('DATABASE_NAME')
}
