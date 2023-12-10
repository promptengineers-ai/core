from bson.objectid import ObjectId

# from fastapi import Request
from promptengineers.core.interfaces.controllers import IController
from promptengineers.core.interfaces.repos import IUserRepo
from promptengineers.repos.user import UserRepo
from promptengineers.mongo.service import MongoService
from promptengineers.models.request import ReqBodySettings

class SettingsController(IController):
	def __init__(
		self, 
		# request: Request = None, 
		request = None,
		user_repo: IUserRepo = None, 
		db_name: str = None,
		col_name: str = None
	):
		self.request = request
		self.user_id = getattr(request.state, "user_id", None)
		self.user_repo = user_repo or UserRepo()
		self.settings_service = MongoService(
			host=self.user_repo.find_token(self.user_id, 'MONGO_CONNECTION'),
			db=db_name or self.user_repo.find_token(self.user_id, 'MONGO_DB_NAME'),
			collection=col_name or 'settings'
		)

	##############################################################
	### Index
	##############################################################
	async def index(self, page: int = 1, limit: int = 10):
		result = await self.settings_service.list_docs(
			{'user_id': ObjectId(self.user_id)},
			limit,
			page
		)
		return result

	##############################################################
	### Create
	##############################################################
	async def create(self, body: ReqBodySettings):
		body = await self.request.json()
		body['user_id'] = ObjectId(self.user_id)
		result = await self.settings_service.create(dict(body))
		return result

	##############################################################
	### Update
	##############################################################
	async def show(self, id: str):
		result = await self.settings_service.read_one(
			{'_id': ObjectId(id), 'user_id': ObjectId(self.user_id)}
		)
		return result


	##############################################################
	### Update
	##############################################################
	async def update(self, id: str, body: ReqBodySettings):
		body = await self.request.json()
		result = await self.settings_service.update_one(
			{'_id': ObjectId(id), 'user_id': ObjectId(self.user_id)},
			dict(body)
		)
		return result

	##############################################################
	### Delete
	##############################################################
	async def delete(self, id: str):
		result = await self.settings_service.delete_one(
			{'_id': ObjectId(id), 'user_id': ObjectId(self.user_id)}
		)
		return result