from utils.headers import *

def test_get_all_posts(api):
    # Given
    endpoint = "/posts"

    # When
    response = api.get(endpoint)

    # Then
    assert response.status_code == 200


def test_get_one_post(api):
    # Given
    post_id = 1
    endpoint = f"/posts/{post_id}"

    # When
    response = api.get(endpoint)
    body = response.json()

    # Then
    assert response.status_code == 200
    assert body["id"] == post_id
    assert "userId" in body
    assert "title" in body
    assert "body" in body


@pytest.mark.parametrize("post_id", [3, 10, 99, 100])
def test_get_posts_by_id(api, post_id):
    # Given
    endpoint = f"/posts/{post_id}"

    # When
    response = api.get(endpoint)
    body = response.json()

    # Then
    assert response.status_code == 200
    assert body["id"] == post_id
    assert "userId" in body
    assert "title" in body
    assert "body" in body


@pytest.mark.parametrize("post_id", [3, 10, 99, 100])
def test_get_comments_by_id(api, post_id):
    # Given
    endpoint = f"/posts/{post_id}/comments"

    # When
    response = api.get(endpoint)
    comments = response.json()

    # Then
    assert response.status_code == 200
    assert isinstance(comments, list)
    assert len(comments) > 0

    comment = comments[0]
    assert comment["postId"] == post_id
    assert "id" in comment
    assert "name" in comment
    assert "email" in comment
    assert "body" in comment


def test_create_post(api, create_payload):
    # Given
    endpoint = "/posts"

    # When
    response = api.post(endpoint, create_payload)
    body = response.json()

    # Then
    assert response.status_code == 201
    assert body["id"] == 101
    assert body["title"] == create_payload["title"]
    assert body["body"] == create_payload["body"]
    assert body["userId"] == create_payload["userId"]


def test_update_post(api, update_payload):
    # Given
    post_id = 1
    endpoint = f"/posts/{post_id}"

    # When
    response = api.put(endpoint, update_payload)
    body = response.json()

    # Then
    assert response.status_code == 200
    assert body["id"] == post_id
    assert body["title"] == update_payload["title"]
    assert body["body"] == update_payload["body"]


def test_delete_post(api):
    # Given
    post_id = 1
    endpoint = f"/posts/{post_id}"

    # When
    response = api.delete(endpoint)

    # Then
    assert response.status_code == 200