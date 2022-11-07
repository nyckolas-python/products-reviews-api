import http
import json

from unittest.mock import patch

from src import app


class TestReviwes:
    def test_get_product_and_reviews_per_page_with_db(self):
        client = app.test_client()
        resp = client.get('/api/v1/products/1/reviews?page=1')

        assert resp.status_code == http.HTTPStatus.OK
        assert len(resp.json['reviews']) == 1

    def test_get_product_and_reviews_with_db(self):
        client = app.test_client()
        resp = client.get('/api/v1/products/1/reviews')

        assert resp.status_code == http.HTTPStatus.OK

    @patch('src.services.ProductService.fetch_all_products', autospec=True)
    def test_get_product_and_reviews_mock_db(self, mock_db_call):
        client = app.test_client()
        resp = client.get('/api/v1/products/1/reviews')

        mock_db_call.assert_called_once()
        assert resp.status_code == http.HTTPStatus.OK

    def test_put_review_with_mock_db(self):
        with patch('src.db.session.add', autospec=True) as mock_session_add, \
                patch('src.db.session.commit', autospec=True) as mock_session_commit:
            client = app.test_client()
            data = {
                'product_id': 1,
                'title': 'Test Title',
                'review': 'Test Review'
            }
            resp = client.put(f"/api/v1/products/{data['product_id']}/reviews", data=json.dumps(
                data), content_type='application/json')

            mock_session_add.assert_called_once()
            mock_session_commit.assert_called_once()
            assert resp.status_code == http.HTTPStatus.CREATED

    def test_post_review_with_mock_db(self):
        with patch('src.db.session.add', autospec=True) as mock_session_add, \
                patch('src.db.session.commit', autospec=True) as mock_session_commit:
            client = app.test_client()
            data = {
                'product_id': 1,
                'title': 'Test Title',
                'review': 'Test Review'
            }
            resp = client.post(f"/api/v1/products/{data['product_id']}/reviews", data=json.dumps(
                data), content_type='application/json')

            assert resp.status_code == http.HTTPStatus.METHOD_NOT_ALLOWED

    def test_delete_review_with_mock_db(self):
        with patch('src.db.session.add', autospec=True) as mock_session_add, \
                patch('src.db.session.commit', autospec=True) as mock_session_commit:
            client = app.test_client()
            data = {
                'product_id': 1,
                'title': 'Test Title',
                'review': 'Test Review'
            }
            resp = client.delete(
                f"/api/v1/products/{data['product_id']}/reviews", data=json.dumps(data), content_type='application/json')

            assert resp.status_code == http.HTTPStatus.METHOD_NOT_ALLOWED
