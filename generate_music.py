"""
Gemini Lyria RealTime 音樂生成器
================================
互動式介面，依照 MIDST 公式引導你設定音樂風格，再呼叫 API 生成音樂。

使用前準備：
1. 安裝套件：pip install google-genai
2. 將下方 API_KEY 替換成你的 Google AI Studio API 金鑰
   取得金鑰：https://aistudio.google.com/apikey
"""

import asyncio
import wave
from google import genai
from google.genai import types

# ==================================================
# >>> 把 YOUR_API_KEY 替換成你自己的金鑰 <<<
API_KEY = "YOUR_API_KEY"
# ==================================================


# ==================== 選單資料 ====================

STYLES = {
    "1": ("Pop 流行樂", "pop"),
    "2": ("Rock 搖滾", "rock"),
    "3": ("Jazz 爵士", "jazz"),
    "4": ("EDM 電子舞曲", "edm electronic dance"),
    "5": ("Classical 古典", "classical orchestral"),
    "6": ("Lo-fi 低保真", "lo-fi chill hop"),
    "7": ("Hip Hop 嘻哈", "hip hop rap beat"),
    "8": ("R&B 節奏藍調", "r&b soul"),
    "9": ("Folk 民謠", "folk acoustic"),
    "10": ("Ambient 環境音樂", "ambient atmospheric"),
}

MOODS = {
    "1": ("Happy 歡樂", "happy cheerful upbeat"),
    "2": ("Sad 憂傷", "sad melancholic emotional"),
    "3": ("Relaxed 放鬆", "relaxed calm peaceful"),
    "4": ("Energetic 激昂", "energetic powerful intense"),
    "5": ("Romantic 浪漫", "romantic warm tender"),
    "6": ("Epic 史詩", "epic cinematic dramatic"),
    "7": ("Mysterious 神秘", "mysterious dark suspenseful"),
    "8": ("Nostalgic 懷舊", "nostalgic bittersweet retro"),
}

INSTRUMENTS = {
    "1": ("Piano 鋼琴", "piano"),
    "2": ("Acoustic Guitar 木吉他", "acoustic guitar"),
    "3": ("Electric Guitar 電吉他", "electric guitar"),
    "4": ("Strings 弦樂", "strings violin cello"),
    "5": ("Saxophone 薩克斯風", "saxophone"),
    "6": ("Synthesizer 合成器", "synthesizer synth"),
    "7": ("Drums 鼓組", "drums percussion"),
    "8": ("Bass 貝斯", "bass"),
    "9": ("Flute 長笛", "flute"),
    "10": ("Ukulele 烏克麗麗", "ukulele"),
}

VOCALS = {
    "0": ("No Vocals 純器樂（不要人聲）", "instrumental, no vocals"),
    "1": ("Male - Deep 男低音（低沉渾厚）", "deep male vocals, baritone"),
    "2": ("Male - Mid 男中音（自然中性）", "male vocals, tenor"),
    "3": ("Male - High 男高音（高亢明亮）", "high male vocals, countertenor"),
    "4": ("Male - Husky 沙啞男聲（磁性粗獷）", "husky raspy male vocals"),
    "5": ("Female - Low 女低音（低沉溫暖）", "low female vocals, contralto"),
    "6": ("Female - Mid 女中音（自然柔和）", "female vocals, mezzo-soprano"),
    "7": ("Female - High 女高音（高亢清亮）", "high female vocals, soprano"),
    "8": ("Female - Breathy 氣息感女聲（輕柔夢幻）", "breathy airy female vocals"),
    "9": ("Choir 合唱團（多人和聲）", "choir vocal harmonies"),
}


# ==================== 互動介面 ====================

def show_menu(title, options):
    """顯示選單並讓使用者選擇"""
    print(f"\n{'=' * 50}")
    print(f"  {title}")
    print(f"{'=' * 50}")
    for key, (label, _) in options.items():
        print(f"  [{key:>2}] {label}")
    print(f"{'=' * 50}")


def get_choice(title, options, allow_multiple=False):
    """取得使用者的選擇"""
    show_menu(title, options)

    if allow_multiple:
        print("  (可多選，用逗號分隔，例如：1,3,5)")

    while True:
        choice = input("\n  請輸入編號：").strip()

        if allow_multiple:
            keys = [k.strip() for k in choice.split(",")]
            if all(k in options for k in keys):
                return keys
            print("  輸入有誤，請重新選擇。")
        else:
            if choice in options:
                return choice
            print("  輸入有誤，請重新選擇。")


def get_bpm():
    """取得 BPM 設定"""
    print(f"\n{'=' * 50}")
    print("  T — Tempo 節奏速度 (BPM)")
    print(f"{'=' * 50}")
    print("  [1] 60  — 非常慢（抒情、冥想）")
    print("  [2] 75  — 慢（放鬆、Lo-fi）")
    print("  [3] 90  — 中慢（R&B、爵士）")
    print("  [4] 110 — 中等（流行、鄉村）")
    print("  [5] 120 — 中快（流行舞曲）")
    print("  [6] 140 — 快（EDM、運動）")
    print("  [7] 170 — 非常快（Drum & Bass）")
    print("  [8] 自訂 BPM（60-200）")
    print(f"{'=' * 50}")

    while True:
        choice = input("\n  請輸入編號：").strip()
        bpm_map = {"1": 60, "2": 75, "3": 90, "4": 110, "5": 120, "6": 140, "7": 170}

        if choice in bpm_map:
            return bpm_map[choice]
        elif choice == "8":
            try:
                custom = int(input("  請輸入 BPM（60-200）：").strip())
                if 60 <= custom <= 200:
                    return custom
                print("  請輸入 60 到 200 之間的數字。")
            except ValueError:
                print("  請輸入數字。")
        else:
            print("  輸入有誤，請重新選擇。")


def get_duration():
    """取得生成秒數"""
    print(f"\n{'=' * 50}")
    print("  生成長度")
    print(f"{'=' * 50}")
    print("  [1] 10 秒（快速試聽）")
    print("  [2] 20 秒")
    print("  [3] 30 秒（完整片段）")
    print("  [4] 60 秒")
    print(f"{'=' * 50}")

    while True:
        choice = input("\n  請輸入編號：").strip()
        duration_map = {"1": 10, "2": 20, "3": 30, "4": 60}
        if choice in duration_map:
            return duration_map[choice]
        print("  輸入有誤，請重新選擇。")


def collect_settings():
    """依照 MIDST 公式收集所有設定"""

    print("\n")
    print("  *********************************************")
    print("  *                                           *")
    print("  *     Gemini Lyria RealTime 音樂生成器      *")
    print("  *     依照 MIDST 公式，一步步設定你的音樂   *")
    print("  *                                           *")
    print("  *********************************************")

    # M — Mood 情緒
    mood_key = get_choice("M — Mood 情緒：你想要什麼感覺？", MOODS)
    mood_label, mood_prompt = MOODS[mood_key]

    # I — Instrument 樂器
    inst_keys = get_choice("I — Instrument 樂器：用什麼樂器？", INSTRUMENTS, allow_multiple=True)
    inst_labels = [INSTRUMENTS[k][0] for k in inst_keys]
    inst_prompts = [INSTRUMENTS[k][1] for k in inst_keys]

    # V — Vocal 人聲
    vocal_key = get_choice("V — Vocal 人聲：要加入歌聲嗎？", VOCALS)
    vocal_label, vocal_prompt = VOCALS[vocal_key]

    # D — Dynamic 動態（簡化為創意程度）
    print(f"\n{'=' * 50}")
    print("  D — Dynamic 動態：AI 的創意程度")
    print(f"{'=' * 50}")
    print("  [1] 保守（0.5）— 穩定、可預測")
    print("  [2] 適中（1.0）— 平衡（推薦）")
    print("  [3] 大膽（1.5）— 多變化、有驚喜")
    print("  [4] 瘋狂（2.5）— 非常隨機、實驗性")
    print(f"{'=' * 50}")

    while True:
        d_choice = input("\n  請輸入編號：").strip()
        temp_map = {"1": 0.5, "2": 1.0, "3": 1.5, "4": 2.5}
        if d_choice in temp_map:
            temperature = temp_map[d_choice]
            break
        print("  輸入有誤，請重新選擇。")

    # S — Style 風格
    style_key = get_choice("S — Style 風格：什麼音樂類型？", STYLES)
    style_label, style_prompt = STYLES[style_key]

    # T — Tempo 節奏
    bpm = get_bpm()

    # 生成長度
    duration = get_duration()

    # 組合提示詞
    all_prompts = [style_prompt, mood_prompt] + inst_prompts + [vocal_prompt]
    combined_prompt = ", ".join(all_prompts)

    # 顯示總覽確認
    print(f"\n{'=' * 50}")
    print("  你的音樂設定總覽")
    print(f"{'=' * 50}")
    print(f"  M 情緒：{mood_label}")
    print(f"  I 樂器：{', '.join(inst_labels)}")
    print(f"  V 人聲：{vocal_label}")
    print(f"  D 動態：創意程度 {temperature}")
    print(f"  S 風格：{style_label}")
    print(f"  T 節奏：{bpm} BPM")
    print(f"  長  度：{duration} 秒")
    print(f"{'=' * 50}")
    print(f"  組合提示詞：{combined_prompt}")
    print(f"{'=' * 50}")

    confirm = input("\n  確認以上設定，開始生成？(y/n)：").strip().lower()
    if confirm != "y":
        print("  已取消。")
        return None

    return {
        "prompt": combined_prompt,
        "style_prompt": style_prompt,
        "mood_prompt": mood_prompt,
        "inst_prompts": inst_prompts,
        "vocal_prompt": vocal_prompt,
        "bpm": bpm,
        "temperature": temperature,
        "duration": duration,
    }


# ==================== 音樂生成 ====================

async def generate_music(settings):
    """連接 Lyria RealTime 並生成音樂"""

    client_instance = genai.Client(
        api_key=API_KEY,
        http_options={'api_version': 'v1alpha'}
    )

    print("\n  正在連接 Lyria RealTime...")

    async with client_instance.aio.live.music.connect(
        model='models/lyria-realtime-exp'
    ) as session:

        # 設定音樂風格（主風格 + 情緒 + 各樂器 + 人聲）
        prompts = [
            types.WeightedPrompt(text=settings["style_prompt"], weight=1.0),
            types.WeightedPrompt(text=settings["mood_prompt"], weight=0.8),
            types.WeightedPrompt(text=settings["vocal_prompt"], weight=0.9),
        ]
        for inst in settings["inst_prompts"]:
            prompts.append(types.WeightedPrompt(text=inst, weight=0.6))

        await session.set_weighted_prompts(prompts=prompts)
        print(f"  已設定提示詞：{settings['prompt']}")

        # 設定生成參數
        await session.set_music_generation_config(
            config=types.LiveMusicGenerationConfig(
                bpm=settings["bpm"],
                temperature=settings["temperature"],
            )
        )
        print(f"  已設定 BPM={settings['bpm']}, 創意程度={settings['temperature']}")

        # 開始生成
        await session.play()
        print("  開始生成音樂，請稍候...\n")

        audio_data = b''
        duration = settings["duration"]
        sample_rate = 48000
        channels = 2
        bytes_per_sample = 2
        total_bytes = duration * sample_rate * channels * bytes_per_sample

        async for message in session.receive():
            chunk = message.server_content.audio_chunks[0].data
            audio_data += chunk

            progress = min(len(audio_data) / total_bytes * 100, 100)
            print(f"\r  生成進度：{'#' * int(progress // 5):<20} {progress:.0f}%", end="", flush=True)

            if len(audio_data) >= total_bytes:
                break

        await session.stop()
        print("\n\n  生成完成！")

        # 儲存為 WAV 檔案
        output_file = "output_music.wav"
        with wave.open(output_file, 'wb') as wav_file:
            wav_file.setnchannels(channels)
            wav_file.setsampwidth(bytes_per_sample)
            wav_file.setframerate(sample_rate)
            wav_file.writeframes(audio_data[:total_bytes])

        print(f"  音樂已儲存為：{output_file}")
        print(f"  長度：{duration} 秒 / 格式：WAV 48kHz 立體聲")
        print(f"\n  用任何播放器打開 {output_file} 就能聽了！")


# ==================== 主程式 ====================

if __name__ == "__main__":
    settings = collect_settings()
    if settings:
        asyncio.run(generate_music(settings))
