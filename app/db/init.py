from app.models import models
from app.db import session


models.Base.metadata.create_all(bind=session.engine)
