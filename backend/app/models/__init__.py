#import your model here

from app.core.database import Base
from app.models.user import User
from app.models.patient import Patient
from app.models.media import Media




__all__=["Base","User","Patient","Media"]





