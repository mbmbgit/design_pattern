"""
4. Decorator（デコレーター）パターン
（機能の「重ね着」による再利用）

既存のオブジェクトに、後から機能を「被せる（デコレーションする）」ことで拡張するパターンです。継承を使って機能を増やすとクラスが爆発的に増えてしまいますが、このパターンなら基本クラスを再利用しながら必要な機能だけを柔軟に組み合わせられます。

シナリオ: 基本のメッセージ表示機能に、「暗号化」や「HTMLタグ付け」の機能を追加する。
"""

from abc import ABC, abstractmethod

# 1. Component: 基本となるインターフェース
class TextPublisher(ABC):
    @abstractmethod
    def publish(self, text: str) -> str:
        pass

# 2. ConcreteComponent: ベースとなるシンプルな実装
class SimplePublisher(TextPublisher):
    def publish(self, text: str) -> str:
        return text

# 3. Decorator: 装飾者の基底クラス
class PublisherDecorator(TextPublisher):
    def __init__(self, wrapped: TextPublisher):
        self._wrapped = wrapped # 中身（別のDecoratorかComponent）を保持

    def publish(self, text: str) -> str:
        return self._wrapped.publish(text)

# 4. ConcreteDecoratorA: 機能を足すクラス（HTML化）
class HTMLDecorator(PublisherDecorator):
    def publish(self, text: str) -> str:
        # 親（中身）の処理結果を受け取り、加工する
        result = super().publish(text)
        return f"<html><body>{result}</body></html>"

# 5. ConcreteDecoratorB: 機能を足すクラス（暗号化風）
class EncryptionDecorator(PublisherDecorator):
    def publish(self, text: str) -> str:
        result = super().publish(text)
        # 簡易的な文字変換（暗号化シミュレーション）
        return "".join([chr(ord(c) + 1) for c in result])

# --- 実行 ---
if __name__ == "__main__":
    simple = SimplePublisher()
    
    print("1. そのまま:")
    print(simple.publish("Hello"))

    print("\n2. HTML装飾を追加:")
    # simple を HTMLDecorator で包む
    html_version = HTMLDecorator(simple)
    print(html_version.publish("Hello"))

    print("\n3. HTML化して、さらに暗号化（重ね着）:")
    # HTML版をさらに EncryptionDecorator で包む
    encrypted_html = EncryptionDecorator(html_version)
    print(encrypted_html.publish("Hello"))
