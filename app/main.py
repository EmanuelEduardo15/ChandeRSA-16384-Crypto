from fastapi import FastAPI, HTTPException, Depends, Header
from pydantic import BaseModel
from token_rsa import issue_token, verify_token
from api_key import generate_api_key, verify_api_key
from turbo_demo import generate_keys, pipeline  # seu motor otimizado

app = FastAPI(title="ChQuantum Demo")

# Modelos
class AuthIn(BaseModel):
    user: str

class DemoIn(BaseModel):
    message: str

class KeyIn(BaseModel):
    pass  # sem payload, usa o user do token

# Dependência para extrair usuário do JWT
def get_current_user(authorization: str = Header(...)) -> str:
    payload = verify_token(authorization)
    return payload["sub"]

# Endpoints

@app.post("/auth")
def auth(data: AuthIn):
    """
    Gera um JWT para o usuário. Use este token no header Authorization.
    """
    token = issue_token(data.user, minutes=60)
    return {"token": token}

@app.post("/generate_key")
def gen_key(user: str = Depends(get_current_user)):
    """
    Gera (ou retorna) a API Key para demos RSA/AES.
    """
    key = generate_api_key(user)
    return {"api_key": key}

@app.post("/demo")
def run_demo(
    payload: DemoIn,
    authorization: str = Header(...),       # JWT
    x_api_key: str = Header(..., alias="X-API-Key")  # sua chave
):
    """
    Executa o pipeline turbo só se JWT e API Key forem válidos.
    """
    user = verify_token(authorization)["sub"]
    if not verify_api_key(user, x_api_key):
        raise HTTPException(401, "API Key inválida")
    # carregar chaves uma vez
    pub, prv = generate_keys(bits=16384, workers=2)
    pt, dec_time = pipeline(payload.message, pub, prv)
    return {
        "user": user,
        "plaintext": pt,
        "decrypt_time_s": round(dec_time, 3)
    }
