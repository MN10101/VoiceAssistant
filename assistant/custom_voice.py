import numpy as np
import simpleaudio as sa

SAMPLE_RATE = 44100  # Standard sample rate for audio

# Extended phoneme frequencies
phoneme_frequencies = {
    'a': 440,   # Open front vowel
    'e': 660,   # Close-mid front vowel
    'i': 880,   # Close front unrounded vowel
    'o': 550,   # Close-mid back vowel
    'u': 330,   # Close back rounded vowel
    'm': 220,   # Nasal
    'n': 240,   # Nasal
    's': 990,   # Voiceless alveolar fricative
    'sh': 720,  # Voiceless postalveolar fricative
    'z': 880,   # Voiced fricative
    'th': 600,  # Voiceless dental fricative
    'r': 440,   # Approximant
    'l': 320,   # Lateral approximant
    'y': 770,   # Palatal approximant
    'k': 450,   # Voiceless stop
    'g': 430,   # Voiced stop
}

# Phoneme durations for better natural flow
phoneme_durations = {
    'a': 0.6, 'e': 0.5, 'i': 0.5, 'o': 0.5, 'u': 0.5,
    's': 0.8, 'sh': 0.7, 'm': 0.7, 'n': 0.7
}

def generate_tone(frequency, duration):
    """Generate a sine wave with amplitude envelope."""
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), False)
    tone = 0.5 * np.sin(2 * np.pi * frequency * t)

    # Apply amplitude envelope (fade in/out)
    fade_len = min(int(SAMPLE_RATE * 0.05), len(t) // 2)
    fade_in = np.linspace(0, 1, fade_len)
    fade_out = np.linspace(1, 0, fade_len)

    tone[:fade_len] *= fade_in
    tone[-fade_len:] *= fade_out

    return tone



def crossfade_tones(tone1, tone2, duration=0.1):
    """Crossfade two tones for smoother transitions."""
    crossfade_samples = int(SAMPLE_RATE * duration)
    
    # Apply crossfade by averaging overlapping samples
    tone1[-crossfade_samples:] *= np.linspace(1, 0, crossfade_samples)
    tone2[:crossfade_samples] *= np.linspace(0, 1, crossfade_samples)

    return np.concatenate((tone1[:-crossfade_samples], tone1[-crossfade_samples:] + tone2[:crossfade_samples], tone2[crossfade_samples:]))


def play_sound(waveform):
    """Play the generated waveform."""
    audio = (waveform * 32767).astype(np.int16)
    play_obj = sa.play_buffer(audio, 1, 2, SAMPLE_RATE)
    play_obj.wait_done()


def play_phoneme_sequence(phonemes):
    """Play a sequence of tones representing phonemes with smooth transitions."""
    combined_tone = np.array([])
    for i, phoneme in enumerate(phonemes):
        if phoneme in phoneme_frequencies:
            duration = phoneme_durations.get(phoneme, 0.5)  # Default duration is 0.5 seconds
            tone = generate_tone(phoneme_frequencies[phoneme], duration)
            if i > 0:
                combined_tone = crossfade_tones(combined_tone, tone)
            else:
                combined_tone = tone
        else:
            print(f"Unknown phoneme: {phoneme}")

    play_sound(combined_tone)

# Example usage
phonemes = ['a', 'm', 'o', 'r', 'e']  # Custom sequence for richer sound
play_phoneme_sequence(phonemes)
