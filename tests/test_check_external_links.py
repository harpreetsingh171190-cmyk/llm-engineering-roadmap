"""Tests for the external link checker. Network calls are mocked."""

import urllib.error
from unittest import mock

import check_external_links as cel


def test_extract_urls_returns_unique_urls_in_order():
    text = "See https://a.com and https://b.com, then https://a.com again."
    assert cel.extract_urls(text) == ["https://a.com", "https://b.com"]


def test_extract_urls_strips_trailing_punctuation():
    assert cel.extract_urls("Visit https://a.com.") == ["https://a.com"]


def test_extract_urls_ignores_local_links():
    assert cel.extract_urls("![x](img/banner.png) and #top") == []


def _fake_response(status):
    resp = mock.MagicMock()
    resp.status = status
    resp.__enter__.return_value = resp
    resp.__exit__.return_value = False
    return resp


def test_check_returns_ok_on_success():
    with mock.patch.object(cel.urllib.request, "urlopen", return_value=_fake_response(200)):
        assert cel.check("https://a.com") == (True, "200")


def test_check_reports_http_error_code():
