# json_diff_reporter (English Version)

## Overview

`report_json_diff.py` compares two JSON files and outputs the differences as:

- HTML report (highlighted table)
- TSV file (tabular for Excel or processing)

## Difference Types

| Type          | Description                              |
| ------------- | ---------------------------------------- |
| `Added`       | New key or list item added               |
| `Removed`     | Existing key or list item removed        |
| `Modified`    | Value changed (same type)                |
| `TypeChanged` | Value type changed (e.g. str → int)      |
| `Reordered`   | List/dict order changed but content same |

## Usage

```bash
python report_json_diff.py before.json after.json
```

This will output:

- `json_diff_report.html`
- `json_diff_report.tsv`

## Comparison Logic

1. **Type mismatch** → `TypeChanged`
2. **Dict comparison**
   - If exactly one key differs → recursively compare contents
   - Otherwise → mark each as `Added`, `Removed`, `Modified`
3. **List comparison**
   - If completely identical → no difference
   - If order only differs → `Reordered`
   - If only one added and one removed → compare those elements
   - Otherwise → mark as `Added` / `Removed`
4. **Primitive comparison** → `Modified` if values differ

## Limitations

- Large JSON files may slow down processing.
- List comparison is content-based; order is ignored except for `Reordered` detection.
- Only recursive comparison is done when exactly one key or one element differs.

## Author

Director : good_relax
Code generation and refine : OpenAI GPT-4o

## Note

This project is licensed under the MIT License. For more details, see [MIT License](https://opensource.org/licenses/MIT).

---

# json_diff_reporter（日本語版）

## 概要

`report_json_diff.py` は、2 つの JSON ファイルの差分を比較し、以下の形式で結果を出力するツールです：

- HTML レポート（視覚的に強調された表形式）
- TSV ファイル（Excel 等で加工可能）

## 出力される差分タイプ

| Type          | 内容の説明                                         |
| ------------- | -------------------------------------------------- |
| `Added`       | 追加されたキーまたは配列要素                       |
| `Removed`     | 削除されたキーまたは配列要素                       |
| `Modified`    | 値の内容が変化（型は同じ）                         |
| `TypeChanged` | 値の型が変更（例：文字列 → 数値）                  |
| `Reordered`   | 配列・オブジェクトの順番が変更されたが、内容は同じ |

## 使い方

```bash
python report_json_diff.py before.json after.json
```

- `json_diff_report.html` と `json_diff_report.tsv` が出力されます。

## 比較ロジック

1. **型が異なる場合** → `TypeChanged`
2. **辞書の比較**
   - 共通キーを比較し、差分が 1 つのみ → 中を再帰的に比較
   - 差分が複数 → それぞれ `Added`, `Removed`, `Modified`
3. **リストの比較**
   - 完全一致 → 差分なし
   - 並び順だけ異なる → `Reordered`
   - 差分要素が 1 組のみ → その要素を比較
   - その他 → `Added` / `Removed`
4. **値の比較** → `Modified`（値が異なる場合）

## 制限事項

- JSON のサイズが非常に大きいと処理が遅くなる可能性があります。
- リストの差分判定は内容ベースであり、順序情報は基本無視（順序に厳密な意味がある場合は注意）。
- 差分が 1 組のときのみ再帰比較を行います。それ以上は打ち切ります。

## 作者

監督 : good_relax
コード生成・最適化 : OpenAI GPT-4o

## Note

このプロジェクトは MIT ライセンスの下で提供されている。 詳しいライセンス内容については、[MIT License](https://opensource.org/licenses/MIT) を参照のこと。
