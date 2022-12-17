from moviepy.editor import *
import json

class StatusCutter:
    def __init__(self):
        self.video = None
        self.current_duration = 0
        self.max_duration = 0
        self.cut_offset = 10
        self.video_index = 0
        self.video_name = ""
        self.video_path = ""
        self.setup()
    
    def setup(self):
        file = open('config.json', "r")
        data = json.loads(file.read())
        self.cut_offset = data["cut_offset"] if data["cut_offset"] > 0 else self.cut_offset
        self.video_path = data["video_path"]
    
    def load_video(self):
        self.video = VideoFileClip(self.video_path)
        self.max_duration = self.video.duration
        self.video_name = self.video.filename.split(".")[0]
        self.cut_video()
        
    
    def cut_video(self):
        while self.current_duration < self.max_duration:
            next_duration = self.current_duration + self.cut_offset
            
            if next_duration > self.max_duration:
                next_duration = self.max_duration
                
            clip = self.video.subclip(self.current_duration, next_duration)
            clip.write_videofile(f"{self.video_name}_{self.video_index}.mp4", codec="libx264")
            self.current_duration  = next_duration
            self.video_index += 1