from utils.api_client import APIClient
from utils.logger import get_logger

logger = get_logger()

def test_get_products():
    response = APIClient.get(
        "/collections/products/records",
        params={"project_id": 13531}
    )

    logger.info("GET products called")

    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, dict)