import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'udacityproject1'
    BLOB_STORAGE_KEY = os.environ.get(
        'BLOB_STORAGE_KEY') or 'zbS2FDp6oPitOdADKP2UxVQpGlX/AYChXu6RGSvB1eHBP/xk6pWQGTN5azHBXLjSfPck1BcGjO4s+AStCW4itA=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'blobcontainer'

    SQL_SERVER = os.environ.get(
        'SQL_SERVER') or 'udacity-project-1-sql-server.database.windows.net'
    SQL_DATABASE = os.environ.get(
        'SQL_DATABASE') or 'Udacity-Project-1-Database'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'udacity-sql-admin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'QuanHa9900'
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + \
        SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + \
        SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    CLIENT_SECRET = "m468Q~iOFLR4t7oLiObdm2RK4WsNrryARBCiIaMC"
    # In your production app, Microsoft recommends you to use other ways to store your secret,
    # such as KeyVault, or environment variable as described in Flask's documentation here:
    # https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    # CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    # if not CLIENT_SECRET:
    #     raise ValueError("Need to define CLIENT_SECRET environment variable")

    # AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app, else put tenant name
    AUTHORITY = "https://login.microsoftonline.com/312f4075-84ae-4729-86c3-9970c40bb5a3"

    CLIENT_ID = "d01f6614-f979-4cee-93d7-777edc8af5b8"

    # Used to form an absolute URL; must match to app's redirect_uri set in AAD
    REDIRECT_PATH = "/index"

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"]  # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session

    REDIRECT_URL = 'https://udacityproject1.azurewebsites.net/index'
    #REDIRECT_URL = 'https://localhost:5555/index'
