# format_json_readable (English)

## Overview

`format_json_readable.py` formats a JSON file into a human-readable layout.  
It supports sorting of keys and control over indentation/folding.

## Key Features

- Sorts keys in the order: `"type"`, `"required"`, then others (optional)
- Allows inline formatting for specific depth levels

## Usage

```bash
python format_json_readable.py [--sort] [--inline-from-top N | --inline-from-tail N] input.json
```

The output will be saved as `input_readable.json`.

## Options

| Option                 | Description                                                       |
| ---------------------- | ----------------------------------------------------------------- |
| `--sort`               | Reorders keys: `"type" → "required" → others"`                    |
| `--inline-from-top N`  | Show everything inline below the Nth depth (absolute from top)    |
| `--inline-from-tail N` | Inline N levels from the bottom per object (relative, per object) |

⚠️ `--inline-from-top` and `--inline-from-tail` cannot be used together.

## Example Usage

```bash
python format_json_readable.py  --inline-from-top 1 input.json
python format_json_readable.py  --inline-from-tail 2 input.json
python format_json_readable.py  --sort --inline-from-tail 2 input.json
```

## Limitations

- Fails if input is not valid JSON
- Inline control does not apply to array elements
- Sorting is limited to fixed key priorities

## Author

Director : good_relax
Code generation and refine : OpenAI GPT-4o

## Note

This project is licensed under the MIT License. For more details, see [MIT License](https://opensource.org/licenses/MIT).

---

# format_json_readable（日本語版）

## 概要

`format_json_readable.py` は JSON ファイルを「人間にとって読みやすい形式」に整形するツールです。  
インデント、改行、並べ替え、折りたたみなどの調整が可能です。

## 主な機能

- `type` / `required` / その他 の順でキーを並び替え（オプション）
- 階層指定によるインライン表示（折りたたみ）制御

## 使い方

```bash
python format_json_readable.py [--sort] [--inline-from-top N | --inline-from-tail N] input.json
```

出力は `input_readable.json` という名前で保存されます。

## オプション一覧

| オプション             | 説明                                                      |
| ---------------------- | --------------------------------------------------------- |
| `--sort`               | キーを `"type" → "required" → その他"` の順で並べ替え     |
| `--inline-from-top N`  | 上から N 階層目以降をすべてインライン表示（改行しない）   |
| `--inline-from-tail N` | 各オブジェクトで下から N 階層をインライン表示（個別制御） |

⚠️ `--inline-from-top` と `--inline-from-tail` は同時に指定できません。

## 使用例

```bash
python format_json_readable.py  --inline-from-top 1 input.json
python format_json_readable.py  --inline-from-tail 2 input.json
python format_json_readable.py  --sort --inline-from-tail 2 input.json
```

## 制限事項

- 入力 JSON が不正な場合は例外が発生します
- 配列内の要素に対してはインライン制御はありません
- `--sort` は特定のキー順（type, required）に限定されています

## 作者

監督 : good_relax
コード生成・最適化 : OpenAI GPT-4o

## Note

このプロジェクトは MIT ライセンスの下で提供されている。 詳しいライセンス内容については、[MIT License](https://opensource.org/licenses/MIT) を参照のこと。
