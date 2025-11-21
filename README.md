# Project-Zero

新增 `safe_division` 範例工具

Files added in this change:

- `src/safe_math/safe_division.py` — 提供 `safe_division(a, b)`，當 `b == 0` 時回傳 `None`。
- `tests/test_safe_division.py` — 對應的簡單單元測試。

使用方法:

```bash
python -c "from src.safe_math import safe_division; print(safe_division(6,3))"
```



