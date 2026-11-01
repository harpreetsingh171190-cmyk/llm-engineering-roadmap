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
    assert cel.extract_urls(
        """
        

![x](img/banner.png)



        and #top
        """
    ) == []


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
    err = urllib.error.HTTPError("https://a.com", 404, "Not Found", None, None)
    with mock.patch.object(cel.urllib.request, "urlopen", side_effect=err):
        assert cel.check("https://a.com") == (False, "404")


def test_check_retries_with_get_when_head_is_refused():
    head_err = urllib.error.HTTPError("https://a.com", 405, "Not Allowed", None, None)
    with mock.patch.object(
        cel.urllib.request, "urlopen", side_effect=[head_err, _fake_response(200)]
    ) as opener:
        assert cel.check("https://a.com") == (True, "200")
        methods = [call.args[0].get_method() for call in opener.call_args_list]
        assert methods == ["HEAD", "GET"]


def test_check_reports_network_failure_without_crashing():
    with mock.patch.object(
        cel.urllib.request, "urlopen", side_effect=urllib.error.URLError("down")
    ):
        ok, status = cel.check("https://a.com")
        assert ok is False
        assert status == "URLError"


def test_main_never_fails_the_build(tmp_path):
    fake_readme = tmp_path / "README.md"
    fake_readme.write_text("https://a.com", encoding="utf-8")
    with mock.patch.object(cel, "README", fake_readme), \
         mock.patch.object(cel, "check", return_value=(False, "500")), \
         mock.patch.object(cel.time, "sleep"):
        assert cel.main() == 0
