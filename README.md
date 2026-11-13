# IP Tracker API

API para gestão de endereços IP e VLANs, com Django REST Framework e PostgreSQL,
toda containerizada com Docker Compose.

## Stack
- Django REST Framework
- PostgreSQL 17
- pgAdmin 4
- Docker + Docker Compose

## Como rodar

```bash
git clone https://github.com/SEU_USUARIO/ip-tracker-docker.git
cd ip-tracker-docker
cp .env.example .env     # no PowerShell: copy .env.example .env
docker-compose up -d --build
```

| Serviço | URL |
|---|---|
| API | http://localhost:8000/api/v1/ips/ |
| Admin Django | http://localhost:8000/admin |
| pgAdmin | http://localhost:4000 |

## Arquitetura
Três containers na mesma rede Docker (`ip-rede`). O Django acessa o banco pelo
nome do serviço (`ip_db`), e os dados persistem em um volume.