# gr_json_tools

## Overview

**`gr_json_tools`** is a set of tools for JSON data comparison and formatting.  
It provides two main scripts:

1. **json_diff_reporter** - Compares two JSON files and generates a report.
2. **format_json_readable** - Formats JSON files for improved readability.

---

## json_diff_reporter

### Overview

`report_json_diff.py` compares two JSON files and generates reports in HTML and TSV format.

### Features

- **HTML report** - Visually highlighted comparison table.
- **TSV file** - Tabular format for Excel or further processing.

### Difference Types

| Type          | Description                                |
| ------------- | ------------------------------------------ |
| `Added`       | A new key or list item was added           |
| `Removed`     | An existing key or list item was removed   |
| `Modified`    | Value changed (same type)                  |
| `TypeChanged` | Value type changed (e.g., `str` → `int`)   |
| `Reordered`   | Order changed but content remains the same |

### Usage

```bash
python report_json_diff.py before.json after.json
```

Outputs:

- `json_diff_report.html`
- `json_diff_report.tsv`

---

## format_json_readable

### Overview

`format_json_readable.py` formats JSON files to improve readability.

### Features

- **Key sorting** (`"type"` → `"required"` → others)
- **Inline formatting** (control over indentation)

### Usage

```bash
python format_json_readable.py [--sort] [--inline-from-top N | --inline-from-tail N] input.json
```

Outputs:

- `input_readable.json`

### Options

| Option                 | Description                                               |
| ---------------------- | --------------------------------------------------------- |
| `--sort`               | Reorders keys in `"type" → "required" → others"` order    |
| `--inline-from-top N`  | Everything inline below the Nth depth (absolute from top) |
| `--inline-from-tail N` | Inline N levels from the bottom per object (relative)     |

⚠️ `--inline-from-top` and `--inline-from-tail` cannot be used together.

---

## Limitations

- Large JSON files may slow down processing.
- Inline control does not apply to array elements.
- Sorting is limited to predefined key priorities.

---

## License

This project is licensed under the **MIT License**.  
For details, see [`LICENSE`](https://opensource.org/licenses/MIT).

---

## Author

Director: **good_relax**  
Code generation & refinement: **OpenAI GPT-4o**

---

# gr_json_tools（日本語版）

## 概要

**`gr_json_tools`** は、JSON データの比較・整形を簡単に行えるツール群です。  
主に以下の 2 つのスクリプトを提供します。

1. **json_diff_reporter** - 2 つの JSON ファイルの差分を分析し、レポートを生成
2. **format_json_readable** - JSON ファイルを人間が読みやすい形式に再整形

---

## json_diff_reporter

### 概要

`report_json_diff.py` は、2 つの JSON ファイルを比較し、HTML と TSV の差分レポートを出力します。

### 主な機能

- **HTML レポート** - 視覚的にハイライトされた比較表
- **TSV ファイル** - Excel などで処理しやすいテーブル形式

### 出力される差分タイプ

| Type          | 説明                                    |
| ------------- | --------------------------------------- |
| `Added`       | 新しく追加されたキーまたはリスト要素    |
| `Removed`     | 既存のキーまたはリスト要素が削除された  |
| `Modified`    | 値が変更された（同じデータ型）          |
| `TypeChanged` | 値の型が変更された（例: `str` → `int`） |
| `Reordered`   | 順序のみ変更された（内容は変わらない）  |

### 使用方法

```bash
python report_json_diff.py before.json after.json
```

出力されるファイル：

- `json_diff_report.html`
- `json_diff_report.tsv`

---

## format_json_readable

### 概要

`format_json_readable.py` は、JSON ファイルを視覚的に整理し、より読みやすい形式に変換するツールです。

### 主な機能

- **キー順の整理** （例: `"type"`, `"required"` を優先）
- **インライン整形** （階層ごとの折りたたみオプション）

### 使用方法

```bash
python format_json_readable.py [--sort] [--inline-from-top N | --inline-from-tail N] input.json
```

出力されるファイル：

- `input_readable.json`

### オプション一覧

| オプション             | 説明                                                      |
| ---------------------- | --------------------------------------------------------- |
| `--sort`               | キーを `"type" → "required" → その他"` の順で並べ替え     |
| `--inline-from-top N`  | 上から N 階層目以降をインライン表示（改行なし）           |
| `--inline-from-tail N` | 各オブジェクトの下から N 階層をインライン表示（個別設定） |

⚠️ `--inline-from-top` と `--inline-from-tail` は同時に指定不可。

---

## 制限事項

- JSON が大きすぎると処理速度が低下する可能性があります。
- インライン制御は配列要素には適用されません。
- `--sort` は特定のキー順のみに適用されます。

---

## ライセンス

このプロジェクトは **MIT ライセンス** のもと提供されています。  
詳細は [`LICENSE`](https://opensource.org/licenses/MIT) を参照してください。

---

## 作者

監督 : **good_relax**  
コード生成・最適化 : **OpenAI GPT-4o**
