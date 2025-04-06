# extract_cube_faces_logging.py

import cv2
import os
from py360convert import e2c

# === Settings ===
video_path = "trimmed-360-felicitas-section.mp4"
output_dir = "cube_faces"
frame_interval = 30  # extract 1 frame per second from 30fps
selected_faces = {
    'L': 'left',
    'R': 'right',
    'U': 'top',
    'D': 'bottom'
}

# === Setup ===
os.makedirs(output_dir, exist_ok=True)
cap = cv2.VideoCapture(video_path)

# Total frames for progress tracking
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
progress_step = total_frames // 10  # every 10%

frame_count = 0
saved_count = 0

print(f"🔧 Processing {total_frames} frames total...")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    if frame_count % frame_interval == 0:
        face_w = frame.shape[1] // 4
        cube_faces = e2c(frame, face_w=face_w, mode='bilinear', cube_format='dict')

        for key, name in selected_faces.items():
            filename = os.path.join(output_dir, f"frame_{saved_count:04d}_{name}.jpg")
            cv2.imwrite(filename, cube_faces[key])

        saved_count += 1

    if frame_count % progress_step == 0 or frame_count == total_frames - 1:
        pct = int(100 * frame_count / total_frames)
        print(f"⏳ {pct}% complete ({frame_count}/{total_frames} frames)")

    frame_count += 1

cap.release()
print(f"\n✅ Done. Saved {saved_count} frames × {len(selected_faces)} faces to: {output_dir}")

