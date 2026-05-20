"""
Gemini Lyria RealTime 音樂生成器
================================
互動式介面，依照 MIDST 公式引導你設定音樂風格，再呼叫 API 生成音樂。

注意事項：
- Lyria RealTime API 僅支援「純器樂」生成，不支援人聲演唱
- 若需要人聲歌曲，請直接使用 Gemini App 的 Lyria 3 對話功能

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
API_KEY = "AIzaSyCghYLNRjHoK4EGHC9oHN-fSeI6Un7WB7E"
# ==================================================


# ==================== 推薦組合（快速模式）====================

PRESETS = {
    "1": {
        "name": "咖啡廳 Lo-fi",
        "desc": "放鬆的低保真音樂，適合讀書、工作",
        "style": "lo-fi chill hop",
        "mood": "relaxed calm peaceful",
        "instruments": ["piano", "acoustic guitar"],
        "bpm": 75,
        "temperature": 1.0,
    },
    "2": {
        "name": "歡樂流行曲",
        "desc": "開朗愉快的流行風格，適合日常背景",
        "style": "pop",
        "mood": "happy cheerful upbeat",
        "instruments": ["piano", "acoustic guitar", "drums percussion"],
        "bpm": 120,
        "temperature": 1.0,
    },
    "3": {
        "name": "史詩電影配樂",
        "desc": "壯闘的管弦樂，適合影片、簡報開場",
        "style": "classical orchestral",
        "mood": "epic cinematic dramatic",
        "instruments": ["strings violin cello", "drums percussion"],
        "bpm": 110,
        "temperature": 1.0,
    },
    "4": {
        "name": "深夜爵士",
        "desc": "慵懶的爵士風情，適合夜晚放鬆",
        "style": "jazz",
        "mood": "relaxed calm peaceful",
        "instruments": ["piano", "saxophone", "bass"],
        "bpm": 90,
        "temperature": 1.0,
    },
    "5": {
        "name": "派對電子舞曲",
        "desc": "高能量 EDM，適合運動、派對",
        "style": "edm electronic dance",
        "mood": "energetic powerful intense",
        "instruments": ["synthesizer synth", "drums percussion", "bass"],
        "bpm": 140,
        "temperature": 1.0,
    },
    "6": {
        "name": "浪漫民謠",
        "desc": "溫暖柔和的民謠吉他，適合旅遊 Vlog",
        "style": "folk acoustic",
        "mood": "romantic warm tender",
        "instruments": ["acoustic guitar", "ukulele"],
        "bpm": 90,
        "temperature": 0.8,
    },
}


# ==================== 自訂模式選單 ====================

STYLES = {
    "1": ("Pop 流行樂",           "pop",                    "BPM 110-130 / 歡樂、浪漫"),
    "2": ("Rock 搖滾",            "rock",                   "BPM 110-140 / 激昂、懷舊"),
    "3": ("Jazz 爵士",            "jazz",                   "BPM 80-110 / 放鬆、浪漫"),
    "4": ("EDM 電子舞曲",         "edm electronic dance",   "BPM 120-150 / 激昂、歡樂"),
    "5": ("Classical 古典",       "classical orchestral",   "BPM 60-120 / 史詩、神秘"),
    "6": ("Lo-fi 低保真",         "lo-fi chill hop",        "BPM 70-90 / 放鬆、懷舊"),
    "7": ("Hip Hop 嘻哈",         "hip hop rap beat",       "BPM 80-110 / 激昂、歡樂"),
    "8": ("R&B 節奏藍調",         "r&b soul",               "BPM 70-100 / 浪漫、憂傷"),
    "9": ("Folk 民謠",            "folk acoustic",          "BPM 80-110 / 放鬆、浪漫"),
    "10": ("Ambient 環境音樂",    "ambient atmospheric",    "BPM 60-80 / 放鬆、神秘"),
}

MOODS = {
    "1": ("Happy 歡樂",       "happy cheerful upbeat"),
    "2": ("Sad 憂傷",         "sad melancholic emotional"),
    "3": ("Relaxed 放鬆",     "relaxed calm peaceful"),
    "4": ("Energetic 激昂",   "energetic powerful intense"),
    "5": ("Romantic 浪漫",    "romantic warm tender"),
    "6": ("Epic 史詩",        "epic cinematic dramatic"),
    "7": ("Mysterious 神秘",  "mysterious dark suspenseful"),
    "8": ("Nostalgic 懷舊",   "nostalgic bittersweet retro"),
}

INSTRUMENTS = {
    "1": ("Piano 鋼琴",              "piano"),
    "2": ("Acoustic Guitar 木吉他",  "acoustic guitar"),
    "3": ("Electric Guitar 電吉他",  "electric guitar"),
    "4": ("Strings 弦樂",            "strings violin cello"),
    "5": ("Saxophone 薩克斯風",      "saxophone"),
    "6": ("Synthesizer 合成器",      "synthesizer synth"),
    "7": ("Drums 鼓組",              "drums percussion"),
    "8": ("Bass 貝斯",               "bass"),
    "9": ("Flute 長笛",              "flute"),
    "10": ("Ukulele 烏克麗麗",       "ukulele"),
}


# ==================== 互動介面 ====================

def show_menu(title, options, show_hint=False):
    """顯示選單並讓使用者選擇"""
    print(f"\n{'=' * 58}")
    print(f"  {title}")
    print(f"{'=' * 58}")
    for key, val in options.items():
        if show_hint and len(val) == 3:
            label, _, hint = val
            print(f"  [{key:>2}] {label:<28} ({hint})")
        else:
            label = val[0]
            print(f"  [{key:>2}] {label}")
    print(f"{'=' * 58}")


def get_choice(title, options, allow_multiple=False, max_select=None, show_hint=False):
    """取得使用者的選擇"""
    show_menu(title, options, show_hint=show_hint)

    if allow_multiple:
        hint = "可多選，用逗號分隔，例如：1,3,5"
        if max_select:
            hint += f"（最多 {max_select} 個）"
        print(f"  ({hint})")

    while True:
        choice = input("\n  請輸入編號：").strip()

        if allow_multiple:
            keys = [k.strip() for k in choice.split(",")]
            if not all(k in options for k in keys):
                print("  輸入有誤，請重新選擇。")
                continue
            if max_select and len(keys) > max_select:
                print(f"  最多只能選 {max_select} 個，請重新選擇。")
                continue
            return keys
        else:
            if choice in options:
                return choice
            print("  輸入有誤，請重新選擇。")


def get_bpm():
    """取得 BPM 設定"""
    print(f"\n{'=' * 58}")
    print("  T — Tempo 節奏速度 (BPM)")
    print(f"{'=' * 58}")
    print("  [1] 60  — 非常慢（抒情、冥想）")
    print("  [2] 75  — 慢（放鬆、Lo-fi）")
    print("  [3] 90  — 中慢（R&B、爵士）")
    print("  [4] 110 — 中等（流行、鄉村）")
    print("  [5] 120 — 中快（流行舞曲）")
    print("  [6] 140 — 快（EDM、運動）")
    print("  [7] 170 — 非常快（Drum & Bass）")
    print("  [8] 自訂 BPM（60-200）")
    print(f"{'=' * 58}")

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
    print(f"\n{'=' * 58}")
    print("  生成長度")
    print(f"{'=' * 58}")
    print("  [1] 10 秒（快速試聽）")
    print("  [2] 20 秒")
    print("  [3] 30 秒（完整片段）")
    print("  [4] 60 秒")
    print(f"{'=' * 58}")

    while True:
        choice = input("\n  請輸入編號：").strip()
        duration_map = {"1": 10, "2": 20, "3": 30, "4": 60}
        if choice in duration_map:
            return duration_map[choice]
        print("  輸入有誤，請重新選擇。")


# ==================== 快速模式 ====================

def quick_mode():
    """使用推薦組合快速生成"""
    print(f"\n{'=' * 58}")
    print("  推薦組合（選一個直接生成，適合新手）")
    print(f"{'=' * 58}")
    for key, preset in PRESETS.items():
        print(f"  [{key}] {preset['name']:<16} — {preset['desc']}")
    print(f"{'=' * 58}")

    while True:
        choice = input("\n  請輸入編號：").strip()
        if choice in PRESETS:
            break
        print("  輸入有誤，請重新選擇。")

    p = PRESETS[choice]
    duration = get_duration()

    combined_prompt = ", ".join([p["style"], p["mood"]] + p["instruments"])

    print(f"\n{'=' * 58}")
    print(f"  已選擇：{p['name']}")
    print(f"{'=' * 58}")
    print(f"  風格：{p['style']}")
    print(f"  情緒：{p['mood']}")
    print(f"  樂器：{', '.join(p['instruments'])}")
    print(f"  BPM：{p['bpm']} / 創意程度：{p['temperature']}")
    print(f"  長度：{duration} 秒")
    print(f"{'=' * 58}")

    confirm = input("\n  確認開始生成？(y/n)：").strip().lower()
    if confirm != "y":
        print("  已取消。")
        return None

    return {
        "prompt": combined_prompt,
        "style_prompt": p["style"],
        "mood_prompt": p["mood"],
        "inst_prompts": p["instruments"],
        "bpm": p["bpm"],
        "temperature": p["temperature"],
        "duration": duration,
    }


# ==================== 自訂模式 ====================

def custom_mode():
    """依照 MIDST 公式自訂設定"""

    # M — Mood 情緒
    mood_key = get_choice("M — Mood 情緒：你想要什麼感覺？", MOODS)
    mood_label, mood_prompt = MOODS[mood_key]

    # I — Instrument 樂器（最多 3 個）
    inst_keys = get_choice(
        "I — Instrument 樂器：用什麼樂器？",
        INSTRUMENTS, allow_multiple=True, max_select=3
    )
    inst_labels = [INSTRUMENTS[k][0] for k in inst_keys]
    inst_prompts = [INSTRUMENTS[k][1] for k in inst_keys]

    # D — Dynamic 動態
    print(f"\n{'=' * 58}")
    print("  D — Dynamic 動態：AI 的創意程度")
    print(f"{'=' * 58}")
    print("  [1] 保守（0.5）— 穩定、可預測的旋律")
    print("  [2] 適中（1.0）— 平衡創意與穩定（推薦）")
    print("  [3] 大膽（1.5）— 更多變化與驚喜")
    print("  [4] 極端（2.0）— 高度隨機，實驗性質")
    print(f"  {'─' * 52}")
    print("  提示：數值越高，生成結果越不可預測。")
    print("        新手建議選 [2] 適中，進階玩家可嘗試 [3]。")
    print(f"{'=' * 58}")

    while True:
        d_choice = input("\n  請輸入編號：").strip()
        temp_map = {"1": 0.5, "2": 1.0, "3": 1.5, "4": 2.0}
        if d_choice in temp_map:
            temperature = temp_map[d_choice]
            break
        print("  輸入有誤，請重新選擇。")

    # S — Style 風格（附帶搭配建議）
    style_key = get_choice(
        "S — Style 風格：什麼音樂類型？",
        STYLES, show_hint=True
    )
    style_label = STYLES[style_key][0]
    style_prompt = STYLES[style_key][1]

    # T — Tempo 節奏
    bpm = get_bpm()

    # 生成長度
    duration = get_duration()

    # 組合提示詞
    all_prompts = [style_prompt, mood_prompt] + inst_prompts
    combined_prompt = ", ".join(all_prompts)

    # 顯示總覽確認
    print(f"\n{'=' * 58}")
    print("  你的音樂設定總覽")
    print(f"{'=' * 58}")
    print(f"  M 情緒：{mood_label}")
    print(f"  I 樂器：{', '.join(inst_labels)}")
    print(f"  D 動態：創意程度 {temperature}")
    print(f"  S 風格：{style_label}")
    print(f"  T 節奏：{bpm} BPM")
    print(f"  長  度：{duration} 秒")
    print(f"{'=' * 58}")
    print(f"  組合提示詞：{combined_prompt}")
    print(f"{'=' * 58}")

    confirm = input("\n  確認以上設定，開始生成？(y/n)：").strip().lower()
    if confirm != "y":
        print("  已取消。")
        return None

    return {
        "prompt": combined_prompt,
        "style_prompt": style_prompt,
        "mood_prompt": mood_prompt,
        "inst_prompts": inst_prompts,
        "bpm": bpm,
        "temperature": temperature,
        "duration": duration,
    }


# ==================== 主選單 ====================

def collect_settings():
    """主選單：選擇快速模式或自訂模式"""

    print("\n")
    print("  *********************************************")
    print("  *                                           *")
    print("  *     Gemini Lyria RealTime 音樂生成器      *")
    print("  *     依照 MIDST 公式，一步步設定你的音樂   *")
    print("  *                                           *")
    print("  *     作者：曾慶良（阿亮老師）              *")
    print("  *     © 2026 僅供課程學員學習使用           *")
    print("  *                                           *")
    print("  *********************************************")
    print()
    print("  注意：RealTime API 僅支援純器樂生成。")
    print("  輸入 [3] 查看人聲功能說明，[4] 查看作者與版權資訊。")

    print(f"\n{'=' * 58}")
    print("  請選擇模式")
    print(f"{'=' * 58}")
    print("  [1] 推薦組合（快速模式，適合新手）")
    print("  [2] 自訂設定（MIDST 公式，進階玩家）")
    print("  [3] 人聲功能說明")
    print("  [4] 關於作者 / 版權聲明")
    print(f"{'=' * 58}")

    while True:
        mode = input("\n  請輸入編號：").strip()
        if mode == "1":
            return quick_mode()
        elif mode == "2":
            return custom_mode()
        elif mode == "3":
            show_vocal_info()
            continue
        elif mode == "4":
            show_about()
            continue
        print("  輸入有誤，請重新選擇。")


def show_vocal_info():
    """顯示人聲功能對照說明"""
    print(f"\n{'=' * 58}")
    print("  人聲（Vocal）功能說明")
    print(f"{'=' * 58}")
    print()
    print("  Lyria 3 確實支援人聲演唱與歌詞生成，但該功能")
    print("  目前僅開放在 Gemini App 的對話介面中使用，")
    print("  尚未開放給 RealTime API。")
    print()
    print(f"  {'─' * 52}")
    print(f"  {'功能':<16} {'Gemini App':<16} {'RealTime API'}")
    print(f"  {'─' * 52}")
    print(f"  {'純器樂生成':<16} {'✓':<16} {'✓'}")
    print(f"  {'人聲演唱':<16} {'✓':<16} {'✗（尚未開放）'}")
    print(f"  {'歌詞生成':<16} {'✓':<16} {'✗（尚未開放）'}")
    print(f"  {'即時互動控制':<16} {'✗':<16} {'✓'}")
    print(f"  {'自訂 BPM':<16} {'✗':<16} {'✓'}")
    print(f"  {'自訂 Temperature':<16} {'✗':<16} {'✓'}")
    print(f"  {'程式化批次生成':<16} {'✗':<16} {'✓'}")
    print(f"  {'─' * 52}")
    print()
    print("  如何在 Gemini App 生成人聲音樂？")
    print("  1. 前往 https://gemini.google.com")
    print("  2. 直接用文字描述，例如：")
    print('     「幫我做一首歡快的流行歌，女聲演唱，120 BPM」')
    print("  3. Gemini 會自動生成含人聲與歌詞的 30 秒音樂")
    print()
    print("  本程式的 RealTime API 優勢在於：")
    print("  可即時調整風格、BPM、創意程度等參數，")
    print("  適合快速實驗不同器樂編曲組合。")
    print()
    print("  期待 Google 未來將人聲功能開放給 API，届時")
    print("  本程式將會更新支援！")
    print(f"\n{'=' * 58}")
    input("  按 Enter 返回主選單...")


def show_about():
    """顯示作者資訊與版權聲明"""
    print(f"\n{'=' * 58}")
    print("  關於作者")
    print(f"{'=' * 58}")
    print()
    print("  曾慶良（阿亮老師）")
    print("  新興科技推廣中心主任")
    print("  教育部學科中心研究教師")
    print()
    print(f"  {'─' * 52}")
    print("  經歷與榮譽：")
    print("  ・獲教育部人工智慧講師認證")
    print("  ・指導學生 XR 專案競賽獲特優")
    print("  ・獲 VR 教材開發教師組特優")
    print("  ・獲百大資訊人才獎")
    print("  ・親子天下創新 100 教師")
    print("  ・臺北市特殊優良教師")
    print()
    print(f"  {'─' * 52}")
    print("  聯絡與社群：")
    print("  Email : 3a01chatgpt@gmail.com")
    print("  FB    : https://www.facebook.com/?locale=zh_TW")
    print("  YT    : https://www.youtube.com/@Liang-yt02")
    print("  3A社團: https://www.facebook.com/groups/2754139931432955")
    print()
    print(f"  {'─' * 52}")
    print("  課程簡報：")
    print("  https://chatgpt3a01.github.io/Gemini-Music-Generation-Tutorial/")
    print("  %E7%B0%A1%E5%A0%B1/index.html")
    print()
    print(f"  {'─' * 52}")
    print("  版權聲明：")
    print("  © 2026 曾慶良（阿亮老師）版權所有")
    print("  本程式僅供「阿亮老師課程學員」學習使用。")
    print("  禁止修改、轉傳、散布或商業使用。")
    print("  如有授權需求，請聯繫作者。")
    print(f"\n{'=' * 58}")
    input("  按 Enter 返回主選單...")


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

        # 設定音樂風格（主風格 + 情緒 + 各樂器）
        prompts = [
            types.WeightedPrompt(text=settings["style_prompt"], weight=1.0),
            types.WeightedPrompt(text=settings["mood_prompt"], weight=0.8),
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
