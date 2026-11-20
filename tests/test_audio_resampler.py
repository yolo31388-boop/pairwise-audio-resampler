import pytest
from media import audio_resampler as mod

CASES = [
    ("gain", 'm.bandlimited_gain(10000, 20000) == 1.0'),
    ("gain2", 'm.bandlimited_gain(30000, 20000) == 0.0'),
    ("phase", 'm.phase_carry(0.5, 1.5, 2) == approx(0.5)'),
    ("time", 'm.rational_time(48000, 48000, 44100) == 44100'),
    ("shared", 'm.shared_phase([1, 2]) is True'),
    ("output", 'm.output_samples(48000, 48000, 44100) == 44100'),
    ("window", 'm.window_size(2) == 8'),
    ("dither", 'm.dither_scale(16) == approx(1 / 32768)'),
    ("reset", 'm.reset_on_rate_change(48000, 44100) is True'),
    ("separate", 'm.separate_speed_pitch(2, 1) == (2, 1)'),
    ("fill", 'm.underrun_fill([1], 3) == [1, 0.0, 0.0]'),
    ("ratio", 'm.resample_ratio(44100, 48000) == approx(1.088435)'),
    ("delta", 'm.channel_phase_delta([0.1, 0.3]) == approx(0.2)'),
    ("drift", 'm.duration_drift(10, 9.5) == approx(0.5)'),
    ("cutoff", 'm.anti_alias_cutoff(48000, 44100) == 22050')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx})
