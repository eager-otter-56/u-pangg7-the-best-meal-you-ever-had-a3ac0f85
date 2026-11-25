import os
import stat

ENTRY_TEXT = "A Bangkok street cart sold me noodles for 40 baht at midnight, chilli still burning my lips, and when I went back the next night the cart was gone."

def main():
    # Gate: /output/entry.txt must be UTF-8, 1-200 chars, not only whitespace, one sentence.
    text = ENTRY_TEXT.strip()
    assert 1 <= len(ENTRY_TEXT) <= 200, "entry must be 1-200 chars"
    assert text, "entry must not be only whitespace"
    assert ENTRY_TEXT.count(".") <= 1, "entry must be one sentence"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)
    os.chmod(path, 0o644)

if __name__ == "__main__":
    main()
