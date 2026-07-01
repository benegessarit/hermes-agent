"""Regression tests for xAI curated model list (OAuth picker)."""

from hermes_cli.models import provider_model_ids


def test_xai_oauth_includes_grok_composer_2_5_fast():
    models = provider_model_ids("xai-oauth")
    assert "grok-composer-2.5-fast" in models


def test_grok_composer_slots_after_grok_build():
    models = provider_model_ids("xai-oauth")
    assert "grok-composer-2.5-fast" in models
    if "grok-build-0.1" in models:
        assert models.index("grok-composer-2.5-fast") == models.index("grok-build-0.1") + 1
