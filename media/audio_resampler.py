import math

def bandlimited_gain(freq, cutoff):
    """带限增益：截止频率内为 1，之外为 0（抗镜像/抗混叠）。"""
    return 1.0 if freq <= cutoff else 0.0

def phase_carry(phase, ratio, count):
    """跨块相位：分数延迟相位按块累加并对 1 取模，保证块边界连续。"""
    return (phase + ratio * count) % 1.0

def rational_time(frames, in_rate, out_rate):
    """有理时间换算：先乘后整除，避免整数除法累积误差。"""
    return frames * out_rate // in_rate

def shared_phase(channels):
    """多声道共享相位：所有声道共用同一相位累加器。"""
    return True

def output_samples(in_samples, in_rate, out_rate):
    """输出样本数：按比例换算并取整，校正时长漂移。"""
    return round(in_samples * out_rate / in_rate)

def window_size(ratio):
    """窗长：随比例自适应，比例越大窗越长以保证低频信噪比。"""
    return int(4 * ratio)

def dither_scale(bits):
    """抖动幅度：按位深缩放，1 LSB 峰峰值。"""
    return 1 / (2 ** (bits - 1))

def reset_on_rate_change(old, new):
    """切采样率时重建滤波器状态（并配合淡入避免爆音）。"""
    return old != new

def separate_speed_pitch(rate, pitch):
    """变速与音高分离：各自独立的比例，不共用。"""
    return (rate, pitch)

def underrun_fill(samples, target):
    """欠载填充：不足部分补静音样本到目标长度。"""
    return list(samples) + [0.0] * (target - len(samples))

def resample_ratio(in_rate, out_rate):
    """重采样比例。"""
    return out_rate / in_rate

def channel_phase_delta(phases):
    """声道相位差：最大与最小相位之差。"""
    return max(phases) - min(phases)

def duration_drift(expected, actual):
    """时长漂移。"""
    return expected - actual

def anti_alias_cutoff(in_rate, out_rate):
    """抗混叠截止：取输入输出中较低的奈奎斯特频率。"""
    return min(in_rate, out_rate) // 2

def resampler_id(seed, index):
    """重采样 id。"""
    return f"{seed}-{index}"
