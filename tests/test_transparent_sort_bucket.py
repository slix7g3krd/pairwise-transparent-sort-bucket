import pytest
import render.transparent_sort_bucket as mod

CASES = [
    ("bucket_by_opacity", (0.5, 0.2)),
    ("depth_peel_resolve", (1, 2)),
    ("readback_depth", (1, 2)),
    ("coverage_threshold_mip", (0.5, 2)),
    ("leaf_tip_preserve", (1, 2)),
    ("material_split", (1, 2)),
    ("sort_key_stable", (1.0, 2.0)),
    ("double_sided", (1, 2)),
    ("caustic_layer", (1, 2)),
    ("alpha_test_consistency", (0.4, 0.5)),
    ("msaa_resolve_order", (1, 2)),
    ("oit_fallback", (1, 2)),
    ("ref_depth_epsilon", (0.001, 0.002)),
    ("batch_key", (1, 2)),
    ("coverage_scale", (0.5, 4)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
