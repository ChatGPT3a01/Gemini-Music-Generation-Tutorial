# Gemini 音樂生成術：從零開始的 AI 作曲完整教學

> **適用對象：完全不懂樂理也能上手的所有人**

---

## 目錄

1. [前言：AI 也能作曲了？](#一前言ai-也能作曲了)
2. [事前準備](#二事前準備)
3. [方法一：文字生成音樂](#三方法一文字生成音樂)
4. [方法二：圖片生成音樂](#四方法二圖片生成音樂)
5. [方法三：Gem 機器人 — 打造你的專屬作曲助手](#五方法三gem-機器人打造你的專屬作曲助手)
6. [方法四：API 開發者進階玩法（Lyria RealTime）](#六方法四api-開發者進階玩法lyria-realtime)
7. [提示詞（Prompt）攻略大全](#七提示詞prompt攻略大全)
8. [SynthID 浮水印：AI 音樂的身分證](#八synthid-浮水印ai-音樂的身分證)
9. [實戰範例：五種情境示範](#九實戰範例五種情境示範)
10. [常見問題 FAQ](#十常見問題-faq)
11. [延伸資源](#十一延伸資源)

---

## 一、前言：AI 也能作曲了？

2026 年 2 月，Google 在 Gemini App 中正式推出了 **Lyria 3** 音樂生成模型，這是 Google DeepMind 打造的最新一代 AI 音樂引擎。從此，只要一句話、一張圖片，甚至一段影片，Gemini 就能在幾秒鐘內為你創作一段 **30 秒的完整音樂**——包含旋律、編曲、人聲與歌詞。

**Lyria 3 的三大亮點：**

- **文字轉音樂**：用自然語言描述你想要的音樂，AI 即時創作
- **圖片/影片轉音樂**：上傳一張照片或影片，AI 自動感知情緒並配樂
- **高保真人聲**：不只是純器樂，還能生成帶有歌詞的人聲演唱

> **重點：你完全不需要懂樂理、不需要會任何樂器，只需要會「說話」就能作曲！**

---

## 二、事前準備

### 2.1 你需要什麼？

| 項目 | 說明 |
|------|------|
| Google 帳號 | 必須年滿 **18 歲** |
| 瀏覽器 | Chrome、Edge、Firefox 等現代瀏覽器 |
| Gemini App | 網頁版：[gemini.google.com](https://gemini.google.com) |

### 2.2 訂閱方案比較

| 方案 | 月費 | 音樂生成 | 建議對象 |
|------|------|----------|----------|
| **免費版** | $0 | 可使用，次數較少 | 想先體驗看看的人 |
| **Google AI Plus** | $7.99/月 | 較多生成次數 | 輕度使用者 |
| **Google AI Pro** | $19.99/月 | 更多次數 + 1,000 AI 點數 | 經常使用的創作者 |
| **Google AI Ultra** | $249.99/月 | 最高次數 + 25,000 AI 點數 | 專業工作者 |

> **好消息：免費版也能使用音樂生成功能！** 只是在尖峰時段可能會被限制次數。

### 2.3 開啟 Gemini App

📸 **【截圖 01】** 打開瀏覽器，進入 [gemini.google.com](https://gemini.google.com)，截取 Gemini 首頁畫面（確認已登入 Google 帳號）。

---

## 三、方法一：文字生成音樂

這是最直覺的方式——用文字告訴 Gemini 你想要什麼音樂，它就幫你作曲。

### 3.1 操作步驟

**Step 1：進入 Gemini 對話介面**

在 Gemini App 的聊天框中，直接輸入你的音樂需求。

📸 **【截圖 02】** Gemini 對話介面，滑鼠指向輸入框的畫面。

**Step 2：輸入音樂提示詞**

在輸入框中，用自然語言描述你想要的音樂。例如：

> **✏️ 提示詞 ▼ 複製貼上到 Gemini**
> ```
> 幫我創作一首輕快的流行歌曲，主題是夏天去海邊玩的快樂心情，
> 帶有吉他和鍵盤，節奏活潑，女聲演唱。
> ```

> **提示：** 雖然 Gemini 音樂生成目前官方支援 8 種語言（英文、日文、韓文、德文、西班牙文、法文、印地文、葡萄牙文），但你可以先用中文描述需求，Gemini 會理解你的意思並生成音樂。如果生成效果不理想，建議改用英文提示。

📸 **【截圖 03】** 在輸入框中輸入音樂提示詞的畫面。

**Step 3：等待 AI 生成**

按下送出後，Gemini 會開始生成音樂，通常需要等待 **10～30 秒**。

📸 **【截圖 04】** Gemini 正在生成音樂的等待畫面（如果有載入動畫的話）。

**Step 4：試聽與下載**

生成完成後，你會看到：
- 一段 **30 秒的音樂播放器**
- 由 AI 自動生成的**封面藝術**（Nano Banana 技術）
- **播放按鈕**：點擊試聽
- **下載按鈕**：儲存到本機
- **分享連結**：可以分享給朋友

📸 **【截圖 05】** 音樂生成完成後的播放介面，標示出播放、下載、分享等按鈕。

**Step 5：不滿意？繼續調整！**

如果對結果不滿意，你可以直接在對話中追加修改需求：

> **✏️ 提示詞 ▼ 複製貼上到 Gemini**
> ```
> 節奏再快一點，加入一段薩克斯風獨奏
> ```

Gemini 會根據你的反饋重新生成音樂。

📸 **【截圖 06】** 在對話中追加修改需求並重新生成的畫面。

### 3.2 文字提示詞範例

**範例 A — 輕鬆背景音樂**

> **✏️ 提示詞 ▼ 複製貼上到 Gemini**
> ```
> Create a chill lo-fi hip hop track with soft piano and vinyl crackle, perfect for studying
> ```

**範例 B — 激昂運動音樂**

> **✏️ 提示詞 ▼ 複製貼上到 Gemini**
> ```
> Make an energetic EDM track with heavy bass drops and a fast tempo around 140 BPM for workout
> ```

**範例 C — 抒情情歌**

> **✏️ 提示詞 ▼ 複製貼上到 Gemini**
> ```
> Compose a slow romantic ballad with acoustic guitar, soft male vocals singing about missing someone
> ```

**範例 D — 兒童歡樂曲**

> **✏️ 提示詞 ▼ 複製貼上到 Gemini**
> ```
> A playful and fun children's song with ukulele and hand claps, about animals in the zoo
> ```

**範例 E — 電影配樂風**

> **✏️ 提示詞 ▼ 複製貼上到 Gemini**
> ```
> An epic cinematic orchestral piece with strings and brass, building tension then resolving triumphantly
> ```

---

## 四、方法二：圖片生成音樂

Lyria 3 最令人驚豔的功能之一，就是能「看圖作曲」。

### 4.1 運作原理

Gemini 會分析你上傳的圖片或影片，解讀其中的：
- **視覺元素**（風景、人物、物品）
- **色彩氛圍**（暖色調、冷色調、高對比）
- **情緒感受**（歡樂、憂傷、壯麗、平靜）

然後自動生成一段與該圖片情緒相符的 30 秒音樂。

### 4.2 操作步驟

**Step 1：準備一張圖片**

選擇你想要配樂的圖片。可以是：
- 風景照片
- 旅遊照
- 寵物照片
- 藝術作品
- 任何有情緒感的圖片

**Step 2：上傳圖片到 Gemini**

在 Gemini 對話介面中，點擊「附件」或「上傳」按鈕，選擇你的圖片。

📸 **【截圖 07】** 點擊上傳按鈕的位置示意。

**Step 3：加上音樂指令**

上傳圖片後，在輸入框中加上音樂相關的提示：

> **✏️ 提示詞 ▼ 複製貼上到 Gemini（中文版）**
> ```
> 根據這張圖片的氛圍，幫我創作一首配樂
> ```

或者更具體：

> **✏️ 提示詞 ▼ 複製貼上到 Gemini（英文版，效果更佳）**
> ```
> Look at this photo and create a music track that captures its mood and atmosphere
> ```

📸 **【截圖 08】** 上傳圖片後加上文字指令的畫面。

**Step 4：試聽結果**

Gemini 會分析圖片並生成配樂。

📸 **【截圖 09】** 圖片音樂生成完成的結果畫面。

### 4.3 圖片配樂情境範例

| 圖片類型 | AI 可能生成的音樂風格 |
|----------|---------------------|
| 海邊夕陽 | 悠緩的環境音樂、帶有海浪質感的氛圍音 |
| 生日派對 | 歡樂活潑的流行舞曲 |
| 森林小徑 | 輕柔的民謠吉他搭配自然音效 |
| 城市夜景 | 電子爵士、Lo-fi 節拍 |
| 雪山壯景 | 氣勢磅礡的管弦樂 |
| 可愛寵物 | 俏皮輕快的小品音樂 |

### 4.4 進階技巧：圖片 + 文字混合提示

你可以同時上傳圖片並加上文字指令來精確控制輸出：

> **✏️ 提示詞 ▼ 上傳圖片後，複製貼上到 Gemini**
> ```
> 根據這張秋天楓葉的照片，創作一首帶有鋼琴和大提琴的
> 輕柔古典風配樂，速度慢一些，情緒偏向溫暖懷舊
> ```

這樣 AI 會同時參考圖片的視覺情緒和你的文字描述。

---

## 五、方法三：Gem 機器人——打造你的專屬作曲助手

**Gems** 是 Gemini 的自訂 AI 機器人功能，你可以建立一個專門用來輔助音樂創作的 Gem。

> **注意：** 目前 Gem 機器人本身不能直接呼叫音樂生成工具，但可以作為**「提示詞產生器」**和**「音樂靈感顧問」**，幫你構思出更好的音樂提示詞，然後再拿去 Gemini 主介面生成音樂。

### 5.1 為什麼要建立音樂 Gem？

- **統一風格**：讓 Gem 記住你偏好的音樂風格，每次都產出一致的提示詞
- **降低門檻**：不知道怎麼描述音樂？Gem 會引導你
- **批量創作**：快速為多個場景產出不同的音樂提示詞
- **學習樂理**：Gem 可以教你基礎樂理知識，讓你的提示更精準

### 5.2 建立「音樂提示詞大師」Gem

**Step 1：進入 Gems 管理頁面**

在 Gemini 左側面板中，找到「Gems」或「我的 Gem」。

📸 **【截圖 10】** Gemini 左側面板中 Gems 入口的位置。

**Step 2：點擊「建立新 Gem」**

📸 **【截圖 11】** 點擊建立新 Gem 的按鈕。

**Step 3：設定 Gem 的指令**

在指令欄位中，輸入以下內容（可以根據你的需求修改）：

> **⚙️ Gem 設定指令 ▼ 複製貼上到 Gem 的「指令」欄位（這不是音樂提示詞！）**
> ```
> 你是一位專業的 AI 音樂提示詞大師。你的工作是幫助使用者創作出
> 高品質的音樂生成提示詞，讓 Gemini 的 Lyria 3 模型能生成最好的音樂。
>
> 你的工作流程：
> 1. 先詢問使用者想要什麼類型的音樂（用途、情境、心情）
> 2. 根據回答，用 MIDST 公式組織提示詞：
>    - M（Mood 情緒）：歡樂、憂傷、激昂、平靜...
>    - I（Instrument 樂器）：鋼琴、吉他、鼓組、弦樂...
>    - D（Dynamic 動態）：漸強、漸弱、爆發...
>    - S（Style 風格）：流行、爵士、古典、電子...
>    - T（Tempo 節奏）：BPM、快慢描述
> 3. 產出「英文版」和「中文版」兩種提示詞
> 4. 解釋為什麼這樣寫，讓使用者學到東西
>
> 注意事項：
> - 提示詞要具體、有畫面感
> - 可以建議加入人聲或純器樂
> - 如果使用者提供圖片，也要能根據圖片構思配樂提示
> - 每次產出 2-3 個不同版本供選擇
> ```

📸 **【截圖 12】** 在 Gem 指令欄位中輸入設定的畫面。

**Step 4：命名並儲存**

- 名稱：`音樂提示詞大師` 或 `Music Prompt Master`
- 儲存後即可使用

📸 **【截圖 13】** 命名並儲存 Gem 的畫面。

### 5.3 使用音樂 Gem 的工作流程

```
┌─────────────────────┐
│  1. 打開音樂 Gem     │
│  告訴它你的需求      │
└──────────┬──────────┘
           ▼
┌─────────────────────┐
│  2. Gem 產出提示詞    │
│  給你 2-3 個版本     │
└──────────┬──────────┘
           ▼
┌─────────────────────┐
│  3. 複製你喜歡的     │
│  提示詞              │
└──────────┬──────────┘
           ▼
┌─────────────────────┐
│  4. 回到 Gemini 主   │
│  介面，貼上提示詞    │
│  生成音樂            │
└──────────┬──────────┘
           ▼
┌─────────────────────┐
│  5. 不滿意？回 Gem   │
│  請它調整提示詞      │
└─────────────────────┘
```

### 5.4 Gem 對話範例

> **你：** 我想要一首適合在咖啡廳播放的背景音樂

> **音樂 Gem：** 好的！讓我幫你構思。先確認幾個方向：
> 1. 偏好什麼風格？（爵士、Bossa Nova、Lo-fi...）
> 2. 需要人聲嗎？
> 3. 早晨/午後/晚間的氛圍？
>
> 以下先給你三個版本：

**Gem 產出的版本 A（爵士風）：**

> **✏️ 提示詞 ▼ 從 Gem 複製，貼到 Gemini 主介面生成音樂**
> ```
> Smooth jazz cafe music with brushed drums, upright bass, and mellow saxophone.
> Relaxed and warm, perfect for a cozy afternoon coffee shop. Tempo around 80 BPM.
> ```

**Gem 產出的版本 B（Lo-fi 風）：**

> **✏️ 提示詞 ▼ 從 Gem 複製，貼到 Gemini 主介面生成音樂**
> ```
> Lo-fi chill hop with soft piano chords, vinyl crackle, and gentle drum beats.
> Dreamy and mellow atmosphere, like studying in a rainy day cafe. 70 BPM.
> ```

**Gem 產出的版本 C（Bossa Nova 風）：**

> **✏️ 提示詞 ▼ 從 Gem 複製，貼到 Gemini 主介面生成音樂**
> ```
> Bossa nova instrumental with nylon guitar, soft percussion, and light flute melody.
> Brazilian cafe vibes, warm and breezy. 110 BPM.
> ```

📸 **【截圖 14】** 與音樂 Gem 對話的畫面，展示 Gem 產出的提示詞建議。

---

## 六、方法四：API 開發者進階玩法（Lyria RealTime）

如果你是開發者或有程式基礎，Google 提供了 **Lyria RealTime API**，可以做到即時互動式的音樂生成。

> **適用對象：** 有 Python 程式基礎的開發者
> **用途：** 遊戲配樂、互動裝置、即時 DJ 應用

### 6.1 Lyria RealTime 是什麼？

| 項目 | 說明 |
|------|------|
| 模型名稱 | `models/lyria-realtime-exp`（實驗版） |
| 連線方式 | WebSocket 雙向低延遲串流 |
| 輸出格式 | 原始 16-bit PCM，48kHz，立體聲 |
| 延遲 | 控制變更到效果最多 2 秒 |
| 音樂類型 | 以純器樂為主（可選人聲哼唱模式） |

### 6.2 取得 API 金鑰

**Step 1：** 前往 [Google AI Studio](https://aistudio.google.com/)

**Step 2：** 登入 Google 帳號後，點擊「Get API Key」取得金鑰

📸 **【截圖 15】** Google AI Studio 取得 API Key 的頁面。

### 6.3 環境設定

在寫程式之前，我們需要先安裝 Google 提供的 **GenAI Python SDK**（軟體開發套件）。這個套件就像一座橋樑，讓你的 Python 程式可以跟 Google 的 Lyria RealTime 音樂模型溝通。

> 你可以把它想像成：你的電腦本來不會講「Lyria 的語言」，安裝這個套件之後，它就聽得懂了。

**操作方式：** 打開終端機（命令提示字元 / Terminal），輸入以下指令：

```bash
pip install google-genai
```

看到類似以下的訊息就代表安裝成功：

```
Successfully installed google-genai-x.x.x
```

📸 **【截圖 21】** 終端機中執行 `pip install google-genai` 安裝成功的畫面。

> **常見問題：**
> - 如果出現 `pip 不是內部或外部命令`，代表你的電腦還沒安裝 Python，請先到 [python.org](https://www.python.org/downloads/) 下載安裝。
> - 如果出現權限錯誤，可以改用 `pip install --user google-genai`。

### 6.4 實作：一起建立互動式音樂生成程式

接下來我們要從零開始建立一個 Python 程式。這個程式執行後會出現互動選單，讓你依照 **MIDST 公式**一步步選擇情緒、樂器、風格、節奏，最後按下確認才會生成音樂。

程式碼比較長，我們分成 **6 個部分**逐步建立。

**Step 1：建立新檔案**

打開你的程式編輯器（VS Code、記事本都可以），新建一個檔案，命名為：

```
generate_music.py
```

**Step 2：匯入套件 + 設定 API 金鑰**

在檔案最上方，貼上以下程式碼。把 `YOUR_API_KEY` 換成你在 6.2 取得的金鑰：

```python
import asyncio          # 處理非同步（async）操作
import wave             # 將音訊資料儲存為 .wav 檔案
from google import genai           # Google GenAI 主套件
from google.genai import types     # 資料型別定義

# ==================================================
# >>> 把 YOUR_API_KEY 替換成你自己的金鑰 <<<
# >>> 例如："AIzaSyB1234567890abcdefg"    <<<
# ==================================================
API_KEY = "YOUR_API_KEY"
```

**Step 3：建立選單資料**

接著貼上選單的資料。這些就是等一下互動介面中會出現的選項：

```python
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
```

> 每個選項的格式是 `"編號": ("顯示名稱", "給 AI 的英文提示詞")`。你可以自由增減選項。
> 人聲選項中，選 `0` 就是純器樂、不帶歌聲。

**Step 4：建立互動介面函式**

這段程式負責顯示選單、接收使用者輸入：

```python
# ==================== 互動介面 ====================

def show_menu(title, options):
    """顯示選單"""
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
        bpm_map = {"1": 60, "2": 75, "3": 90, "4": 110,
                   "5": 120, "6": 140, "7": 170}
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
```

**Step 5：建立 MIDST 設定收集流程**

這段把所有選單串起來，依照 **M → I → V → D → S → T** 的順序引導使用者，最後顯示總覽讓使用者確認：

```python
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

    # I — Instrument 樂器（可多選）
    inst_keys = get_choice(
        "I — Instrument 樂器：用什麼樂器？", INSTRUMENTS, allow_multiple=True
    )
    inst_labels = [INSTRUMENTS[k][0] for k in inst_keys]
    inst_prompts = [INSTRUMENTS[k][1] for k in inst_keys]

    # V — Vocal 人聲
    vocal_key = get_choice("V — Vocal 人聲：要加入歌聲嗎？", VOCALS)
    vocal_label, vocal_prompt = VOCALS[vocal_key]

    # D — Dynamic 動態（創意程度）
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
    all_prompts = [style_prompt, mood_prompt] + inst_prompts
    combined_prompt = ", ".join(all_prompts)

    # --------- 顯示總覽，讓使用者確認 ---------
    print(f"\n{'=' * 50}")
    print("  你的音樂設定總覽")
    print(f"{'=' * 50}")
    print(f"  M 情緒：{mood_label}")
    print(f"  I 樂器：{', '.join(inst_labels)}")
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
        "bpm": bpm,
        "temperature": temperature,
        "duration": duration,
    }
```

**Step 6：建立音樂生成函式 + 主程式**

最後一段，負責呼叫 API 生成音樂並儲存檔案：

```python
# ==================== 音樂生成 ====================

async def generate_music(settings):
    """連接 Lyria RealTime 並生成音樂"""

    client = genai.Client(
        api_key=API_KEY,
        http_options={'api_version': 'v1alpha'}
    )

    print("\n  正在連接 Lyria RealTime...")

    async with client.aio.live.music.connect(
        model='models/lyria-realtime-exp'
    ) as session:

        # 設定音樂風格（主風格 + 情緒 + 各樂器，分別給不同權重）
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
            print(f"\r  生成進度：{'#' * int(progress // 5):<20} {progress:.0f}%",
                  end="", flush=True)
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


# ==================== 主程式 ====================

if __name__ == "__main__":
    settings = collect_settings()
    if settings:
        asyncio.run(generate_music(settings))
```

**Step 7：儲存檔案**

確認檔案已儲存為 `generate_music.py`。

**Step 8：執行程式**

打開終端機（命令提示字元 / Terminal），切換到檔案所在的資料夾，輸入：

```bash
python generate_music.py
```

程式會依序顯示互動選單，引導你完成 MIDST 五個步驟的設定：

```
  *********************************************
  *                                           *
  *     Gemini Lyria RealTime 音樂生成器      *
  *     依照 MIDST 公式，一步步設定你的音樂   *
  *                                           *
  *********************************************

==================================================
  M — Mood 情緒：你想要什麼感覺？
==================================================
  [ 1] Happy 歡樂
  [ 2] Sad 憂傷
  [ 3] Relaxed 放鬆
  ...

  請輸入編號：3

==================================================
  I — Instrument 樂器：用什麼樂器？
==================================================
  [ 1] Piano 鋼琴
  [ 2] Acoustic Guitar 木吉他
  ...
  (可多選，用逗號分隔，例如：1,3,5)

  請輸入編號：1,5

  ...（依序完成 D、S、T 的設定）...

==================================================
  你的音樂設定總覽
==================================================
  M 情緒：Relaxed 放鬆
  I 樂器：Piano 鋼琴, Saxophone 薩克斯風
  D 動態：創意程度 1.0
  S 風格：Jazz 爵士
  T 節奏：90 BPM
  長  度：30 秒
==================================================
  組合提示詞：jazz, relaxed calm peaceful, piano, saxophone
==================================================

  確認以上設定，開始生成？(y/n)：y

  正在連接 Lyria RealTime...
  已設定提示詞：jazz, relaxed calm peaceful, piano, saxophone
  已設定 BPM=90, 創意程度=1.0
  開始生成音樂，請稍候...

  生成進度：#################### 100%

  生成完成！
  音樂已儲存為：output_music.wav
  長度：30 秒 / 格式：WAV 48kHz 立體聲
```

同一個資料夾中會出現 `output_music.wav`，用任何播放器打開就能聽到你的 AI 音樂了！

📸 **【截圖 19】** 程式執行後的 MIDST 互動選單畫面。

📸 **【截圖 20】** 設定總覽確認畫面，按下 y 開始生成。

📸 **【截圖 21a】** 音樂生成過程。
📸 **【截圖 21b】** 音樂生成過程。
📸 **【截圖 21a】** 音樂生成完成，資料夾中出現 `output_music.wav` 檔案。


### 6.5 可調整的參數一覽

| 參數 | 範圍 | 說明 |
|------|------|------|
| `bpm` | 60 - 200 | 每分鐘節拍數 |
| `temperature` | 0.0 - 3.0 | 創意多樣性（越高越隨機） |
| `guidance` | 0.0 - 6.0 | 提示遵從度（越高越嚴格遵循提示） |
| `density` | 0.0 - 1.0 | 音符密度 |
| `brightness` | 0.0 - 1.0 | 音色明亮度 |
| `scale` | 列舉值 | 音階/調性 |
| `mute_bass` | True/False | 靜音貝斯 |
| `mute_drums` | True/False | 靜音鼓組 |

### 6.6 進階玩法：混合風格

```python
# 用加權提示混合兩種風格
await session.set_weighted_prompts(prompts=[
    types.WeightedPrompt(text='jazz piano trio', weight=1.0),
    types.WeightedPrompt(text='electronic ambient', weight=0.3),
])
```

### 6.7 免費試玩工具（不用寫程式）

不想寫程式也能體驗 Lyria RealTime 的威力。Google 提供了三個現成工具：

---

#### 工具 A：Prompt DJ（最簡單，推薦先試這個）

用文字提示即時操控音樂生成，像 DJ 一樣混音。打開網頁就能玩。

**連結：** [aistudio.google.com/apps/bundled/promptdj](https://aistudio.google.com/apps/bundled/promptdj)

**操作步驟：**

1. 點擊上方連結，用 Google 帳號登入
2. 如果要求 API 金鑰，貼上你在 6.2 取得的金鑰
3. 進入介面後，你會看到一個文字輸入區和播放控制面板
4. 在提示欄輸入音樂風格，例如：`jazz piano, relaxed`
5. 按下 **Play** 開始播放，音樂會即時串流生成
6. **邊播邊改**：修改提示詞文字，音樂會平滑過渡到新風格
7. 調整 **BPM 滑桿** 改變速度、**Temperature 滑桿** 改變創意程度
8. 聽到喜歡的段落，可以錄製或截取

> **小技巧：** 不要一次大改提示詞，而是慢慢加入或替換關鍵字（例如先加 `saxophone`，再把 `piano` 換成 `guitar`），音樂轉場會更自然。

📸 **【截圖 16】** Prompt DJ 介面：標示出提示欄、Play 按鈕、BPM 滑桿的位置。

---

#### 工具 B：MIDI DJ（需要 MIDI 控制器）

跟 Prompt DJ 一樣的功能，但額外支援用**實體 MIDI 設備**操控參數。

**連結：** [aistudio.google.com/apps/bundled/promptdj-midi](https://aistudio.google.com/apps/bundled/promptdj-midi)

**你需要：**
- 一台 MIDI 控制器（MIDI 鍵盤、旋鈕控制器等）
- Chrome 瀏覽器（支援 Web MIDI API）
- USB 線連接 MIDI 控制器到電腦

**操作步驟：**

1. 用 USB 線把 MIDI 控制器接上電腦
2. 用 **Chrome 瀏覽器**打開上方連結
3. 網頁會偵測你的 MIDI 設備，可能會彈出「允許存取 MIDI 裝置」的提示，按**允許**
4. 輸入音樂風格提示詞，按 Play 開始播放
5. 用 MIDI 控制器上的**旋鈕**即時調整 BPM、風格混合比例、音色明暗等參數
6. 用 MIDI 控制器上的**按鍵**觸發風格切換或靜音特定樂器

> **沒有 MIDI 控制器？** 直接用工具 A（Prompt DJ）就好，功能幾乎一樣，差別只是操控方式。

📸 **【截圖 16b】** MIDI DJ 介面，以及 MIDI 控制器連接後的偵測畫面。

---

#### 工具 C：The Infinite Crate（DAW 音樂製作外掛）

Google Magenta 團隊推出的**免費 DAW 外掛**，可以在 Ableton Live、Logic Pro 等音樂製作軟體中直接使用 Lyria RealTime。

**下載連結：** [magenta.withgoogle.com/infinite-crate](https://magenta.withgoogle.com/infinite-crate)

**支援平台：**
| 系統 | 格式 |
|------|------|
| Windows | VST3 外掛 / 獨立應用程式 |
| Mac | AU 外掛 / VST3 外掛 / 獨立應用程式 |

**安裝步驟：**

1. 到上方連結下載對應你系統的安裝檔
2. 執行安裝程式
3. 安裝完成後，在你的 DAW 中搜尋外掛「**The Infinite Crate**」載入
4. 第一次開啟時，貼上你的 API 金鑰（跟 6.2 取得的同一組）

**操作步驟：**

1. 在 DAW 中的音軌上載入 The Infinite Crate 外掛
2. 在外掛介面的提示欄輸入音樂風格，例如：`funk bass groove`
3. 按下 **Play**，音樂會即時串流到 DAW 的音軌中
4. 調整介面上的控制項：
   - **BPM**：設為 `SYNC` 可自動同步 DAW 的速度
   - **Key**：指定音階調性
   - **TopK / Temp**：控制音樂的多樣性
5. 在 DAW 中直接**錄製**生成的音訊片段
6. 對錄下來的片段進行剪輯、混音、加效果器

> **限制：** 每次最多連續生成 **10 分鐘**，時間到了按 **Reset** 重新開始。
>
> **沒有 DAW？** 可以選安裝時的「**獨立應用程式（Standalone）**」模式，不需要 DAW 也能單獨使用。

📸 **【截圖 16c】** The Infinite Crate 下載頁面。

📸 **【截圖 16d】** The Infinite Crate 在 DAW 中的外掛介面（如果有安裝的話）。

---

## 七、提示詞（Prompt）攻略大全

好的提示詞 = 好的音樂。這是最重要的一個章節。

### 7.1 MIDST 公式

記住這個口訣：**M-I-D-S-T**

| 字母 | 全稱 | 說明 | 範例 |
|------|------|------|------|
| **M** | Mood（情緒） | 你想要什麼感覺？ | 歡樂、憂傷、激昂、平靜、神秘 |
| **I** | Instrument（樂器） | 用什麼樂器演奏？ | 鋼琴、吉他、鼓組、小提琴、合成器 |
| **D** | Dynamic（動態） | 音量和力度變化 | 漸強、漸弱、開場柔和後段爆發 |
| **S** | Style（風格） | 什麼音樂類型？ | 流行、爵士、古典、電子、嘻哈 |
| **T** | Tempo（節奏） | 快還是慢？ | 60 BPM（慢）、120 BPM（中）、150 BPM（快） |

### 7.2 額外可加入的元素

| 元素 | 說明 | 範例 |
|------|------|------|
| **人聲** | 要不要歌手演唱？ | 女聲、男聲、合唱、無人聲 |
| **音域** | 歌手的聲音特質 | 高亢女高音、低沉男中音、沙啞嗓音 |
| **歌詞主題** | 唱什麼內容？ | 關於旅行、關於友情、關於失戀 |
| **年代感** | 什麼時代的音樂風格？ | 80 年代合成器、90 年代嘻哈、2020 年代流行 |
| **參考情境** | 在什麼場景播放？ | 咖啡廳、健身房、婚禮、電影預告 |

### 7.3 從差到好的提示詞進化

**等級 1 — 太模糊 ❌**

> **✏️ 提示詞（反面教材，不建議使用）**
> ```
> 幫我做一首歌
> ```

→ AI 不知道你要什麼，結果隨機。

---

**等級 2 — 有方向 △**

> **✏️ 提示詞（勉強可用，但效果不穩定）**
> ```
> 做一首快樂的歌
> ```

→ 比較好了，但還是太寬泛。

---

**等級 3 — 具體描述 ✓**

> **✏️ 提示詞 ▼ 複製貼上到 Gemini（推薦）**
> ```
> Create an upbeat pop song with acoustic guitar and piano,
> female vocals, about enjoying a sunny day at the beach.
> Tempo around 120 BPM.
> ```

→ AI 能精準理解你的需求。

---

**等級 4 — 專業級 ✓✓**

> **✏️ 提示詞 ▼ 複製貼上到 Gemini（最佳示範）**
> ```
> Compose a feel-good indie pop track featuring bright acoustic guitar strumming,
> layered with soft synth pads and a groovy bass line. Sweet female vocals with
> airy harmonies singing about spontaneous road trips and summer freedom.
> Start with a gentle verse, build into an anthemic chorus with hand claps.
> 120 BPM, key of G major.
> ```

→ 近乎完美的提示詞，AI 能生成非常符合預期的音樂。

### 7.4 常用音樂風格英文對照表

| 中文 | English | 特色 |
|------|---------|------|
| 流行樂 | Pop | 朗朗上口的旋律 |
| 搖滾 | Rock | 電吉他為主導 |
| 嘻哈 | Hip Hop | 節奏強烈，饒舌 |
| 電子舞曲 | EDM | 合成器、重低音 |
| 爵士 | Jazz | 即興、搖擺感 |
| 古典 | Classical | 管弦樂團 |
| R&B | R&B / Soul | 節奏藍調，靈魂樂 |
| 鄉村 | Country | 木吉他、班鳩琴 |
| 雷鬼 | Reggae | 牙買加節奏 |
| Lo-fi | Lo-fi | 低保真、放鬆 |
| Bossa Nova | Bossa Nova | 巴西風情 |
| 民謠 | Folk | 原聲樂器 |
| 金屬 | Metal | 重型吉他 |
| 環境音樂 | Ambient | 氛圍、背景 |
| 放克 | Funk | 律動強烈 |
| 藍調 | Blues | 12 小節藍調 |

### 7.5 常用樂器英文對照表

| 中文 | English |
|------|---------|
| 鋼琴 | Piano |
| 木吉他 | Acoustic Guitar |
| 電吉他 | Electric Guitar |
| 貝斯 | Bass |
| 鼓組 | Drums |
| 小提琴 | Violin |
| 大提琴 | Cello |
| 薩克斯風 | Saxophone |
| 長笛 | Flute |
| 小號 | Trumpet |
| 合成器 | Synthesizer |
| 烏克麗麗 | Ukulele |
| 口琴 | Harmonica |
| 豎琴 | Harp |

---

## 八、SynthID 浮水印：AI 音樂的身分證

### 8.1 什麼是 SynthID？

**SynthID** 是 Google DeepMind 開發的數位浮水印技術，所有由 Gemini 生成的音樂都會被自動嵌入這個不可見的浮水印。

### 8.2 運作原理

```
原始音訊波形 → 轉換為頻譜圖 → 嵌入數位浮水印 → 轉回音訊波形 → 輸出
                                    ↑
                            人耳完全聽不出來
```

### 8.3 特性

| 特性 | 說明 |
|------|------|
| 不可聽 | 人耳完全無法感知 |
| 高韌性 | 經過 MP3 壓縮、加速、降速後仍可偵測 |
| 強制性 | 所有 AI 生成音樂都會自動加上，無法移除 |
| 可驗證 | 可上傳到 Gemini App 驗證是否為 AI 生成 |

### 8.4 如何驗證一段音樂是否為 AI 生成？

你可以將音樂檔案上傳到 Gemini App，詢問：

> **✏️ 提示詞 ▼ 上傳音樂檔案後，複製貼上到 Gemini**
> ```
> 請幫我檢查這段音樂是否包含 SynthID 浮水印
> ```

📸 **【截圖 17】** 上傳音樂檔案到 Gemini 進行 SynthID 驗證的畫面（如有此功能可截取）。

---

## 九、實戰範例：五種情境示範

### 情境 1：YouTube 影片背景音樂

**需求：** 為一部 3 分鐘的旅遊 Vlog 製作背景音樂

> **✏️ 提示詞 ▼ 複製貼上到 Gemini**
> ```
> Create a cheerful and inspiring travel vlog background music.
> Acoustic guitar with light percussion and soft synth pads.
> Feel-good and adventurous mood. No vocals. 120 BPM.
> ```

**技巧：** 你可以生成多段 30 秒的音樂，然後在剪輯軟體中串接起來。

---

### 情境 2：Podcast 開場音樂

**需求：** 科技 Podcast 的開場 jingle

> **✏️ 提示詞 ▼ 複製貼上到 Gemini**
> ```
> Short tech podcast intro jingle. Modern electronic beat with
> futuristic synth sounds and a catchy melody hook.
> Energetic and professional. 100 BPM.
> ```

---

### 情境 3：簡報背景音樂

**需求：** 商業簡報投影片的背景音樂

> **✏️ 提示詞 ▼ 複製貼上到 Gemini**
> ```
> Corporate presentation background music. Gentle piano with soft strings.
> Clean, professional, and uplifting. Minimal and not distracting.
> 90 BPM. No vocals.
> ```

---

### 情境 4：社群短影音配樂

**需求：** Instagram Reels / TikTok 短影音的配樂

> **✏️ 提示詞 ▼ 複製貼上到 Gemini**
> ```
> Trendy social media short video music. Catchy beat with bass and
> trap hi-hats. Fun and energetic with a memorable drop. 130 BPM.
> ```

---

### 情境 5：用照片生成旅遊回憶配樂

**操作：** 上傳一張旅遊照片 + 以下文字

> **✏️ 提示詞 ▼ 上傳照片後，複製貼上到 Gemini**
> ```
> Look at this travel photo and compose a nostalgic, warm soundtrack
> that captures the memory. Use acoustic instruments like guitar and
> light strings. Bittersweet and beautiful.
> ```

📸 **【截圖 18】** 上傳旅遊照片並生成配樂的完整對話畫面。

---

## 十、常見問題 FAQ

### Q1：生成的音樂只有 30 秒，怎麼做更長的？

**A：** 目前 Gemini App 的 Lyria 3 限制為 30 秒。如果需要更長的音樂：
- 多次生成相同風格的片段，用剪輯軟體（如 Audacity、CapCut）串接
- 使用 Lyria RealTime API 可以串流式持續生成
- 在提示詞中保持一致的風格描述，以確保片段間的連貫性

### Q2：生成的音樂可以商用嗎？

**A：** Google 目前尚未明確公佈 Lyria 3 生成音樂的商業授權條款。建議：
- 個人使用、學習用途基本上沒問題
- 商業用途請關注 Google 官方的最新使用條款
- 所有生成音樂都帶有 SynthID 浮水印

### Q3：可以指定特定歌手的聲音嗎？

**A：** 不行。Gemini 的設計原則是鼓勵**原創表達**，不會模仿特定藝術家的聲音。你可以描述聲音特質（如「沙啞的男聲」「高亢的女聲」），但不能指定「像某某歌手」。

### Q4：中文提示詞效果好嗎？

**A：** 目前官方支援 8 種語言，暫不含中文。中文提示詞可以使用，Gemini 會理解意思，但建議**關鍵的音樂描述用英文**效果更佳。可以搭配前面介紹的「音樂 Gem」來幫你翻譯和優化提示詞。

### Q5：生成的音樂是原創的嗎？會不會侵權？

**A：** Lyria 3 具備過濾系統，會避免生成與現有歌曲過於相似的內容。但 Google 也承認過濾器不是 100% 完美。如果你發現生成結果與某首歌非常相似，建議不要使用該段音樂。

### Q6：手機上可以使用嗎？

**A：** 音樂生成功能先在桌面版推出，手機版隨後跟進。請確認你的 Gemini App 已更新到最新版本。

---

## 十一、延伸資源

### 官方資源

| 資源 | 連結 |
|------|------|
| Gemini App | [gemini.google.com](https://gemini.google.com) |
| Google AI Studio | [aistudio.google.com](https://aistudio.google.com) |
| Lyria RealTime API 文件 | [ai.google.dev/gemini-api/docs/music-generation](https://ai.google.dev/gemini-api/docs/music-generation?hl=zh-tw) |
| DeepMind Lyria 3 介紹 | [deepmind.google/models/lyria](https://deepmind.google/models/lyria/) |
| SynthID 說明 | [deepmind.google/models/synthid](https://deepmind.google/models/synthid/) |

### 參考文章

1. [Gemini 正式加入「音樂生成」功能！最新 Lyria 3 模型登場](https://www.koc.com.tw/archives/631603)
2. [Gemini 導入音樂生成模型 Lyria 3，一鍵生成 30 秒 AI 音樂](https://technews.tw/2026/02/19/gemini-app-now-features-lyria-3/)
3. [Gemini 可以創作音樂啦！Lyria：你的 AI 聲音旅伴（附贈提示詞指南）](https://vocus.cc/article/69966db9fd89780001725740)
4. [給它文字、圖片，Gemini 音樂模型生成 30 秒配樂（YouTube）](https://youtu.be/DHz0cYd_xlI)

### 搭配工具推薦

| 工具 | 用途 | 費用 |
|------|------|------|
| **Audacity** | 免費音訊剪輯，串接多段 AI 音樂 | 免費 |
| **CapCut** | 影片剪輯，搭配 AI 音樂做短影音 | 免費 |
| **Canva** | 製作搭配音樂的社群圖文 | 免費/付費 |

---

## 截圖清單總整理

以下是本文所有需要截圖的位置，請依序截取：

| 編號 | 截圖說明 | 所在章節 |
|------|----------|----------|
| **截圖 01** | Gemini 首頁畫面（已登入狀態） | 二、事前準備 |
| **截圖 02** | Gemini 對話介面，輸入框位置 | 三、文字生成音樂 |
| **截圖 03** | 在輸入框中輸入音樂提示詞 | 三、文字生成音樂 |
| **截圖 04** | Gemini 正在生成音樂的等待畫面 | 三、文字生成音樂 |
| **截圖 05** | 音樂生成完成的播放介面（標示播放/下載/分享按鈕） | 三、文字生成音樂 |
| **截圖 06** | 追加修改需求並重新生成的對話畫面 | 三、文字生成音樂 |
| **截圖 07** | 上傳按鈕的位置示意 | 四、圖片生成音樂 |
| **截圖 08** | 上傳圖片後加上文字指令的畫面 | 四、圖片生成音樂 |
| **截圖 09** | 圖片音樂生成完成的結果畫面 | 四、圖片生成音樂 |
| **截圖 10** | Gemini 左側面板中 Gems 入口位置 | 五、Gem 機器人 |
| **截圖 11** | 點擊建立新 Gem 的按鈕 | 五、Gem 機器人 |
| **截圖 12** | 在 Gem 指令欄位中輸入設定 | 五、Gem 機器人 |
| **截圖 13** | 命名並儲存 Gem | 五、Gem 機器人 |
| **截圖 14** | 與音樂 Gem 對話，展示產出的提示詞建議 | 五、Gem 機器人 |
| **截圖 15** | Google AI Studio 取得 API Key 的頁面 | 六、API 進階玩法 |
| **截圖 16** | Google AI Studio 中 Prompt DJ 的介面 | 六、API 進階玩法 |
| **截圖 17** | 上傳音樂進行 SynthID 驗證的畫面 | 八、SynthID 浮水印 |
| **截圖 18** | 上傳旅遊照片並生成配樂的完整對話 | 九、實戰範例 |
| **截圖 19** | 程式執行後的 MIDST 互動選單畫面 | 六、API 進階玩法 |
| **截圖 20** | 設定總覽確認畫面，按下 y 開始生成 | 六、API 進階玩法 |
| **截圖 21** | 終端機中 `pip install google-genai` 安裝成功的畫面 | 六、API 進階玩法 |
| **截圖 21a** | 音樂生成完成，資料夾中出現 `output_music.wav` | 六、API 進階玩法 |

---

