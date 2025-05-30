# Copyright (c) 2025 GoodRelax
# MIT License
# This code was generated by ChatGPT-4o based on specifications provided by GoodRelax.

import argparse
import json
import sys
from pathlib import Path

def is_flat_primitive(value):
    return isinstance(value, (str, int, float, bool, type(None)))

def get_max_depth(obj, current=0):
    if isinstance(obj, dict):
        return max((get_max_depth(v, current + 1) for v in obj.values()), default=current)
    elif isinstance(obj, list):
        return max((get_max_depth(v, current + 1) for v in obj), default=current)
    else:
        return current

def enforce_type_required_order(obj):
    if isinstance(obj, dict):
        keys = list(obj.keys())
        keys.sort(key=lambda x: (0 if x == "type" else 1 if x == "required" else 2))
        return {k: enforce_type_required_order(obj[k]) for k in keys}
    elif isinstance(obj, list):
        return [enforce_type_required_order(v) for v in obj]
    else:
        return obj

def dump_json_with_depth_control(obj, indent=2, level=0, inline_from_top=None, inline_from_tail=None, root_depth=None):
    if root_depth is None:
        root_depth = get_max_depth(obj, level)

    pad = " " * (indent * level)

    inline_top = inline_from_top is not None and level >= inline_from_top
    inline_tail = inline_from_tail is not None and level >= (root_depth - inline_from_tail)

    if inline_top or inline_tail:
        return json.dumps(obj, ensure_ascii=False)

    if isinstance(obj, dict):
        if not obj:
            return "{}"
        items = []
        for k, v in obj.items():
            v_str = dump_json_with_depth_control(v, indent, level + 1, inline_from_top, inline_from_tail, root_depth)
            items.append(f'{pad}{" " * indent}"{k}": {v_str}')
        return "{\n" + ",\n".join(items) + f"\n{pad}}}"
    elif isinstance(obj, list):
        if not obj:
            return "[]"
        if all(is_flat_primitive(v) for v in obj):
            return "[ " + ", ".join(json.dumps(v, ensure_ascii=False) for v in obj) + " ]"
        items = [f'{pad}{" " * indent}{dump_json_with_depth_control(v, indent, level + 1, inline_from_top, inline_from_tail, root_depth)}' for v in obj]
        return "[\n" + ",\n".join(items) + f"\n{pad}]"
    else:
        return json.dumps(obj, ensure_ascii=False)

def main():
    parser = argparse.ArgumentParser(description="Format JSON with optional inline display from top or bottom depth levels.")
    parser.add_argument("input_json", help="Path to input JSON file")
    parser.add_argument("--sort", action="store_true", help="Enable 'type'/'required' key reordering (default: off)")
    parser.add_argument("--inline-from-top", type=int, help="Render all levels inline starting from this depth")
    parser.add_argument("--inline-from-tail", type=int, help="Render bottom N levels inline (per object)")
    args = parser.parse_args()

    if args.inline_from_top is not None and args.inline_from_tail is not None:
        print("Error: Please specify only one of --inline-from-top or --inline-from-tail.")
        sys.exit(1)

    input_path = Path(args.input_json)
    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    processed = enforce_type_required_order(data) if args.sort else data
    formatted = dump_json_with_depth_control(
        processed,
        inline_from_top=args.inline_from_top,
        inline_from_tail=args.inline_from_tail
    )

    output_path = input_path.with_name(input_path.stem + "_readable.json")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(formatted + "\n")

    print(f"Formatted JSON saved to: {output_path}")

if __name__ == "__main__":
    main()
