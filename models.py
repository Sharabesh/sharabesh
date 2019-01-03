import os
from urllib.parse import urlparse
from playhouse import signals
from playhouse.postgres_ext import *


url = urlparse(os.environ["WEBSITE_DB"])

config = dict(
	database=url.path[1:],
	user=url.username,
	password=url.password,
	host=url.hostname,
	port=url.port,
	sslmode='require'
)


conn = PostgresqlExtDatabase(
	autocommit=True,
	autorollback=True,
	register_hstore=False,
	**config
)

class BaseModel(signals.Model):

	class Meta:
		database = conn


class Cookies(BaseModel):
	cookie_value = CharField(primary_key=True)
	date_added = DateTimeField(null= True)

	class Meta:
		db_table = "cookies"


