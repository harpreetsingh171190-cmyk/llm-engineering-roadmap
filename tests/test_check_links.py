"""Tests for the offline link checker. No internet needed."""

import check_links as cl


def test_slugify_removes_emoji_and_punctuation():
    assert cl.slugify("📝 Notebooks") == "-notebooks"


def test_slugify_lowercases_and_joins_words():
    assert cl.slugify("The LLM Scientist") == "the-llm-scientist"


def test_slugify_keeps_hyphens_and_underscores():
    assert cl.slugify("Fine-tune my_model") == "fine-tune-my_model"


def test_is_external_detects_web_and_mail_links():
    assert cl.is_external("https://example.com")
    assert cl.is_external("http://example.com")
    assert cl.is_external("mailto:me@example.com")


def test_is_external_rejects_local_paths_and_anchors():
    assert not cl.is_external("img/banner.png")
    assert not cl.is_external("#notebooks")


def test_readme_has_no_broken_local_links():
    # The real README must pass the same check that CI runs.
    assert cl.main() == 0
