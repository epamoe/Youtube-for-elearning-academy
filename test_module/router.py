

from fastapi import APIRouter

from accounts.activation.account_activation_handler import AccountActivationHandler
from accounts.data_classes.user import User


router = APIRouter(
    prefix="/tests",
    tags= ["tests"]
)

@router.get("/{id}")
def test(registration_id : str, email: str):
    try:
        AccountActivationHandler.send_activation_mail(
            User(
                mail=email,
                login="icono",
                password="string",
                profile_img="string"
            ),
            registration_id
        )
        return {
            "message" : "Finished"
        }
    except Exception as e:
        return "Error"