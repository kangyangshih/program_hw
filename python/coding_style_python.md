# coding style 和命名規則

寫出漂亮的 Python 代碼，不只是為了讓機器跑得動，更重要的是讓「人」看得懂。

Python 社群有一份權威的指導文件叫 **PEP 8**。

以下我為你整理了最核心的命名規則與撰寫風格：

---

## 1. 命名規則 (Naming Conventions)

Python 對不同類型的對象有不同的命名偏好，這被稱為「慣例」。

| 對象 | 命名格式 | 範例 |
| --- | --- | --- |
| **變數 (Variables)** | 小寫 + 底線 (snake_case) | `user_name`, `total_count` |
| **函式 (Functions)** | 小寫 + 底線 (snake_case) | `calculate_price()`, `get_data()` |
| **類別 (Classes)** | 首字母大寫 (PascalCase) | `UserProfile`, `DatabaseConnection` |
| **常數 (Constants)** | 全大寫 + 底線 (UPPER_CASE) | `MAX_RETRY`, `API_KEY` |
| **模組/套件 (Modules)** | 全小寫 | `requests`, `json_parser` |

### ⚠️ 特別注意：

* **私有屬性/函式**：若想暗示該項目僅限類別內部使用，會在前面加一個底線，例如 `_internal_method()`。
* **避免衝突**：如果變數名跟關鍵字衝突（如 `class`），可以在後面加底線：`class_`。

---

## 2. 代碼排版風格 (Code Layout)

良好的排版能讓你一眼看清代碼邏輯。

* **縮排 (Indentation)**：一律使用 **4 個空白鍵**，不要使用 Tab（或設定編輯器將 Tab 自動轉為 4 個空白）。
* **每行長度**：建議每行不超過 **79 個字元**。這能讓你在左右並排開啟視窗時依然能閱讀代碼。
* **空行 (Blank Lines)**：
* 頂層函式與類別之間：空 **2 行**。
* 類別內的方法 (Method) 之間：空 **1 行**。


* **引號**：Python 不差分單引號 `'` 或雙引號 `"`，但建議**全程統一**。

---

## 3. 空格的使用 (Whitespace)

適度的空格能減少視覺上的壓迫感。

* **二元運算子**：在賦值 (`=`)、比較 (`==`, `<`, `>`)、算術 (`+`, `-`, `*`, `/`) 前後各加一個空格。
* ✅ `x = y + 1`
* ❌ `x=y+1`


* **逗號、分號、冒號**：緊跟在前面字元後，後面加空格。
* ✅ `print(x, y)`
* ❌ `print(x ,y)`


* **小括號/中括號內部**：不要加不必要的空格。
* ✅ `my_list[1]`
* ❌ `my_list[ 1 ]`



---

## 4. 註解與文件字串 (Comments & Docstrings)

* **行內註解**：代碼與 `#` 之間至少空兩個空格。
* **文件字串 (Docstrings)**：所有公共模組、函式、類別都應該撰寫 `"""Docstring"""`。

```python
def complex_calculation(a, b):
    """
    這是一個計算 a 加上 b 的範例函式。
    
    :param a: 第一個數字
    :param b: 第二個數字
    :return: 兩數之和
    """
    return a + b

```
