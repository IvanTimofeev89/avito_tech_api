import io

import pytest
from PIL import Image
from rest_framework.test import APIClient

from announcement_api.models import Ad


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def test_image():
    image = Image.new("RGB", (100, 100))
    image_file = io.BytesIO()
    image.save(image_file, format="JPEG")
    image_file.name = "test_image.jpg"
    image_file.seek(0)
    return image_file


@pytest.fixture
def create_ads():
    Ad.objects.bulk_create(
        [
            Ad(name="Ad 1", description="Description 1", price=100),
            Ad(name="Ad 2", description="Description 2", price=200),
            Ad(name="Ad 3", description="Description 3", price=300),
        ]
    )
