import requests
import pytest
import json
import os
import time

def test_get_all_posts(base_url) :
    response = requests.get(f"{base_url}/posts")
    
    assert response.status_code == 200
    
def test_get_one_post(base_url) :
    response = requests.get(f"{base_url}/posts/1")
    body = response.json()
    
    assert response.status_code == 200
    assert body["id"] == 1
    assert "userId" in body
    assert "title" in body
    assert "body" in body

@pytest.mark.parametrize("post_id", [3, 10, 99, 100])
def test_get_posts_by_id(base_url, post_id) :
    response = requests.get(f"{base_url}/posts/{post_id}")
    body = response.json()
    
    assert response.status_code == 200
    assert body["id"] == post_id
    assert "userId" in body
    assert "title" in body
    assert "body" in body
    
@pytest.mark.parametrize("post_id", [3, 10, 99, 100])
def test_get_comments_by_id(base_url, post_id) :
    response = requests.get(f"{base_url}/posts/{post_id}/comments")
    body = response.json()
    comment = body[0]
    
    assert response.status_code == 200
    assert comment["postId"] == post_id
    assert "id" in comment
    assert "name" in comment
    assert "email" in comment
    assert "body" in comment
    
def test_post(base_url) :
    payload = {
        "title" : "classic",
        "body" : "fly me to the moon",
        "userId" : 1
    }
    
    response = requests.post(f"{base_url}/posts", json=payload)
    body = response.json()
    
    assert response.status_code == 201
    assert body["id"] == 101
    assert body["title"] == payload["title"]
    assert body["body"] == payload["body"]
    assert body["userId"] == payload["userId"]
    
def test_put(base_url) :
    payload = {
        "title" : "classic",
        "body" : "fly me to the moon"
    }
    
    response = requests.put(f"{base_url}/posts/1", json=payload)
    body = response.json()
    
    assert response.status_code == 200
    assert body["id"] == 1
    assert body["title"] == payload["title"]
    assert body["body"] == payload["body"]
    
def test_delete(base_url) :
    response = requests.delete(f"{base_url}/posts/1")
    
    assert response.status_code == 200