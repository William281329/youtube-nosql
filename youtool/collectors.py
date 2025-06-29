
class YouTubeComments:
    def __init__(self, api_keys):
        self.api_keys = api_keys
    def __call__(self, video_id):
        return [{"author": "Exemplo", "text": "Comentário exemplo"}]

class YouTubeTranscript:
    def __init__(self, api_keys):
        self.api_keys = api_keys
    def __call__(self, video_id):
        return ["Texto de transcrição exemplo"]
