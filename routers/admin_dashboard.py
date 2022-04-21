from fastapi import APIRouter

router = APIRouter(
    prefix = "/ydev/dashboard/admin",
    tags = ["Admin's dashboard"]
)

@router.get("/validate/{demand_id}")
def validate(demand_id: int):
    ...