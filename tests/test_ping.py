from httpx import AsyncClient


async def test_ping(client: AsyncClient):
    response = await client.get('/')
    assert response.status_code == 200
    assert response.json() == 'pong'