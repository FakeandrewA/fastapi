import pytest
from app import schemas
from jose import jwt
from app.config import settings




def test_create_user(client):
    res = client.post("/users/",json={"email":"example@example.com","password":"example123"})
    new_user = schemas.UserResponse(**res.json())
    assert new_user.email == "example@example.com"
    assert res.status_code == 201

def test_login_user(client,test_user):
    
    res = client.post("/login",data={"username":test_user["email"],"password":test_user["password"]})
    login_res = schemas.Token(**res.json())

    payload = jwt.decode(login_res.access_token,settings.secret_key,algorithms=[settings.algorithm])
    id = payload.get("user_id")
    assert id == test_user['id']
    assert login_res.token_type == "bearer"
    assert res.status_code == 200

@pytest.mark.parametrize("email, password, status_code",[
    ("wrongemail@gmail.com","password123",403),
    ("testuser@example.com","wrongpassword",403),
    ("wrongemail@gmail.com","wrongpassword",403),
])
def test_incorrect_login(test_user,client,email,password,status_code):
    res = client.post("/login",data={"username":email,"password":password})
    print(res.status_code)
    assert res.status_code == status_code