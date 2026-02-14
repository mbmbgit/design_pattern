"""
1. Template Method パターン
（継承を使った再利用）

親クラスで「処理の大枠（アルゴリズムの骨格）」を定義し、子クラスで「具体的な中身」を実装するパターンです。共通の処理フローを再利用したい場合に最適です。

シナリオ: 異なるデータ形式（CSVとJSON）を読み込んで解析するプログラム。
"""



from abc import ABC, abstractmethod

# 抽象クラス: 処理のテンプレート（骨格）を定義
class DataMiner(ABC):
    
    # これがテンプレートメソッドです
    # 処理の流れ（手順）を固定し、各ステップの実装はサブクラスに任せます
    def mine(self, path: str):
        data = self.open_file(path)
        raw_data = self.extract_data(data)
        analysis = self.analyze_data(raw_data)
        self.close_file(data)
        return analysis

    # 共通の処理はここで実装して再利用
    def analyze_data(self, raw_data):
        print("  -> データを分析中...")
        return f"分析結果: {len(raw_data)} 件のデータ"

    # 具体的な実装はサブクラスに強制する
    @abstractmethod
    def open_file(self, path: str):
        pass

    @abstractmethod
    def extract_data(self, file):
        pass

    @abstractmethod
    def close_file(self, file):
        pass

# 具体的なクラス1: CSV用
class CSVDataMiner(DataMiner):
    def open_file(self, path: str):
        print(f"CSVファイルを開きます: {path}")
        return "CSV_FILE_HANDLE"

    def extract_data(self, file):
        print("  -> CSVから行を抽出")
        return ["row1", "row2", "row3"]

    def close_file(self, file):
        print("CSVファイルを閉じました")

# 具体的なクラス2: PDF用
class PDFDataMiner(DataMiner):
    def open_file(self, path: str):
        print(f"PDFファイルを開きます: {path}")
        return "PDF_FILE_HANDLE"

    def extract_data(self, file):
        print("  -> PDFからテキストを抽出")
        return ["text_block1", "text_block2"]

    def close_file(self, file):
        print("PDFファイルを閉じました")

# --- 実行 ---
if __name__ == "__main__":
    print("--- CSVの処理 ---")
    csv_miner = CSVDataMiner()
    csv_miner.mine("data.csv")

    print("\n--- PDFの処理 ---")
    pdf_miner = PDFDataMiner()
    pdf_miner.mine("report.pdf")
