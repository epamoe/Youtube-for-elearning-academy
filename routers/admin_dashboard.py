from fastapi import APIRouter

router = APIRouter(
    prefix = "/dashboard/admin",
    tags = ["Admin's dashboard"]
)

@router.get("/validate/{demand_id}")
def validate(demand_id: int):
    ...