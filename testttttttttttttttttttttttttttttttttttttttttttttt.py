import mido
from mido import MidiFile, Message, MetaMessage, MidiTrack

# Create a new MIDI file
midi_file = MidiFile()
track = MidiTrack()
midi_file.tracks.append(track)

# Set the ticks per beat
ticks_per_beat = 480

# Set the tempo
tempo = mido.bpm2tempo(120)  # 120 BPM
meta_message = MetaMessage('set_tempo', tempo=tempo)
track.append(meta_message)

# Define the notes and their durations
notes = [
    ('G4', 4),
    ('G4', 4),
    ('C5', 4),
    ('C5', 4),
    ('B4', 2),
    ('A4', 2),
    ('G4', 8),
    ('G4', 4),
    ('C5', 4),
    ('C5', 4),
    ('B4', 2),
    ('A4', 2),
    ('G4', 8),
    ('D5', 4),
    ('D5', 4),
    ('D5', 4),
    ('D5', 4),
    ('B4', 4),
    ('B4', 4),
    ('G4', 8),
    ('G4', 4),
    ('C5', 4),
    ('C5', 4),
    ('B4', 2),
    ('A4', 2),
    ('G4', 8)
]

# Add note events to the track
time = 0
for note, duration in notes:
    octave = int(note[1])
    note_name = note[0]
    note_offset = {
        'C': 0, 'C#': 1, 'Db': 1, 'D': 2, 'D#': 3, 'Eb': 3,
        'E': 4, 'F': 5, 'F#': 6, 'Gb': 6, 'G': 7, 'G#': 8,
        'Ab': 8, 'A': 9, 'A#': 10, 'Bb': 10, 'B': 11
    }[note_name]
    note_number = (octave * 12) + note_offset
    track.append(Message('note_on', note=note_number, velocity=80, time=int(time)))
    time += ticks_per_beat // duration
    track.append(Message('note_off', note=note_number, velocity=0, time=int(time)))

# Save the MIDI file
midi_file.save('fallout_theme2.mid')

# Get the list of available output ports
output_ports = mido.get_output_names()

# Check if any output ports are available
if not output_ports:
    print("No MIDI output ports found.")
else:
    print("Available output ports:")
    for port in output_ports:
        print(port)

    # Open the first available output port
    output_port = mido.open_output(output_ports[0])