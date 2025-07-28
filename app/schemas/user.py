from pydantic import BaseModel, HttpUrl
from typing import List, Optional, Literal


class User(BaseModel):
    id: str
    name: str
    nickname: str
    email: str
    avatar_url: Optional[HttpUrl]
    display_name: str
    department: str
    position: str
    responsibility: str
    space_id: str
    mobiles: List[str]
    tels: List[str]
    vacation_start_time: Optional[int]
    vacation_end_time: Optional[int]
    work_start_time: int
    work_end_time: int
    status: str


class UsersFindByEmailResponse(BaseModel):
    success: bool
    user: Optional[User]  # 존재하지 않을 수도 있으므로 Optional

class UserAddRequest(BaseModel):
    id: str
    name: str
    nickname: str
    email: str
    avatar_url: str
    display_name: str
    department: str
    position: str
    responsibility: str
    space_id: str
    mobiles: List[str]
    tels: List[str]
    vacation_start_time: Optional[int]
    vacation_end_time: Optional[int]
    work_start_time: int
    work_end_time: int
    status: Literal["activated", "deactivated"]