"""
3. Adapter（アダプター）パターン
（インターフェースの変換による再利用）

互換性のないクラス同士をつなぐ「変換アダプター」のような役割を果たします。「すでに動いている古いコード」や「外部ライブラリ」を、修正することなく新しいシステムで再利用したい場合に非常に有効です。

シナリオ: 新しいシステムは StandardMediaPlayer インターフェースを使っているが、古い LegacyVideoPlayer クラス（メソッド名が違う）も再利用して動画を再生したい。
"""

from abc import ABC, abstractmethod

# 1. Target: 新しいシステムが期待している共通インターフェース
class MediaPlayer(ABC):
    @abstractmethod
    def play(self, filename: str):
        pass

# 2. Adaptee: 再利用したい既存のクラス（インターフェースが異なる）
class LegacyVideoPlayer:
    def play_old_format(self, filename: str):
        # 昔の複雑な初期化処理などが入っていると仮定
        print(f"LegacyPlayer: 古いアルゴリズムで {filename} を再生中...")

# 3. Adapter: 既存クラスを新しいインターフェースに適合させる
class VideoPlayerAdapter(MediaPlayer):
    def __init__(self, legacy_player: LegacyVideoPlayer):
        self.legacy_player = legacy_player

    # 新しいメソッド名(play)で呼ばれたら、内部で古いメソッド(play_old_format)を呼ぶ
    def play(self, filename: str):
        print("Adapter: 新しい形式の呼び出しを古い形式に変換します")
        self.legacy_player.play_old_format(filename)

# 4. Client: 新しいシステム（Adapterのおかげで統一的に扱える）
def run_media_player(player: MediaPlayer, filename: str):
    player.play(filename)

# --- 実行 ---
if __name__ == "__main__":
    # 既存のクラスのインスタンス
    old_system = LegacyVideoPlayer()
    
    # アダプターを噛ませる
    adapter = VideoPlayerAdapter(old_system)
    
    # クライアントは古いクラスであることを意識せずに使える
    run_media_player(adapter, "movie.avi")
