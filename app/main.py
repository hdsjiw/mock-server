from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.models import APIKey, APIKeyIn, SecuritySchemeType
from fastapi.openapi.utils import get_openapi
from app.api.v1 import router as v1_router

app = FastAPI(
    title="Mock API Server",
    version="1.0.0",
    description="FastAPI 기반 Mock 서버입니다."
)

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API 라우터 등록
app.include_router(v1_router.router)


# ✅ OpenAPI 보안 스키마 등록 (Authorize 버튼용)
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        description=app.description,
        routes=app.routes,
    )

    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": SecuritySchemeType.apiKey.value,
            "in": APIKeyIn.header.value,
            "name": "Authorization",
            "description": "예: **Bearer mock_app_key**",
        }
    }

    # 모든 path에 BearerAuth 적용
    for path in openapi_schema["paths"].values():
        for method in path.values():
            method.setdefault("security", [{"BearerAuth": []}])

    app.openapi_schema = openapi_schema
    return app.openapi_schema


# 🔧 OpenAPI 설정 반영
app.openapi = custom_openapi
