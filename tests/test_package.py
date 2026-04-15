"""Package smoke tests."""

from __future__ import annotations

from ycb_sim import get_asset_root, resolve_asset


def test_asset_root_exists() -> None:
    root = get_asset_root()
    assert root.exists()
    assert (root / "README.md").exists()


def test_can_resolve_known_xml() -> None:
    xml_path = resolve_asset("includes/defaults_ycb.xml")
    assert xml_path.exists()
