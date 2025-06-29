import os
import sys
import json
from dotenv import load_dotenv

# Adiciona o caminho da youtool local
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from youtool.collectors import YouTubeComments, YouTubeTranscript
from youtool.utils import get_channel_videos

# Carrega a API KEY
load_dotenv()
API_KEY = os.getenv("YOUTUBE_API_KEY")
CHANNEL_ID = "UC5fvF4s6PRW4N0Yg2sPzLww"  # Manual do Mundo

# Busca os 5 vídeos mais recentes
videos = get_channel_videos(channel_id=CHANNEL_ID, api_keys=[API_KEY], max_results=5)

# Inicializa os coletores
comments_collector = YouTubeComments(api_keys=[API_KEY])
transcript_collector = YouTubeTranscript(api_keys=[API_KEY])

data = []

# Coleta os dados de cada vídeo
for video in videos:
    video_id = video["id"]
    title = video["title"]
    print(f"🎥 Coletando: {title}")

    try:
        comments = comments_collector(video_id)
    except Exception as e:
        print(f"⚠️ Erro ao coletar comentários: {e}")
        comments = []

    try:
        transcript = transcript_collector(video_id)
    except Exception as e:
        print(f"⚠️ Erro ao coletar transcrição: {e}")
        transcript = []

    data.append({
        "video_id": video_id,
        "title": title,
        "comments": comments,
        "transcript": transcript
    })

# Salva os dados
os.makedirs("../data", exist_ok=True)
with open("../data/export.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("✅ Dados coletados com sucesso e salvos em data/export.json")
