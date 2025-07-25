from playwright.sync_api import sync_playwright

def test_get_request():
    with sync_playwright() as p:
        request_context = p.request.new_context()
        response = request_context.get("https://jsonplaceholder.typicode.com/posts/1")

        assert response.status == 200
        json_data = response.json()
        assert json_data["id"] == 1
