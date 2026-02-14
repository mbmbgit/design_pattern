from abc import ABC, abstractmethod
from typing import List

# Strategy インターフェース: 戦略の共通仕様
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: int):
        pass

# 具体的な戦略1: クレジットカード
class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number, cvc):
        self.card_number = card_number
        self.cvc = cvc

    def pay(self, amount: int):
        print(f"クレジットカード {self.card_number} で {amount}円 支払いました。")

# 具体的な戦略2: PayPal
class PayPalPayment(PaymentStrategy):
    def __init__(self, email):
        self.email = email

    def pay(self, amount: int):
        print(f"PayPalアカウント {self.email} で {amount}円 支払いました。")

# Context: 戦略を利用する側（ショッピングカート）
class ShoppingCart:
    def __init__(self):
        self.items: List[int] = []
        # ここに戦略（支払い方法）を保持する
        self.payment_strategy: PaymentStrategy = None

    def add_item(self, price: int):
        self.items.append(price)

    # 実行時に戦略をセットできる（再利用性が高い）
    def set_payment_strategy(self, strategy: PaymentStrategy):
        self.payment_strategy = strategy

    def checkout(self):
        total = sum(self.items)
        if self.payment_strategy:
            self.payment_strategy.pay(total)
        else:
            print("支払い方法が設定されていません。")

# --- 実行 ---
if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_item(1000)
    cart.add_item(500)

    # 支払い方法を「クレジットカード」に設定
    print("--- クレジットカードで決済 ---")
    cart.set_payment_strategy(CreditCardPayment("1234-5678", "123"))
    cart.checkout()

    # 同じカートオブジェクトのまま、支払い方法だけを「PayPal」に変更（再利用）
    print("\n--- PayPalで決済 ---")
    cart.set_payment_strategy(PayPalPayment("user@example.com"))
    cart.checkout()
