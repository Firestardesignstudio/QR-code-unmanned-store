# 無人販売所システム（Camera + IR Beam, optional RFID）

カメラのROI比較で棚の**あり/なし**を判定し、赤外線ビームのイベントで誤検出を抑える軽量構成。重量センサーは不要。

## 主な機能
- あり/なし判定（ヒストグラム相関 + 補助指標）
- IRブレークビーム連動（手挿入トリガ）
- 証跡スナップ保存・イベントログ
- （任意）RFIDで入店ID関連付け
- 実機不要の**シミュレーションモード**同梱

## ハードウェア
- Raspberry Pi 4/5（3.3V GPIO）
- USBカメラ（/dev/video0）
- IRブレークビーム（3.3V）
- LED（330Ω）/ ブザー（必要に応じてトランジスタ駆動）
- RC522（任意・SPI/3.3V）

GPIO例:

| 機能 | ピン |
|---|---|
| IR_BEAM_INPUT | GPIO17 |
| LED_OUT | GPIO24 |
| BUZZER_OUT | GPIO23 |
| RC522 | CE0/SCLK/MOSI/MISO + RST(GPIO25) |

## セットアップ
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

## 実機クイックスタート
1. `config/slots.json` にスロットROIを定義  
2. `docs/UnmannedStore_Final_Manual.pdf` の第4章に従い「あり/なし」の基準画像と閾値を取得  
3. 実行:
```bash
python3 software/bridge_trigger.py
```

## シミュレーション（実機不要）
```bash
cd software/sim_unmanned_store
python3 detect_sim.py
```

## ログ
- 出力例: `logs/2025-11-07_event.log`  
- 記録: `timestamp, slot_id, state(ari|nashi), snap_path, ΔH, Hcorr(ari), Hcorr(nashi)`

## ドキュメント
- `docs/UnmannedStore_Final_Manual.pdf` … 回路・配線・ループフロー・SOP・評価フォーム・エビデンスチェックシート  
- `docs/ROI_Threshold_SOP.pdf` … ROI・閾値算出要点  
- `docs/Flow_Sheet_Page3_fixed.pdf` … 等幅修正版フローシート（単体）

## ライセンス
MIT（商用利用可・無保証）。`LICENSE` を参照。
