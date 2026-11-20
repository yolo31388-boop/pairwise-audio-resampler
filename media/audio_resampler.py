import math

def bandlimited_gain(freq, cutoff):
    """带限增益。"""
    raise NotImplementedError("TODO: bandlimited_gain")

def phase_carry(phase, ratio, count):
    """跨块相位。"""
    raise NotImplementedError("TODO: phase_carry")

def rational_time(frames, in_rate, out_rate):
    """有理时间换算。"""
    raise NotImplementedError("TODO: rational_time")

def shared_phase(channels):
    """多声道共享相位。"""
    raise NotImplementedError("TODO: shared_phase")

def output_samples(in_samples, in_rate, out_rate):
    """输出样本数。"""
    raise NotImplementedError("TODO: output_samples")

def window_size(ratio):
    """窗长。"""
    raise NotImplementedError("TODO: window_size")

def dither_scale(bits):
    """抖动幅度。"""
    raise NotImplementedError("TODO: dither_scale")

def reset_on_rate_change(old, new):
    """切采样率重置。"""
    raise NotImplementedError("TODO: reset_on_rate_change")

def separate_speed_pitch(rate, pitch):
    """变速与音高分离。"""
    raise NotImplementedError("TODO: separate_speed_pitch")

def underrun_fill(samples, target):
    """欠载填充。"""
    raise NotImplementedError("TODO: underrun_fill")

def resample_ratio(in_rate, out_rate):
    """重采样比例。"""
    raise NotImplementedError("TODO: resample_ratio")

def channel_phase_delta(phases):
    """声道相位差。"""
    raise NotImplementedError("TODO: channel_phase_delta")

def duration_drift(expected, actual):
    """时长漂移。"""
    raise NotImplementedError("TODO: duration_drift")

def anti_alias_cutoff(in_rate, out_rate):
    """抗混叠截止。"""
    raise NotImplementedError("TODO: anti_alias_cutoff")

def resampler_id(seed, index):
    """重采样 id。"""
    raise NotImplementedError("TODO: resampler_id")
