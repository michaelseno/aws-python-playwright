import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True).new_context(
            record_video_dir="./videos"
        )
        yield browser
        browser.close()
